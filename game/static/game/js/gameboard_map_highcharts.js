// Initiate the chart

var width = window.innerWidth-300,
    height = window.innerHeight-100;

function highcharts_map(data, connection){

    Highcharts.mapChart('container', {
        chart: {
        zoom:'xy',
        width: width,
        height: height,
        backgroundColor: '#d2d2d2',
        marginTop: 0,
        },
        mapNavigation: {
            enabled: false
        },
        legend:{
            enabled:false
        },
        credits:{
            enabled:false
        },
        exporting: {
            enabled: false
        },
        title:{
            text:''
        },
        tooltip: {
            enabled: false
        },
        plotOptions: {
            series: {
                marker: {
                    enabled: true,
                    symbol: 'circle',
                    radius: 7
                },
                point: {
                    events: {
                        click: function () {
                            popUp(this.id);
                        }
                    }
                }
            }
        },
        series: [{
            // Use the gb-all map with no data as a basemap
            mapData: Highcharts.maps['custom/world'],
            name: 'Basemap',
            borderColor: '#A0A0A0',
            nullColor: '#415993',
            showInLegend: false
        }, {
            name: 'Separators',
            type: 'mapline',
            data: Highcharts.geojson(Highcharts.maps['custom/world'], 'mapline'),
            color: '#707070',
            showInLegend: false,
            enableMouseTracking: false
        }, {
            // Specify points using lat/lon
            type: 'mappoint',
            name: 'Cities',
            color: Highcharts.getOptions().colors[1],
            data: data
        }].concat(connection)
    });
}

function popUp(city){
    $('#pop_up').show();
    $('#city_pop').html(city);
      url = getInfectionMap;
      data = {
        'roomId': roomId,
        'user': username,
        'city': city
      };
      $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: function(msg) {
            $('#infectionBlockBlue').html(msg["cityInfo"]["blue"]);
            $('#infectionBlockBlack').html(msg["cityInfo"]["black"]);
            $('#infectionBlockPurple').html(msg["cityInfo"]["purple"]);
            $('#infectionBlockRed').html(msg["cityInfo"]["red"]);
            $('#infectionBlockYellow').html(msg["cityInfo"]["yellow"]);
            $('#research_center').prop('checked', msg["cityInfo"]["researchCenter"]);
        }
      });
}

function increment_infection(color){
    city = $('#city_pop').text();
    var table = $('#infection_table').DataTable();
    var idx = table.columns( 0 ).data().eq( 0 );

    url = incrementInfection;
    data = {
        'roomId': roomId,
        'user': username,
        'city': city,
        'color': color,
        'order': idx.join(",")
    };
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: function(msg) {
          socket.send(JSON.stringify({
            "command": "updateinfectionmap",
            "roomId": roomId,
            "user": username,
          }));
          color = color.charAt(0).toUpperCase() + color.slice(1)
          $('#infectionBlock'+color).html(parseInt($('#infectionBlock'+color).text())+1);
        }
    });
}

function decrement_infection(color){
    city = $('#city_pop').text();
    var table = $('#infection_table').DataTable();
    var idx = table.columns( 0 ).data().eq( 0 );

    url = decrementInfection;
    data = {
        'roomId': roomId,
        'user': username,
        'city': city,
        'color': color,
        'order': idx.join(",")
    };
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: function(msg) {
          socket.send(JSON.stringify({
            "command": "updateinfectionmap",
            "roomId": roomId,
            "user": username,
          }));
          color = color.charAt(0).toUpperCase() + color.slice(1)
          $('#infectionBlock'+color).html(parseInt($('#infectionBlock'+color).text())-1);
        }
    });
}

$('#research_center').change(function() {
    url = toggleResearch;
    city = $('#city_pop').text();
    data = {
        'roomId': roomId,
        'city': city
    };
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: function(msg) {
            socket.send(JSON.stringify({
                "command": "updateinfectionmap",
                "roomId": roomId,
                "user": username,
              }));
        }
    });
})

function set_current_location(){
    city = $('#city_pop').text();
    url = setLocation;
    data = {
        'roomId': roomId,
        'user': username,
        'city': city,
    };
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: function(msg) {
          socket.send(JSON.stringify({
            "command": "updatecurrentlocation",
            "roomId": roomId,
            "user": username,
          }));
        }
    });
}
