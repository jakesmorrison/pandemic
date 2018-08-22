function line_chart(id, title, yaxis) {
    return new Highcharts.Chart({
        chart: {
            borderColor: '#58585A',
            borderWidth: 2,
            backgroundColor: null,
            renderTo: id,
        },
        exporting: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        tooltip: {
            enabled: false
        },
        title: {
            text: title,
        },
        legend: {
            enabled: true
        },
        xAxis: {
            title: {
                text: '',
            },
            labels:{
                enabled: false
            },
            minorTickLength: 0,
            tickLength: 0,
            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
        },
        yAxis: [{
            min: 0,
            opposite: true,
            title: {
                text: yaxis,
            },
            labels: {
                enabled:true
            },
        }],
        plotOptions: {
            line:{
                marker: {
                    enabled: false,
                    states: {
                        hover:{
                            enabled: false
                        }
                    }
                }
            }
        },
        series: [{
            name: 'NVME',
            data: [],
            color: '#873299',
            type: 'line',
        },{
            name: 'NVME + NVDIMM',
            data: [],
            color: '#ffb500',
            type: 'line',
        }]
    });
}
