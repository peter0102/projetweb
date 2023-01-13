const emojiSelectorIcon = document.getElementById("emojiSelectorIcon");
const emojiSelector = document.getElementById("emojiSelector");
const emojiList = document.getElementById("emojiList");
const emojiSearch = document.getElementById("emojiSearch");

emojiSelectorIcon.addEventListener('click', () => {
    emojiSelector.classList.toggle("active");
});

fetch("emoji-api-main/src/emojis.json")
    .then(res => res.json())
    .then(data => loadEmoji(data))


function loadEmoji(data){
    data.forEach(emoji => {
        let li = document.createElement('li');
        li.setAttribute("emoji-name", emoji.name);
        li.textContent = emoji.emoji;
        emojiList.appendChild(li);
    });
}

emojiSearch.addEventListener('keyup', e =>{
    let value = e.target.value;
    console.log(value);
    let emojis = document.querySelectorAll('emojiList li')
    emojis.forEach(emoji => {
        if (emoji.getAttribute('emoji-name').toLowerCase().includes(value)) {
            emoji.getElementsByClassName.display = "flex"; //montre le(s) emoji(s) si un résultat match, en changeant la propriété du css à 'flex'
        } else {
            emoji.style.display = "none" ////cache l'emoji si le résultat de la recherche n'apparaît pas
        }
    })
})