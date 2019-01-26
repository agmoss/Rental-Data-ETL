function arrayToGeoJson(data){

    var jsonFeatures = [];

    data.forEach(function(point){
        var lat = point.latitude;
        var lon = point.longitude;

        var feature = {type: 'Feature',
            properties: point,
            geometry: {
                type: 'Point',
                coordinates: [lon,lat]
            },

            properties:{
                price : point.price,
                type : point._type,

            }


        };

        jsonFeatures.push(feature);
    });

    var geoJ = { type: 'FeatureCollection', features: jsonFeatures };

    return geoJ
}