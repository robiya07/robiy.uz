
const sr = ScrollReveal({
    origin: 'left',
    distance: '60px',
    duration: 2000,
    delay: 300
})

sr.reveal(`.header__content-title`, { delay: 200 })
sr.reveal(`.header__content-sub, .about__content-img,   
            .about__content-text,  .blog__detail-title, .blog__detail-data, .none-img, .portfolio-detail-btn`, { origin: 'top', delay: 300 })
sr.reveal(`.header__content-btns`, { distance: '100px', delay: 600, origin: 'bottom' })
sr.reveal(`.blog__content-menu`, { duration: 1000, delay: 100, origin: 'top' })
sr.reveal(`.blog__content-card, .blog__detail-img, .portfolio__cards, .portfolio__detail-img, .blog__detail-box, .contact__form`, { duration: 1500, origin: 'left', distance: '60px' })
sr.reveal(`.seeMore,`, { duration: 1500, origin: 'bottom', delay: 100 })

