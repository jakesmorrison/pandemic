function my_map(countries_json, lat_long){
//var width = 1000,
//    height = 480
//
//
//var map = d3.geomap()
//        .geofile(countries_json);
//
//var svg = d3.select('#map')
//            .append("svg")
//            .attr("width", width)
//            .attr("height", height);
//
//var projection = d3.geo.equirectangular();
//
//var path = d3.geo.path()
//    .projection(projection);
//
//var graticule = d3.geo.graticule();
//
//var g = svg.append("g");
//
//aa = [-122.490402, 37.786453];
//bb = [-122.389809, 37.72728];
//g.selectAll("circle")
//    .data([aa,bb]).enter()
//    .append("circle")
//    .attr("cx", function (d) { console.log(projection(d)); return projection(d)[0]; })
//    .attr("cy", function (d) { return projection(d)[1]; })
//    .attr("r", "8px")
//    .attr("fill", "red")
//
//
//svg.call(map.draw, map)

var width = 1200,
    height = 900,
    radius = 6,
    fill = "rgba(255, 49, 255, 0.388)",
    stroke = "rgba(0, 0, 0, 0.5)",
    strokeWidth = 0.1;

var width = window.innerWidth,
    height = window.innerHeight;


var projection = d3.geo.equirectangular()
    .scale(153)
    .translate([width / 2, height / 2])
    .precision(.1);

var path = d3.geo.path()
    .projection(projection);

var graticule = d3.geo.graticule();

var svg = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height)

var zoom = d3.behavior.zoom()
  .scaleExtent([1, 20])
  .on("zoom", zoomed);

var g = svg.append("g")
    .attr("class", "g_main");


// This invisible rect catches events for the zooming interaction.
var rect = svg.append("rect")
  .attr("width", width)
  .attr("height", height)
  .style("fill", "none")
  .style("pointer-events", "all")
  .call(zoom);

g.append("path")
  .datum(graticule)
  .attr("class", "graticule")
  .attr("d", path);

function zoomed(){
  g.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}

d3.json("https://gist.githubusercontent.com/mbostock/4090846/raw/d534aba169207548a8a3d670c9c2cc719ff05c47/world-50m.json", function(error, world) {
  if (error) throw error;
  g.insert("path", ".graticule")
      .datum(topojson.feature(world, world.objects.land))
      .attr("class", "land")
      .attr("d", path);

  g.insert("path", ".graticule")
      .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
      .attr("class", "boundary")
      .attr("d", path);


  d3.csv(lat_long, function(error, data) {
    var points = g.selectAll("circle")
    .data(data).enter()
    .append("circle")
    .attr("cx", function (d) {return projection([d.long,d.lat])[0]; })
    .attr("cy", function (d) {return projection([d.long,d.lat])[1]; })
    .attr("r", "5px")
    .attr("fill", "white")
    .attr("stroke-width", "5px")
    .attr("stroke",  function (d) {return d.color; })
    .on('mouseover', handleMouseOver);


    var text = g.selectAll("text")
    .data(data).enter()
    .append("text");

    var textLabels = text
       .attr("x", function(d) { return projection([d.long,d.lat])[0]; })
       .attr("y", function(d) {return projection([d.long,d.lat])[1] -10; })
       .text( function (d) { return d.city; })
       .attr("font-family", "sans-serif")
       .attr("font-size", "6px")
       .attr("font-weight", "bold")
       .attr("fill", "white");

    function handleMouseOver(d, i) {
        console.log("test");
    }
  })
});
function type(d){

  // This should actually be [d.longitude, d.latitude]
  // It looks like these are reversed in the data.
  d.projected = projection([d.latitude, d.longitude]);
  return d;
}

d3.select(self.frameElement).style("height", height + "px");

}