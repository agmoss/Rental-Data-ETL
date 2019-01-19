Plotly.d3.json('http://127.0.0.1:8000/api/hist_data', function(data){

    let xData = [];
      
    data.forEach(function(item){

        xData.push(item.price);

    });

    let trace = {
        x: xData,

        marker: {
            color: 'rgba(44, 160, 101, 0.5)'},
            type:'histogram',
        }

    let layout = {
        title: "Distribution of Price",
        yaxis:{title: "Frequency"},
        xaxis: {title: "Price"} 
    }

    Plotly.plot(document.getElementById("histogram"), [trace], layout, {displayModeBar: false}); 

})