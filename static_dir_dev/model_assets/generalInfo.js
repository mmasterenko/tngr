(function($) {
    $(document).ready(function () {
        $('.change-form .field-logo').each(function () {
            var img_url = $(this).find('a').attr('href');
            var img = $('<img>').attr({
                'src': img_url
            });
            $(this).find('a').html(img);
        });
    });
})(django.jQuery);
