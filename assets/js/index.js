const imgHamburguer = document.getElementById("imgHamburguer");
const menuHeader = document.getElementById("menuHeader");

let displayMenuHeader;

imgHamburguer.addEventListener("click", () => {
    displayMenuHeader = getComputedStyle(menuHeader).display;

    if(displayMenuHeader === "none") {
        menuHeader.style.display = "block";
    }else {
        menuHeader.style.display = "none";
    }
});
