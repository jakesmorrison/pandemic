function plot_stock_stack(stack_data, dates){
    var chart = Highcharts.chart('stock_stacked', {
        chart: {
            type: 'column'
        },
        exporting: { enabled: false },
        credits: {enabled: false },
        title: {
            text: 'Daily Change by Stock Transaction'
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
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            useHTML: true,
            formatter: function () {
                if ( this.point.y != 0 ){
                    current_price = Math.round((this.point.cost + this.point.y)*100)/100
                    table = "<table class='tt_table'><tr><td class='table_left'>Daily Change</td><td>"+this.point.y+"</td></tr><tr><td class='table_left'>Current Price</td><td>$"+current_price+"</td></tr><tr><td class='table_left'>Initial Price</td><td>$"+this.point.cost+"</td></tr><tr><td class='table_left'>Quanity</td><td>"+this.point.quanity+"</td></tr><tr><td class='table_left'>Buy Date</td><td>"+this.point.buydate+"</td></tr><tr><td class='table_left'>Sell Date</td><td>"+this.point.selldate+"</td></tr><tr><td class='table_left'>Transaction ID</td><td>"+this.point.transaction+"</td></tr></table>"
                    header = '<p class="date"><i>'+this.point.category+'</i></p><br><h4 class="tt_header">' + this.series.name + '</h4>'
                    $( ".my_table" ).html(header);
                    $( ".my_table" ).append(table);
                    return '<i>'+this.point.category+'</i><br><span class="tt_header">' + this.series.name + '</span>'
                }
                else{
                }
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                borderColor: '#fff',
                borderWidth: 5
            }
        },
        series: stack_data
    });
}