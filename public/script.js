// Use same-origin WebSocket URL so the browser connects to the page host
const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const host = window.location.host; // includes port when present
const ws = new WebSocket(`${protocol}//${host}/agent`);

ws.onopen = () => {
  console.log('Connected');
  ws.send('Hello from browser!');
};
ws.onmessage = (event) => console.log('Received:', event.data);
ws.onclose = () => console.log('Disconnected');


// IGNORE THIS CODE FOR NOW

// const home = () => document.querySelector('.home');
// const chat = () => document.querySelector('.chat');
// const chatMessages = () => chat().querySelector('.messages');
// const chatForm = () => chat().querySelector('form');
// const chatInput = () => chatForm().querySelector('input');

// function createDiv(className, textContent) {
//   const div = document.createElement('div');
//   div.classList.add(className);
//   if (textContent) {
//     div.textContent = textContent;
//   }
//   return div;
// }

// function createBotMsg(message) {
//   return createDiv('msgbot', message);
// }

// function createUserMsg(message) {
//   return createDiv('msgusr', message);
// }

// function addMessageToChat(message) {
//   chatMessages().appendChild(message);
//   chatMessages().scrollTop = chatMessages().scrollHeight;
// }

// function onSubmit(event) {
//   event.preventDefault();

//   const message = chatInput().value.trim();

//   if (!message) {
//     return;
//   }

//   chatForm().reset();
//   addMessageToChat(createUserMsg(message));
//   // Send message through WebSocket

// }


// function webSocketMessage(event) {
//   const msg = event.data;
//   if (!msg) {
//     return;
//   }
//   addMessageToChat(createBotMsg(event.data));
// }

// chatForm().addEventListener('submit', onSubmit);




