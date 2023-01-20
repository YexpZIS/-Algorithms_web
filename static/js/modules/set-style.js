function changeFont(element){
    element.setAttribute("style",element.getAttribute("style")+";font-family: Courier New; font-size: 30px;");
    for(var i=0; i < element.children.length; i++){
        changeFont(element.children[i]);
    }
}
// changeFont(document.getElementsByTagName("body")[0]);