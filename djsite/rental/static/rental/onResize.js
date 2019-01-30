// Define plot divs for the Plotly functions and the resize event (maybe put this somewhere else)
var bDiv = document.getElementById('scatterplotdiv')
var pDiv = document.getElementById('pieplotdiv')
var boxDiv = document.getElementById('boxplotdiv')
var hDiv = document.getElementById('distplotdiv')
var heatDiv = document.getElementById('heatdiv')

window.addEventListener("resize", function(){

    Plotly.relayout(bDiv, {
        width: 0.9 * bDiv.innerWidth,
        height: 0.9 * bDiv.innerHeight
    })

    Plotly.relayout(pDiv, {
        width: 0.9 * pDiv.innerWidth,
        height: 0.9 * pDiv.innerHeight
    })

    Plotly.relayout(boxDiv, {
        width: 0.9 * boxDiv.innerWidth,
        height: 0.9 * boxDiv.innerHeight
    })

    Plotly.relayout(hDiv, {
        width: 0.9 * hDiv.innerWidth,
        height: 0.9 * hDiv.innerHeight
    })

    Plotly.relayout(heatDiv, {
        width: 0.9 * heatDiv.innerWidth,
        height: 0.9 * heatDiv.innerHeight
    })
    
});