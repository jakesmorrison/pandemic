$("#card_pill").click(function(){
    $("#board_pill").removeClass("active");
    $("#card_pill").addClass("active");
    $('#game_board').fadeOut(100);
    $('#cards').fadeIn(500);
});

$("#board_pill").click(function(){
    $("#card_pill").removeClass("active");
    $("#board_pill").addClass("active");
    $('#cards').fadeOut(100);
    $('#game_board').fadeIn(500);
});

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

function close_pop(){
    $("#pop_up").hide();
}

function hide_table(){
    $("#infection_status").toggleClass("toggled");
}