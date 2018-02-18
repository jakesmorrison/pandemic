var hidden = false;
var toggle = 0;
function stock_spline(data1,data2){
    var chart = Highcharts.stockChart('stock_stacked', {
            chart: {
                borderWidth: 0,
                backgroundColor: null,
            },
            exporting: { enabled: false },
            credits: { enabled: false },
            rangeSelector: { enabled: false },
            title: {
                text: ''
            },
            xAxis: {
                type: 'datetime',
                minTickInterval: 20000,
                tickPositioner: function (min, max) {
                  var ticks = this.series[0].processedXData.slice(); // get point positions copy
                  ticks.info = this.tickPositions.info;              // copy format for labels
                  return ticks;                                      // return new ticks
                },
                range: 14 * 24 * 3600 * 1000,
            },
            yAxis: [{
                min: 0,
                labels: {
                    align: 'right',
                    x: -3
                },
                title: {
                    text: 'Portfolio Value $'
                },
                gridLineWidth: 0,
                tickLength: 5,
                tickWidth: 1,
                height: '35%',
                lineWidth: 2,
                resize: {
                    enabled: true
                }
            }, {
                resize: {
                    enabled: true
                },
                labels: {
                    align: 'right',
                    x: -3,
                    color: 'white',
                    fontSize:'12px',
                    textShadow: false,
                },
                opposite: true,
                title: {
                    text: 'zzz'
                },
                plotLines: [{
                    value: 0,
                    color: 'rgb(112,134,158)',
                    width: 3,
                    zIndex: 5
                }],
                top: '40%',
                height: '60%',
                offset: 0,
                lineWidth: 2,
                stackLabels: {
                    enabled: true,
                    style: {
                        fontWeight: 'bold',
                        color:  'black',
                        textShadow: false,
                        cursor: 'default'
                    },
                },
            }],
            tooltip: {
                split: false,
                formatter: function () {
                    if ((typeof this.key) == (typeof "test")){
                        return '<span>'+this.key+'('+this.point.id+')'+'</span>'+'<span>'+": $"+this.y+'</span>'
                    }
                    else{
                        gain = get_daily_gain(this.point.index);
                        d = new Date(0);
                        d.setUTCSeconds(this.key/1000);
                        return '<span>'+d.toString().split("00")[0]+'</span>'+'<span>'+"<br>Total: $"+this.y+'</span><br><span>Daily Gain: '+gain+'%</span>'
                    }
                }
            },

            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels:{
                        enabled: true,
                        style: {
                            fontWeight: 'bold',
                            color: 'black',
                            textShadow: false,
                            cursor: 'default',
                            textOutline: false,
                            zIndex:100
                        },
                        formatter: function () {
                            if ( this.point.y != 0 ){
                                return this.key
                            }
                        }
                    },
                    borderColor: 'white',
                    borderWidth: 3,
                    point: {
                        events: {
                            click: function () {
                                isolate_stock(this.options.name);
                            }
                        }
                    },
                },
                areaspline: {
                    color: 'rgb(47, 58, 69)',
                    fillColor: {
                        linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1},
                        stops: [
                            [0, 'rgb(47, 58, 69)'],
                            [1, 'rgb(112,134,158)'],
                        ]
                    },
                    lineWidth: 6,
                    marker: {
                        enabled: false
                    },
                    shadow: false,
                    states: {
                        hover: {
                            lineWidth: 3
                        }
                    },
                    threshold: null
                }
            },
            series: [{
                type: 'areaspline',
                data: data1,
            }, {
                type: 'column',
                stacking: 'normal',
                data: data2,
                yAxis: 1,
                dataGrouping: {
                    enabled: false
                }
            }],
        });


    function isolate_stock(symbol){
        if(hidden === false){
            new_data = [];
            for(x=0;x<data2.length;x++){
                if( symbol === data2[x]["name"] ){
                    new_data.push(data2[x])
                }
            }
            hidden = true
            chart.series[1].setData(new_data);
        }
        else{
            hidden = false
            chart.series[1].setData(data2);

        }
    }

    $('#toggle').click(function(){
        toggle_data = [];
        if(toggle===0){
            toggle = 1;
            for(x=0;x<data2.length;x++){
                if( data2[x]["y"] > 0 ){
                    toggle_data.push(data2[x])
                }
            }
            chart.series[1].setData(toggle_data);
        }
        else if(toggle===1){
            toggle = 2;
            for(x=0;x<data2.length;x++){
                if( data2[x]["y"] < 0 ){
                    toggle_data.push(data2[x])
                }
            }
            chart.series[1].setData(toggle_data);
        }
        else{
            toggle = 0;
            chart.series[1].setData(data2);
        }
    });

    function get_daily_gain(index){
        prev = index - 1;
        if (prev >=0 ){
            x1 = chart.series[0].data[index].y
            x2 = chart.series[0].data[prev].y
            return (((x1-x2)/x2)*100).toFixed(2);
        }
        else{
            return 0
        }
    }
}