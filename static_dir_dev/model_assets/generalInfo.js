(function($) {
    $(document).ready(function () {
        $('.change-form .field-logo').each(function () {
            var img_url = $(this).find('a').attr('href');
            var img = $('<img>').attr({
                'src': img_url
            }).css({'max-width': '172px', 'max-height': '64px'});
            $(this).find('a').html(img);
        });
        $('.change-form .field-logo_down').each(function () {
            var img_url = $(this).find('a').attr('href');
            var img = $('<img>').attr({
                'src': img_url
            }).css({'max-width': '172px', 'max-height': '64px'});
            $(this).find('a').html(img);
        });
    });
})(django.jQuery);
