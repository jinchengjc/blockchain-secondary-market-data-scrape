import requests
import datetime
import csv


today = datetime.date.today()
date_last_month = today + datetime.timedelta(-30 )
today = str(today).replace('-','')
date_last_month = str(date_last_month).replace('-','')
print(today, date_last_month)
url_BTC_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=bitcoin&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
date_last_month, today)
BTC_history = requests.get(url_BTC_history)
BTC_text = BTC_history.text

tickertime_list = BTC_text.split(sep='"tickertime":')
tickertime_list = tickertime_list[1:14]
for i in range(0, 13):
    tickertime_list[i] = tickertime_list[i][1:11]


def btc_turnover():

    url_BTC_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=bitcoin&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    BTC_history = requests.get(url_BTC_history)
    BTC_text = BTC_history.text

    tickertime_list = BTC_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = BTC_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = BTC_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_BTC_list = list()
    for i in range(0, 13):
        Turnover_BTC_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_BTC_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    print(url_BTC_history)
    return Turnover_BTC_list

def eth_turnover():
    url_ETH_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=ethereum&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    ETH_history = requests.get(url_ETH_history)
    ETH_text = ETH_history.text

    tickertime_list = ETH_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = ETH_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = ETH_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_ETH_list = list()
    for i in range(0, 13):
        Turnover_ETH_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_ETH_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_ETH_list


def XRP_turnover():
    url_XRP_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=ripple&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    XRP_history = requests.get(url_XRP_history)
    XRP_text = XRP_history.text

    tickertime_list = XRP_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = XRP_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = XRP_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_XRP_list = list()
    for i in range(0, 13):
        Turnover_XRP_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_XRP_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_XRP_list

def XLM_turnover():
    url_XLM_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=stellar&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    XLM_history = requests.get(url_XLM_history)
    XLM_text = XLM_history.text

    tickertime_list = XLM_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = XLM_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = XLM_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_XLM_list = list()
    for i in range(0, 13):
        Turnover_XLM_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_XLM_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_XLM_list


def BCH_turnover():
    url_BCH_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=bitcoin-cash&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    BCH_history = requests.get(url_BCH_history)
    BCH_text = BCH_history.text

    tickertime_list = BCH_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = BCH_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = BCH_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_BCH_list = list()
    for i in range(0, 13):
        Turnover_BCH_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_BCH_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_BCH_list
BCH_list = BCH_turnover()


def EOS_turnover():
    url_EOS_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=eos&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    EOS_history = requests.get(url_EOS_history)
    EOS_text = EOS_history.text

    tickertime_list = EOS_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = EOS_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = EOS_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_EOS_list = list()
    for i in range(0, 13):
        Turnover_EOS_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_EOS_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_EOS_list
EOS_list = EOS_turnover()

def LTC_turnover():
    url_LTC_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=litecoin&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    LTC_history = requests.get(url_LTC_history)
    LTC_text = LTC_history.text

    tickertime_list = LTC_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = LTC_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = LTC_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_LTC_list = list()
    for i in range(0, 13):
        Turnover_LTC_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_LTC_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_LTC_list
LTC_list = LTC_turnover()


def ADA_turnover():
    url_ADA_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=cardano&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    ADA_history = requests.get(url_ADA_history)
    ADA_text = ADA_history.text

    tickertime_list = ADA_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = ADA_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = ADA_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_ADA_list = list()
    for i in range(0, 13):
        Turnover_ADA_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_ADA_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_ADA_list
ADA_list = ADA_turnover()



def ETC_turnover():
    url_ETC_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=ethereum-classic&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    ETC_history = requests.get(url_ETC_history)
    ETC_text = ETC_history.text

    tickertime_list = ETC_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = ETC_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = ETC_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_ETC_list = list()
    for i in range(0, 13):
        Turnover_ETC_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_ETC_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_ETC_list
ETC_list = ETC_turnover()


def DASH_turnover():
    url_DASH_history = 'https://dncapi.bqrank.net/api/v3/coin/history?coincode=dash&begintime={}&endtime={}&page=1&per_page=70&webp=1'.format(
        date_last_month, today)
    DASH_history = requests.get(url_DASH_history)
    DASH_text = DASH_history.text

    tickertime_list = DASH_text.split(sep='"tickertime":')
    tickertime_list = tickertime_list[1:14]
    for i in range(0, 13):
        tickertime_list[i] = tickertime_list[i][1:11]

    marketcap_list = DASH_text.split(sep='"marketcap":')
    marketcap_list = marketcap_list[1:14]
    for i in range(0, 13):
        marketcap_list[i] = marketcap_list[i][:marketcap_list[i].find(',')]

    vol_list = DASH_text.split(sep='"vol":')
    vol_list = vol_list[1:14]
    for i in range(0, 13):
        vol_list[i] = vol_list[i][:vol_list[i].find(',')]

    Turnover_DASH_list = list()
    for i in range(0, 13):
        Turnover_DASH_list.append(str(round(100 * float(vol_list[i]) / float(marketcap_list[i]), 2)) + '%')

    print(Turnover_DASH_list)
    print(tickertime_list)
    print(marketcap_list)
    print(vol_list)
    return Turnover_DASH_list
DASH_list = DASH_turnover()




BTC_list = btc_turnover()
ETH_list = eth_turnover()
XRP_list = XRP_turnover()
XLM_list = XLM_turnover()


mylist = []
for i in range(0,13):
    mylist.append([tickertime_list[i], BTC_list[i],ETH_list[i],XRP_list[i],XLM_list[i],BCH_list[i],EOS_list[i],LTC_list[i],ADA_list[i],ETC_list[i],DASH_list[i]])

mylist.reverse()


with open('C:/Users/Bebe\Desktop\实习生数据交接文件/换手率.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(mylist)