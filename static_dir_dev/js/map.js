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

var markers_inode = [
    {lat: 59.950366, lng: 30.076602, title: 'Объект 1', id: 'id 1'},
    {lat: 59.851566, lng: 30.176802, title: 'Объект 2', id: 'id 2'},
    {lat: 60.000001, lng: 30.376602, title: 'Объект 3', id: 'id 3'},
    {lat: 60.001000, lng: 30.576602, title: 'Объект 4', id: 'id 4'},
    {lat: 60.010000, lng: 30.976602, title: 'Объект 5', id: 'id 5'}
];

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('google-map'), {
        center: {lat: 59.950366, lng: 30.076602},
        zoom: 8,
        styles: styles,
        scrollwheel: false
    });

    var i, markers = [];

    for (i in markers_inode) {
        var latLng = new google.maps.LatLng(markers_inode[i].lat, markers_inode[i].lng);
        var marker = new google.maps.Marker({
            'position': latLng,
            'title': markers_inode[i].title,
            //'label': 'метка',
            'teng_id': markers_inode[i].id
        });
        markers.push(marker);
        marker.addListener('click', function() {
            //map.setCenter(this.getPosition());
            console.log(this.teng_id)
            alert(this.teng_id)
        });
    }
    //var markerCluster = new MarkerClusterer(map, markers);

}
