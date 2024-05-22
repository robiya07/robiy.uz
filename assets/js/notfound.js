const hamMenu = document.querySelector('#hamburger-menu')

hamMenu.onclick = function () {
    navBar = document.querySelector('.nav__content-list')
    overlay = document.querySelector('#overlay')
    navBar.classList.toggle('show-menu')
    overlay.classList.toggle('show-menu')

}

overlay.onclick = function () {
    overlay.classList.remove('show-menu')
    navBar.classList.remove('show-menu')

}

document.addEventListener('keydown', (e) => {
    if (e.key == 'Escape') {
        overlay.classList.remove('show-menu')
        navBar.classList.remove('show-menu')
    }
})



document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector(".found__btn");
    const paragraph = document.querySelector(".fount__text");
    const span = document.querySelector(".found__span");
    const arrow = document.querySelector('.found__arrow')


    button.addEventListener("mouseover", function () {
        paragraph.classList.add("found__text--hover");
        span.classList.add('found__text--hover-black')
        arrow.classList.add('arrow-black')
    });

    button.addEventListener('mouseout', function () {
        paragraph.classList.remove("found__text--hover");
        span.classList.remove('found__text--hover-black')
        arrow.classList.remove('arrow-black')
    });

})