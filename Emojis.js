const emojis = [
    "😀", // grinning face
    "😃", // grinning face with big eyes
    "😄", // grinning face with smiling eyes
    "😁", // beaming face with smiling eyes
    "😆", // grinning squinting face
    "😅", // grinning face with sweat
    "😂", // rolling on the floor laughing
    "🤣", // face with tears of joy
    "😊", // slightly smiling face
    "🙃", // upside-down face
    "😍", // melting face
    "😉", // winking face
    "😘", // smiling face with smiling eyes
    "😇", // smiling face with halo
    "😻", // face-affection
    "😽", // smiling face with hearts
    "😍", // smiling face with heart-eyes
    "🤩", // star-struck
    "😗", // face blowing a kiss
    "😚", // kissing face
    "😙", // smiling face
    "😋", // kissing face with closed eyes
    "😛", // kissing face with smiling eyes
    "😜", // smiling face with tear
    "😝", // face-tongue
    "😛", // g food
    "😜", // face with tongue
    "😝", // winking face with tongue
    "🤪", // zany face
    "😝", // squinting face with tongue
    "🤑", // money-mouth face
    "🤗", // face-hand
    "😊", // smiling face with open hands
    "🤫", // face with hand over mouth
    "🤔", // face with open eyes and hand over mouth
    "🤭", // face with peeking eye
    "🤫", // shushing face
    "🤔", // thinking face
    "🤗", // saluting face
    "🧐", // face-neutral-skeptical
    "🤐", // zipper-mouth face
    "🙄", // face with raised eyebrow
    "😶", // neutral face
    "😑", // expressionless face
    "😐", // face without mouth
    "😬", // dotted line face
    "🥴", // face in clouds
    "😏", // smirking face
    "😒", // unamused face
    "🙁", // face with rolling eyes
    "😬", // grimacing face
    "😷", // face exhaling
    "🤥", // lying face
    "🤢" // shaking face
     "😌", // relieved face
    "😔", // pensive face
    "😴", // sleepy face
    "🤤", // drooling face
    "😴", // sleeping face
    "😷", // face-unwell
    "😷", // face with medical mask
    "🤒", // face with thermometer
    "🤕", // face with head-bandage
    "🤢", // nauseated face
    "🤮", // face vomiting
    "🤧", // sneezing face
    "🥵", // hot face
    "🥶", // cold face
    "🥴", // woozy face
    "🙁", // face with crossed-out eyes
    "🤯", // face with spiral eyes
    "🤯", // exploding head
    "🤠", // face-hat
    "🤠", // cowboy hat face
    "🥳", // partying face
    "🥸", // disguised face
    "😎", // face-glasses
    "😎", // smiling face with sunglasses
    "🤓", // nerd face
    "🧐", // face with monocle
    "😕", // face-concerned
    "😕", // confused face
    "😟", // face with diagonal mouth
    "😟", // worried face
    "😔", // slightly frowning face
    "😞", // frowning face
    "😶", // face with open mouth
    "😶", // hushed face
    "😲", // astonished face
    "😳", // flushed face
    "🥺", // pleading face
    "😭", // face holding back tears
    "😩", // frowning face with open mouth
    "😰", // anguished face
    "😱", // fearful face
    "😰", // anxious face with sweat
    "😥", // sad but relieved face
    "😢", // crying face
    "😭", // loudly crying face
    "😱", // face screaming in fear
    "😖", // confounded face
    "😣", // persevering face
    "😞", // disappointed face
    "😓", // downcast face with sweat
    "😩", // weary face
    "😫", // tired face
    "😪", // yawning face
    "😠", // face-negative
    "😠", // face with steam from nose
    "😠", // enraged face
    "😠", // angry face
    "😡", // face with symbols on mouth
    "😈", // smiling face with horns
    "👿", // angry face with horns
    "💀", // skull
    "☠️" // skull and crossbones
    "💩", // pile of poo
    "🤡", // clown face
    "👹", // ogre
    "👺", // goblin
    "👻", // ghost
    "👽", // alien
    "👾", // alien monster
    "🤖", // robot
    "🐱", // cat-face
    "😺", // grinning cat
    "😸", // grinning cat with smiling eyes
    "😹", // cat with tears of joy
    "😻", // smiling cat with heart-eyes
    "😼", // cat with wry smile
    "😽", // kissing cat
    "🙀", // weary cat
    "😿", // crying cat
    "😾", // pouting cat
    "🙈", // see-no-evil monkey
    "🙉", // hear-no-evil monkey
    "🙊", // speak-no-evil monkey
    "❤️", // red heart
    "🧡", // orange heart
    "💛", // yellow heart
    "💚", // green heart
    "💙", // blue heart
    "💜", // purple heart
    "🖤", // black heart
    "❤️" // red heart
    "💕" // two hearts
    "💖" // sparkling heart
    "💗" // growing heart
    "💘" // heart with arrow
    "💝" // heart with ribbon
    "💞" // revolving hearts
    "💟" // heart decoration
    "❣️" // heart exclamation
    "💔" // broken heart
    "💓" // beating heart
    "💕" // two hearts
    "💖" // sparkling heart
    "💗" // growing heart
    "💘" // heart with arrow
    "💝" // heart with ribbon
    "💞" // revolving hearts
    "💟" // heart decoration
    "❣️" // heart exclamation
    "💔" // broken heart
    "💓" // beating heart
    "🔥" // heart on fire
    "💖" // mending heart
    "💗" // pink heart
    "💙" // light blue heart
    "🤍", // white heart
    "🤎", // brown heart
    "🖤", // black heart
    "😀", // grinning face
    "😎", // sunglasses face
    "😂", // rolling on the floor laughing
    "🙂", // slightly smiling face
    "❤️", // red heart
    "🔥", // fire
    "🍔", // hamburger
    "🍟", // french fries
    "🚗", // car
    "🛍", // shopping bags
    "🌞", // sun with face
    "💻", // computer
    "📱", // mobile phone
    "🎵", // musical note
    "🎉", // party popper
    "🏆", // trophy
    "💰", // money bag
    "🌍", // earth globe
    "🔍", // magnifying glass
    "💬", // speech bubble
    "🚶‍♀️", // woman walking
    "🚶‍♂️", // man walking
    "🚴‍♀️", // woman biking
    "🚴‍♂️", // man biking
    "🏃‍♀️", // woman running
    "🏃‍♂️", // man running
    "🏋️‍♀️", // woman lifting weights
    "🏋️‍♂️", // man lifting weights
    "🚣‍♀️", // woman rowing boat
    "🚣‍♂️", // man rowing boat
    "🕵️‍♀️", // woman detective
    "🕵️‍♂️", // man detective
    "💄", // lipstick
    "🛍", // shopping bags
    "🎓", // graduation cap
    "🎒", // school backpack
    "🎵", // musical note
    "🎸", // guitar
    "🚣‍♀️", // woman rowing boat
    "🚣‍♂️", // man rowing boat
    "🕵️‍♀️", // woman detective
    "🕵️‍♂️", // man detective
    "💄", // lipstick
    "🛍", // shopping bags
    "🎓", // graduation cap
    "🎒", // school backpack
    "🎵", // musical note
    "🎸", // guitar
];

const displayEmojis = () => {
    let emojiDiv = document.getElementById("emoji-container");
    for (let i = 0; i < emojis.length; i++) {
        let emojiSpan = document.createElement("span");
        emojiSpan.innerHTML = emojis[i];
        emojiDiv.appendChild(emojiSpan);
    }
};

