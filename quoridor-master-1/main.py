from console.game import Game
import csv
import numpy as np 

# np.random.seed(5)
n = int(input("Enter the number of iterations: "))

# Create an empty list to store the dictionaries
data_rows = []

for i in range(1,n+1):
    print(i)
    g = Game()
    g.play()
    g.save_end_state()
    # Create a dictionary for each iteration
    row = {}
    row['p1 algorithm name'] = g.player_simulation_algorithms[0]
    row['p2 algorithm name'] = g.player_simulation_algorithms[1]
    row['winner'] = g.game_state.get_winner() 
    row['game_result'] = g.game_state.game_result()  
    row['exec_time'] = sum(g.execution_times)
    row['num_turns'] = len(g.execution_times)
    row['p1_rem_walls'] = g.game_state.player_one_walls_num  # Count the number of remaining walls for player one
    row['p2_rem_walls'] = g.game_state.player_two_wall_num  # Count the number of remaining walls for player two
    row['Distance of p1 to the goal'] = g.game_state.player_one_pos[0] # Distance to the goal
    row['Distance of p2 to the goal'] = 16 - g.game_state.player_two_pos[0] # Distance to the goal

    # Append the dictionary to the list
    data_rows.append(row)
    if i == 0.25*n:
        print(f"{25} % is done")
    elif i==0.5*n:
        print(f"{50} % is done")
    elif i==0.75*n:
        print(f"{75} % is done")
    elif i==1*n:
        print(f"{100} % is done")
    else:
        continue


# field names
fields = ['winner', 'game_result', 'exec_time', 'num_turns', 'p1_rem_walls', 'p2_rem_walls', 'p1 algorithm name', 'p2 algorithm name', 'Distance of p1 to the goal', 'Distance of p2 to the goal']

# name of the CSV file
filename = "quoridor_data.csv"

# writing to the CSV file
with open(filename, 'w', newline='') as csvfile:
    # creating a csv writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(data_rows)

print(data_rows)