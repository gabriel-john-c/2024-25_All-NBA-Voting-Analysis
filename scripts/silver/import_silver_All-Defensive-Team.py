import os
import pandas as pd

#grab working directory
current_dir = os.path.dirname(__file__)

#path for csv imput file
csv_path = os.path.join(current_dir, '..', '..', 'data', 'bronze', '2024-25-Kia-NBA-All-Defensive-Team-Voter-Selections.csv')
csv_path = os.path.abspath(csv_path)

#create pandas df
df = pd.read_csv(csv_path)

print(df)

columns = ['voter', 'affil', 'DefTeam1_1', 'DefTeam1_2', 'DefTeam1_3', 'DefTeam1_4', 'DefTeam1_5', 'DefTeam2_1', 'DefTeam2_2', 'DefTeam2_3', 'DefTeam2_4', 'DefTeam2_5']

df_clean = pd.DataFrame(
    [[row['Voter, Affiliation'].split(', ')[0], 
      row['Voter, Affiliation'].split(', ')[1], 
      row['All-Defensive First Team'], 
      row['All-Defensive First Team.1'], 
      row['All-Defensive First Team.2'], 
      row['All-Defensive First Team.3'], 
      row['All-Defensive First Team.4'], 
      row['All-Defensive Second Team'], 
      row['All-Defensive Second Team.1'], 
      row['All-Defensive Second Team.2'], 
      row['All-Defensive Second Team.3'], 
      row['All-Defensive Second Team.4']] for index, row in df.iterrows()], columns=columns
)

print(df_clean)

export_csv_path = os.path.join(current_dir, '..', '..', 'data', 'silver', 'silver_NBA-All_Defensive-Team.csv')

df_clean.to_csv(export_csv_path, encoding='utf-8', index=False)