function plot_picture(){
    var chart = Highcharts.chart('container', {
        chart: {
            type: 'scatter',
            zoomType: 'xy',
            height: '100%'
        },

        boost: {
            useGPUTranslations: true,
            usePreAllocated: true
        },

        xAxis: {
            min: 0,
            max: 3024,
            gridLineWidth: 1,
            allowDecimals: false
        },

        yAxis: {
            // Renders faster when we don't have to compute min and max
            min: 0,
            max: 4032,
            minPadding: 0,
            maxPadding: 0,
            allowDecimals: false,
            title: {
                text: null
            }
        },
        plotOptions:{
            scatter:{
                turboThreshold:1000000,
                pointPadding: 0,
                groupPadding: 0,
            }
        },
        title: {
            text: 'Scatter chart with '
        },

        legend: {
            enabled: false
        },

        series: [{}]
    });
}
