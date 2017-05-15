function update_all(data){
    update_user_location(data['userLocation']);
    get_and_update_tokens(data["tokens"]);
    get_and_update_action_cards(data["actionCards"], data["actionDiscards"]);
    get_player_cards();
    get_and_update_infection_cards(data["infectionCards"], data["infectionDiscards"]);
    update_cures(data["cures"]);
    update_infection_table(data["infectionMap"])

    $("#startgame").html("");
    $("#initial_user").html("");
    $("#user_location_hide").show();
}

function get_and_update_tokens(tokens){
    for (var k in tokens) {
      if (tokens.hasOwnProperty(k)) {
        $("#" + k).html(tokens[k])
      }
    }
}

function get_and_update_action_cards(actionCards, actionDiscards){
    $("#actioncards").html("")
    $("#actioncards").append("<button type='button' style='overflow-y: hidden;height: 219px;width: 100%; background-color: #383838; border-color: #383838; color: #d0d0d0;' class='btn btn-success' id='getNewCard' onclick='get_new_card()'>Get New Card <br>" + actionCards.length + "</button>")

    $("#actiondiscards").html("");
    for (i = 0; i < actionDiscards.length; i++) {
      $("#actiondiscards").append("<h4><a id='" + actionDiscards[i]["city"] + "' style='cursor: pointer; color:" + actionDiscards[i]['color'] + "' onclick='pickup_discard(id)'>" + actionDiscards[i]["city"] + "</a></h4>")
    }
}

function get_player_cards(){
    url = getPlayerCards;
    city = $('#city_pop').text();
    data = {
        'roomId': roomId,
        'city': city,
        'user': username
    };
    $.ajax({
        type: "GET",
        url: url,
        data: data,
        success: function(msg) {
            cards = msg["cards"];
            roles = msg["roles"]
            $("#playercards1").html("");
            $("#playercards2").html("")
            for (i = 0; i < cards.length; i++) {
              if (i%2 === 0) {
                if (cards[i]["city"] === 'Pandemic!' || cards[i]["city"] === 'Mutation' || cards[i]["city"] === 'Event'){
                    $("#playercards1").append("<h4><a data-toggle='tooltip' data-placement='bottom' title='"+cards[i]['description']+"' style='cursor: pointer; color:" + cards[i]['color'] + "' id='" + cards[i]["city"] + "' onclick='discard(this,id)'>" + cards[i]["city"] + "</a></h4>")
                }
                else{
                    $("#playercards1").append("<h4><a style='cursor: pointer; color:" + cards[i]['color'] + "' id='" + cards[i]["city"] + "' onclick='discard(this,id)'>" + cards[i]["city"] + ", " + cards[i]["country"] + ", " + cards[i]["population"] + "</a></h4>")
                }
              }
              else {
                if (cards[i]["city"] === 'Pandemic!' || cards[i]["city"] === 'Mutation' || cards[i]["city"] === 'Event'){
                    $("#playercards2").append("<h4><a data-toggle='tooltip' data-placement='bottom' title='"+cards[i]['description']+"' style='cursor: pointer; color:" + cards[i]['color'] + "' id='" + cards[i]["city"] + "' onclick='discard(this,id)'>" + cards[i]["city"] + "</a></h4>")
                }
                else{
                    $("#playercards2").append("<h4><a style='cursor: pointer; color:" + cards[i]['color'] + "' id='" + cards[i]["city"] + "' onclick='discard(this,id)'>" + cards[i]["city"] + ", " + cards[i]["country"] + ", " + cards[i]["population"] + "</a></h4>")
                }
              }
            }

            //Role Cards
            $("#roles").html("")
            for (i = 0; i < roles.length; i++) {
              $("#roles").append("<h4><a style='cursor: pointer;' id=" + roles[i]["name"].replace(" ","_") + " onclick='remove_role(id)' data-toggle='tooltip' data-placement='bottom' title='" + roles[i]["description"].replace(new RegExp("-", "g"), "\n") + "'>" + roles[i]["name"] + "</a></h4>")
            }
        }
    });
}

function get_and_update_infection_cards(infectionCards, infectionDiscards){
//    $("#infectioncards").html("")
//    $("#infectioncards").append("<button type='button' style='overflow-y: hidden; width: 100%; height:73px; background-color: #383838;border-color: #b1b1b1;border-width: 5px;' class='btn btn-success' id='playInfectionTop' onclick='infection_play_top()'>Top</button>")
//    $("#infectioncards").append("<button type='button' style='overflow-y: hidden; width: 100%; height:73px; background-color: #383838;border-color: #b1b1b1;border-width: 5px;' class='btn btn-success' id='playInfectionBottom' onclick='infection_play_bottom()'>Bottom</button>")
//    $("#infectioncards").append("<button type='button' style='overflow-y: hidden; width: 100%; height:73px; background-color: #383838;border-color: #b1b1b1;border-width: 5px;' class='btn btn-success' id='reshuffleinfectiondeck' onclick='reshuffle_infection_deck()'>Reshuffle</button>")

    $("#infectiondiscards").html("");
    for (i = 0; i < infectionDiscards.length; i++) {
      $("#infectiondiscards").append("<h4><a style='cursor: pointer; color:" + infectionDiscards[i]['color'] + "'>" + infectionDiscards[i]["city"] + "</a></h4>")
    }


}

function update_user_location(userLocation){
    $('#currentlocation').html("")
    for (i = 0; i < userLocation.length; i++) {
        if(userLocation[i]['user'] === username){
            $('#currentlocation').append("<option selected>"+userLocation[i]['user']+": "+userLocation[i]['currentLocation']+"</option>")
        }
        else{
            $('#currentlocation').append("<option>"+userLocation[i]['user']+": "+userLocation[i]['currentLocation']+"</option>")
        }
    }
}

function update_research_station(researchStationList){
    $('#researchList').html("")
    for (i = 0; i < researchStationList.length; i++) {
        if(i===0){
            $('#researchList').append("<option selected>"+researchStationList[i]+"</option>")
        }
        $('#researchList').append("<option>"+researchStationList[i]+"</option>")
    }
}

function update_cures(cures){
    for (var k in cures) {
      if (cures.hasOwnProperty(k)) {
        if (cures[k] === true) {
          //$("#" + k).css("background-color", k.replace("Cure", ""));
          if(k.replace("Cure", "") === "red"){$("#" + k).removeClass("redUnCure"); $("#" + k).addClass("redCure");}
          else if(k.replace("Cure", "") === "blue"){$("#" + k).removeClass("blueUnCure"); $("#" + k).addClass("blueCure");}
          else if(k.replace("Cure", "") === "black"){$("#" + k).removeClass("blackUnCure"); $("#" + k).addClass("blackCure");}
          else if(k.replace("Cure", "") === "yellow"){$("#" + k).removeClass("yellowUnCure"); $("#" + k).addClass("yellowCure");}
          else if(k.replace("Cure", "") === "purple"){$("#" + k).removeClass("purpleUnCure"); $("#" + k).addClass("purpleCure");}
        } else {
          if(k.replace("Cure", "") === "red"){$("#" + k).removeClass("redCure"); $("#" + k).addClass("redUnCure");}
          else if(k.replace("Cure", "") === "blue"){$("#" + k).removeClass("blueCure"); $("#" + k).addClass("blueUnCure");}
          else if(k.replace("Cure", "") === "black"){$("#" + k).removeClass("blackCure"); $("#" + k).addClass("blackUnCure");}
          else if(k.replace("Cure", "") === "yellow"){$("#" + k).removeClass("yellowCure"); $("#" + k).addClass("yellowUnCure");}
          else if(k.replace("Cure", "") === "purple"){$("#" + k).removeClass("purpleCure"); $("#" + k).addClass("purpleUnCure");}
          //$("#" + k).css("background-color", "grey");
        }
      }
    }
}


function update_infection_table(infectionMap){
    var data = infectionMap;
    if ( ! $.fn.DataTable.isDataTable( '#infection_table' ) ) {
        $('#infection_table').DataTable({
            data: data,
            scrollX:        true,
            scrollCollapse: false,
            bScrollCollapse: false,
            paging:         false,
            bFilter:        false,
            bAutoWidth:     false,
            fixedColumns:   {
                leftColumns: 1,
                rightColumns: 0
            },
            bSort:          true,
            bAutoWidth:     false,
            bInfo:          false,
            bJQueryUI:      true,
            bLengthChange:  true,
            bPaginate:      true,
            bProcess:       true,
            bScrollInfinite:false,
        });
    }
    else{
        var table = $('#infection_table').DataTable();
        table.clear().rows.add(data).draw();
    }
}

columnDefs:[
    { orderSequence:["desc","asc"], targets:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]} ,
]
