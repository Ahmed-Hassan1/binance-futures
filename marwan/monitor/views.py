import requests
import json
from operator import itemgetter

from django.shortcuts import render
from .models import *

# Create your views here.

def homePage(request):
    return render(request,"monitor/index.html")

def table(request):
    #url="https://fapi.binance.com/fapi/v1/ticker/24hr"

    #data = requests.get(url=url)
    # symbols = data.json()
    # sorted_symbols=sorted(symbols,key=lambda x: float(x['priceChangePercent']),reverse=True)
    # for sub in sorted_symbols:
    #     sub['lastPrice'] = float(sub['lastPrice'])
    #     sub['priceChangePercent'] = float(sub['priceChangePercent'])
    #     sub['highPrice'] = float(sub['highPrice'])
    #     sub['lowPrice'] = float(sub['lowPrice'])
    #     sub['quoteVolume'] = float(sub['lowPrice'])
    
    symbols = Symbol.objects.order_by('priceChangePercent').reverse()
    context={"symbols":symbols}
    return render(request,"monitor/table.html",context) 

def table_1(request):
    symbols = Symbol.objects.filter(inGreen__gt=6).filter(inGreen__lt=30).order_by('priceChangePercent').reverse()
    context={"symbols":symbols}
    return render(request,"monitor/table.html",context) 

def table_5(request):
    symbols = Symbol.objects.filter(inGreen__gt=30).filter(inGreen__lt=90).order_by('priceChangePercent').reverse()
    context={"symbols":symbols}
    return render(request,"monitor/table.html",context) 

def table_15(request):
    symbols = Symbol.objects.filter(inGreen__gt=90).filter(inGreen__lt=180).order_by('priceChangePercent').reverse()
    context={"symbols":symbols}
    return render(request,"monitor/table.html",context) 

def table_30(request):
    symbols = Symbol.objects.filter(inGreen__gt=180).order_by('priceChangePercent').reverse()
    context={"symbols":symbols}
    return render(request,"monitor/table.html",context) 