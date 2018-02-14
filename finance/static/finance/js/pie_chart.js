function pie_chart(pie_series){
    var my_pie_chart = Highcharts.chart('pie_chart', {
      colors: ['#641E16','#512E5F','#1B4F72','#0B5345','#186A3B','#7E5109','#995324','#4D5656','#1B2631','#F9E79F'],
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
        margin: [0, 0, 0, 0],
        spacingTop: 0,
        spacingBottom: 0,
        spacingLeft: 0,
        spacingRight: 0

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
            }
          },
          point: {
            events: {
                click: function () {
                    custom_tooltip();
                }
            }
          }
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