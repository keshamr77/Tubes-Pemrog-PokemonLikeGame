document.addEventListener('DOMContentLoaded', function () {
    const socket = new WebSocket('ws://' + window.location.host + '/ws/game/');

    socket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        console.log('Message from server:', data.message);
    };

    socket.onopen = function (e) {
        console.log('WebSocket connection established');
    };

    socket.onclose = function (e) {
        console.log('WebSocket connection closed');
    };
});