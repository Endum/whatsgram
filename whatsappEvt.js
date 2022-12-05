function subscribeToMessages(){
  const mainEl = document.querySelector('#main')
  const messages = mainEl.querySelector('div[tabindex="-1"]')

  messages.addEventListener('DOMNodeInserted', function(event){
    if(event.target.parentNode == messages){
      alert(event.target)
    }
  }, false );
}