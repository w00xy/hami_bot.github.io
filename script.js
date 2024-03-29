var setElementHeight = function () {
    var height = $(window).height();
    $('.autoheight').css('min-height', (height));
};

$(window).on("resize", function () {
    setElementHeight();
}).resize();