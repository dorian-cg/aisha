let messageHistory = [];
const webSocket = new WebSocket(`/ws/agent`);

const homeElement = document.querySelector('.home');

const livingElement = homeElement.querySelector('.living');
const kitchenElement = homeElement.querySelector('.kitchen');
const garageElement = homeElement.querySelector('.garage');
const bedroomElement = homeElement.querySelector('.bedroom');
const bathroomElement = homeElement.querySelector('.bathroom');
const officeElement = homeElement.querySelector('.office');

const chatElement = document.querySelector('.chat');
const chatMessagesElement = chatElement.querySelector('.messages');
const chatFormElement = chatElement.querySelector('form');
const chatInputElement = chatFormElement.querySelector('input');
const chatSubmitButtonElement = chatFormElement.querySelector('button');
let isWaitingForResponse = false;


async function getAllRooms() {
  return await fetch('/api/room/all').then(res => res.json());
}

async function getDevicesForRoom(roomId) {
  return await fetch(`/api/device/room/${roomId}`).then(res => res.json());
}

async function getLightForDevice(deviceId) {
  return await fetch(`/api/light/${deviceId}`).then(res => res.json());
}

async function getLockForDevice(deviceId) {
  return await fetch(`/api/lock/${deviceId}`).then(res => res.json());
}

async function getThermoForDevice(deviceId) {
  return await fetch(`/api/thermo/${deviceId}`).then(res => res.json());
}


function userMessage(message) {
  return {
    sender: 'user',
    content: message,
  };
}

function assistantMessage(message) {
  return {
    sender: 'assistant',
    content: message,
  };
}

function onWebSocketOpen() {
  sendMessageToAgent('Hi!');
}

async function onWebSocketReceivesMessage(event) {
  const responses = JSON.parse(event.data);

  for (const response of responses) {
    messageHistory.push(assistantMessage(response));
    addMessageToChatUi(createAssistantMessageUi(response));
  }

  await updateHomeState();

  isWaitingForResponse = false;
  updateButtonUi();
}

function onWebSocketClose() {
  addMessageToChatUi(createAssistantMessageUi('Session ended. Please refresh the page to start a new session.'));
}

function sendMessageToAgent(message) {
  messageHistory.push(userMessage(message));
  webSocket.send(JSON.stringify(messageHistory));
}

function onUserSendsMessage(event) {
  event.preventDefault();

  if (isWaitingForResponse) {
    alert('Please wait for the current response before sending a new message.');
    return;
  }

  isWaitingForResponse = true;
  updateButtonUi();

  const message = chatInputElement.value.trim();

  if (!message) {
    isWaitingForResponse = false;
    updateButtonUi();
    return;
  }

  chatFormElement.reset();
  addMessageToChatUi(createUserMessageUi(message));
  sendMessageToAgent(message);
}

function createDivElement(className, textContent) {
  const div = document.createElement('div');
  div.classList.add(className);
  if (textContent) {
    div.textContent = textContent;
  }
  return div;
}

function createAssistantMessageUi(message) {
  return createDivElement('msgbot', message);
}

function createUserMessageUi(message) {
  return createDivElement('msgusr', message);
}

function addMessageToChatUi(message) {
  chatMessagesElement.appendChild(message);
  chatMessagesElement.scrollTop = chatMessagesElement.scrollHeight;
}

function getUiLightWithState(lightState) {
  if (lightState.is_on) {
    return createDivElement('bulb-on');
  }
  return createDivElement('bulb');
}

function getUiOfThermoWithState(thermostatState) {
  if (!thermostatState.is_on) {
    return createDivElement('thermostat-off', '- °C');
  }
  return createDivElement('temp', `${thermostatState.temperature}°C`);
}

function getUiOfLockWithState(lockState) {
  if (lockState.is_locked) {
    return createDivElement('lock');
  }
  return createDivElement('unlock');
}

function updateButtonUi() {
  if (isWaitingForResponse) {
    chatSubmitButtonElement.disabled = true;
    chatSubmitButtonElement.textContent = 'Thinking...';
  } else {
    chatSubmitButtonElement.disabled = false;
    chatSubmitButtonElement.textContent = 'Send';
  }
}

async function updateRoomState(roomId, roomElement) {
  const devices = await getDevicesForRoom(roomId);

  const lightDevice = devices.filter(d => d.kind === 'Light').at(0);
  const getLightPromise = lightDevice ? getLightForDevice(lightDevice.id) : Promise.resolve(null);

  const lockDevice = devices.filter(d => d.kind === 'Lock').at(0);
  const getLockPromise = lockDevice ? getLockForDevice(lockDevice.id) : Promise.resolve(null);

  const thermoDevice = devices.filter(d => d.kind === 'Thermo').at(0);
  const getThermoPromise = thermoDevice ? getThermoForDevice(thermoDevice.id) : Promise.resolve(null);

  await Promise.all([getLightPromise, getLockPromise, getThermoPromise]);

  const lightState = await getLightPromise;
  const lockState = await getLockPromise;
  const thermoState = await getThermoPromise;

  const stateContainer = roomElement.querySelector('.state');
  stateContainer.innerHTML = '';

  if (lightState) {
    stateContainer.appendChild(getUiLightWithState(lightState));
  }

  if (thermoState) {
    stateContainer.appendChild(getUiOfThermoWithState(thermoState));
  }

  if (lockState) {
    stateContainer.appendChild(getUiOfLockWithState(lockState));
  }
}

async function updateHomeState() {
  const rooms = await getAllRooms();

  let updateLivingPromise = Promise.resolve();
  let updateKitchenPromise = Promise.resolve();
  let updateGaragePromise = Promise.resolve();
  let updateBedroomPromise = Promise.resolve();
  let updateBathroomPromise = Promise.resolve();
  let updateOfficePromise = Promise.resolve();

  for (const room of rooms) {
    switch (room.name.toLowerCase()) {
      case 'living':
        updateLivingPromise = updateRoomState(room.id, livingElement);
        break;
      case 'kitchen':
        updateKitchenPromise = updateRoomState(room.id, kitchenElement);
        break;
      case 'garage':
        updateGaragePromise = updateRoomState(room.id, garageElement);
        break;
      case 'bedroom':
        updateBedroomPromise = updateRoomState(room.id, bedroomElement);
        break;
      case 'bathroom':
        updateBathroomPromise = updateRoomState(room.id, bathroomElement);
        break;
      case 'office':
        updateOfficePromise = updateRoomState(room.id, officeElement);
        break;
    }
  }

  await Promise.all([
    updateLivingPromise,
    updateKitchenPromise,
    updateGaragePromise,
    updateBedroomPromise,
    updateBathroomPromise,
    updateOfficePromise,
  ]);
}

webSocket.addEventListener('open', onWebSocketOpen);
webSocket.addEventListener('message', onWebSocketReceivesMessage);
webSocket.addEventListener('close', onWebSocketClose);
chatFormElement.addEventListener('submit', onUserSendsMessage);
