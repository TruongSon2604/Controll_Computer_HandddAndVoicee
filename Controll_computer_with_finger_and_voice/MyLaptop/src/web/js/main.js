

eel.expose(setUserInput)
eel.expose(setAppInput)
function setUserInput(msg) {
    addUserMsg(msg);
}
function setAppInput(msg){
    addAppMsg(msg);
}
function getUserInput(msg)
{
    eel.getUserInput(msg)
}
var button = document.getElementById("userInputButton")
button.addEventListener('click',function() {
    getUserInput("OpenSetting")
})

function addUserMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message from ready rtol">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message from"), 500);
}

function addAppMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message to ready ltor">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    //add delay for animation to complete and then modify class to => "message to"
    index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message to"), 500);
}

function changeClass(element, index, newClass) {
    console.log(newClass +' '+ index);
    element.children[index].className = newClass;
}

