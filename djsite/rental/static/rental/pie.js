Plotly.d3.json(domainName + 'api/pie_data', function(data){

    var allTypeNames = [] ;   
    var alldcount = [] ;
    var allCommunity = []; 
    var listofTypes = []; // uniuque
    var currentItem;
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

    // Default 
    setPlot('Condo');

    // Actual plotting function 
    function setPlot(chosenItem) {
        getTypeData(chosenItem);

        var trace1 = {
            labels: currentCommunity,
            values: currentdcount,           
            type:'pie',
            textposition: 'inside',
        };

        var data = [trace1];

        let layout = {
            plot_bgcolor:customPlotLayout.background.plotBackgroundColor,
            paper_bgcolor:customPlotLayout.background.paperBackgroundColor,

            showlegend : false,

            textinfo:'none',
  
              margin: {
                l: 5,
                r: 5,
                b: 5,
                t: 5,
                pad: 1
              }, 
              
            autosize : true, // Important for responsiveness
        }

        Plotly.newPlot(pDiv, data, layout, {displayModeBar: false});
    };

    var innerContainer = document.querySelector('[data-num="1"'),
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
