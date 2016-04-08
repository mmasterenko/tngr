(function($){
    $(document).ready(function () {

        if($('#id_text').length) {
            CKEDITOR.replace('id_text', {
                language: 'ru',
                height: 500
            });
        }

        if($('#id_desc').length) {
            CKEDITOR.replace('id_desc', {
                language: 'ru',
                height: 500
            });
        }

    });
})(django.jQuery);
