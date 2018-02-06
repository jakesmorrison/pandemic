var hidden = false;
function plot_stock_stack(stack_data, dates){
    var chart = Highcharts.chart('stock_stacked', {
        chart: {
            type: 'column',
            borderWidth: 0,
            backgroundColor: null,
        },
        exporting: { enabled: false },
        credits: {enabled: false },
        title: {
            text: ''
        },
        xAxis: {
            categories: dates
        },
        yAxis: {
            title: {
                text: 'Dollar Change ($)'
            },
            stackLabels: {
                enabled: true,
                style: {
                    fontWeight: 'bold',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                }
            },
            plotLines: [{
                value: 0,
                color: 'black',
                width: 3,
                zIndex: 5
            }]
        },
        legend: {
            enabled: false
        },
        tooltip: {
            useHTML: true,
            formatter: function () {
                if ( this.point.y != 0 ){
                    current_price = Math.round((this.point.cost + this.point.y/this.point.quanity)*100)/100;
                    current_value = current_price * this.point.quanity;
                    table = "<table class='tt_table'><tr><td class='table_left'>Daily Change</td><td>"+this.point.y+"</td></tr><tr><td class='table_left'>Daily Price</td><td>$"+current_price+"</td></tr><tr><tr><td class='table_left'>Total Value</td><td>$"+current_value+"</td></tr><tr><td class='table_left'>Initial Price</td><td>$"+this.point.cost+"</td></tr><tr><td class='table_left'>Quanity</td><td>"+this.point.quanity+"</td></tr><tr><td class='table_left'>Buy Date</td><td>"+this.point.buydate+"</td></tr><tr><td class='table_left'>Sell Date</td><td>"+this.point.selldate+"</td></tr><tr><td class='table_left'>Transaction ID</td><td>"+this.point.transaction+"</td></tr></table>"
                    header = '<p class="date"><i>'+this.point.category+'</i></p><br><h4 class="tt_header">' + this.series.name + '</h4>'
                    $( ".my_table" ).html(header);
                    $( ".my_table" ).append(table);
                    return '<i>'+this.point.category+'</i><br><span class="tt_header">' + this.series.name + '('+this.point.transaction+'): '+this.point.y+'</span>'
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
                            return this.series.name
                        }
                    }
                },
                borderColor: '#fff',
                borderWidth: 5,
                point: {
                    events: {
                        click: function () {
                            isolate_stock(this.series.name);
                        }
                    }
                }
            },
        },
        series: stack_data
    });

    function isolate_stock(symbol){
        if(hidden === false){
            $.each(chart.series, function(i, ser) {
                if(ser.name === symbol){
                    console.log(ser)
                }
                else{
                    ser.hide();
                }
            });
            hidden = true;
        }
        else{
            $.each(chart.series, function(i, ser) {
                ser.show();
            });
            hidden = false;
        }
    }
}
