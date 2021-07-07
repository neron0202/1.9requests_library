import requests
from pprint import pprint

mes = requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1625443200&todate=1625616000&order=desc&sort=activity&tagged=python&site=stackoverflow')
mes2 = mes.json()
pprint(mes2)
