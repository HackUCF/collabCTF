$(function() {
  var addr = "http://"+window.location.hostname+":7000";
  console.log(addr);
  var socket = io.connect(addr);
  socket.on('new_message', function(data) {
    console.log(data);
  });
});
