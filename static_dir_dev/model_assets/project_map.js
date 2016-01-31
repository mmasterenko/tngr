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
    map = new google.maps.Map(document.getElementById('google-map'), {
        center: {lat: 59.950366, lng: 30.076602},
        zoom: 8,
        styles: styles,
        scrollwheel: false
    });

    map.addListener('click', function(e) {
        placeMarker(e.latLng);
    });
}

function placeMarker(latLng) {
    marker = marker || new google.maps.Marker({
            position: latLng,
            map: map
        });
    marker.setPosition(latLng);
    django.jQuery('#id_latitude').val(latLng.lat());
    django.jQuery('#id_longitude').val(latLng.lng());
}
