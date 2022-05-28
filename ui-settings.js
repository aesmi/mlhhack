function getNumber() {
    var input = document.getElementById("num-input"). value;
    var topMessage = document.getElementById("error");
    var c = document.getElementById("code").value;
    var n = "+" + c.toString() + input;
    
    var page1 = document.getElementById("page1");
    var page2 = document.getElementById("page2");

    page1.style.display = "none";
    page2.style.display = "block";
    
}
