function setSuperUser(username) {
    $.ajax({
        url: '/setSuperUser/',
        type: 'POST',
        data: {
            username: username,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        dataType: 'json',
        success:function(response){
            if (response.isSuperUser) {
                alert("User " + username +" is already superuser")
            }
        },
    })
};
function unsetSuperUser(username) {
    $.ajax({
        url: '/unsetSuperUser/',
        type: 'POST',
        data: {
            username: username,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        dataType: 'json',
        success: function(response) {
            if (response.isNotSuperUser) {
                alert("User " + username + " is not superuser already")
            }
        }
    })
};
function deleteUser(username) {
    $.ajax({
        url: '/deleteUser/',
        type: 'POST',
        data: {
            username: username,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        dataType: 'json',
    })
};
setInterval(function() {
    $.ajax({
        url: '/getUsers/',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            document.getElementById("userWindow").innerHTML = ""
            for (let i = 0; i < response.users.length; i++) {
                document.getElementById("userWindow").innerHTML += '<p>' + response.users[i].username + '</p>'
                var setSuperUser=document.createElement("button")
                setSuperUser.innerHTML="Set superuser"
                setSuperUser.setAttribute("onclick", "setSuperUser('"+response.users[i].username+"')")
                document.getElementById("userWindow").appendChild(setSuperUser)

                var unsetSuperUser=document.createElement("button")
                unsetSuperUser.innerHTML="Unset superuser"
                unsetSuperUser.setAttribute("onclick", "unsetSuperUser('"+response.users[i].username+"')")
                document.getElementById("userWindow").appendChild(unsetSuperUser)

                var deleteUser=document.createElement("button")
                deleteUser.innerHTML="Delete user"
                deleteUser.setAttribute("onclick", "deleteUser('"+response.users[i].username+"')")
                document.getElementById("userWindow").appendChild(deleteUser)
            }
        }
    })
},500)