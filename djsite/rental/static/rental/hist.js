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
        //title: "Distribution of Price",
        yaxis: {
            title: {
              text: 'y Axis',
              font: {
                family: customPlotLayout.axis.axisFont,
                size: customPlotLayout.axis.axisTitleSize,
                color: customPlotLayout.axis.axisColor,
              }
            },
            tickcolor: customPlotLayout.axis.axisColor,
            tickfont: {
                family: customPlotLayout.axis.axisFont,
                size: 14,
                color: customPlotLayout.axis.axisColor
              },
          },
          xaxis: {
            title: {
              text: 'x Axis',
              font: {
                family: customPlotLayout.axis.axisFont,
                size: customPlotLayout.axis.axisTitleSize,
                color: customPlotLayout.axis.axisColor
              }
            },
            tickcolor: customPlotLayout.axis.axisColor,
            tickfont: {
                family: customPlotLayout.axis.axisFont,
                size: customPlotLayout.axis.axisTickSize,
                color: customPlotLayout.axis.axisColor
              },
          },
        plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
        paper_bgcolor:customPlotLayout.background.paperBackgroundColor,
    }

    Plotly.plot(document.getElementById("histogram"), [trace], layout, {displayModeBar: false}); 

})