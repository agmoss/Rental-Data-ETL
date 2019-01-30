Plotly.d3.json(domainName + 'api/box_data', function(data){

    var allTypeNames = [] ;   
    var allQuadrant = [] ;
    var allPrice = []; 
    var listofTypes = []; // uniuque
    var currentSelection;
    var currentQuadrant = []; // Data on current selection
    var currentPrice = []; // Data on current selection 

    data.forEach(function(item){

        allTypeNames.push(item._type)
        allQuadrant.push(item.quadrant);
        allPrice.push(item.price);

    });

    // Makes things uniuque
    for (var i = 0; i < allTypeNames.length; i++ ){ 
        if (listofTypes.indexOf(allTypeNames[i]) === -1 ){
            listofTypes.push(allTypeNames[i]);
        }
    }
   
    // Gets current selection
    function getTypeData(chosenItem) {
        currentQuadrant = [];
        currentPrice = [];
        for (var i = 0 ; i < allTypeNames.length ; i++){
            if ( allTypeNames[i] === chosenItem ) {
                currentQuadrant.push(allQuadrant[i]);
                currentPrice.push(allPrice[i]);
            }
        }
    };

    // Default Country Data
    setPlot('Apartment');

    // Actual plotting function 
    function setPlot(chosenItem) {
        getTypeData(chosenItem);


        var trace1 = {
            x: currentQuadrant,
            y: filterOutliers(currentPrice),
            mode: 'markers',
    
            marker: {
                color: colorScheme.primary},
                type:'box',
            }
    
            let layout = {
                yaxis: {
                    title: {
                      text: 'Rent per Month',
                      font: {
                        size: customPlotLayout.axis.axisTitleSize,
                        color: customPlotLayout.axis.axisColor,
                      }
                    },
                    tickcolor: customPlotLayout.axis.axisColor,
                    tickfont: {
                        size: 14,
                        color: customPlotLayout.axis.axisColor
                      },
                      automargin : true,
                  },
                  xaxis: {
                    title: {
                      text: 'Quadrant',
                      font: {
                        size: customPlotLayout.axis.axisTitleSize,
                        color: customPlotLayout.axis.axisColor
                      }
                    },
                    tickcolor: customPlotLayout.axis.axisColor,
                    tickfont: {
                        size: customPlotLayout.axis.axisTickSize,
                        color: customPlotLayout.axis.axisColor
                      },
                      automargin : true,
                  },
                plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
                paper_bgcolor:customPlotLayout.background.paperBackgroundColor,
    
                margin: {
                    l: 50,
                    r: 10,
                    b: 50,
                    t: 1,
                    pad: 1
                  },

                autosize : true, // Important for responsiveness
            }

        var data = [trace1];

        Plotly.newPlot(boxDiv, data, layout,{displayModeBar: false});
    };

    var innerContainer = document.querySelector('[data-num="2"'),
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