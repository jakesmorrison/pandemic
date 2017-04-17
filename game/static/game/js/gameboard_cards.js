function start_game(e) {
  console.log("Deal Cards");
  url = dealCards;
  data = {
    'roomId': roomId,
    'users': $('#users_here').text()
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      socket.send(JSON.stringify({
        "command": "dealcards",
        "roomId": roomId,
        "user": username,
        "message": "hello"
      }));
    }
  });
}

function get_cards_from_db(socketCall) {
  console.log("Update Cards");
  url = getCards;
  data = {
    'roomId': roomId,
    'user': username
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      if (msg["gameStarted"] === true) {
        $("#startgame").html("");
        $("#initial_user").html("");
        $("#user_location_hide").show();
        cards = msg["cards"];

        //user location
        userLocation = msg["currentLocation"];
        $('#currentlocation').html("")
        for (i = 0; i < userLocation.length; i++) {
            if(userLocation[i]['user'] === username){
                $('#currentlocation').append("<option selected>"+userLocation[i]['user']+": "+userLocation[i]['currentLocation']+"</option>")
            }
            else{
                $('#currentlocation').append("<option>"+userLocation[i]['user']+": "+userLocation[i]['currentLocation']+"</option>")
            }
        }

        //Player Cards
        $("#playercards1").html("");
        $("#playercards2").html("")
        for (i = 0; i < cards.length; i++) {
          if (typeof cards[i]["city"] === 'undefined'){
            console.log("Pandemic!!")
          }
          else if (i%2 === 0) {
            $("#playercards1").append("<h4><a style='cursor: pointer; color:" + cards[i]['color'] + "' id='" + cards[i]["city"] + "' onclick='discard(this,id)'>" + cards[i]["city"] + ", " + cards[i]["country"] + ", " + cards[i]["population"] + "</a></h4>")
          } else {
            $("#playercards2").append("<h4><a style='cursor: pointer; color:" + cards[i]['color'] + "' id='" + cards[i]["city"] + "' onclick='discard(this,id)'>" + cards[i]["city"] + ", " + cards[i]["country"] + ", " + cards[i]["population"] + "</a></h4>")
          }
        }

        //Role Cards
        roles = msg["roles"];
        $("#roles").html("")
        for (i = 0; i < roles.length; i++) {
          $("#roles").append("<h4><a style='cursor: pointer;' id=" + roles[i]["name"] + " onclick='remove_role(id)' title='" + roles[i]["description"].replace(new RegExp("-", "g"), "\n") + "'>" + roles[i]["name"] + "</a></h4>")
        }

        //Action Deck
        actionCards = msg["actionCards"];
        $("#actioncards").html("")
        $("#actioncards").append("<button type='button' style='height: 219px;width: 100%; background-color: #383838; border-color: #383838; color: #d0d0d0;' class='btn btn-success' id='getNewCard' onclick='get_new_card()'>Get New Card <br>" + actionCards.length + "</button>")

        //Action Discards
        actionDiscards = msg["actionDiscards"];
        $("#actiondiscards").html("");
        for (i = 0; i < actionDiscards.length; i++) {
          $("#actiondiscards").append("<h4><a id='" + actionDiscards[i]["city"] + "' style='cursor: pointer; color:" + actionDiscards[i]['color'] + "' onclick='pickup_discard(id)'>" + actionDiscards[i]["city"] + "</a></h4>")
        }

        //Infection Deck
        infectionCards = msg["infectionCards"];
        $("#infectioncards").html("")
        $("#infectioncards").append("<button type='button' style='width: 100%; height:73px; background-color: #383838;border-color: #b1b1b1;border-width: 5px;' class='btn btn-success' id='playInfectionTop' onclick='infection_play_top()'>Top</button>")
        $("#infectioncards").append("<button type='button' style='width: 100%; height:73px; background-color: #383838;border-color: #b1b1b1;border-width: 5px;' class='btn btn-success' id='playInfectionBottom' onclick='infection_play_bottom()'>Bottom</button>")
        $("#infectioncards").append("<button type='button' style='width: 100%; height:73px; background-color: #383838;border-color: #b1b1b1;border-width: 5px;' class='btn btn-success' id='reshuffleinfectiondeck' onclick='reshuffle_infection_deck()'>Reshuffle</button>")

        //Infection Discards
        infectionDiscards = msg["infectionDiscards"];
        $("#infectiondiscards").html("");
        for (i = 0; i < infectionDiscards.length; i++) {
          $("#infectiondiscards").append("<h4><a style='cursor: pointer; color:" + infectionDiscards[i]['color'] + "'>" + infectionDiscards[i]["city"] + "</a></h4>")
        }

        //Tokens
        tokens = msg["tokens"];
        for (var k in tokens) {
          if (tokens.hasOwnProperty(k)) {
            $("#" + k).html(tokens[k])
          }
        }

        //Cures
        cures = msg["cures"];
        for (var k in cures) {
          if (cures.hasOwnProperty(k)) {
            if (cures[k] === true) {
              $("#" + k).css("background-color", k.replace("Cure", ""));
            } else {
              $("#" + k).css("background-color", "grey");
            }
          }
        }

        //Notes
        notes = msg["notes"];
        notes = notes.replace(new RegExp("-", "g"), "\n");
        $("#notes").text(notes);

        //Map
        infectionMap = msg["infectionMap"];
//        $('#body_table').html("");
//        for (i = 0; i < infectionMap.length; i++) {
//            $('#body_table').append('<tr><td>'+infectionMap[i]["city"]+'</td><td>'+infectionMap[i]["blue"]+'</td><td>'+infectionMap[i]["black"]+'</td><td>'+infectionMap[i]["red"]+'</td><td>'+infectionMap[i]["yellow"]+'</td><td>'+infectionMap[i]["purple"]+'</td></tr>');
//        }

        setup_table((infectionMap));

        if (socketCall === "true") {
          socket.send(JSON.stringify({
            "command": "getcards",
            "roomId": roomId,
            "user": username,
            "message": "hello"
          }));
        }
      }
    }
  });
}

function discard(obj, city) {
  console.log("Discard Action");
  $("#playercards1").html("")
  $("#playercards2").html("")
  url = discardAction;
  data = {
    'roomId': roomId,
    'user': username,
    'city': city
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function get_new_card() {
  console.log("Get New Action Card");
  url = getNewCard;
  data = {
    'roomId': roomId,
    'user': username
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function infection_play_top() {
  console.log("Play Top Infection Card")
  url = infectionPlayTop;
  data = {
    'roomId': roomId,
    'user': username
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function infection_play_bottom() {
  console.log("Play Bottom Infection Card")
  url = infectionPlayBottom;
  data = {
    'roomId': roomId,
    'user': username
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function increment(color) {
  console.log("Increment Color");
  url = incrementColor;
  data = {
    'roomId': roomId,
    'user': username,
    'color': color
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function decrement(color) {
  console.log("Decrement Color");
  url = decrementColor;
  data = {
    'roomId': roomId,
    'user': username,
    'color': color
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function increment_other(indicator) {
  console.log("Increment Other");
  url = incrementOther;
  data = {
    'roomId': roomId,
    'user': username,
    'indicator': indicator
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function decrement_other(indicator) {
  console.log("Decrement Other");
  url = decrementOther;
  data = {
    'roomId': roomId,
    'user': username,
    'indicator': indicator
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function change_cure(cureName) {
  console.log("Toggle Cure");
  url = changeCure;
  data = {
    'roomId': roomId,
    'user': username,
    'cureName': cureName
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function reshuffle_infection_deck() {
  console.log("Reshuffle Infection Deck");
  url = reshuffleInfectionDeck;
  data = {
    'roomId': roomId,
    'user': username
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function remove_role(role) {
  console.log("Remove Role");
  url = removeRole;
  data = {
    'roomId': roomId,
    'user': username,
    'role': role
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("false");
    }
  });
}

$(document).keypress(function(e) {
  if (e.which == 13) {
    if ($("#input").is(":focus")) {
      save_notes();
    }
  }
});

function save_notes() {
  console.log("Add Notes");
  note = $("#input").val();
  url = saveNotes
  data = {
    'roomId': roomId,
    'user': username,
    'note': note
  };
  $("#input").val("");
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("false");
    }
  });
}

function pickup_discard(city) {
  console.log("Pickup City Card");
  url = pickupDiscard;
  data = {
    'roomId': roomId,
    'user': username,
    'city': city
  };
  $.ajax({
    type: "GET",
    url: url,
    data: data,
    success: function(msg) {
      get_cards_from_db("true");
    }
  });
}

function setup_table(data){
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
