// hiding elements by id
function hide(x) {
    var target = document.getElementById(x);
    target.setAttribute("style", "display:none;");
}

// showing elements by id
function show(y) {
    var target = document.getElementById(y);
    target.setAttribute("style", "display:inline;");
}

function say(x) {
    alert(x);
}