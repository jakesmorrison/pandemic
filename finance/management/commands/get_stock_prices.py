from django.core.management.base import BaseCommand
from ...models import Prices, MyStocks
import pandas as pd
import urllib.request
import re
import json
import time

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('symbol')
        parser.add_argument('number_of_days')


    def handle(self, *args, **options):
        if options['number_of_days'] == 1:
            self.add_to_db()
        else:
            self.get_historic_stock_prices(options["symbol"], int(options['number_of_days']))

    def add_to_db(self):
        q = MyStocks.objects.values("Symbol")
        df = pd.DataFrame.from_records(q)
        symbol_list = list(set(df["Symbol"].tolist()))
        for x in symbol_list:
            date, close_price = self.get_stock_price(x)
            p = Prices(
                Date=date,
                Symbol=x,
                Price=close_price,
            )
            p.save()

    def get_stock_price(self,symbol):
        url = "https://finance.yahoo.com/quote/"+symbol+"/history"
        html = ""
        with urllib.request.urlopen(url) as response:
            html = response.read()

        html = str(html)
        m = re.search('HistoricalPriceStore.*?\}', html)
        newest_data = m.group(0)
        newest_data = newest_data.replace('HistoricalPriceStore":{"prices":[',"")
        newest_data = json.loads(newest_data)
        date = time.strftime('%Y-%m-%d', time.localtime(newest_data["date"]))
        closing_price = round(newest_data["close"],2)
        return date, closing_price

    def get_historic_stock_prices(self, symbol, days):
        url = "https://finance.yahoo.com/quote/"+symbol+"/history"
        html = ""

        with urllib.request.urlopen(url) as response:
            html = response.read()

        html = str(html)
        re_search = 'HistoricalPriceStore'
        for x in range(0,days):
            re_search = re_search + '.*?\}'
        m = re.search(re_search, html)
        newest_data = m.group(0)
        newest_data = newest_data.replace('HistoricalPriceStore":{"prices":[',"")

        newest_data = json.loads("["+newest_data+"]")

        df = pd.DataFrame(newest_data)
        df["date"] = df["date"].apply(lambda x: time.strftime('%Y-%m-%d', time.localtime(x)))
        df = df[["date","close"]]
        for index, row in df.iterrows():
            p = Prices(
                Date=row["date"],
                Symbol=symbol,
                Price=round(row["close"],2),
            )
            p.save()


# python manage.py get_stock_prices 1
# python manage.py get_stock_prices "S" 10
