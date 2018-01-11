Highcharts.chart('left_chart', {
  chart: {
    type: 'column',
    borderWidth: 0,
    backgroundColor: 'transparent',
  },
  title: {
    text: 'Bandwidth',
    style: {
        color: 'white',
        fontSize:'50px'
    },
    align: 'left',
//    x: 70,
  },
  xAxis: {
    categories: ['SSD', 'NVME', 'NVDIMM'],
//    lineWidth: 0,
//    minorGridLineWidth: 0,
//    lineColor: 'transparent',
//    minorTickLength: 0,
//    tickLength: 0,
//    gridLineColor: 'transparent',
    labels: {
        style: {
            color: 'white',
            fontSize:'20px'
        }
    }
  },
  yAxis: {
    min: 0,
    max: 18,
    title: {
      text: '',
      style: {
            color: 'white',
            fontSize:'20px'
       },
    },
    lineWidth: 0,
    minorGridLineWidth: 0,
    lineColor: 'transparent',
    minorTickLength: 0,
    tickLength: 0,
    gridLineColor: 'transparent',
    labels: {
        style: {
            color: 'white',
            fontSize:'15px'
        }
    }
  },
  legend: {
    enabled: false
  },
  credits: {
    enabled: false
  },
  exporting: {
    enabled: false
  },
  tooltip: {
    enabled: false
  },
  plotOptions: {
    series: {
      stacking: 'normal',
      borderRadius: 5
    }
  },
  annotations: [{
    labels: [{
        point: {
            x: 0,
            y: 7.5,
            xAxis: 0,
            yAxis: 0
        },
        text: 'Price You Want',
        align: 'center',
        style: {
            color: 'white',
            fontSize:'20px'
        }
    },{
        point: {
            x: 2,
            y: 15.5,
            xAxis: 0,
            yAxis: 0
        },
        text: 'Performance<br>You Want',
        align: 'center',
        style: {
            color: 'white',
            fontSize:'20px'
        }
    }]
  }],
  series: [{
    name: 'Line',
    data: [1, 1, 1],
    color: '#58595B',
    borderColor: '#2C2C2E'

  },{
    name: 'Blank',
    data: [.5, .5, .5],
    color: 'transparent',
    borderColor: 'transparent'

  },{
    name: 'Bar',
    data: [6, 9, 14],
    color: 'transparent',
    borderColor: 'transparent',
  }]
});
