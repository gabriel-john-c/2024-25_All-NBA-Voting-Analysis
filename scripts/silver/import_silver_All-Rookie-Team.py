import os
import pandas as pd

#grab working directory
current_dir = os.path.dirname(__file__)

#path for csv imput file
csv_path = os.path.join(current_dir, '..', '..', 'data', 'bronze', '2024-25-Kia-NBA-All-Rookie-Team-Voter-Selections.csv')
csv_path = os.path.abspath(csv_path)

#create pandas df
df = pd.read_csv(csv_path)

print(df)

columns = ['voter', 'affil', 'RookieTeam1_1', 'RookieTeam1_2', 'RookieTeam1_3', 'RookieTeam1_4', 'RookieTeam1_5', 'RookieTeam2_1', 'RookieTeam2_2', 'RookieTeam2_3', 'RookieTeam2_4', 'RookieTeam2_5']

df_clean = pd.DataFrame(
    [[row['Voter, Affiliation'].split(', ')[0], 
      row['Voter, Affiliation'].split(', ')[1], 
      row['ALL-ROOKIE FIRST TEAM'], 
      row['ALL-ROOKIE FIRST TEAM.1'], 
      row['ALL-ROOKIE FIRST TEAM.2'], 
      row['ALL-ROOKIE FIRST TEAM.3'], 
      row['ALL-ROOKIE FIRST TEAM.4'], 
      row['ALL-ROOKIE SECOND TEAM'], 
      row['ALL-ROOKIE SECOND TEAM.1'], 
      row['ALL-ROOKIE SECOND TEAM.2'], 
      row['ALL-ROOKIE SECOND TEAM.3'], 
      row['ALL-ROOKIE SECOND TEAM.4']] for index, row in df.iterrows()], columns=columns
)

print(df_clean)

export_csv_path = os.path.join(current_dir, '..', '..', 'data', 'silver', 'silver_NBA-All_Rookie-Team.csv')

df_clean.to_csv(export_csv_path, encoding='utf-8', index=False)