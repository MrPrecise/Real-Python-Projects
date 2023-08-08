import pandas as pd

# Read the csv files
player_stats = pd.read_csv('data/2017-18_playerBoxScore.csv',
                           parse_dates=['gmDate'])
team_stats = pd.read_csv('data/2017-18_teamBoxScore.csv',
                         parse_dates=['gmDate'])
standings = pd.read_csv('data/2017-18_standings.csv',
                        parse_dates=['stDate'])

# Create west_top_2
west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') |
              (standings['teamAbbr'] == 'GS')]
              .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
              .sort_values(['teamAbbr', 'stDate']))

# Find players who took at least 1 three-point shot during the season
three_takers = player_stats[player_stats['play3PA'] > 0]

# Clean up the player names, placing them in a single column
three_takers['name'] = [f'{p["playFNm"]} {p["playLNm"]}'
                        for _, p in three_takers.iterrows()]

# Aggregate the total three-point attempts and makes for each player
three_takers = (three_takers.groupby('name')
                            .sum()
                            .loc[:, ['play3PA', 'play3PM']]
                            .sort_values('play3PA', ascending=False))

# Filter out anyone who didn't take at least 100 three-point shots
three_takers = three_takers[three_takers['play3PA'] >= 100].reset_index()

# Add a column with a calculated three-point percentage (made/attempted)
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']
