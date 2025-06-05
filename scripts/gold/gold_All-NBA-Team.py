import os
import pandas as pd

#grab working directory
current_dir = os.path.dirname(__file__)

#path for csv imput file
csv_path = os.path.join(current_dir, '..', '..', 'data', 'silver', 'silver_All-NBA-Team.csv')
csv_path = os.path.abspath(csv_path)

#create pandas df
df = pd.read_csv(csv_path)

#players only
players_df = df.drop(columns=['voter','affil'])

#stack table
stacked_df = players_df.stack()

#store a list of unique player names
players = stacked_df.unique()

#store a list of voters
voters = df['voter'].values

#store a list of each vote assignment
team_vote_categories = players_df.columns

#store new table of counts
player_team_counts = players_df.apply(pd.Series.value_counts).fillna(0)

#store individual team (1/2/3) votes per player
player_team_counts['team1-votes'] = player_team_counts['Team1_1'] + player_team_counts['Team1_2'] + player_team_counts['Team1_3'] + player_team_counts['Team1_4'] + player_team_counts['Team1_5']
player_team_counts['team2-votes'] = player_team_counts['Team2_1'] + player_team_counts['Team2_2'] + player_team_counts['Team2_3'] + player_team_counts['Team2_4'] + player_team_counts['Team2_5']
player_team_counts['team3-votes'] = player_team_counts['Team3_1'] + player_team_counts['Team3_2'] + player_team_counts['Team3_3'] + player_team_counts['Team3_4'] + player_team_counts['Team3_5']


#build points columns and index
points_columns = ['Team1_1', 'Team1_2', 'Team1_3', 'Team1_4', 'Team1_5', 'Team2_1', 'Team2_2', 'Team2_3', 'Team2_4', 'Team2_5', 'Team3_1', 'Team3_2', 'Team3_3', 'Team3_4', 'Team3_5']
points_index = player_team_counts.index

#points dataframe calculation
df_points_calc = pd.DataFrame(
    [[row['Team1_1'] * 5, 
      row['Team1_2'] * 5, 
      row['Team1_3'] * 5, 
      row['Team1_4'] * 5, 
      row['Team1_5'] * 5, 
      row['Team2_1'] * 3, 
      row['Team2_2'] * 3, 
      row['Team2_3'] * 3, 
      row['Team2_4'] * 3, 
      row['Team2_5'] * 3, 
      row['Team3_1'] * 1, 
      row['Team3_2'] * 1, 
      row['Team3_3'] * 1, 
      row['Team3_4'] * 1, 
      row['Team3_5'] * 1] for index, row in player_team_counts.iterrows()], columns=points_columns, index=points_index
)

#sum across columns, store in new column
df_points_calc['total-pts'] = df_points_calc[list(df_points_calc.columns)].sum(axis=1)

#.drop(columns=points_columns)
print(team_vote_categories)
print(player_team_counts)
print (df_points_calc)