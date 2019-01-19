var data = []
var queriedData = []
var json = [];

  // Get the data
  $.ajax({

    url: 'http://127.0.0.1:8000/api/map_data',
    type: 'GET',
    dataType: 'json',
    async: false,

    success : function(data) {

        queriedData.push(data);
        json = JSON.stringify(data);
      }, 
      
        error : function(req, err) {
        alert: ("Request:"+ JSON.stringify(req));
        }
    });

    var obj = $.parseJSON(json)
    console.log(obj)

    // Map 
    var map = L.map('map',{
        }).setView([51.0486, -114.0708], 12);

    var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);


    //Add the json to the map