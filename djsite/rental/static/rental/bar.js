d3.json("http://127.0.0.1:8000/api/scatter_data", function(data) {

    var convertedData = [];
    data.forEach(function(item){
    convertedData.push([item.community, item.price__avg]);
    });
    
    var chart = c3.generate({
    bindto : '#chart',
    data: {
        columns: convertedData,
        type: 'bar'
    },
    axis: {
        x: {
          type: 'categorized',
        }
      },
      legend: {
        show: false
    },
      bar: {
        width: {
          ratio:1, //The bars will fill out the axes area
        },
      }
    });

});