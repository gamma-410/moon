function searchG() {
    var text = document.getElementById("search");
    window.location.href = "https://www.google.com/search?q=" + text.value; 
}
function searchB() {
    var text = document.getElementById("search");
    window.location.href = "https://www.bing.com/search?q=" + text.value;
}
function searchY() {
    var text = document.getElementById("search");
    window.location.href = "https://search.yahoo.co.jp/search?p=" + text.value; 
}
function searchD() {
    var text = document.getElementById("search");
    window.location.href = "https://duckduckgo.com/?q=" + text.value;
}