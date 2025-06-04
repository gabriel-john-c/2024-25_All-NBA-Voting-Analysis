import os
import pandas as pd

#grab working directory
current_dir = os.path.dirname(__file__)

#path for csv imput file
csv_path = os.path.join(current_dir, '..', '..', 'data', 'bronze', '2024-25-Kia-NBA-Most-Valuable-Player-Voter-Selections.csv')
csv_path = os.path.abspath(csv_path)

#create pandas df
df = pd.read_csv(csv_path)

for index, row in df.iterrows():
    voter_raw = row['Voter, Affiliation']
    voter = voter_raw.split(', ')[0]
    affiliation = voter_raw.split(', ')[1]
    print('{0} - {1}'.format(voter, affiliation))

    place_1 = row['1st Place (10 points)']
    place_2 = row['2nd Place (7 points)']
    place_3 = row['3rd Place (5 points)']
    place_4 = row['4th Place (3 points)']
    place_5 = row['5th Place (1 point)']

print(df)

columns = ['voter', 'affil', '1st', '2nd', '3rd', '4th', '5th']

df_clean = pd.DataFrame(
    [[row['Voter, Affiliation'].split(', ')[0], row['Voter, Affiliation'].split(', ')[1], row['1st Place (10 points)'], row['2nd Place (7 points)'], row['3rd Place (5 points)'], row['4th Place (3 points)'], row['5th Place (1 point)']] for index, row in df.iterrows()], columns=columns
)

print(df_clean)