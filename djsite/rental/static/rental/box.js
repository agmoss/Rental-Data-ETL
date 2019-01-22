Plotly.d3.json('http://127.0.0.1:8000/api/box_data', function(data){

    let xData = [];
    let yData = [];
      
    data.forEach(function(item){

        xData.push(item.quadrant);
        yData.push(item.price);

    });

    let trace = {
        x: xData,
        y: filterOutliers(yData),

        marker: {
            color: 'rgba(44, 160, 101, 0.5)'},
            type:'box',
        }

        let layout = {
            //title: "Price Distribution per Quadrant",
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

            margin: {
                l: 10,
                r: 10,
                b: 50,
                t: 1,
                pad: 4
              },
        }

    Plotly.plot(document.getElementById("box_plot"), [trace],layout,  {displayModeBar: false}); 

})