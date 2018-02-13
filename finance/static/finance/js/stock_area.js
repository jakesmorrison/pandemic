var hidden = false;
function stock_spline(data1,data2){
    var chart = Highcharts.stockChart('stock_stacked', {
            chart: {
                borderWidth: 0,
                backgroundColor: null,
            },
            exporting: { enabled: false },
            credits: {enabled: false },
            rangeSelector: {enabled: false},
            title: {
                text: ''
            },
            xAxis: {
                type: 'datetime',
//                showLastLabel: false,
//                endOnTick: true,
//                range: 14 * 24 * 3600 * 1000,
//                crosshair: true,
            },
            yAxis: [{
                min: 0,
                labels: {
                    align: 'right',
                    x: -3
                },
                title: {
                    text: 'Portfolio Value'
                },
//                gridLineWidth: 0,
//                tickLength: 5,
//                tickWidth: 1,
//                height: '35%',
//                lineWidth: 2,
//                resize: {
//                    enabled: true
//                }
            }, {
                labels: {
                    align: 'right',
                    x: -3,
                    color: 'white',
                    fontSize:'12px',
                    textShadow: false,
                },
                opposite: true,
                title: {
                    text: 'Dollar Change ($)'
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
//                stackLabels: {
//                    enabled: true,
//                    style: {
//                        fontWeight: 'bold',
//                        color:  'black',
//                        textShadow: false,
//                        cursor: 'default'
//                    }
//                },

            }],

//            tooltip: {
//                split: false,
//                formatter: function () {
//                    if ((typeof this.key) == (typeof "test")){
//                        return '<span>'+this.key+'</span>'+'<span>'+": $"+this.y+'</span>'
//                    }
//                    else{
//                        d = new Date(0);
//                        d.setUTCSeconds(this.key/1000);
//                        return '<span>'+d.toString().split("00")[0]+'</span>'+'<span>'+"<br>$"+this.y+'</span>'
//                    }
//                }
//            },

            plotOptions: {
                column: {
                    stacking: 'normal',
//                    dataLabels:{
//                        enabled: true,
//                        style: {
//                            fontWeight: 'bold',
//                            color: 'black',
//                            textShadow: false,
//                            cursor: 'default',
//                            textOutline: false,
//                            zIndex:100
//                        },
//                        formatter: function () {
//                            if ( this.point.y != 0 ){
//                                console.log(this)
//                                return this.key
//                            }
//                        }
//                    },
                    borderColor: 'white',
                    borderWidth: 3,
//                    point: {
//                        events: {
//                            click: function () {
//                                isolate_stock(this.options.name);
//                            }
//                        }
//                    },
                },
                areaspline: {
                    color: 'rgb(47, 58, 69)',
                    fillColor: {
                        linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1},
                        stops: [
                            [0, 'rgb(47, 58, 69)'],
                            [1, 'rgb(112,134,158)']
                        ]
                    },
                    lineWidth: 5,
                    marker: {
                        enabled: false
                    },
                    shadow: false,
                    states: {
                        hover: {
                            lineWidth: 1
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

            }]
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
}