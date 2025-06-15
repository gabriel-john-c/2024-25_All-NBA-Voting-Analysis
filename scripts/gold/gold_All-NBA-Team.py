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

#average vote score - vote sum divided by total number of voters (100)
df_points_calc['avg-vote-score'] = (df_points_calc['total-pts']) / len(voters)

#create df for voter skew, voters as index, columns for each player
df_voter_skew = pd.DataFrame(index=voters,columns=players)

#loop through our new skew df
for i, row in df_voter_skew.iterrows():
    skew_voter = i #store the voter name
    for column, value in row.items():
      skew_player = column #store the player name

      #lookup the average score of the player by referencing the df_points_calc dataframe
      skew_player_avg_score = df_points_calc.loc[df_points_calc.index == skew_player,'avg-vote-score'].values[0]
      
      #calculate the voters value assignment, get the team assignment (team1 / team2 / team3)
      skew_voter_player_team = df[df['voter'] == skew_voter].apply(lambda row: row[row == skew_player], axis=1).columns.values
      
      #calculate the points depending on the team
      if skew_voter_player_team.size > 0: #if the array has items - some players are omitted from voters ballots resulting in empty value here
        if skew_voter_player_team[0].startswith('Team1'):
          skew_voter_player_value = 5
        elif skew_voter_player_team[0].startswith('Team2'):
          skew_voter_player_value = 3
        elif skew_voter_player_team[0].startswith('Team3'):
          skew_voter_player_value = 1
      else:
        skew_voter_player_value = 0 #default value for ommissions
      
      #calculate the skew for this voter + player combination. take assigned value - avg value to determine skew. 0 is exact, negative value is undervalueing/unconventional, positive value is overvalue/conventional
      skew = round(skew_voter_player_value - skew_player_avg_score, 2)
      print(f"Player: {skew_player} has an avg score of: {skew_player_avg_score} points")
      print(f"Voter skew {skew_voter} for player {skew_player} is {skew} points")
      #update/store skew in cell for df_voter_skew dataframe
      df_voter_skew.at[i, column] = skew

#print(team_vote_categories)
#print(player_team_counts)
#print(df_points_calc)
print(df_voter_skew)
#print(df[df['voter'] == 'David Aldridge'])
#print(df[df['voter'] == 'David Aldridge'].apply(lambda row: row[row == 'Giannis Antetokounmpo, Milwaukee'], axis=1).columns.values[0])
#print(df_points_calc.loc[df_points_calc.index == 'Giannis Antetokounmpo, Milwaukee','avg-vote-score'])