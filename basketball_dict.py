players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, players_dict):
        self.name = players_dict["name"]
        self.age = players_dict["age"]
        self.position = players_dict["position"]
        self.team = players_dict["team"]

# player_kevin = Player(players[0])
# player_jason = Player(players[1])
# player_kyrie = Player(players[2])
# player_damian = Player(players[3])
# player_joel = Player(players[4])
# player_demar = Player(players[5])

new_team = []
for i in range(len(players)):
    new_team.append(Player(players[i]))

@classmethod
def get_team(cls, team_list):
    player_list = []
    for i in range(len(team_list)):
        player_list.append(Player(team_list[i]))
    return player_list