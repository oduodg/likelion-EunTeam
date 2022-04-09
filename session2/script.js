window.onscroll = function () {
  stickyNav();
};

var navbar = document.getElementById("navbar");

var navPos = navbar.offsetTop;

function stickyNav() {
  if (window.pageYOffset >= navPos) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}
