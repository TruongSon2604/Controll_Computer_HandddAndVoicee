document.addEventListener('DOMContentLoaded', function() {
    var divone = document.getElementById("one");
    var divtwo = document.getElementById("two");
    var divthree = document.getElementById("three");

    divone.style.boxShadow = "0 0 10px #fff";
    divone.style.borderRadius = "0 0 30px 30px";
    divone.addEventListener('click', function() {
        postDataToSetting(); 
        divone.style.boxShadow = "0 0 10px #fff";
        divone.style.borderRadius = "0 0 30px 30px";

        divtwo.style.boxShadow = "0 0 0";
        divtwo.style.borderRadius = "0";

        divthree.style.boxShadow = "0";
        divthree.style.borderRadius = "0";
    });
    divtwo.addEventListener('click', function() {
        divtwo.style.boxShadow = "0 0 10px #fff";
        divtwo.style.borderRadius = "0 0 30px 30px";

        divone.style.boxShadow = "0 0 0";
        divone.style.borderRadius = "0";

        divthree.style.boxShadow = "0 0 0";
        divthree.style.borderRadius = "0";
    });
    divthree.addEventListener('click', function() {
        divthree.style.boxShadow = "0 0 10px #fff";
        divthree.style.borderRadius = "0 0 30px 30px";

        divtwo.style.boxShadow = "0 0 0";
        divtwo.style.borderRadius = "0";

        divone.style.boxShadow = "0 0 0";
        divone.style.borderRadius = "0";
    });
});
async function postDataToSetting() {
    const data = await eel.postDataToSetting()(); 
    const contentDiv = document.getElementById("content");
    contentDiv.innerHTML = ""; 

    for (const [key, value] of Object.entries(data)) {
        const keyValueDiv = document.createElement("div");
        keyValueDiv.classList.add("key-value-container");


        const title = document.createElement("h3");
        title.textContent = key;
        const titleDiv= document.createElement("div")
        titleDiv.classList.add("title_div")
        titleDiv.appendChild(title)

        const link = document.createElement("input");
        link.classList.add("urlIp")
        link.type = "text";
        link.value = value;
        const edit = document.createElement("button")
        edit.classList.add("editUrl")
        edit.value = "Edit"
        edit.type = "Button"

        const linkDiv= document.createElement("div")
        linkDiv.classList.add("link_div")
        linkDiv.appendChild(link)
        linkDiv.appendChild(edit)

        keyValueDiv.appendChild(titleDiv);
        keyValueDiv.appendChild(linkDiv)

        contentDiv.appendChild(keyValueDiv);
    }
}
