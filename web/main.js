function searchGoogle() {
    var text = document.getElementById("search");
    window.location.href = "https://www.google.com/search?q=" + text.value; 
}
function searchBing() {
    var text = document.getElementById("search");
    window.location.href = "https://www.bing.com/search?q=" + text.value;
}
function searchYahoo() {
    var text = document.getElementById("search");
    window.location.href = "https://search.yahoo.co.jp/search?p=" + text.value; 
}
function searchDuckDuckGo() {
    var text = document.getElementById("search");
    window.location.href = "https://duckduckgo.com/?q=" + text.value;
}