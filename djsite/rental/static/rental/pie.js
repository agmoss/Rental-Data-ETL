Plotly.d3.json('http://127.0.0.1:8000/api/pie_data', function(data){

    let xData = [];
    let yData = [];
    

    var colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)', 'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)', 'rgba(255, 140, 184, 0.5)', 'rgba(79, 90, 117, 0.5)', 'rgba(222, 223, 0, 0.5)'];
      
    data.forEach(function(item){

        xData.push(item.community);
        yData.push(item.dcount);

    });

    let trace = {
        labels: xData,
        values: yData,

        marker: {
            colors: colors},
            type:'pie',
        }

    let layout = {
        //title: "Rental Listings per Community",
        plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
        paper_bgcolor:customPlotLayout.background.paperBackgroundColor,
        legend: {
            orientation : 'h',
            // traceorder: 'normal',
            font: {
                family: customPlotLayout.axis.axisFont,
                size: customPlotLayout.axis.axisTickSize,
                color: customPlotLayout.axis.axisColor
              }
          },

          margin: {
            l: 5,
            r: 5,
            b: 5,
            t: 5,
            pad: 1
          },
    }

    Plotly.plot(document.getElementById("pie_chart"), [trace], layout,  {displayModeBar: false}); 

})