$("#card_pill").click(function(){
    $("#board_pill").removeClass("active");
    $("#card_pill").addClass("active");
    $('#game_board').hide();
    $('#cards').show();
});

$("#board_pill").click(function(){
    $("#card_pill").removeClass("active");
    $("#board_pill").addClass("active");
    $('#cards').hide();
    $('#game_board').show();
});

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

function close_pop(){
    $("#pop_up").hide();
}