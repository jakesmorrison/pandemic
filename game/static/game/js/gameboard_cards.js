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
        "user": username
      }));
    }
  });
}

function discard(obj, city) {
  console.log("Discard Action");
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
     socket.send(JSON.stringify({
        "command": "updateactioncards",
        "roomId": roomId,
        "user": username,
     }));
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
      socket.send(JSON.stringify({
        "command": "updateactioncards",
        "roomId": roomId,
        "user": username,
     }));
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
     socket.send(JSON.stringify({
        "command": "updateactioncards",
        "roomId": roomId,
        "user": username,
     }));
    }
  });
}

function remove_role(role) {
  url = removeRole;
  console.log("Remove Role")
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
      socket.send(JSON.stringify({
        "command": "updateactioncards",
        "roomId": roomId,
        "user": username,
     }));
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
     socket.send(JSON.stringify({
        "command": "updateinfectioncards",
        "roomId": roomId,
        "user": username,
     }));
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
     socket.send(JSON.stringify({
        "command": "updateinfectioncards",
        "roomId": roomId,
        "user": username,
     }));
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
      socket.send(JSON.stringify({
        "command": "updateinfectioncards",
        "roomId": roomId,
        "user": username,
     }));
    }
  });
}

//function increment(color) {
//  console.log("Increment Color");
//  url = incrementColor;
//  data = {
//    'roomId': roomId,
//    'user': username,
//    'color': color
//  };
//  $.ajax({
//    type: "GET",
//    url: url,
//    data: data,
//    success: function(msg) {
//      socket.send(JSON.stringify({
//        "command": "updatetokens",
//        "roomId": roomId,
//        "user": username,
//      }));
//    }
//  });
//}

//function decrement(color) {
//  console.log("Decrement Color");
//  url = decrementColor;
//  data = {
//    'roomId': roomId,
//    'user': username,
//    'color': color
//  };
//  $.ajax({
//    type: "GET",
//    url: url,
//    data: data,
//    success: function(msg) {
//        socket.send(JSON.stringify({
//            "command": "updatetokens",
//            "roomId": roomId,
//            "user": username,
//         }));
//    }
//  });
//}

function increment_other(indicator) {
  console.log("Increment Other");
  url = incrementOther;
  $('#infectionRate').toggleClass( "circle_toggle" );
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
        socket.send(JSON.stringify({
            "command": "updatetokens",
            "roomId": roomId,
            "user": username,
         }));
    }
  });
}

function decrement_other(indicator) {
  console.log("Decrement Other");
  url = decrementOther;
  $('infectionRate').toggleClass( "circle_toggle" );
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
        socket.send(JSON.stringify({
            "command": "updatetokens",
            "roomId": roomId,
            "user": username,
         }));
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
      notes = msg["notes"];
      notes = notes.replace(new RegExp("-", "g"), "\n");
      $("#notes").text(notes);
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
      socket.send(JSON.stringify({
            "command": "updatecures",
            "roomId": roomId,
            "user": username,
         }));
    }
  });
}

