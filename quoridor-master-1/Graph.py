
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data into a DataFrame
# Replace 'your_data.csv' with the path to your data file
data =  pd.read_csv('purple_cluster.csv')



# Prepare the data for win rates
win_rate_p1 = data[data['winner'] == 1].shape[0] 
win_rate_p2 = data[data['winner'] == 2].shape[0] 

labels = ['P1 (Alpha-Beta-Pruning)', 'P2 (Monte Carlo Tree Search)']
win_rates = [win_rate_p1, win_rate_p2]

# Creating the plot
plt.figure(figsize=(8, 5))

# Title and labels
plt.title('Win Rate Comparison')
plt.ylabel('Win Rate')

# Adding text labels above the bars
bars = plt.bar(labels, win_rates, width=0.06, color=['green', 'red'])
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=10)

plt.show()


# # Data preparation and setting up your plot
# palette = {1: "green", 2: "red"}  # Adjust keys based on your actual data labels
# plt.figure(figsize=(10, 6))
# plot = sns.scatterplot(x='exec_time', y='num_turns', hue='winner', data=data, palette=palette)

# # Setting up titles and labels
# plt.title('Execution Time vs Number of Turns')
# plt.xlabel('Execution Time')
# plt.ylabel('Number of Turns')

# # Customizing legend labels
# handles, labels = plot.get_legend_handles_labels()
# labels = ['P1 (Alpha-Beta-Pruning)', 'P2 (Monte Carlo Tree Search)']
# plt.legend(handles, labels, title='Winner')

# plt.show()


# # Calculate the average execution time for each winner
# avg_exec_time_p1 = data[data['winner'] == 'P1']['exec_time'].mean()
# avg_exec_time_p2 = data[data['winner'] == 'P2']['exec_time'].mean()

# # Prepare the plot
# plt.figure(figsize=(8, 5))  # Match the size to the first plot

# winners = ['P1 (Alpha-Beta-Pruning)', 'P2 (Monte Carlo Tree Search)']
# avg_times = [avg_exec_time_p1, avg_exec_time_p2]
# bars = plt.bar(winners, avg_times, width=0.06, color=['green', 'red'])  # Adjusted width for aesthetic match

# # Adding labels and title
# plt.xlabel('Winner')
# plt.ylabel('Average Execution Time (seconds)')
# plt.title('Average Execution Time by Winner')

# # Add text annotations on the bars
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=10)  # Adjusted text positioning and formatting

# plt.show()

# # Calculate the average number of turns for each winner
# average_turns_p1 = data[data['winner'] == 'P1']['num_turns'].mean()
# average_turns_p2 = data[data['winner'] == 'P2']['num_turns'].mean()

# # Data to plot
# winners = ['P1 (Alpha-Beta-Pruning)', 'P2 (Monte Carlo Tree Search)']
# averages = [average_turns_p1, average_turns_p2]

# # Creating the bar plot
# plt.figure(figsize=(8, 6))
# bars = plt.bar(winners, averages, width=0.06, color=['green', 'red'])

# # Adding labels and title
# plt.xlabel('Winner')
# plt.ylabel('Average Number of Turns')
# plt.title('Average Number of Turns by Winner')
# plt.ylim(0, max(averages) + 5)  # Adjust the y-axis limit to have some space above the highest bar

# # Labeling the bars
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2), ha='center', va='bottom')

# # Show the plot
# plt.show()



# # Plotting remaining walls
# plt.figure(figsize=(8, 4))
# plt.boxplot([data['p1_rem_walls'], data['p2_rem_walls']], labels=['P1 (Alpha-Beta-Pruning)', 'P2 (Monte Carlo Tree Search)'])
# plt.title('Remaining Walls Comparison')
# plt.ylabel('Remaining Walls')
# plt.show()




# # Calculate the average distance to the goal for each player
# average_distance_p1 = data['Distance of p1 to the goal'].mean()
# average_distance_p2 = data['Distance of p2 to the goal'].mean()

# # Creating the plot
# plt.figure(figsize=(8, 5))

# # Title and labels
# plt.title('Average Distance to the Goal')
# plt.ylabel('Average Distance')

# # Data for plotting
# players = ['P1 (Alpha-Beta-Pruning)', 'P2 (Monte Carlo Tree Search)']
# averages = [average_distance_p1, average_distance_p2]

# # Plotting bars
# bars = plt.bar(players, averages, width=0.06, color=['green', 'red'])

# # Adding text labels above the bars
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=10)

# # Show the plot
# plt.show()
























# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load data from three CSV files
# df1 = pd.read_csv('/Users/DELL/Desktop/Code/excel/Alpha beta pruning & Expectimax with randomness.csv')
# df2 = pd.read_csv('/Users/DELL/Desktop/Code/excel/Alpha beta pruning & Monte Carlo with randomness.csv')
# df3 = pd.read_csv('/Users/DELL/Desktop/Code/excel/Alpha beta pruning & Expectimax with randomness.csv')

# # Add a 'Dataset' column to identify the data
# df1['Dataset'] = 'Minimax vs Expectimax'
# df2['Dataset'] = 'Minimax vs Monte Carlo 1'
# df3['Dataset'] = 'Minimax vs Monte Carlo 2'

# # Combine the three datasets
# df = pd.concat([df1, df2, df3])

# # Compare average execution time by algorithm and dataset
# plt.figure(figsize=(12, 6))
# sns.barplot(x='Dataset', y='exec_time', hue='algorithm', data=df)
# plt.title('Average Execution Time by Algorithm and Dataset')
# plt.xlabel('Dataset')
# plt.ylabel('Execution Time')
# plt.xticks(rotation=45)
# plt.legend(title='Algorithm')
# plt.show()

# # Win rate comparison (assuming 'winner' column exists and contains the algorithm name)
# win_rates = df.pivot_table(index='Dataset', columns='winner', values='exec_time', aggfunc='count') / df.groupby('Dataset').size()
# win_rates.plot(kind='bar', figsize=(12, 6))
# plt.title('Win Rate by Algorithm and Dataset')
# plt.xlabel('Dataset')
# plt.ylabel('Win Rate')
# plt.xticks(rotation=45)
# plt.show()

