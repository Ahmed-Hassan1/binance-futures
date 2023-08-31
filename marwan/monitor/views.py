import requests
import json
from operator import itemgetter

from django.shortcuts import render
from .models import *

# Create your views here.

def homePage(request):
    return render(request,"monitor/index.html")

def table(request):
    url="https://fapi.binance.com/fapi/v1/ticker/24hr"

    data = requests.get(url=url)
    symbols = data.json()
    sorted_symbols=sorted(symbols,key=lambda x: float(x['priceChangePercent']),reverse=True)
    for sub in sorted_symbols:
        sub['priceChangePercent'] = float(sub['priceChangePercent'])
    context={"symbols":sorted_symbols}
    return render(request,"monitor/table.html",context) 