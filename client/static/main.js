import { UI } from './ui.js';
import { WS } from './ws.js';

const ui = new UI();
const ws = new WS();

document.getElementById('createRoom').addEventListener('click', async () => {
    const response = await fetch('/api/create-room');
    const data = await response.json();
    ui.showRoomLink(data.link);
    ws.connect(data.room_id);
});

ui.init();