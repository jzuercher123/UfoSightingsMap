var map = L.map('map').setView([29.8830556, -97.9411111], 13);
        L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=WFS69K0G42GklCPTMZmf', {
            maxZoom: 20,
        }).addTo(map);
        $.getJSON('../data/test_data/test_points.geojson', function(data) {
    L.geoJSON(data).addTo(map);
});