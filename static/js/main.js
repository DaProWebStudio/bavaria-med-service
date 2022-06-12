(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    $(document).ready(function () {
        $('.navbar-nav a').each(function(){
            let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
            let link = this.href;
            if(location == link){
                $(this).parent().addClass('active');
            }
        });
    });
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });

    // Navbar 
    $(document).ready(function() {
        $('.burger').click(function() {
            $(this).toggleClass('burger_active');
            $('.navbar-collapse').toggleClass('navbar-collapse-active')
        });
    })
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });

    $(".mega-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });

    $(".doctor-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : false,
        responsive: {
            0:{
                items:1
            },
            992:{
                items:4
            }
        }
    });
    $(".diagnostic-carousel").owlCarousel({
        loop: false, 
        nav: true, 
        autoplay: false, 
        autoplayTimeout:8000, 
        responsive:{ 
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            },
            1200:{
                items:3
            }
        }
    });
    
})(jQuery);


// Diagnostic
$('ul.catalog__tabs').on('click', 'li:not(.catalog__tab_active)', function() {
    $(this)
      .addClass('catalog__tab_active').siblings().removeClass('catalog__tab_active')
      .closest('div.container').find('div.catalog__content').removeClass('catalog__content_active').eq($(this).index()).addClass('catalog__content_active');
});

function toggleSlide(item) {
    $(item).each(function(i) {
        $(this).on('click', function(e) {
            e.preventDefault();
            $('.catalog-item__content').eq(i).toggleClass('catalog-item__content_active');
            $('.catalog-item__list').eq(i).toggleClass('catalog-item__list_active');
        })
    });
};

toggleSlide('.catalog-item__link');
toggleSlide('.catalog-item__back');

// slider-diagnostic

const slider = document.querySelector('.catalog__content catalog__content_active');

// treatment
$('ul.treatment__list').on('click', 'li:not(.treatment__item-active)', function() {
    $(this)
      .addClass('treatment__item-active').siblings().removeClass('treatment__item-active')
      .closest('div.container').find('div.treatment__content').removeClass('treatment__content_active').eq($(this).index()).addClass('treatment__content_active');
});

function toggleSlide(item) {
    $(item).each(function(i) {
        $(this).on('click', function(e) {
            e.preventDefault();
            $('.treatment__content').eq(i).toggleClass('treatment__content_active');
            $('.treatment__content-list').eq(i).toggleClass('treatment__content-list_active');
        })
    });
};

toggleSlide('.treatment__content-list');
toggleSlide('.treatment__content-back');