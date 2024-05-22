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


const fillBtns = document.querySelectorAll('.blog__content-btn')

fillBtns.forEach(btns => {
    btns.addEventListener('click', () => {
        fillBtns.forEach(btn => btn.classList.remove('fill'))
        btns.classList.add('fill')

    })

})


const signupForm = document.querySelector('.contact__form');
const username = document.querySelector('.username');
const number = document.querySelector('.number');
const message = document.querySelector('.message');

const regEX = /^[a-zA-Z\s]{4,20}$/;
const numEX = /^[0-9]{9}$/;



const matchInput = (input, regEX,) => {
    if (regEX.test(input.value)) {
        input.classList.remove('error');
        input.classList.add('success');
    } else {
        input.classList.remove('success');
        input.classList.add('error');
    }
};

username.addEventListener('input', () => {
    matchInput(username, regEX)
});

number.addEventListener('input', () => {
    matchInput(number, numEX)
});


signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (regEX.test(username.value) && numEX.test(number.value)) {
        window.location.href = '404.html'
        username.value = "";
        number.value = "";
        message.value = "";
    } else if (username.value == '' || number.value == '') {
        console.log('1');

    }

});





