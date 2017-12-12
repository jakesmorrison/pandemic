function create_top_chart(data,year,month,day,lastday){
  window.chart = new Highcharts.StockChart({
    chart: {
      renderTo: 'top_chart'
    },
    rangeSelector: {
      selected: 5
    },
    title: {
      text: ''
    },
    scrollbar: {
      barBackgroundColor: 'gray',
      barBorderRadius: 7,
      barBorderWidth: 0,
      buttonBackgroundColor: 'gray',
      buttonBorderWidth: 0,
      buttonArrowColor: 'blue',
      buttonBorderRadius: 7,
      rifleColor: 'blue',
      trackBackgroundColor: 'white',
      trackBorderWidth: 1,
      trackBorderColor: 'silver',
      trackBorderRadius: 7
    },
    tooltip: {
        formatter: function() {
            var d = new Date(parseInt(this.x));
            return "Date: "+(d.getMonth()+1)+'/'+d.getDate()+'/'+d.getFullYear()+"<br>"+
            "TOP Hours: "+this.y+"<br>"+
            "TOP Days: "+(this.y/8).toString().split(".")[0]
        }
    },
    exporting: { enabled: false },
    credits: {enabled: false },
    rangeSelector : {
        selected: 4,
        inputEnabled: true,
        buttonTheme: {
            visibility: 'hidden'
        },
        labelStyle: {
            visibility: 'hidden'
        }
    },

    xAxis: {
      type: 'datetime',
      ordinal: true,
      plotBands: [{
        color: 'rgba(95,175,255, 0.25)',
        from: Date.UTC(year,month,day),
        to: Date.UTC(lastday.split("-")[0],lastday.split("-")[1],lastday.split("-")[2])
      }],
        plotLines: [{
            value: Date.UTC(year,month,day),
            color: 'black',
            dashStyle: 'shortdash',
            width: 2
        }]
    },
    yAxis: [{
      title: {
        text: 'TOP (Hours)'
      },
      plotLines: [{
        value: 80,
        color: 'green',
        dashStyle: 'shortdash',
        width: 2,
        label: {
          text: '80 Hours'
        }
      }],
      min: 0
    }],
    series: [{
      name: 'TOP Hours',
      id: 'dataseries',
      data: data,
      type: 'areaspline',
        threshold: 80,
        negativeColor: '#ff1a1a',
        color: '#00cc00',
        tooltip : {
            valueDecimals : 2
        }
    }
    ,{
    type : 'flags',
        data : [{
            x : Date.UTC(2018, 4, 02),
            title : 'A',
            text : 'Costa Rica'
        }],
        onSeries : 'dataseries',
        shape : 'circlepin',
        width : 16
    }]
  });
}