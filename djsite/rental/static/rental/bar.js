Plotly.d3.json('http://127.0.0.1:8000/api/scatter_data', function(data){

    let xData = [];
    let yData = [];
      
    data.forEach(function(item){

        xData.push(item.community);
        yData.push(item.price__avg);

    });

    let trace = {
        x: xData,
        y: yData,

        marker: {
            color: 'rgba(44, 160, 101, 0.5)'},
            type:'bar',
        }

        let layout = {
            title: "Average Price Per Community",
            yaxis:{title: "Average Price"},
            xaxis: {title: "Community"} 
        }

    Plotly.plot(document.getElementById("bar_chart"), [trace],layout,  {displayModeBar: false}); 

})
