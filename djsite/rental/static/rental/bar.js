Plotly.d3.json('http://127.0.0.1:8000/api/scatter_data', function(data){

    var allTypeNames = [] ;   
    var allprice__avg = [] ;
    var allCommunity = []; 
    var listofTypes = []; // uniuque
    var currentSelection;
    var currentCommunity = []; // Data on current selection
    var currentprice__avg = []; // Data on current selection 

    data.forEach(function(item){

        allTypeNames.push(item._type)
        allprice__avg.push(item.community);
        allCommunity.push(item.price__avg);

    });

    // Makes things uniuque
    for (var i = 0; i < allTypeNames.length; i++ ){ 
        if (listofTypes.indexOf(allTypeNames[i]) === -1 ){
            listofTypes.push(allTypeNames[i]);
        }
    }
   
    // Gets current selection
    function getTypeData(chosenItem) {
        currentCommunity = [];
        currentprice__avg = [];
        for (var i = 0 ; i < allTypeNames.length ; i++){
            if ( allTypeNames[i] === chosenItem ) {
                currentCommunity.push(allCommunity[i]);
                currentprice__avg.push(allprice__avg[i]);
            }
        }
    };

    // Default Country Data
    setPlot('Apartment');

    // Actual plotting function 
    function setPlot(chosenItem) {
        getTypeData(chosenItem);

        var trace1 = {
            x: currentprice__avg,
            y: currentCommunity,
            mode: 'markers',
            type: 'bar',
            marker: {
                color: colorScheme.primary,
                //size: 12,
            }
        };

        var data = [trace1];

        let layout = {
            //title: "Average Price Per Community",
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
                    size: customPlotLayout.axis.axisTickSize,
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
                l: 100,
                r: 10,
                b: 100,
                t: 1,
                pad: 4
              },
        }
        Plotly.newPlot('scatterplotdiv', data, layout,{displayModeBar: false});
    };

    var innerContainer = document.querySelector('[data-num="0"'),
        plotEl = innerContainer.querySelector('.plot'),
        itemSelector = innerContainer.querySelector('.selection');

    function assignOptions(textArray, selector) {
        for (var i = 0; i < textArray.length;  i++) {
            var currentOption = document.createElement('option');
            currentOption.text = textArray[i];
            selector.appendChild(currentOption);
        }
    }

    assignOptions(listofTypes, itemSelector);

    function updateSelection(){
        setPlot(itemSelector.value);
    }

    itemSelector.addEventListener('change', updateSelection, false);

});