import os
import requests
import pandas as pd
import time
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

while True:
    name = input("Enter name: ")
    tag = input("Enter tag: ")
    
    #grabs account details
    account_response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}" , headers = {"Authorization":API_KEY,"Accept":"*/*"})
    if account_response.status_code == 200:    
        account_data = account_response.json()
        puuid = account_data["data"]["puuid"]
        region = account_data["data"]["region"]
        
        #grabs full match history and data for that player
        #params for now
        match_response = requests.get(f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}", headers = {"Authorization":API_KEY,"Accept":"*/*"}, params={"size": 20})
        match_data = match_response.json()
        
        #sets empty list for each match's dataframe
        all_frames = []
        
        #loop for all matches pulled
        for match in match_data["data"]:
            metadata = pd.json_normalize(match["metadata"])
            players = pd.json_normalize(match["players"]["all_players"])
            teams_raw = pd.json_normalize(match["teams"])
            
            #adds matchid column to players
            players["matchid"] = metadata["matchid"].iloc[0] 
            
            #adds team color to metrics
            teams = pd.DataFrame([
            {"team": "Red", "has_won": teams_raw["red.has_won"].iloc[0], "rounds_won": teams_raw["red.rounds_won"].iloc[0], "rounds_lost": teams_raw["red.rounds_lost"].iloc[0]},
            {"team": "Blue", "has_won": teams_raw["blue.has_won"].iloc[0], "rounds_won": teams_raw["blue.rounds_won"].iloc[0], "rounds_lost": teams_raw["blue.rounds_lost"].iloc[0]}])
            
            #merges
            players_teams_merge = pd.merge(players, teams, on="team", how="left")
            match_frame = pd.merge(metadata, players_teams_merge, on="matchid", how="left")
            
            #adds dataframe to list
            all_frames.append(match_frame)

        #combines all dataframes into one
        full_frame = pd.concat(all_frames, ignore_index=True)

        #analytics
        Red_Average_Kills = full_frame[full_frame["team"] == "Red"].groupby("matchid")["stats.kills"].mean().mean()
        full_frame["Red Average Kills"] = Red_Average_Kills
        print(f"Red Team Global Avg: {Red_Average_Kills:.2f}")
        Blue_Average_Kills = full_frame[full_frame["team"] == "Blue"].groupby("matchid")["stats.kills"].mean().mean()
        full_frame["Blue Average Kills"] = Blue_Average_Kills
        print(f"Blue Team Global Avg: {Blue_Average_Kills:.2f}")
        print(f"Matches Analyzed: ", len(all_frames))
        
        time.sleep(60)
        break
        #metadata(map, game_length, rounds_played, cluster(region in us))
        #players(puuid, name, level, team, character, currenttier(rank but in #s), behavior->afk_rounds, ability_casts->x_cast e_cast q_cast c_cast)
        #players(stats->score, kills, deaths, assists, bodyshots, headshots, legshots, economy->spent->overall average economy->loadout value->overall average)
        #players(damage_made damage_recieved)
        #teams(red->has_won, rounds_won, rounds_lost blue->red->has_won, rounds_won, rounds_lost)
        break
    
    else: 
        print(account_response.status_code)
        time.sleep(10)
        break
