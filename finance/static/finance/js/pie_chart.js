function pie_chart(pie_series){
    var my_pie_chart = Highcharts.chart('pie_chart', {
      colors: ['rgba(100, 30, 22,.8)','rgba(81, 46, 95,.8)',
               'rgba(27, 79, 114,.8)','rgba(11, 83, 69,.8)',
               'rgba(77, 86, 86,.8)','rgba(153, 99, 13,.8)',
               'rgba(153, 83, 36,.8)','rgba(27, 38, 49,.8)'],
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
        margin: [0, 0, 0, 0],
        spacingTop: 0,
        spacingBottom: 0,
        spacingLeft: 0,
        spacingRight: 0,
        borderWidth: 0,
        backgroundColor: null,
      },
    exporting: { enabled: false },
    credits: {enabled: false },
      title: {
        text: ''
      },
      tooltip: {
        formatter: function () {
            return '<span>'+this.key+'</span><br><span>Quanity :'+this.y+'</span><br>'
        }
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
            enabled: false,
            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            style: {
              color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
            },
          },
          point: {
            events: {
                click: function () {
                    custom_tooltip();
                }
            }
          },
          innerSize: '30%',
        }
      },
      series: pie_series
    });

    function custom_tooltip(){
//        $(".test").sparkline([5,6,7,2,0,-4,-2,4], {
//            type: 'bar',
//            height: '30px',
//            barWidth: 10,
//            barSpacing: 2,
//            barColor: '#5fbf00'});
        console.log()
    }
}