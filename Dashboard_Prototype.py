# Laser Tag data -----------------------------------------------------------------------------------
# Player Names
red_team_players = [ "Einstein",  "Bond",  "Spock",  "Noob",  "Snake",  "Pineapple",  "Kirk",  "Worf",  "Bean",  "Mabel" ]
green_team_players = [ "Cupcake",  "Boss Level",  "Pudding",  "Watermelon",  "Ham Sandwich",  "Hot Sauce",  "Jelly Bean",  "Rambo",  "Weasley",  "Sherlock" ]

# Red Player Scores for Games 1-8
red_player_scores_game_1 = [ 32645, 43254, 30085, 27778, 34794, 22655, 32973, 22573, 52667, 22427 ]
red_player_scores_game_2 = [ 44130, 40428, 20832, 34975, 36619, 36397, 31588, 42207, 14973, 21269 ]
red_player_scores_game_3 = [ 32163, 53576, 26532, 28946, 11174, 11714, 27134, 30225, 23268, 26403 ]
red_player_scores_game_4 = [ 21929, 49045, 38619, 25720, 22744, 53698, 30021, 37116, 24387, 47893 ]
red_player_scores_game_5 = [ 55633, 24876, 32801, 20512, 47961, 23739, 37963, 25277, 22272, 33279 ]
red_player_scores_game_6 = [ 30177, 19649, 31110, 15494, 33072, 42076, 41820, 31452, 33373, 42131 ]
red_player_scores_game_7 = [ 31759, 31375, 31975, 24144, 24347, 30379, 36231, 24711, 41653, 38181 ]
red_player_scores_game_8 = [ 35060, 15172, 42249, 17547, 12911, 17610, 19106, 29184, 29837, 28373 ]

# Green Player Scores for Games 1-8
green_player_scores_game_1 = [ 24548, 36897, 37525, 56700, 32273, 33940, 20613, 28572, 33729, 35685 ]
green_player_scores_game_2 = [ 39750, 44572, 6245, 36579, 37148, 31459, 46677, 35618, 35141, 35239 ]
green_player_scores_game_3 = [ 36341, 37177, 38622, 42036, 23647, 45705, 36379, 26774, 23467, 33767 ]
green_player_scores_game_4 = [ 29791, 22841, 36018, 39865, 20988, 31962, 13360, 31564, 28691, 33899 ]
green_player_scores_game_5 = [ 17418, 35085, 29004, 11515, 25331, 26541, 32692, 33534, 42084, 23517 ]
green_player_scores_game_6 = [ 38350, 9773, 40169, 36308, 24686, 36011, 29035, 21147, 43224, 36988 ]
green_player_scores_game_7 = [ 42046, 31046, 44619, 25441, 35483, 36049, 19678, 25663, 38857, 36171 ]
green_player_scores_game_8 = [ 37927, 27397, 33541, 52990, 15259, 29571, 31181, 22372, 26975, 34130 ]

# Team Roster Dashboard Prototype ----------------------------------------------------------

# store the number of players on the green team and red team value
num_green_players = len(green_team_players)
num_red_players = len(red_team_players)

# Generate the output
print("Team Roster Dashboard Prototype\n")
print("-" * len("Part A: Team Roster Dashboard Prototype"))
print('The Green Team has {} players\n'.format(num_green_players))
      
print("Player        Name")
print("-" * len("Player") + " " * len("        ") + "-" * len("Name"))
      

# Reformat the output, making it neater
blankSpace = ""
for i in range(num_green_players):
    blankSpace = " " * (len("Player        ")-1)
    if i == 9:
        blankSpace = " " * (len("Player        ")-2)
    print('{}{}{}'.format(i+1, blankSpace, green_team_players[i]))

        

print('\nThe Red Team has {} players\n'.format(num_red_players))
print("Player        Name")
print("-" * len("Player") + " " * len("        ") + "-" * len("Name"))

blankSpace = ""
for i in range(num_red_players):
    blankSpace = " " * (len("Player        ")-1)
    if i == 9:
        blankSpace = " " * (len("Player        ")-2)
    print('{}{}{}'.format(i+1, blankSpace, red_team_players[i]))


# Game Summary Dashboard Prototype A ----------------------------------------------------------

# Put all player_score_games lists in a large list(list in list)
green_player_scores_game_total = [green_player_scores_game_1, green_player_scores_game_2, green_player_scores_game_3,
                                  green_player_scores_game_4, green_player_scores_game_5, green_player_scores_game_6,
                                  green_player_scores_game_7, green_player_scores_game_8]
red_player_scores_game_total = [red_player_scores_game_1, red_player_scores_game_2, red_player_scores_game_3,
                                red_player_scores_game_4, red_player_scores_game_5, red_player_scores_game_6,
                                red_player_scores_game_7, red_player_scores_game_8]

print("\nGame Summary Dashboard Prototype A\n------------------------------------------\n")
print('Game       Green        Red\n----       -----        ---')

#  calculate the total points scored by the Green and Red Teams and generate the output.
numberOfGames = len(green_player_scores_game_total)
green_team_scores = []
red_team_scores = []
for i in range(numberOfGames):
        green_team_scores.append(sum(green_player_scores_game_total[i]))
        red_team_scores.append(sum(red_player_scores_game_total[i]))
        print('{}          {:,}      {:,}'.format(i+1, green_team_scores[i], red_team_scores[i]))


# Game Summary Dashboard Prototype B ----------------------------------------------------------

# Create the empty lists
green_team_scores = []
red_team_scores = []
games_winners = []
games_total_points = []

# Use a loop to iterate once for each game played.
# For each game, determine the score that Green and Red teams got, which team won and the total score
for i in range(numberOfGames):
        green_team_scores.append(sum(green_player_scores_game_total[i]))
        red_team_scores.append(sum(red_player_scores_game_total[i]))
        if sum(green_player_scores_game_total[i]) > sum(red_player_scores_game_total[i]):
            games_winners.append('Green')
        elif sum(green_player_scores_game_total[i]) < sum(red_player_scores_game_total[i]):
            games_winners.append('Red')
        games_total_points.append(sum(green_player_scores_game_total[i]) + sum(red_player_scores_game_total[i]))

# generate the output

from beautifultable import BeautifulTable
table = BeautifulTable()

for i in range(numberOfGames):
    table.rows.append([i+1, '{:,}'.format(green_team_scores[i]),
                       '{:,}'.format(red_team_scores[i]),
                       '{:,}'.format(games_total_points[i]),
                       games_winners[i]])

table.columns.header = ['Game','Green','Red','Total','Winner']

# Modify the table format
table.columns.alignment["Winner"] = BeautifulTable.ALIGN_LEFT 
table.columns.alignment["Game"] = BeautifulTable.ALIGN_LEFT

print("\nGame Summary Dashboard Prototype B\n------------------------------------------\n")
print(table)


# Part D: Green Team Post-Game Dashboard Prototype ------------------------------------------------------

# Calculate the number of games won by the Green Team.
num_games_won_by_green_team = games_winners.count('Green')

# Calculate the Green Team win percentage.
green_team_win_percentage = num_games_won_by_green_team / numberOfGames * 100

# Calculate the average Green Team score per game.
import statistics
green_team_average_score = statistics.mean(green_team_scores)

# Calculate the total individual points scored for each Green Team player across all games.
green_player_total_points = []
green_player_average_points = []

for i in range(num_green_players):
    each_player_points = []
    for k in range(numberOfGames):
        each_player_points.append(green_player_scores_game_total[k][i])
    green_player_total_points.append(sum(each_player_points))
    green_player_average_points.append(statistics.mean(each_player_points))


# Determine which Green Team players averaged at least 30,000 points per game.

all_stars = []
test = []

# Initialize the list 'test' to store boolean values. For each 'green player', 
# the list contains 'True' if their average score is at least 30000, otherwise 'False'.

for i in range(len(green_player_average_points)):
    test.append(green_player_average_points[i] >= 30000)

# making all_stars list contains all the elements of the green_team_players list corresponding to True in test list
for i in range(len(test)):
    if test[i]:
        all_stars.append(green_team_players[i])


# determine the Most Valuable Player (the "MVP"): the highest scoring player
mvp_name = []
mvp_total_points = []

for i in range(len(green_player_total_points)):
    if green_player_total_points[i] == max(green_player_total_points):
        mvp_total_points.append(green_player_total_points[i])
        mvp_name.append(green_team_players[i])


# Generate the example output
print("\nGreen Team Post-Game Dashboard Prototype\n------------------------------------------------\n")

print("Number of players:        {}".format(num_green_players))
print("Games won:                {} of {} ({:1}%)".format(num_games_won_by_green_team,
                                                            numberOfGames,
                                                            green_team_win_percentage))
print("Average team score:       {:,} points".format(green_team_average_score))

all_star_display = all_stars[:]
all_star_display.remove(mvp_name[0])

print("All-Stars:               " , *all_star_display)
print("MVP:                      " + mvp_name[0] + " ({:,} total points)".format(mvp_total_points[0]))

    

# Part E: player Summary Dahiboard Prototype  ------------------------------------------------------

# Calculate the total number of points scored by the Green Team across all games.
green_total_number_of_points = sum(green_player_total_points)

# Each player's score is extracted into a list and placed in a large player_points list(list in list)
player_points = []
for i in range(num_green_players):
    each_player_points = []
    for k in range(numberOfGames):
        each_player_points.append(green_player_scores_game_total[k][i])
    player_points.append(each_player_points)

# Use a loop to iterate over each Green Team player.

best_score = []
best_game = []
worst_score = []
worst_game = []
average_score = []
total_number_of_points = []
percentage_scored = []

for i in range(num_green_players):
    best_score.append(max(player_points[i]))
    worst_score.append(min(player_points[i]))
    average_score.append(statistics.mean(player_points[i]))
    total_number_of_points.append(sum(player_points[i]))
    percentage_scored.append(sum(player_points[i]) / green_total_number_of_points *100)
    for k in range(numberOfGames):
        if player_points[i][k] == max(player_points[i]):
            best_game.append(k+1)
        if player_points[i][k] == min(player_points[i]):
            worst_game.append(k+1)
    

# Use the beautifultable Python package to achieve column-based layout.

table = BeautifulTable()
for i in range(num_green_players):
    display_data = (green_team_players[i], "{:,} ({})".format(best_score[i], best_game[i]),
                      "{:,} ({})".format(worst_score[i], worst_game[i]),
                      "{:,.3f}".format(average_score[i]), "{:,}".format(total_number_of_points[i]),
                      "{}%".format(round(percentage_scored[i],1)))
    table.rows.append(display_data)
                      
table.columns.header = ['Player','Best','Worst','Average','Total','Percent']

# print the result
print("\nPlayer Summary Dahiboard Prototype\n------------------------------------------")
print("\nGreen Team\n")
print(table)




