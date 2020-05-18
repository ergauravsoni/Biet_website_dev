(function ($) {
    "use strict";

    jQuery(document).ready(function ($) {


        $(".embed-responsive iframe").addClass("embed-responsive-item");
        $(".carousel-inner .item:first-child").addClass("active");

        $('[data-toggle="tooltip"]').tooltip();


        (function ($) {

            var allPanels = $('.single_faq > p').hide();

            $('.single_faq > h3 > i').click(function () {
                allPanels.slideUp();
                $(this).parent().next().slideDown();
                return false;
            });

        })(jQuery);

        //Owl carusel slider....
        $('.slider_bottom').owlCarousel({
            loop: true,
            autoplay: true,
            nav: true,
            navText: ['<i class="fa fa-angle-double-left"></i>', '<i class="fa fa-angle-double-right"></i>'],
            margin: 10,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 6
                }
            }
        });

        //Responsive Mobile Menu....
        $('#mobile_menu').slicknav();

        jQuery('.tp-banner').revolution({
            delay: 9000,
            startwidth: 1170,
            startheight: 500,
            hideThumbs: 10
        });

    });
	
jQuery(window).load(function(){

    $("#preloader").fadeOut(500);
    
});	




}(jQuery));