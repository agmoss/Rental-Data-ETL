Plotly.d3.json(domainName + 'api/map_data', function(data){

    var map = L.map('map',{
        preferCanvas: true
    }).setView([51.0486, -114.0708], 12);
    

    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 19
    }).addTo(map);

    // Convert array to geoJson with function
    geoJson = arrayToGeoJson(data);

    console.log(geoJson)

    // Custom circlemarkers
    var geojsonMarkerOptions = {
        radius: 3,
        fillColor: "#ff7800",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

    L.geoJSON(geoJson, {
        pointToLayer: function (feature, latlng) {

            var mypopup = L.popup().setContent(
                '<h3>' + feature.properties.type + '</h3>' 
                + '<h4>' + "Price:" + feature.properties.price + '</h4>'
                );

            var mymarker = L.circleMarker(latlng, geojsonMarkerOptions);
      
            mymarker.bindPopup(mypopup);
            return mymarker;               
        }
      }).addTo(map);

})