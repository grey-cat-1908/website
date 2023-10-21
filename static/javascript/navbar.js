let navOpen = false
function getNavbar() {
    let navbar = document.getElementById("nav-toggle")

    switch (navOpen) {
        case false:
            navbar.classList.add("active")
            navOpen = true;
            break;
        case true:
            navbar.classList.remove("active")
            navOpen = false;
            break;
    }
}