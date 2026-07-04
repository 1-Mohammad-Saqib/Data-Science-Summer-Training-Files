# create a data structure to store the data of players of 2021 that world cup already happend store in tuples and 2027 that world cup is going to happen store in dictionaries
# year = int(input("Enter the year (2021 or 2027): "))
# if year == 2021:
#     players_2021 = (
#         ("Player 1", "Team A", 10),
#         ("Player 2", "Team B", 5),
#         ("Player 3", "Team C", 8),
#         ("Player 4", "Team D", 12),
#     )
# elif year == 2027:
#     players_2027 = {
#         "Player 1": {"team": "Team A", "runs": 10},
#         "Player 2": {"team": "Team B", "runs": 5},
#         "Player 3": {"team": "Team C", "runs": 8},
#         "Player 4": {"team": "Team D", "runs": 12},
#     }
# if year == 2021:
#     players_2021 = (
#         ("Player 1", "Team A", 10),
#         ("Player 2", "Team B", 5),
#         ("Player 3", "Team C", 8),
#         ("Player 4", "Team D", 12),
#     )
#     print("Players of 2021 World Cup:")
#     for player in players_2021:
#         print(f"Name: {player[0]}, Team: {player[1]}, Runs: {player[2]}")
# elif year == 2027:
#     players_2027 = {
#         "Player 1": {"team": "Team A", "runs":0 },
#         "Player 2": {"team": "Team B", "runs":0},
#         "Player 3": {"team": "Team C", "runs":0},
#         "Player 4": {"team": "Team D", "runs": 0},
#     }
#     append_runs = int(input("Enter the runs scored by each player in 2027 World Cup: "))
#     for player_name in players_2027:
#         players_2027[player_name]["runs"] = append_runs
#     print("Players of 2027 World Cup:")
#     for player_name, player_info in players_2027.items():
#         print(f"Name: {player_name}, Team: {player_info['team']}, Runs: {player_info['runs']}")

# else:
#     print("Invalid year. Please enter either 2021 or 2027.")

# 2021 World Cup players (stored in tuples)
world_cup_2021 = (
    ("Babar Azam", "Pakistan", "Captain"),
    ("Virat Kohli", "India", "Batsman"),
    ("Kane Williamson", "New Zealand", "Captain"),
    ("Jos Buttler", "England", "Wicketkeeper"),
    ("David Warner", "Australia", "Batsman")
)

# 2027 World Cup players (stored in a dictionary)
world_cup_2027 = {
    "Pakistan": {
        "Captain": "Babar Azam",
        "Player": "Mohammad Rizwan"
    },
    "India": {
        "Captain": "Shubman Gill",
        "Player": "Yashasvi Jaiswal"
    },
    "Australia": {
        "Captain": "Pat Cummins",
        "Player": "Travis Head"
    },
    "England": {
        "Captain": "Jos Buttler",
        "Player": "Harry Brook"
    }
}

print("=== 2021 World Cup Players (Tuple) ===")
for player in world_cup_2021:
    print(player)

print("\n=== 2027 World Cup Players (Dictionary) ===")
for country, details in world_cup_2027.items():
    print(country, ":", details)