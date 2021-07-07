import requests
heroes_intelligence_dict = {}

hulk_stats = requests.get('https://superheroapi.com/api/2619421814940190/332/powerstats')
c_america_stats = requests.get('https://superheroapi.com/api/2619421814940190/149/powerstats')
thanos_stats = requests.get('https://superheroapi.com/api/2619421814940190/655/powerstats')

heroes_intelligence_dict[hulk_stats.json()['name']] = int(hulk_stats.json()['intelligence'])
heroes_intelligence_dict[c_america_stats.json()['name']] = int(c_america_stats.json()['intelligence'])
heroes_intelligence_dict[thanos_stats.json()['name']] = int(thanos_stats.json()['intelligence'])

print(f"the most intelligent hero is {max(heroes_intelligence_dict)}: {max(heroes_intelligence_dict.values())}")
