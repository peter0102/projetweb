function deleteRoom(roomName) {
        $.ajax({
            url : '/deleteRoom/',
            type : 'POST',
            data : {
                roomName: roomName,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            dataType: 'json',
        })
    };

setInterval(function(){
    $.ajax({
        url: '/getRooms/',
        type: 'GET', //GET, on reçoit des donénes du serveur
        dataType: 'json',
        success: function(response) {
            document.getElementById("roomWindow").innerHTML = "" //on vide la fenêtre de chat à chaque rafraichissement de la page pour éviter les doublons de messages
            //sinon les messages s'affichent plusieurs fois
            for (let i = 0; i < response.allRooms.length; i++) {
                document.getElementById("roomWindow").innerHTML+='<p>' + response.allRooms[i].roomName+ '</p>'
                document.getElementById("roomWindow").innerHTML+='<a href="/chatroom/room_name='+response.allRooms[i].roomName+'">Join this chatroom</a>'
                {% if user.is_superuser %} // syntaxe marquée comme une erreur par vscode, mais fonctionne avec des extensions django qui reconnaissent le langage template
                    var deletetionButton=document.createElement("button")
                    deletetionButton.innerHTML="Delete"
                    deletetionButton.setAttribute("onclick", "deleteRoom('"+response.allRooms[i].roomName+"')") //execute la fonction deleteRoom au clic
                    document.getElementById("roomWindow").appendChild(deletetionButton)
                {% endif %}

            }
        }
    });
},200) //envoie une requete toutes les 200ms