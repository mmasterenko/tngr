(function($) {
    $(document).ready(function () {
        $('.change-list .field-photo').each(function () {
            var img_url = $(this).find('a').attr('href');
            var img = $('<img>').attr({
                'src': img_url,
                'width': '88px',
                'height': '88px'
            }).css('border-radius', '50%');
            $(this).find('a').replaceWith(img);
        });
    });
})(django.jQuery);
