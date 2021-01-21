import requests

url2 = 'https://coinmarketcap.com/charts/'
text_url2 = requests.get(url2)


market_cap_position = text_url2.text.find('$',text_url2.text.find('market cap'))
market_cap = text_url2.text[market_cap_position:market_cap_position+20]
market_cap = market_cap[:market_cap.find('<')]
print('market_cap', market_cap)

Vol24h_position = text_url2.text.find('$',text_url2.text.find('24h Vol'))
Vol24h = text_url2.text[Vol24h_position:Vol24h_position+20]
Vol24h = Vol24h[:Vol24h.find('<')]
print('Vol24h', Vol24h)




input('Press ANY KEY to exit')