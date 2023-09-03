from monitor.models import Symbol
import requests



def job_1():
    url="https://fapi.binance.com/fapi/v1/ticker/24hr"

    data = requests.get(url=url)
    symbols = data.json()
    #sorted_symbols=sorted(symbols,key=lambda x: float(x['priceChangePercent']),reverse=True)
    for sub in symbols:
        symbol = sub['symbol']
        lastPrice = sub['lastPrice'] = float(sub['lastPrice'])
        priceChangePercent = sub['priceChangePercent'] = float(sub['priceChangePercent'])
        highPrice = sub['highPrice'] = float(sub['highPrice'])
        lowPrice = sub['lowPrice'] = float(sub['lowPrice'])
        quoteVolume = sub['quoteVolume'] = float(sub['quoteVolume'])

        try:
            obj = Symbol.objects.get(symbol=symbol)
            obj.lastPrice=lastPrice
            obj.priceChangePercent=priceChangePercent
            obj.highPrice=highPrice
            obj.lowPrice=lowPrice
            obj.quoteVolume=quoteVolume
            if priceChangePercent>0:
                obj.inGreen+=1
            else:
                obj.inGreen=0
            obj.save()
        except Symbol.DoesNotExist:
            obj=Symbol(symbol=symbol,lastPrice=lastPrice,priceChangePercent=priceChangePercent,highPrice=highPrice,lowPrice=lowPrice,quoteVolume=quoteVolume)
            obj.save()