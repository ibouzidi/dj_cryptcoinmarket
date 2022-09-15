import requests
from django.shortcuts import render


def index(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency' \
          '=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    coins = requests.get(url).json()
    return render(request, 'coins/index.html', context={
        'coins': coins,
    })

