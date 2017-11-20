function draw_issuer_hist(cat,data,cont,ytitle,adder,mult){
    return new Highcharts.Chart({
        chart: {
            renderTo: cont,
            borderWidth: 0,
            backgroundColor: null,
            type: 'column',
        },
        title: {
            text: ''
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        xAxis: {
            title:{
              text: "",
              style: {
                  font: '',
                  color: '#565656'
                }
            },
            labels: {
                //enabled: false,
                style: {
                  color: '#565656;',
                  fontSize: '12px'
                },
            },
            categories: cat,
            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            minorTickLength: 0,
            tickLength: 0
        },
        yAxis: {
            //type: 'logarithmic',
            //min: 0,
            //max: 350,
            title: {
              text: ytitle,
              style: {
                  font: '',
                  color: '#565656'
                }
            },
            labels: {
                style: {
                  color: '#565656;',
                  fontSize: '12px'
                },
                formatter: function() {
                  val = numberWithCommas(this.value);
                  return '' + val.toLocaleString() + adder;
                }
            },
            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            minorTickLength: 0,
            tickLength: 0,
            gridLineColor: 'transparent'
        },
        tooltip: {
            formatter: function() {
                return this.key +"<br> Points Earned: "+numberWithCommas(this.y*mult)
          }
        },

        plotOptions: {
            column: {
                pointPadding: 0,
                borderWidth: 2,
                groupPadding: 0,
                shadow: true,
            },
            series: {
                borderColor: 'rgba(236, 91, 173, 1)',
            }
        },
        series: [{
            color: 'rgba(236, 91, 173, 0.90)',
            type: 'column',
            data: data
        }]
    });
}