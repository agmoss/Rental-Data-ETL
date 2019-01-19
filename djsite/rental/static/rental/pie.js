d3.json("http://127.0.0.1:8000/api/pie_data", function(data) {

    var convertedData = [];
    data.forEach(function(item){
    convertedData.push([item.community, item.dcount]);
    });
    
    var chart = c3.generate({
    bindto : '#chart2',
    data: {
        columns: convertedData,
        type: 'pie'
    },
    
    });

});