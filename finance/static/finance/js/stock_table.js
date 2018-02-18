$('.table').DataTable({
    sScrollY:      $(document).height()*.20,
    scrollCollapse: true,
    scrollX:        true,
    paging:         false,
    "order": [[ 0, "decs" ]],
    language: { search: "<span class='sum_span'>Search</span>" },
    fixedColumns:   {
        leftColumns: 2,
        rightColumns: 0
    },
    "search": {
        "regex": true
    }
});

$('.table_button').on('click mouseover', function (e) {
    if (e.shiftKey === true){
        label = $("#DataTables_Table_0_filter").children()[0];
        span = $(label).children()[0];
        row = $(this).parent()[0];
        quanity_row = $(row).find("td:nth-child(3)")[0]
        buy_price_row = $(row).find("td:nth-child(5)")[0]
        sell_price_row = $(row).find("td:nth-child(7)")[0]
        ret = $(row).find("td:nth-child(9)")[0]

        if ($(this).parent().children().index($(this)) != column_number){
            summation = 0;
            $('.table_button').css("background","rgba(0, 0, 0, 0) ");
        }

        column_number = $(this).parent().children().index($(this));

        //Quanity
        if (column_number === 2){
            if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
                summation = parseInt(summation) + parseInt($(this).text());
                summation = summation.toFixed(0);
                $(this).css("background","rgba(185, 219, 255, .5)");
                $(span).text(summation);
            }
            else{
                $('.table_button').css("background","rgba(0, 0, 0, 0) ");
                summation = 0;
                $(span).text("");
            }
        }

        else if (column_number === 4){
            if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
                summation = parseFloat(summation) + (parseFloat($(this).text())*parseFloat($(quanity_row).text()));
                summation = summation.toFixed(2);
                $(this).css("background","rgba(185, 219, 255, .5)");
                $(span).text("$ "+summation);
            }
            else{
                $('.table_button').css("background","rgba(0, 0, 0, 0) ");
                summation = 0;
                $(span).text("");
            }
        }

        else if (column_number === 6){
            if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
                summation = parseFloat(summation) + (parseFloat($(this).text())*parseFloat($(quanity_row).text()));
                summation = summation.toFixed(2);
                $(this).css("background","rgba(185, 219, 255, .5)");
                $(span).text("$ "+summation);
            }
            else{
                $('.table_button').css("background","rgba(0, 0, 0, 0) ");
                summation = 0;
                $(span).text("");
            }
        }

        else if (column_number === 8){
            if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
                summation = parseFloat(summation) + (parseFloat($(this).text().replace("$","")));
                summation = summation.toFixed(2);
                $(this).css("background","rgba(185, 219, 255, .5)");
                $(span).text("$ "+summation);
            }
            else{
                $('.table_button').css("background","rgba(0, 0, 0, 0) ");
                summation = 0;
                $(span).text("");
            }
        }

    }
});

$('.table_button').click(function(){
    label = $("#DataTables_Table_0_filter").children()[0];
    span = $(label).children()[0];
    row = $(this).parent()[0];
    stock = $(row).find("td:nth-child(2)")[0]
    quanity_row = $(row).find("td:nth-child(3)")[0]
    buy_price_row = $(row).find("td:nth-child(5)")[0]
    sell_price_row = $(row).find("td:nth-child(7)")[0]
    ret = $(row).find("td:nth-child(9)")[0]

    if ($(this).parent().children().index($(this)) != column_number){
        summation = 0;
        $('.table_button').css("background","rgba(0, 0, 0, 0) ");
    }

    column_number = $(this).parent().children().index($(this));

    //Quanity
    if (column_number === 2){
        if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
            summation = parseInt(summation) + parseInt($(this).text());
            summation = summation.toFixed(0);
            $(this).css("background","rgba(185, 219, 255, .5)");
            $(span).text(summation);
        }
        else{
            $('.table_button').css("background","rgba(0, 0, 0, 0) ");
            summation = 0;
            $(span).text("");
        }
    }

    else if (column_number === 4){
        if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
            summation = parseFloat(summation) + (parseFloat($(this).text())*parseFloat($(quanity_row).text()));
            summation = summation.toFixed(2);
            $(this).css("background","rgba(185, 219, 255, .5)");
            $(span).text("$ "+summation);
        }
        else{
            $('.table_button').css("background","rgba(0, 0, 0, 0) ");
            summation = 0;
            $(span).text("");
        }
    }

    else if (column_number === 6){
        if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
            summation = parseFloat(summation) + (parseFloat($(this).text())*parseFloat($(quanity_row).text()));
            summation = summation.toFixed(2);
            $(this).css("background","rgba(185, 219, 255, .5)");
            $(span).text("$ "+summation);
        }
        else{
            $('.table_button').css("background","rgba(0, 0, 0, 0) ");
            summation = 0;
            $(span).text("");
        }
    }

    else if (column_number === 8){
        if($(this).css("background").split("none")[0] === "rgba(0, 0, 0, 0) "){
            summation = parseFloat(summation) + (parseFloat($(this).text().replace("$","")));
            summation = summation.toFixed(2);
            $(this).css("background","rgba(185, 219, 255, .5)");
            $(span).text("$ "+summation);
        }
        else{
            $('.table_button').css("background","rgba(0, 0, 0, 0) ");
            summation = 0;
            $(span).text("");
        }
    }
});