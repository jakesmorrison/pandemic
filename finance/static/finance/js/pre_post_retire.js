var chart = Highcharts.chart('my_chart', {
    chart: {
        type: 'area',
        zoomType: 'xy'
    },
    title: {
        text: ''
    },
    legend: {enabled: true},
    exporting: { enabled: false },
    credits: {enabled: false},
    xAxis: {
        allowDecimals: false,
        labels: {
            formatter: function () {
                return current_year+this.value; // clean, unformatted number for year
            }
        }
    },
    yAxis: {
        title: {
            text: 'Money ($)'
        },
        labels: {
            formatter: function () {
                val = numberWithCommas(this.value);
                return '$'+val.toLocaleString();
            }
        }
    },
    tooltip: {
        formatter: function () {
            val = numberWithCommas(Math.round(this.y));
            year = 2017+parseInt(this.x)
            return 'Year: '+year+'<br> Amount: $' + val ;
        }
    },
    plotOptions: {
        area: {
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: false
                    }
                }
            }
        }
    },
    series: [{
        name: 'Pre Retirement',
        color: '#008000',
        data: []
    },
    {
        name: 'Post Retirement',
        color: '#00cd00',
        negativeColor: '#ff5f5f',
        data: []
    }]
});
