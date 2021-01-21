import requests
import datetime
import random
import csv

today = datetime.date.today()
date_target = datetime.datetime.strptime('2021-01-10', '%Y-%m-%d').date()
time_diff = (today - date_target).days
print('time difference with 2021/1/10:', time_diff, '\n')

fx = 'https://www.investing.com/currencies/usd-cny'
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
cookies = '__cfduid=da8564e22530c576df8447225f88c16941606793790; _ga=GA1.2.639261529.1606793789; ajs_anonymous_id=%22d6a0cf' \
          '1d-98a2-43c3-a7ad-36bb7dfdd948%22; _gid=GA1.2.434042602.1608876587; cf_clearance=f5deee867450e0a347ed03bd86689b7d' \
          '7eed744a-1608960893-0-150; XSRF-TOKEN=xt5ieJlSzAdN%2B5gZmHj6AC0DvouK9uDaoEkOx5ak%2F0c%3D; _session_id=f05d1a2a93dc735a885c7845b2c6c372'

page = requests.request('GET',fx ,headers={'User-agent': ua, 'Cookie': cookies}).text
exchange_rate = page[page.find('id="last_last" dir="ltr">'):]
exchange_rate = exchange_rate[25:exchange_rate.find('</span>')]
exchange_rate = exchange_rate.replace(',','')
exchange_rate = float(exchange_rate)
print("today's FX of USD-CNY:", exchange_rate)


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Bithumb = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=Bithumb&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Bithumb = requests.get(url_Bithumb).text
tickertime_list = text_Bithumb.split('"tickertime":')[-17:]
tickertime_list = [i[0:8] for i in tickertime_list]

Bithumb_volume_list = text_Bithumb.split('"volume":')[-17:]
Bithumb_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Bithumb_volume_list]



timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Bittrex = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=Bittrex&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Bittrex = requests.get(url_Bittrex).text
Bittrex_volume_list = text_Bittrex.split('"volume":')[-17:]
Bittrex_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Bittrex_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Bitfinex = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=Bitfinex&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Bitfinex = requests.get(url_Bitfinex).text
Bitfinex_volume_list = text_Bitfinex.split('"volume":')[-17:]
Bitfinex_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Bitfinex_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Poloniex = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=Poloniex&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Poloniex = requests.get(url_Poloniex).text
Poloniex_volume_list = text_Poloniex.split('"volume":')[-17:]
Poloniex_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Poloniex_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_BitMex = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=BitMex&begintime=0&endtime={}&webp=1'.format(timestamp)
text_BitMex = requests.get(url_BitMex).text
BitMex_volume_list = text_BitMex.split('"volume":')[-17:]
BitMex_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in BitMex_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Binance = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=Binance&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Binance = requests.get(url_Binance).text
Binance_volume_list = text_Binance.split('"volume":')[-17:]
Binance_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Binance_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Huobi = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=Huobipro&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Huobi = requests.get(url_Huobi).text
Huobi_volume_list = text_Huobi.split('"volume":')[-17:]
Huobi_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Huobi_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_OKEX = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=OKEX&begintime=0&endtime={}&webp=1'.format(timestamp)
text_OKEX = requests.get(url_OKEX).text
OKEX_volume_list = text_OKEX.split('"volume":')[-17:]
OKEX_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in OKEX_volume_list]


timestamp = 1610208000 + time_diff * 86400 + random.randint(1,86399)
url_Coinbase = 'https://dncapi.bqrank.net/api/v3/futuresmarket/exchangehischarts?exchangecode=CoinbasePro&begintime=0&endtime={}&webp=1'.format(timestamp)
text_Coinbase = requests.get(url_Coinbase).text
Coinbase_volume_list = text_Coinbase.split('"volume":')[-17:]
Coinbase_volume_list = [exchange_rate * float(i[0:i.find(',')]) for i in Coinbase_volume_list]

my_csv_list = []
for i in range(0,17):
    my_csv_list.append([tickertime_list[i], Bithumb_volume_list[i], Bittrex_volume_list[i],Bitfinex_volume_list[i]
                        , Poloniex_volume_list[i]
                        ,BitMex_volume_list[i]
                        ,Binance_volume_list[i]
                        ,Huobi_volume_list[i]
                        ,OKEX_volume_list[i]
                        ,Coinbase_volume_list[i]
                        ])


print('每天会统计当天数据，但当天数据并不准确，所以周二查数据，使用周一的数据')

volume_text = '本周九大交易所一周累计总成交量为62719.20亿元人民币，较上周上升28739.27亿元，' \
              '增幅为84.58%，从交易量结构来看，成交量占比前三名的交易所分别是Binance（38.87%)，' \
              'Huobi（28.61%)，OKEX（22.48%)，前三名交易所成交量占九大交易所总成交量的89.96%，' \
              '前三名占比较上周增加0.2%；Binance本周累计成交量较上周上升1.1267万亿元，增幅为85.87%，' \
              'Huobi本周累计成交量较上周上升8523.54亿元，增幅为85.59%，OKEX本周累计成交量较上周上升6051.21亿元，' \
              '增幅为83.61%。'

for e in range(0,7):

    my_csv_list[16 - e].append(sum([i for i in my_csv_list[16-e][1:]]))

volume_total_thisweek = sum([my_csv_list[16-e][10] for e in []])


with open('C:/Users/Bebe\Desktop\实习生数据交接文件/成交量.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(my_csv_list)