function draw_cum_spline(data,container){
  Highcharts.stockChart(container, {
    rangeSelector: {
      selected: 0
    },

    title: {
      text: 'USD to EUR exchange rate'
    },

    tooltip: {
      style: {
        width: '200px'
      },
      valueDecimals: 4,
      shared: true
    },

    yAxis: {
      title: {
        text: 'Exchange rate'
      }
    },

    series: [{
      name: 'USD to EUR',
      data: data,
      id: 'dataseries'
    }]
  });
}