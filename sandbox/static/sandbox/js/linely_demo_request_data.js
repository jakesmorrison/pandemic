function requestData(url_base) {
    $.ajax({
        type: 'GET',
        url: url_base,
        success: function(msg) {
            var error = Math.floor((Math.random() * -20)+5);

            if (error<0){
                bubble_chart.series[0].addPoint({ x: msg.write_bw , y: msg.read_bw-1000, z: 1, name: '', country: '' ,color: '#9ACA3C'}, false, shift);
            }
            else{
                bubble_chart.series[0].addPoint({ x: msg.write_bw , y: msg.read_bw-1000, z: error ,color: 'rgba(255, 75, 75, 1)'}, false, shift);
            }


            var series = bw_chart.series[0], shift = series.data.length > 50;
            bw_chart.series[0].addPoint(msg.write_bw, false, shift);
            bw_chart.series[1].addPoint(msg.read_bw-1000, false, shift);
            bw_chart.series[2].addPoint(error, false, shift);

//            bw_chart.series[2].addPoint([msg.write_bw-5,msg.write_bw+5], false, shift);
//            bw_chart.series[3].addPoint([msg.read_bw-5,msg.read_bw+5], false, shift);
//            bw_chart.series[2].addPoint(msg.write_bw-msg.write_bw*.05, false, shift);
//            bw_chart.series[3].addPoint(msg.read_bw-msg.read_bw*.05, false, shift);

            bw_chart.redraw();
            bubble_chart.redraw();

            if (error_log_counter >=num_log_items){
                $('#error_logging').find('span').first().remove();
            }

            if(msg.errors>0){
                $('#error_logging').append("<span class='log_line'><span class='date_time'>"+new Date()+": </span><span class='errors'>memory errors have occured! error count: "+msg.errors+"</span><br></span>");
            }
            else{
                $('#error_logging').append("<span class='log_line'><span class='date_time'>"+new Date()+": </span><span class='errors'>no errors. error count: "+msg.errors+"</span><br></span>");
            }
            error_log_counter += 1;
            if (pause === false){
                setTimeout(function(){requestData(url_base);}, 500);
            }

        }
    });
}
