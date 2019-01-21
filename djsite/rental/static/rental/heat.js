Plotly.d3.json('http://127.0.0.1:8000/api/corr_data', function(error,data){

    if (error) return console.warn(error);

    var colorscale =  [
        ['0.0', 'rgb(165,0,38)'],
        ['0.111111111111', 'rgb(215,48,39)'],
        ['0.222222222222', 'rgb(244,109,67)'],
        ['0.333333333333', 'rgb(253,174,97)'],
        ['0.444444444444', 'rgb(254,224,144)'],
        ['0.555555555556', 'rgb(224,243,248)'],
        ['0.666666666667', 'rgb(171,217,233)'],
        ['0.777777777778', 'rgb(116,173,209)'],
        ['0.888888888889', 'rgb(69,117,180)'],
        ['1.0', 'rgb(49,54,149)'],
      ]

    var d = [{
        x: data.xValues,
        y: data.yValues,
        z: data.zValues,
        colorscale: colorscale,
        type: 'heatmap',
    }]

    var layout = {
        //title: 'Correlation',
        annotations: [],
        yaxis: {
          ticks: '',
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
          ticks: '',
          side: 'top',
          title: {
            text: 'x Axis',
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
        plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
        paper_bgcolor:customPlotLayout.background.paperBackgroundColor,
      };

    Plotly.plot(document.getElementById("heat"), d, layout, {displayModeBar: false}); 

})