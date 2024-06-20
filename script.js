const form = document.querySelector('#translateForm');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    let formData = new FormData(event.target);

    fetch('/translate', {
        method: 'POST',
        body: formData,
    }).then(response => {
        return response.json();        
    }).then(json => {
        document.querySelector('#result').innerText = json.translated_text;
    });
});

document.querySelector('#swapLangs').addEventListener('click', (event) => {
    let srcLang = document.querySelector('#src_lang');
    let targetLang = document.querySelector('#tgt_lang');
    let srcValue = srcLang.value;
    let targetValue = targetLang.value;
    srcLang.value = targetValue;
    targetLang.value = srcValue;
});
function limitWords(textarea) {
    var maxWords = 500;
    var words = textarea.value.split(/\s+/);
    if (words.length > maxWords) {
        textarea.value = words.slice(0, maxWords).join(" ");
        alert('You can only type 500 words!');
    }
}