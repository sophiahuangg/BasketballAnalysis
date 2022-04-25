import pandas as pd
import time
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv2, boxscoreadvancedv2
from nba_api.stats.static import teams


custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


# Getting the Mavs' team id
nba_teams = teams.get_teams()
for i in nba_teams:
    if i['abbreviation'] == 'DAL':
        print("i=", i)
        team_id = i['id']
        print("team_id=", team_id)

# Looking at Mavs' games
gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable = '2021-22', league_id_nullable='00', season_type_nullable='Regular Season')
mavs_games = gamefinder.get_data_frames()[0]
print(mavs_games.to_csv(r"/Users/sophia/Desktop/Interview/mavs.csv"))


# Looking at Mavs' box score from their games
mavs_game_ids = mavs_games['GAME_ID'].unique().tolist() #finds unique game ids
print("mavs game ids=", mavs_game_ids)

# Advanced Box Scores
box_score_advanced = []
def get_box_score(mavs_game_ids):
    for game_id in mavs_game_ids:
        print("GAME=", game_id)
        box_score_data = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id)
        df = box_score_data.player_stats.get_data_frame()
        box_score_advanced.append(df)
        print(box_score_advanced)
        time.sleep(1)
    full_df = pd.concat(box_score_advanced, ignore_index = True)
    print("full_df=", full_df)
    return full_df.to_csv(r"/Users/sophia/Desktop/Interview/mavsBoxScoresAdvanced21_22.csv")
    
get_box_score(mavs_game_ids)

# Traditional Box Scores

box_score_traditional = []
def get_box_score(mavs_game_ids):
    for game_id in mavs_game_ids:
        print("GAME=", game_id)
        box_score_data = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id)
        df = box_score_data.player_stats.get_data_frame()
        box_score_traditional.append(df)
        print(box_score_traditional)
        time.sleep(1)
    full_df = pd.concat(box_score_traditional, ignore_index = True)
    print("full_df=", full_df)
    return full_df.to_csv(r"/Users/sophia/Desktop/Interview/mavs_box_scores21_22.csv")
    
get_box_score(mavs_game_ids)



