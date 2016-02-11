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

/*var markers_inode = [
    {lat: 59.950366, lng: 30.076602, title: 'Объект 1', id: 'id 1'},
    {lat: 59.851566, lng: 30.176802, title: 'Объект 2', id: 'id 2'},
    {lat: 60.000001, lng: 30.376602, title: 'Объект 3', id: 'id 3'},
    {lat: 60.001000, lng: 30.576602, title: 'Объект 4', id: 'id 4'},
    {lat: 60.010000, lng: 30.976602, title: 'Объект 5', id: 'id 5'}
];*/

var map;
function initMap() {

    var current_area = $('.page-content .projects-page .tabs .group .btn.filter').first();
    var lat = $(current_area).data('areaLat') || 59.950366;
    var lng = $(current_area).data('areaLng') || 30.076602;
    var zoom = $(current_area).data('areaZoom') || 8;
    var center = {lat: Number(lat), lng: Number(lng)};

    map = new google.maps.Map(document.getElementById('google-map'), {
        center: center, // {lat: 59.950366, lng: 30.076602},
        zoom: zoom,     // 8,
        styles: styles,
        scrollwheel: false
    });

    var i, markers = [];

    for (i in markers_inode) {
        var latLng = new google.maps.LatLng(markers_inode[i].latitude, markers_inode[i].longitude);
        var marker = new google.maps.Marker({
            'position': latLng,
            'title': markers_inode[i].name
        });
        markers.push(marker);
        attachBubble(marker, marker.getTitle());
    }
    var markerCluster = new MarkerClusterer(map, markers);

}

function attachBubble(marker, title) {
    var bubble = new google.maps.InfoWindow({content: title});
    marker.addListener('click', function () {
        bubble.open(map, marker);
    });
}


$(document).ready(function () {
    $('.page-content .projects-page .tabs .group .btn.filter').each(function(){
        $(this).on('click', function(event){
            var lat = $(this).data('areaLat');
            var lng = $(this).data('areaLng');
            var zoom = $(this).data('areaZoom');
            var center = {lat: Number(lat), lng: Number(lng)};
            map.setCenter(center);
            map.setZoom(zoom);
        })
    });
    $.getScript("https://maps.googleapis.com/maps/api/js?key=AIzaSyC37S4JUrdlmWAB3CmczT6gL_U0pP-Dvj0&callback=initMap");
});
