import requests
import datetime
# 搞定当周的结算日期，晚些爬数据的js脚本网址要用
today = datetime.date.today()

if (4-today.weekday())%7 != 0:

    date_of_weekly = today + datetime.timedelta( (4-today.weekday()) % 7 )
else:
    date_of_weekly = today + datetime.timedelta(7)

date_of_weekly_year = str(date_of_weekly.year)

date_of_weekly_month = str(date_of_weekly.month)
if len(date_of_weekly_month) == 1:
    date_of_weekly_month = '0' + date_of_weekly_month

date_of_weekly_day = str(date_of_weekly.day)
if len(date_of_weekly_day) == 1:
    date_of_weekly_day = '0' + date_of_weekly_day

date_of_weekly_string = date_of_weekly_year + date_of_weekly_month + date_of_weekly_day + '00000011'

print('the deliver date of weekly future:\n', date_of_weekly, '\n')

#同理推算出次周的交割日期和当季交割日期

date_of_biweekly = date_of_weekly + datetime.timedelta(7)

date_of_biweekly_year = str(date_of_biweekly.year)

date_of_biweekly_month = str(date_of_biweekly.month)
if len(date_of_biweekly_month) == 1:
    date_of_biweekly_month = '0' + date_of_biweekly_month

date_of_biweekly_day = str(date_of_biweekly.day)
if len(date_of_biweekly_day) == 1:
    date_of_biweekly_day = '0' + date_of_biweekly_day

date_of_biweekly_string = date_of_biweekly_year + date_of_biweekly_month + date_of_biweekly_day + '00000011'

print('the deliver date of biweekly future:\n', date_of_biweekly, '\n')


date_of_quarterly = date_of_weekly + datetime.timedelta(21)

date_of_quarterly_year = str(date_of_quarterly.year)

date_of_quarterly_month = str(date_of_quarterly.month)
if len(date_of_quarterly_month) == 1:
    date_of_quarterly_month = '0' + date_of_quarterly_month

date_of_quarterly_day = str(date_of_quarterly.day)
if len(date_of_quarterly_day) == 1:
    date_of_quarterly_day = '0' + date_of_quarterly_day

date_of_quarterly_string = date_of_quarterly_year + date_of_quarterly_month + date_of_quarterly_day + '00000011'

print('the deliver date of quarterly future:\n', date_of_quarterly, '\n')



#BTCUSD Swap Future Perpetual 永续
url_BTCUSD_Swap_Perpetual = 'https://www.okexcn.com/v2/market/index/lastPrice?t=1606976225366&symbol=f_usd_btc'
text_url_BTCUSD_Swap_Perpetual = requests.get(url_BTCUSD_Swap_Perpetual)
Perpetual_position = text_url_BTCUSD_Swap_Perpetual.text.find(':',text_url_BTCUSD_Swap_Perpetual.text.find('futureIndex'))
Perpetual_Future_Index = text_url_BTCUSD_Swap_Perpetual.text[Perpetual_position+1:]
Perpetual_Future_Index = Perpetual_Future_Index[:Perpetual_Future_Index.find(',')]
print('Perpetual BTCUSD Swap:\n', Perpetual_Future_Index, '\n')

#BTXT指数
url_BTXT = 'https://www.coingecko.com/en/indexes/kumex/bxbt'
text_url_BTXT = requests.get(url_BTXT)
text_url_BTXT = text_url_BTXT.text
BTXT_position = text_url_BTXT.find('<div class="text-3xl">')
BTXT_position = text_url_BTXT.find('>',BTXT_position)+2
BTXT_Index = text_url_BTXT[BTXT_position:text_url_BTXT.find('<',BTXT_position)-1]
print('BTXT_Index:\n', BTXT_Index, '\n')

#各种时长的期货价格，这里用到了开头的时间
url_BTC_weekly = 'https://www.okex.com/v2/futures/pc/market/usd/marketRefresh.do?symbol=f_usd_btc&contractId=' + date_of_weekly_string
text_url_BTC_weekly = requests.get(url_BTC_weekly)
text_url_BTC_weekly = text_url_BTC_weekly.text
BTC_weekly_position = text_url_BTC_weekly.find('asks')
BTC_weekly_position = text_url_BTC_weekly.find('[',BTC_weekly_position)+4
BTC_weekly_Index = text_url_BTC_weekly[BTC_weekly_position:text_url_BTC_weekly.find('"',BTC_weekly_position)-1]
print('BTC_weekly_Index:\n', BTC_weekly_Index, '\n')

url_BTC_biweekly = 'https://www.okex.com/v2/futures/pc/market/usd/marketRefresh.do?symbol=f_usd_btc&contractId=' + date_of_biweekly_string
text_url_BTC_biweekly = requests.get(url_BTC_biweekly)
text_url_BTC_biweekly = text_url_BTC_biweekly.text
BTC_biweekly_position = text_url_BTC_biweekly.find('asks')
BTC_biweekly_position = text_url_BTC_biweekly.find('[',BTC_biweekly_position)+4
BTC_biweekly_Index = text_url_BTC_biweekly[BTC_biweekly_position:text_url_BTC_biweekly.find('"',BTC_biweekly_position)-1]
print('BTC_biweekly_Index:\n', BTC_biweekly_Index, '\n')

url_BTC_quarterly = 'https://www.okex.com/v2/futures/pc/market/usd/marketRefresh.do?symbol=f_usd_btc&contractId=' + '20210326' + '00000011'
text_url_BTC_quarterly = requests.get(url_BTC_quarterly)
text_url_BTC_quarterly = text_url_BTC_quarterly.text
BTC_quarterly_position = text_url_BTC_quarterly.find('asks')
BTC_quarterly_position = text_url_BTC_quarterly.find('[',BTC_quarterly_position)+4
BTC_quarterly_Index = text_url_BTC_quarterly[BTC_quarterly_position:text_url_BTC_quarterly.find('"',BTC_quarterly_position)-1]
print('BTC_quarterly_Index:\n', BTC_quarterly_Index, '\n')



input('Press ANY KEY to exit')