var hidden = false;
function stock_spline(data1,data2){
    var chart = Highcharts.stockChart('stock_stacked', {
            chart: {
                borderWidth: 0,
                backgroundColor: null,
            },
            rangeSelector: {
                selected: 1
            },

            title: {
                text: 'AAPL Historical'
            },
            xAxis: {
                type: 'datetime',
                showLastLabel: false,
                endOnTick: true

            },
            yAxis: [{
                labels: {
                    align: 'right',
                    x: -3
                },
                title: {
                    text: 'OHLC'
                },
                height: '60%',
                lineWidth: 2,
                resize: {
                    enabled: true
                }
            }, {
                labels: {
                    align: 'right',
                    x: -3
                },
                title: {
                    text: 'Volume'
                },
                top: '65%',
                height: '35%',
                offset: 0,
                lineWidth: 2
            }],

            tooltip: {
                split: false,
                formatter: function () {
                    if ((typeof this.key) == (typeof "test")){
                        return '<span>'+this.key+'</span>'+'<span>'+": $"+this.y+'</span>'
                    }
                    else{
                        d = new Date(0);
                        d.setUTCSeconds(this.key/1000);
                        return '<span>'+d.toString().split("00")[0]+'</span>'+'<span>'+"<br>$"+this.y+'</span>'
                    }
                }
            },

            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels:{
                        enabled: true,
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
                                console.log(this.options)
//                                isolate_stock(this.options.name);
                            }
                        }
                    }
                },
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


//    function isolate_stock(symbol){
//
//        if(hidden === false){
//            $.each(chart.series, function(i, ser) {
//                console.log(ser)
//                if(ser.name === symbol){
//                    console.log(ser)
//                }
//                else{
//                    ser.hide();
//                }
//            });
//            hidden = true;
//        }
//        else{
//            $.each(chart.series, function(i, ser) {
//                ser.show();
//            });
//            hidden = false;
//        }
//    }

}