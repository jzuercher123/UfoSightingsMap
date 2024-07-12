function onEachFeature(feature, layer) {
    var coords = new Array();
    coords.push([feature.geometry.coordinates[1], feature.geometry.coordinates[0]]);
    var popupContent = " <strong>Name:</strong> " +
        feature.properties.Name +
        " <br /><br /> " +
        " <strong>Description:</strong> " +
        feature.properties.description +
        " <br /><br /> " +
        " <strong>LAT/LONG:</strong> " +
        " <a href='https://www.google.com/maps/search/?api=1&query=" + feature.geometry.coordinates[1] + "," + feature.geometry.coordinates[0] + "'" + " target='_blank'>" + feature.geometry.coordinates[1] + "," + feature.geometry.coordinates[0] + "</a>" +
        " <br /><br /> " +
        "<strong>Geometry Type:</strong> " +
        feature.geometry.type;

    if (feature.properties && feature.properties.popupContent) {
        popupContent += feature.properties.popupContent;
    }

    layer.bindPopup(popupContent);

}