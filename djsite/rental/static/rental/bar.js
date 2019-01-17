// set the dimensions of the canvas
var margin = {top: 20, right: 20, bottom: 70, left: 40},
  width = 1200 - margin.left - margin.right,
  height = 800 - margin.top - margin.bottom;


// set the ranges
var x = d3.scale.ordinal().rangeRoundBands([0, width], .1);

var y = d3.scale.linear().range([height, 0]);

// define the axis
var xAxis = d3.svg.axis()
  .scale(x)
  .orient("bottom")

var yAxis = d3.svg.axis()
  .scale(y)
  .orient("left")
  .ticks(10);              
              
// add the SVG element
var svg = d3.select("#svg").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform", 
        "translate(" + margin.left + "," + margin.top + ")");


// load the data
d3.json("{% url 'box_data' %}", function(error, data) {

  data.forEach(function(d) {
      d.community = d.community;
      d.dcount = +d.dcount;
  });

// scale the range of the data
x.domain(data.map(function(d) { return d.community; }));
y.domain([0, d3.max(data, function(d) { return d.dcount; })]);

// add axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
  .selectAll("text")
    .style("text-anchor", "end")
    .attr("dx", "-.8em")
    .attr("dy", "-.55em")
    .attr("transform", "rotate(-90)" );

svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
  .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 5)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Frequency");


// Add bar chart
svg.selectAll("bar")
    .data(data)
  .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) { return x(d.community); })
    .attr("width", x.rangeBand())
    .attr("y", function(d) { return y(d.dcount); })
    .attr("height", function(d) { return height - y(d.dcount); });

});