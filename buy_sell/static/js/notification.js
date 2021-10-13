
const roomName = JSON.parse(document.getElementById('room-name').textContent);

const notificationSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/notification/'
    + roomName
    + '/'
);

notificationSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    //document.querySelector('#chat-log').value += (data.message + '\n');
    console.log(data);
    document.getElementById("notifications-dropdown").innerHTML = "<li class='dropdown-item'>" + data + "</li><hr class='dropdown-divider'>" + document.getElementById("notifications-dropdown").innerHTML;
    //document.getElementById("notification-badge").innerHTML = parseInt(document.getElementById("notification-badge").innerHTML) + 1;
    document.getElementById("notification-badge").innerHTML = parseInt(document.getElementById("notification-badge").innerHTML) + 1;
};

notificationSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
