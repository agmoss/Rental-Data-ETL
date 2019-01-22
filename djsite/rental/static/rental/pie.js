Plotly.d3.json('http://127.0.0.1:8000/api/pie_data', function(data){

    var allTypeNames = [] ;   
    var alldcount = [] ;
    var allCommunity = []; 
    var listofTypes = []; // uniuque
    var currentCountry;
    var currentCommunity = []; // Data on current selection
    var currentdcount = []; // Data on current selection 

    data.forEach(function(item){

        allTypeNames.push(item._type)
        alldcount.push(item.dcount);
        allCommunity.push(item.community);

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
        currentdcount = [];
        for (var i = 0 ; i < allTypeNames.length ; i++){
            if ( allTypeNames[i] === chosenItem ) {
                currentCommunity.push(allCommunity[i]);
                currentdcount.push(alldcount[i]);
            }
        }
    };

    // Default Country Data
    setBubblePlot('Apartment');

    // Actual plotting function 
    function setBubblePlot(chosenItem) {
        getTypeData(chosenItem);

        var trace1 = {
            labels: currentCommunity,
            values: currentdcount,           
            type:'pie',

        };

        var data = [trace1];

        let layout = {
            //title: "Rental Listings per Community",
            plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
            paper_bgcolor:customPlotLayout.background.paperBackgroundColor,

            showlegend : false,
    
              margin: {
                l: 5,
                r: 5,
                b: 5,
                t: 5,
                pad: 1
              },          
        }
        Plotly.newPlot('pieplotdiv', data, layout, {displayModeBar: false});
    };

    var innerContainer = document.querySelector('[data-num="1"'),
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
        setBubblePlot(itemSelector.value);
    }

    itemSelector.addEventListener('change', updateSelection, false);

});