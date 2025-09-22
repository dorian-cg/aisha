const homeState = {
  rooms: [
    {
      id: 'living',
      name: 'Living Room',
      devices: [
        {
          type: 'light',
          name: 'light',
          state: {
            on: true
          }
        },
        {
          type: 'thermostat',
          name: 'thermostat',
          state: {
            on: false,
            temperature: 22
          }
        },
        {
          type: 'lock',
          name: 'door lock',
          state: {
            locked: true
          }
        }
      ]
    },
    {
      id: 'kitchen',
      name: 'Kitchen',
      devices: [
        {
          type: 'light',
          name: 'light',
          state: {
            on: false
          }
        },
        {
          type: 'thermostat',
          name: 'thermostat',
          state: {
            on: false,
            temperature: 22
          }
        },
      ]
    },
    {
      id: 'garage',
      name: 'Garage',
      devices: [
        {
          type: 'light',
          name: 'light',
          state: {
            on: false
          }
        },
        {
          type: 'lock',
          name: 'door lock',
          state: {
            locked: true
          }
        }
      ]
    },
    {
      id: 'bedroom',
      name: 'Bedroom',
      devices: [
        {
          type: 'light',
          name: 'light',
          state: {
            on: false
          }
        },
        {
          type: 'thermostat',
          name: 'thermostat',
          state: {
            on: false,
            temperature: 22
          }
        },
      ]
    },
    {
      id: 'bathroom',
      name: 'Bathroom',
      devices: [
        {
          type: 'light',
          name: 'light',
          state: {
            on: false
          }
        },
        {
          type: 'thermostat',
          name: 'thermostat',
          state: {
            on: false,
            temperature: 22
          }
        },
      ]
    },
    {
      id: 'office',
      name: 'Office',
      devices: [
        {
          type: 'light',
          name: 'light',
          state: {
            on: false
          }
        },
        {
          type: 'thermostat',
          name: 'thermostat',
          state: {
            on: false,
            temperature: 22
          }
        },
      ]
    },
  ]
};

const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const host = window.location.host;
const webSocket = new WebSocket(`${wsProtocol}//${host}/agent`);
const home = document.querySelector('.home');

const chat = document.querySelector('.chat');
const chatMessages = chat.querySelector('.messages');
const chatForm = chat.querySelector('form');
const chatInput = chatForm.querySelector('input');

function sendAction(type, data) {
  webSocket.send(JSON.stringify({ type, data }));
}

function createDiv(className, textContent) {
  const div = document.createElement('div');
  div.classList.add(className);
  if (textContent) {
    div.textContent = textContent;
  }
  return div;
}

function createBotMsg(message) {
  return createDiv('msgbot', message);
}

function createUserMsg(message) {
  return createDiv('msgusr', message);
}

function addMessageToChat(message) {
  chatMessages.appendChild(message);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function onSubmit(event) {
  event.preventDefault();

  const message = chatInput().value.trim();

  if (!message) {
    return;
  }

  chatForm.reset();
  addMessageToChat(createUserMsg(message));
  sendAction('message', message);
}

function onWebSocketOpen() {
  sendAction('init', homeState);
}

function onWebSocketMessage(event) {
  const msg = JSON.parse(event.data);
  if (msg.type === 'message') {
    addMessageToChat(createBotMsg(msg.data));
  }
}

function onWebSocketClose() {
  addMessageToChat(createBotMsg('Session ended. Please refresh the page to start a new session.'));
}

function getLightForState(lightState) {
  if (lightState.on) {
    return createDiv('bulb-on');
  }
  return createDiv('bulb');
}

function getThermostatForState(thermostatState) {
  if (!thermostatState.on) {
    return createDiv('thermostat-off', '- °C');
  }
  return createDiv('temp', `${thermostatState.temperature}°C`);
}

function getLockForState(lockState) {
  if (lockState.locked) {
    return createDiv('lock');
  }
  return createDiv('unlock');
}

function applyStateToRoom(room, roomElement) {
  const stateContainer = roomElement.querySelector('.state');
  stateContainer.innerHTML = '';

  for (const device of room.devices) {
    switch (device.type) {
      case 'light':
        stateContainer.appendChild(getLightForState(device.state));
        break;
      case 'thermostat':
        stateContainer.appendChild(getThermostatForState(device.state));
        break;
      case 'lock':
        stateContainer.appendChild(getLockForState(device.state));
        break;
      default:
        break;
    }
  }
}

function reflectHomeState() {
  for (const room of homeState.rooms) {
    switch (room.id) {
      case 'living':
        applyStateToRoom(room, home.querySelector('.living'));
        break;
      case 'kitchen':
        applyStateToRoom(room, home.querySelector('.kitchen'));
        break;
      case 'garage':
        applyStateToRoom(room, home.querySelector('.garage'));
        break;
      case 'bedroom':
        applyStateToRoom(room, home.querySelector('.bedroom'));
        break;
      case 'bathroom':
        applyStateToRoom(room, home.querySelector('.bathroom'));
        break;
      case 'office':
        applyStateToRoom(room, home.querySelector('.office'));
        break;
      default:
        break;
    }
  }
}

reflectHomeState();

chatForm.addEventListener('submit', onSubmit);
webSocket.addEventListener('open', onWebSocketOpen);
webSocket.addEventListener('message', onWebSocketMessage);
webSocket.addEventListener('close', onWebSocketClose);
