import requests
api_key = "RGAPI-4b5f9c73-2148-4884-8e1a-3153f23a4fbe"
user_input = input("Enter username: ")
modified_input = user_input.replace(" ", "%20")
api_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + user_input
match_history = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/mlKKXg1RwDU1hj3UWSOHgKrKU95w5kEQ_UXaadXcruSpIQtS4lcBL0JOoxRIfAoDvQA8HnRxMzHetQ/ids?start=0&count=20"
api_url = api_url + '?api_key=' + api_key
resp = requests.get(api_url)
player_info = resp.json()
player_account_id = player_info['accountId']
print(player_info)
print(player_info['summonerLevel'])