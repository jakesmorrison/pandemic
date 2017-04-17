class Config(object):
    cities = [
        {"city": "Milan","country":"Italy","population":5232000,"color":"blue","type":"Type 1","connectionCities":["Essen","Paris","Istanbul"]},
        {"city": "Montreal", "country": "Canada", "population":3429000 , "color": "blue", "type": "Type 1","connectionCities": ["Chicago","Washington","New York"]},
        {"city": "Paris", "country": "France", "population":10755000, "color": "blue", "type": "Type 1", "connectionCities": ["Madrid","London","Essen","Algiers","Milan"]},
        {"city": "Chicago", "country": "United States", "population":9121000, "color": "blue", "type": "Type 1", "connectionCities": ["San Francisco", "Los Angeles", "Atlanta", "Mexico City", "Montreal"]},
        {"city": "Atlanta", "country": "United States", "population":4715000, "color": "blue", "type": "Type 1", "connectionCities": ["Chicago","Washington","Miami"]},
        {"city": "St. Petersburg", "country": "Russia", "population":4879000, "color": "blue", "type": "Type 1", "connectionCities": ["Essen","Istanbul"]},
        {"city": "Madrid", "country": "Spain", "population":5427000, "color": "blue", "type": "Type 1", "connectionCities": ["New York","Sao Paulo","Paris","London","Algiers"]},
        {"city": "Washington", "country": "United States", "population":4679000, "color": "blue", "type": "Type 1", "connectionCities": ["Miami","Atlanta","Montreal","New York"]},
        {"city": "San Francisco", "country": "United States", "population":5864000, "color": "blue", "type": "Type 1", "connectionCities": ["Tokyo","Manila","Loas Angeles","Chicago"]},
        {"city": "London", "country": "United Kingdom", "population":8586000, "color": "blue", "type": "Type 1", "connectionCities": ["Madrid","New York","Paris","Essen"]},
        {"city": "Essen", "country": "Germany", "population":575000, "color": "blue", "type": "Type 1", "connectionCities": ["London","Paris","Milan","St. Petersburg"]},
        {"city": "New York", "country": "United States", "population": 20464000, "color": "blue", "type": "Type 1","connectionCities": ["Washington","Montreal","London","Madrid"]},
        {"city": "Osaka", "country": "Japan", "population":2871000 , "color": "red", "type": "Type 1","connectionCities": ["Tokyo","Taipei"]},
        {"city": "Manila", "country": "Philippines", "population":20767000, "color": "red", "type": "Type 1", "connectionCities": ["San Francisco","Ho Chi Minh City","Sydney","Taipei","Hong Kong"]},
        {"city": "Jakarta", "country": "Indonesia", "population":26063000, "color": "red", "type": "Type 1", "connectionCities": ["Chennai","Bangkok","Ho Chi Minh City","Sydney"]},
        {"city": "Ho Chi Minh City", "country": "Vietnam", "population":8314000, "color": "red", "type": "Type 1", "connectionCities": ["Jakarta","Bangkok","Hong Kong","Manila"]},
        {"city": "Sydney", "country": "Australia", "population":3785000, "color": "red", "type": "Type 1", "connectionCities": ["Los Angeles","Jakarta","Manila"]},
        {"city": "Shanghai", "country": "China", "population":13482000, "color": "red", "type": "Type 1", "connectionCities": ["Beijing","Seoul","Hong Kong","Taipei"]},
        {"city": "Beijing", "country": "China", "population":17311000, "color": "red", "type": "Type 1", "connectionCities": ["Shanghai","Seoul"]},
        {"city": "Bangkok", "country": "Thailand", "population":7151000, "color": "red", "type": "Type 1", "connectionCities": ["Chennai","Kolkata","Hong Kong","Ho Chi Minh City","Jakarta"]},
        {"city": "Tokyo", "country": "Japan", "population":13189000, "color": "red", "type": "Type 1", "connectionCities": ["San Francisco","Seoul","Shanghai","Osaka"]},
        {"city": "Hong Kong", "country": "China", "population":7106000, "color": "red", "type": "Type 1", "connectionCities": ["Kolkata","Bangkok","Ho Chi Minh City","Manila","Taipei","Shanghai"]},
        {"city": "Taipei", "country": "Taiwan", "population":8338000, "color": "red", "type": "Type 1", "connectionCities": ["Shanghai","Hong Kong","Manila","Osaka"]},
        {"city": "Seoul", "country": "South Korea", "population":22547000, "color": "red", "type": "Type 1", "connectionCities": ["Beijing","Shanghai","Tokyo"]},
        {"city": "Chennai", "country": "India", "population":8865000, "color": "black", "type": "Type 1","connectionCities": ["Mumbai","Delhi","Kolkata","Bangkok","Jakarta"]},
        {"city": "Algiers", "country": "Algeria", "population":2946000, "color": "black", "type": "Type 1", "connectionCities": ["Madrid","Paris","Istanbul","Cairo"]},
        {"city": "Karachi", "country": "Pakistan", "population":20711000, "color": "black", "type": "Type 1", "connectionCities": ["Baghdad","Riyadh","Mumbai","Delhi","Tehran"]},
        {"city": "Moscow", "country": "Russia", "population":15512000, "color": "black", "type": "Type 1", "connectionCities": ["St. Petersburg","Tehran","Istanbul"]},
        {"city": "Mumbai", "country": "India", "population":16910000, "color": "black", "type": "Type 1", "connectionCities": ["Karachi","Delhi","Chennai"]},
        {"city": "Baghdad", "country": "Iraq", "population":6204000, "color": "black", "type": "Type 1", "connectionCities": ["Cairo","Istanbul","Tehran","Karachi","Riyadh"]},
        {"city": "Riyadh", "country": "Saudi Arabia", "population":5037000, "color": "black", "type": "Type 1", "connectionCities": ["Cairo","Baghdad","Karachi"]},
        {"city": "Kolkata", "country": "India", "population":14374000, "color": "black", "type": "Type 1", "connectionCities": ["Delhi","Chennai","Bangkok","Hong Kong"]},
        {"city": "Delhi", "country": "India", "population":22242000, "color": "black", "type": "Type 1", "connectionCities": ["Tehran","Karachi","Mumbai","Chennai","Kolkata"]},
        {"city": "Cairo", "country": "Egypt", "population":14718000, "color": "black", "type": "Type 1", "connectionCities": ["Algiers","Istanbul","Baghdad","Riyadh","Khartoum"]},
        {"city": "Tehran", "country": "Iran", "population":7419000, "color": "black", "type": "Type 1", "connectionCities": ["Moscow","Baghdad","Karachi","Delhi"]},
        {"city": "Istanbul", "country": "Turkey", "population":13576000, "color": "black", "type": "Type 1", "connectionCities": ["Milan","St. Petersburg","Moscow","Baghdad","Cairo","Algiers"]},
        {"city": "Miami", "country": "United States", "population":5582000 , "color": "yellow", "type": "Type 1","connectionCities": ["Washington","Atlanta","Mexico City","Bogota"]},
        {"city": "Kinshasa", "country": "Congo", "population":9046000, "color": "yellow", "type": "Type 1", "connectionCities": ["Lagos","Khartoum","Johannesburg"]},
        {"city": "Buenos Aires", "country": "Argentina", "population":13639000, "color": "yellow", "type": "Type 1", "connectionCities": ["Bogota","Sao Paulo"]},
        {"city": "Mexico City", "country": "Mexico", "population":19463000, "color": "yellow", "type": "Type 1", "connectionCities": ["Los Angeles","Chicago","Miami","Bogota","Lima"]},
        {"city": "Lagos", "country": "Nigeria", "population":11547000, "color": "yellow", "type": "Type 1", "connectionCities": ["Sao Paulo","Kinshasa","Khartoum"]},
        {"city": "Johannesburg", "country": "South Africa", "population":3883000, "color": "yellow", "type": "Type 1", "connectionCities": ["Khartoum","Kinshasa"]},
        {"city": "Bogota", "country": "Colombia", "population":8702000, "color": "yellow", "type": "Type 1", "connectionCities": ["Miami","Mexico City","Lima","Buenos Aires","Sao Paulo"]},
        {"city": "Los Angeles", "country": "United States", "population":14900000, "color": "yellow", "type": "Type 1", "connectionCities": ["Sydney","Mexico City","San Francisco","Chicago"]},
        {"city": "Santiago", "country": "Chile", "population":6015000, "color": "yellow", "type": "Type 1", "connectionCities": ["Lima"]},
        {"city": "Lima", "country": "Peru", "population":9121000, "color": "yellow", "type": "Type 1", "connectionCities": ["Santiago","Bogota","Mexico City"]},
        {"city": "Khartoum", "country": "Sudan", "population":4887000, "color": "yellow", "type": "Type 1", "connectionCities": ["Lagos","Kinshasa","Johannesburg","Cairo"]},
        {"city": "Sao Paulo", "country": "Brazil", "population":20186000, "color": "yellow", "type": "Type 1", "connectionCities": ["Madrid","Lagos","Buenos Aires","Bogota"]},
    ]

    roles = [
        {"name":"Dispatcher",
         "description":"-Move another player's pawn as if it were yours. -As an action, move any pawn to a city with another pawn.",
         "color":"red",
         "type":"Type 3"
         },
        {"name": "Scientist",
         "description": "-You need only 4 cards of the same color to do the Discover a Cure action.",
         "color": "white",
         "type": "Type 3"
         },
        {"name": "Containment Specialist",
         "description": "-When you enter a city with 2 or more diesease cubes of the same color, remove one of them.",
         "color": "tan",
         "type": "Type 3"
         },
        {"name": "Field Operative",
         "description": "-Once per turn, as an action, you may move 1 diesease cube from the city you are in onto this Role Card. -When you Discover a Cure, you may replace 2 of the needed City cards with 3 cubes of the cure color from this card.",
         "color": "yellow",
         "type": "Type 3"
         },
        {"name": "Operations Expert",
         "description": "-As an action, build a research station in the city you are in. -Once per turn as an action, move from a research station to any city bu discarding any City Card.",
         "color": "lime",
         "type": "Type 3"
         },
        {"name": "Generalist",
         "description": "-You may do up to 5 actions each turn.",
         "color": "lavendar",
         "type": "Type 3"
         },
        {"name": "Medic",
         "description": "-Remove all cubes of one color when doing Treat Disease. -Automatically remove cubes of cured diseases from the city you are in (and prevent them from being placed there).",
         "color": "orange",
         "type": "Type 3"
         },
        {"name": "First Responder",
         "description": "-As an action, you may move to any city with a research station. -Immediately after an Epidemic, you may, out of turn, move to the epidemic city and Treat Disease there (before Infections).",
         "color": "lime",
         "type": "Type 3"
         },
        {"name": "Quarantine Specialist",
         "description": "-Prevent disease cube placements (and outbreaks) in the city you are in and all cities connected to it.",
         "color": "green",
         "type": "Type 3"
         },
        {"name": "Gene Splicer",
         "description": "-You may Discover a Cure at a research station - in a city of the color being cured by turning in 2 city cards of the cure color; plus 1 City card each of the 3 other (standard) disease colors.",
         "color": "violet",
         "type": "Type 3"
         },
        {"name": "Pharmcist",
         "description": "-As an action, reveal a City card to Treat Disease there. -As an action, remove 1 cube of a cured diesease from any city to the supply.",
         "color": "yellow",
         "type": "Type 3"
         },
        {"name": "Archivist",
         "description": "-Your hand limit is 8 cards. -Once per turn, as an action, you may take the City card that matches the city you are in from the Player Discard Pile into your hand.",
         "color": "blue",
         "type": "Type 3"
         },
        {"name": "Epidemiologist",
         "description": "-Once during your turn, you may take any City card from a player in the same city. Doing this is not an action.",
         "color": "pink",
         "type": "Type 3"
         },
        {"name": "Researcher",
         "description": "-As an action, you may give (or a player can take) any City card from your hand. You must both be in the same city. The card does not have to match the city you are in.",
         "color": "black",
         "type": "Type 3"
         },
        {"name": "Contingency Planner",
         "description": "-As an action, take any discarded Event card and store it on this card. -When you play the stored Event card, remove it from the game. -Limit 1 event card at a time, which is not part of your hand.",
         "color": "light blue",
         "type": "Type 3"
         },
        {"name": "Troubleshooter",
         "description": "-Start your turn by looking at as many Infection cards as the current infection rate. -When you do a Direct Flight, reveal the city card used, but do not discard it.",
         "color": "red",
         "type": "Type 3"
         },
    ]

    infectedCites = [{"city":x["city"],"country":x["country"],"color":x["color"],"type":"Type 2"}for x in cities]

    outbreaks = 1
    maxOutbreaks = 10

    infectionRate = [2,2,2,3,3,4,4]

    maxCubes = 24

    {"city": "Milan", "country": "Italy", "population": 5232000, "color": "blue", "type": "Type 1",
     "connectionCities": ["Essen", "Paris", "Istanbul"]},

    pandemic = {'city':'Pandemic!','Country':'','color':'','type':'',"connectionCities":[],'increase':'Move the infection rate marker forward 1 space',
                'infect':'Draw the bottom card from the Infection Deck and put 3 cubes on that city. Discard the card.',
                'intensify': 'Shuffle the cards in the Infection Discard and put them on top of the Infection Deck.'}


