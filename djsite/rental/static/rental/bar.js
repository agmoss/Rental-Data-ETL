Plotly.d3.json(domainName +'api/scatter_data', function(data){

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

    // Default Data
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
            }
        };

        var data = [trace1];

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
                    size: customPlotLayout.axis.axisTickSize,
                    color: customPlotLayout.axis.axisColor
                  },
                  automargin : true,
              },
              xaxis: {
                title: {
                  text: 'Community',
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

                tickangle: (45),
                ticks: 'outside',
              },
            plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
            paper_bgcolor:customPlotLayout.background.paperBackgroundColor,

            margin: {
                l: 100,
                r: 50,
                b: 100,
                t: 1,
                pad: 4
              },

              autosize : true, // Important for responsiveness
        }

        var bDiv = document.getElementById('scatterplotdiv')

        Plotly.newPlot(bDiv, data, layout,{displayModeBar: false},{responsive: true});

        // Where to put this?
        window.onresize = function() {
            Plotly.relayout(bDiv, {
                width: 0.9 * bDiv.innerWidth,
                height: 0.9 * bDiv.innerHeight
            }),
        
            Plotly.relayout(pDiv, {
                width: 0.9 * pDiv.innerWidth,
                height: 0.9 * pDiv.innerHeight
            })
            }       
    };

    var innerContainer = document.querySelector('[data-num="0"'),
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