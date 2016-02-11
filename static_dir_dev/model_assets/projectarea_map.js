var styles = [
    {
        "stylers": [
            { "hue": "#00b2ff" },
            { "saturation": 29 },
            { "lightness": -14 },
            { "gamma": 0.69 }
        ]
    },{
        "featureType": "water",
        "stylers": [
            { "lightness": -43 },
            { "hue": "#00b2ff" },
            { "saturation": -42 }
        ]
    },{
        "featureType": "landscape.natural",
        "stylers": [
            { "hue": "#ff0000" },
            { "saturation": -85 },
            { "lightness": 65 }
        ]
    }
];

var map, marker;
function initMap() {
    var $ = django.jQuery;
    var lat = $('#id_latitude').val();
    var lng = $('#id_longitude').val();
    var zoom = Number( $('#id_zoom').val() );
    var latLng = {lat: Number(lat), lng: Number(lng)};
    map = new google.maps.Map(document.getElementById('google-map'), {
        center: latLng, // {lat: 59.950366, lng: 30.076602},
        zoom: zoom,     // 8,
        styles: styles,
        scrollwheel: false
    });

    map.addListener('dragend', function() {
        var center = map.getCenter();
        django.jQuery('#id_latitude').val(center.lat());
        django.jQuery('#id_longitude').val(center.lng());
    });

    map.addListener('zoom_changed', function() {
        var zoom = map.getZoom();
        django.jQuery('#id_zoom').val(zoom);
    });
}
