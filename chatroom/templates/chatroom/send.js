function sendMessage() {
  // Get the message text from the input field
  var messageText = document.getElementById("message-input").value;
  
  // Clear the message input
  document.getElementById("message-input").value = "";
  
  // Update the chat window with the new message
  var chatWindow = document.getElementById("chat-window");
  chatWindow.innerHTML += "<p>" + messageText + "</p>";
}

