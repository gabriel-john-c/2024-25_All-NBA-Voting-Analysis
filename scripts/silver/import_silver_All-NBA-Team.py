import os
import pandas as pd

#grab working directory
current_dir = os.path.dirname(__file__)

#path for csv imput file
csv_path = os.path.join(current_dir, '..', '..', 'data', 'bronze', '2024-25-Kia-All-NBA-Team-Voter-Selections.csv')
csv_path = os.path.abspath(csv_path)

#create pandas df
df = pd.read_csv(csv_path)

print(df)

columns = ['voter', 'affil', 'Team1_1', 'Team1_2', 'Team1_3', 'Team1_4', 'Team1_5', 'Team2_1', 'Team2_2', 'Team2_3', 'Team2_4', 'Team2_5', 'Team3_1', 'Team3_2', 'Team3_3', 'Team3_4', 'Team3_5']

df_clean = pd.DataFrame(
    [[row['Voter, Affiliation'].split(', ')[0], 
      row['Voter, Affiliation'].split(', ')[1], 
      row['ALL-NBA FIRST TEAM'], 
      row['ALL-NBA FIRST TEAM.1'], 
      row['ALL-NBA FIRST TEAM.2'], 
      row['ALL-NBA FIRST TEAM.3'], 
      row['ALL-NBA FIRST TEAM.4'], 
      row['ALL-NBA SECOND TEAM'], 
      row['ALL-NBA SECOND TEAM.1'], 
      row['ALL-NBA SECOND TEAM.2'], 
      row['ALL-NBA SECOND TEAM.3'], 
      row['ALL-NBA SECOND TEAM.4'], 
      row['ALL-NBA THIRD TEAM'], 
      row['ALL-NBA THIRD TEAM.1'], 
      row['ALL-NBA THIRD TEAM.2'],
      row['ALL-NBA THIRD TEAM.3'], 
      row['ALL-NBA THIRD TEAM.4']] for index, row in df.iterrows()], columns=columns
)

print(df_clean)

export_csv_path = os.path.join(current_dir, '..', '..', 'data', 'silver', 'silver_All-NBA-Team.csv')

df_clean.to_csv(export_csv_path, encoding='utf-8', index=False)