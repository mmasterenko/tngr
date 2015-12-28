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

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('google-map'), {
        center: {lat: 59.950366, lng: 30.076602},
        zoom: 8,
        styles: styles,
        scrollwheel: false
    });
}
