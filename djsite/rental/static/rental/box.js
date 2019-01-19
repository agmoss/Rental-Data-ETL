Plotly.d3.json('http://127.0.0.1:8000/api/box_data', function(data){

    let xData = [];
    let yData = [];
      
    data.forEach(function(item){

        xData.push(item.quadrant);
        yData.push(item.price);

    });

    let trace = {
        x: xData,
        y: yData,

        marker: {
            color: 'rgba(44, 160, 101, 0.5)'},
            type:'box',
        }

        let layout = {
            title: "Price Distribution per Quadrant",
            yaxis:{title: "Average Price"},
            xaxis: {title: "City Quadrant"} 
        }

    Plotly.plot(document.getElementById("box_plot"), [trace],layout,  {displayModeBar: false}); 

})