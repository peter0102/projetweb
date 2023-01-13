function sendMessage() {
  // Get the message text from the input field
  var messageText = document.getElementById("message-input").value;
  
  // Clear the message input
  document.getElementById("message-input").value = "";
  
  // Update the chat window with the new message
  var chatWindow = document.getElementById("chat-window");
  chatWindow.innerHTML += "<p>" + messageText + "</p>";
}

function messageSubmit(event) { //fonction qui est appelée quand on appuie sur le bouton submit
  event.preventDefault(); // empêche le formulaire de se soumettre normalement ce qui ferait rafrachir la page
  $.ajax({ //requete ajax au serveur, 
      url: '/send/', //à cette url, appelle la vue sendMessage et la stocke avec les données suivantes
      type: 'POST', //POST, on envoie des données au serveur
      data: {
          messageSent: $('#messageSent').val(),
          chatRoomName: $('#chatRoomName').val(), //val() pour récupérer les valeurs
          whoSent: $('#whoSent').val(),
          csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      dataType: 'json',
      success: function(response) {
          if (response.isEmpty) {
              alert("You can't send an empty message !")
          }
          else if (response.isMuted) { // si l'utilisateur est muet, on affiche un message d'erreur
              alert("You are muted !")
          } 
          else {
          document.getElementById("messageSent").value="" //on vide le formulaire
          }
      }
  });
}

function deleteMessage(messageId) { // on récupère l'id du message qu'on cherche à supprimer
  $.ajax({
      url : '/deleteMessage/', // redirige vers cette url pour que la vue deleteMessage soit appelée 
      type : 'POST',
      data : {
          messageId: messageId,
          csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      dataType: 'json',
  })
}
function muteUser(username) {
  $.ajax({
      url: '/muteUser/',
      type: 'POST',
      data: {
          username: username,
          csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      dataType: 'json',
      success: function(response) {
          if (response.isMuted) {
              alert("User " + username + " is muted already")
          }
      }
  })
};
function unmuteUser(username) {
  $.ajax({
      url: '/unmuteUser/',
      type: 'POST',
      data: {
          username: username,
          csrfmiddlewaretoken: '{{ csrf_token }}'
      },
      dataType: 'json',
      success: function(response) {
          if (response.isNotMuted) {
              alert("User " + username + " is unmuted already")
          }
      }
  })
};

setInterval(function(){
  var url='/get/{{nameOfTheRoom}}'
  $.ajax({
      url: url,
      type: 'GET', //GET, on reçoit des donénes du serveur
      dataType: 'json',
      success: function(response) {
          document.getElementById("chatWindow").innerHTML = "" //on vide la fenêtre de chat à chaque rafraichissement de la page pour éviter les doublons de messages
          //sinon les messages s'affichent plusieurs fois
          var username="{{who}}"
          for (let i = 0; i < response.allMessagesList.length; i++) {
              document.getElementById("chatWindow").innerHTML+='<p>' + response.allMessagesList[i].who + " : " + 
              response.allMessagesList[i].allMessagesValue +'</p>' // //on récupère la valeur ième allMessagesValue de la liste allMessagesList
              {% if user.is_superuser %} // s'il s'agit d'un super utilisateur, crée des boutons de suppression pour chaque message
                  var deletetionButton=document.createElement("button")
                  deletetionButton.innerHTML="Delete"
                  deletetionButton.setAttribute("onclick", "deleteMessage("+response.allMessagesList[i].messageId+")")
                  document.getElementById("chatWindow").appendChild(deletetionButton)
              {% endif %}

          }
      }
  });
  $.ajax({
      url: '/getUsers/',
      type: 'GET',
      dataType: 'json',
      success: function(response) {
          document.getElementById("userWindow").innerHTML = ""
          for (let i = 0; i < response.users.length; i++) {
              document.getElementById("userWindow").innerHTML += '<p>' + response.users[i].username + '</p>'

              var muteUser=document.createElement("button")
              muteUser.innerHTML="Mute user"
              muteUser.setAttribute("onclick", "muteUser('"+response.users[i].username+"')")
              document.getElementById("userWindow").appendChild(muteUser)

              var unmuteUser=document.createElement("button")
              unmuteUser.innerHTML="Unmute user"
              unmuteUser.setAttribute("onclick", "unmuteUser('"+response.users[i].username+"')")
              document.getElementById("userWindow").appendChild(unmuteUser)
          }
      }
  })
},300) //envoie une requête toutes les 600ms