import config, requests, json

holdings=open('qqqq.csv').readlines()

print(holdings)
symbols=[holding.split(',')[2].strip() for holding in holdings][1:]
symbols=",".join(symbols)
print(symbols)

"""for u in holdings:
    u.split(',')[:2]
    print(u)"""



minute_bars_url=config.bars_url+'/5Min?symbols=TSLA'
daily_bars_url=config.bars_url+'/day?symbols=AAPL'
daily_bars_url_anotherway='{}/day?symbols={}&limit=2'.format(config.bars_url,symbols)
r=requests.get(daily_bars_url_anotherway, headers=config.headers)

print(r.content)
y=json.dumps(r.json(),indent=4)
z=y.replace('h','high').replace('l','low').replace('c','close').replace(' o ','open').replace('t','time')
print(z)