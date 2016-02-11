(function($){
    $(document).ready(function () {
        $('<div>')
            .attr('id', 'google-map')
            .height('400px')
            .width('100%').appendTo('.form-row.field-latitude.field-longitude');
        $.getScript('https://maps.googleapis.com/maps/api/js?key=AIzaSyC37S4JUrdlmWAB3CmczT6gL_U0pP-Dvj0&callback=initMap');
    });
})(django.jQuery);
