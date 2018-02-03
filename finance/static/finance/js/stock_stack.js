function plot_stock_stack(stack_data, dates){
    Highcharts.chart('stock_stacked', {
        chart: {
            type: 'column'
        },
        exporting: { enabled: false },
        credits: {enabled: false },
        title: {
            text: 'Stacked column chart'
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
//            align: 'right',
//            x: -30,
//            verticalAlign: 'top',
//            y: 25,
//            floating: true,
//            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
//            borderColor: '#CCC',
//            borderWidth: 1,
//            shadow: false
        },
        tooltip: {
//            headerFormat: '<b>{point.x}</b><br/>',
//            pointFormat: '{series.name} : {point.y} <br> Initial Cost: {series.cost} <br> Shares: {series.quanity} <br> Buy Date: {series.buydate} <br> Sell Date: {series.selldate}'
            //Total: {point.stackTotal}
            useHTML: true,
            formatter: function () {
                current_price = Math.round((this.point.cost + this.point.y)*100)/100
                table = "<table class='tt_table'><tr><td>Daily Change</td><td>"+this.point.y+"</td></tr><tr><td>Current Price</td><td>$"+current_price+"</td></tr><tr><td>Initial Price</td><td>$"+this.point.cost+"</td></tr><tr><td>Quanity</td><td>"+this.point.quanity+"</td></tr><tr><td>Buy Date</td><td>"+this.point.buydate+"</td></tr><tr><td>Sell Date</td><td>"+this.point.selldate+"</td></tr></table>"
                return '<i>'+this.point.category+'</i><br><span class="tt_header">' + this.series.name + '</span><br>' +table
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                borderColor: '#FFFFFF',
                borderWidth: 5
            }
        },
        series: stack_data
    });
}