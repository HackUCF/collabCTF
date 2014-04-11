var io = require('socket.io').listen(7000);

var users = [];

io.sockets.on('connection', function (socket) {
  socket.on('connect', function(user) {
     console.log('Connection!');
  });

  socket.emit('new_message', {
      user: 'userid',
      message: 'message',
      time: 'time'
  });

  socket.on('event', function(data) {
    console.log(data);
  });
});
