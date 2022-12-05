// Wait for an elem to appear.
// If from specified, uses this as root of search.
function waitForElm(selector, from=null){
    return new Promise(resolve => {
      const origin = ((from != null) ? from : document)
      const observer = new MutationObserver(mutations => {
        if (origin.querySelector(selector)){
          observer.disconnect()
          return resolve(origin.querySelector(selector))
        }
      })
      observer.observe(((from != null) ? from : document.body),
        {
          childList: true,
          subtree: true
        })
      if (origin.querySelector(selector)) {
        observer.disconnect()
        return resolve(origin.querySelector(selector))
      }
    })
}

// Get login QRcode as base64 string.
async function getQRcode(){
  const canvas = await waitForElm('canvas')
  
  return canvas.toDataURL()
}

// Send message to the opened chat.
async function sendMessage(message){
  const mainEl = await waitForElm('#main')
  const textareaEl = await waitForElm('div[contenteditable="true"]', mainEl)

  textareaEl.focus()
  document.execCommand('insertText', false, message)
  textareaEl.dispatchEvent(new Event('change', { bubbles: true }))

 await new Promise(resolve => setTimeout(() => {
  (mainEl.querySelector('[data-testid="send"]') || mainEl.querySelector('[data-icon="send"]')).click()
      resolve();
  }, 100))
}

// Get all messages from opened chat.
async function getAllMessages(){
  const mainEl = await waitForElm('#main')
  const chat = await waitForElm('div[tabindex="-1"]', mainEl)
  await waitForElm('div[data-pre-plain-text]', chat)
  const infos = chat.querySelectorAll('div[data-pre-plain-text]')

  allMessages = []

  infos.forEach(info => {
    allMessages.push([
      info.getAttribute('data-pre-plain-text'),
      info.querySelector('div span span').innerText
    ])
  })
  return allMessages
}

// Get last message from opened chat.
function getLastMessage(){
  const mainEl = document.querySelector('#main')
  const chat = mainEl.querySelector('div[tabindex="-1"]')
  const infos = chat.querySelectorAll('div[data-pre-plain-text]')
  if(infos.length == 0)
    return null
  const info = infos[infos.length - 1]
  return [
      info.getAttribute('data-pre-plain-text'),
      info.querySelector('div span span').innerText
    ]
}

// Get all chats from the side pane.
async function getAllChats(){
  const pane_side = await waitForElm('#pane-side')
  await waitForElm('span[dir="auto"][title][aria-label]', pane_side)
  const chats = pane_side.querySelectorAll('span[dir="auto"][title][aria-label]')

  allChats = []

  chats.forEach(chat => {
    allChats.push(chat.getAttribute('title'))
  })

  return allChats
}

// Open a chat from side pane by name.
async function selectChat(name){
  const evt = new MouseEvent('mousedown', {bubbles: true});
  const pane_side = await waitForElm('#pane-side')
  const chat = await waitForElm('span[title="'+name+'"]', pane_side)

  chat.dispatchEvent(evt)
}

// Utility to send messages in topic.
function send(topic, message){
  window.toPyt.postMessage(topic + ":" + message)
}

async function baseSetup() {
  // Get the qrCode to connect device.
  await waitForElm('div[data-testid="qrcode"]')
  const qr = await getQRcode()
  send('qrcode', qr)
  // Get all available chats
  const chats = await getAllChats()
  send('chats', chats)
}

// Base setup to initial.
async function nicestBaseSetup(){
  // Get the qrCode to connect device.
  var lastQr = ""
  const qrObs = new MutationObserver(async mutations => {
    const qr = await getQRcode()
    if(qr.localeCompare(lastQr) != 0){
      lastQr = qr
      send('qrcode', qr)
    }
  })
  qrObs.observe(await waitForElm('div[data-testid="qrcode"]'), {attributes: true})
  // Get all available chats
  const chats = await getAllChats()
  qrObs.disconnect() // Detach observations on canvas.
  send('chats', chats)
}