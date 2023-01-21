const emojiSelectorIcon = document.getElementById("emojiSelectorIcon");
const emojiSelector = document.getElementById("emojiSelector");
const emojiList = document.getElementById("emojiList");
const emojiSearch = document.getElementById("emojiSearch");
const emojiInput = document.getElementById("taper-ici")

emojiSelectorIcon.addEventListener('click', () => {
    emojiSelector.classList.toggle("active");
});

fetch("{% static 'emojis.json' %}")
    .then(res => res.json())
    .then(data => loadEmoji(data))


function loadEmoji(data){
    data.forEach(emoji => {
        let li = document.createElement('li');
        li.setAttribute("emoji-name", emoji.name);
        li.textContent = emoji.emoji;
        li.addEventListener('click', addEmojiToInput); 
        emojiList.appendChild(li);
    });
}

function addEmojiToInput(e) {
    let selectedEmoji = e.target.textContent;
    emojiInput.value += selectedEmoji; 
    emojiSelector.classList.remove("active");
}

emojiSearch.addEventListener('keyup', e => {
    let value = e.target.value;
    let emojis = document.querySelectorAll('#emojiList li')
    if(value == "") {
        emojis.forEach(emoji => {
            emoji.style.display = "flex"; //display all emojis if the search bar is empty
        });
    } else {
        emojis.forEach(emoji => {
            if (emoji.getAttribute('emoji-name').toLowerCase().includes(value)) {
                emoji.style.display = "flex"; //display the matching emojis
            } else {
                emoji.style.display = "none"; //hide the non-matching emojis
            }
        });
    }
});