function rotten_meta_jake_chart(data){
    Highcharts.chart('rotten_meta_jake_chart', {

      chart: {
        type: 'scatter',
//        plotBorderWidth: 1,
//        zoomType: 'xy'
      },

      legend: {
        enabled: false
      },

      title: {
        text: ''
      },

      subtitle: {
        text: ''
      },

      xAxis: {
        <!--min: 0,-->
        <!--max: 100,-->
        gridLineWidth: 1,
        title: {
          text: 'Rotten Tomatoes'
        },
        labels: {
          format: '{value}%'
        },
        <!--plotLines: [{-->
          <!--color: 'black',-->
          <!--dashStyle: 'dot',-->
          <!--width: 2,-->
          <!--value: 65,-->
          <!--label: {-->
            <!--rotation: 0,-->
            <!--y: 15,-->
            <!--style: {-->
              <!--fontStyle: 'italic'-->
            <!--},-->
            <!--text: 'Safe fat intake 65g/day'-->
          <!--},-->
          <!--zIndex: 3-->
        <!--}]-->
      },
        exporting: { enabled: false },
        credits: {enabled: false },

      yAxis: {
        <!--min: 0,-->
        <!--max: 100,-->
        startOnTick: false,
        endOnTick: false,
        title: {
          text: 'Metacritic'
        },
        labels: {
          format: '{value}'
        },
        maxPadding: 0.2,
        <!--plotLines: [{-->
          <!--color: 'black',-->
          <!--dashStyle: 'dot',-->
          <!--width: 2,-->
          <!--value: 50,-->
          <!--label: {-->
            <!--align: 'right',-->
            <!--style: {-->
              <!--fontStyle: 'italic'-->
            <!--},-->
            <!--text: 'Safe sugar intake 50g/day',-->
            <!--x: -10-->
          <!--},-->
          <!--zIndex: 3-->
        <!--}]-->
      },

      tooltip: {
        useHTML: true,
        headerFormat: '<table>',
        pointFormat: '<tr><th colspan="2"><h3>{point.name}</h3></th></tr>' +
          '<tr><th>Rotten Tomatoes:</th><td>{point.x}%</td></tr>' +
          '<tr><th>Metacritic:</th><td>{point.y}</td></tr>' +
          '<tr><th>Jake:</th><td>{point.Jake}</td></tr>',
        footerFormat: '</table>',
        followPointer: true
      },

      plotOptions: {
        series: {
          dataLabels: {
            enabled: false,
            format: '{point.name}'
          },
            marker: {
                radius: 8
            }

        }
      },

      series: data

    });
}