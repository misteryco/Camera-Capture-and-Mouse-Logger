const socket = new WebSocket("ws://localhost:8765");

socket.onopen = (event) => {
    console.log("WebSocket connection opened:", event);
};

socket.onmessage = (event) => {
    const message = event.data;
    console.log("WebSocket message received:", message);
    document.getElementById("socket data").innerHTML = `<p>Mouse Position: ${message}</p>`;
};

socket.onclose = (event) => {
    console.log("WebSocket connection closed:", event);
};

socket.onerror = (error) => {
    console.error("WebSocket error:", error);
};