(function($){
    $(document).ready(function () {
        CKEDITOR.replace('id_desc', {language: 'ru'});
        $('<div>')
            .attr('id', 'google-map')
            .height('400px')
            .width('100%').appendTo('.form-row.field-latitude.field-longitude');
        $.getScript('https://maps.googleapis.com/maps/api/js?key=AIzaSyC37S4JUrdlmWAB3CmczT6gL_U0pP-Dvj0&callback=initMap', function(){
            var lat = $('#id_latitude').val();
            var lng = $('#id_longitude').val();
            var latLng = {lat: Number(lat), lng: Number(lng)};
            setTimeout(function () {
                window.marker = window.marker || new google.maps.Marker({
                        position: latLng,
                        map: map
                    });
                window.marker.setPosition(latLng);
            }, 1500);
        });
    });
})(django.jQuery);
