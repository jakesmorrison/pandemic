function create_spider_web(name, stats, container, color){
    Highcharts.chart(container, {
        chart: {
            polar: true,
            type: 'area',
            borderWidth: 0,
            backgroundColor: null,
            margin: [0, 0, 0, 0],
        },
        exporting: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        title: {
            text: '',
        },
        pane: {
            size: '55%'
        },

        xAxis: {
            categories: ['Strength', 'Dexterity', 'Constitution', 'Intelligence','Wisdom','Charisma'],
            tickmarkPlacement: 'on',
            lineWidth: 0,
        },

        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0,
            labels:{
                enabled:false
            }

        },

        tooltip: {
            shared: true,
            formatter: function ()  {
                ability = this.y;
                if (ability>=10){
                    return '<b>'+this.x+'</b><br> Modifier: +'+Math.floor((ability-10)/2).toString()+'<br> Value: '+ability;
                }
                else if(ability===9){
                    return '+'+Math.ceil((ability-10)/2).toString();
                }
                else{
                    return ''+Math.ceil((ability-10)/2).toString();
                }
            }
        },

        legend: {
            enabled: false
        },

        plotOptions: {
            area: {
                dataLabels: {
                    enabled: true,
                    formatter: function ()  {
                        ability = this.y;
                        if (ability>=10){
                            return '+'+Math.floor((ability-10)/2).toString();
                        }
                        else if(ability===9){
                            return '+'+Math.ceil((ability-10)/2).toString();
                        }
                        else{
                            return ''+Math.ceil((ability-10)/2).toString();
                        }
                    }
                },
                enableMouseTracking: true
            }
        },

        series: [{
            name: name,
            color: color,
            fillColor: color+'80',
            data: stats,
            pointPlacement: 'on'
        }]

    });
}

