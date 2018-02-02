import datetime
from ..models import MyStocks, Prices

class Stock_Tracker_Methods(object):
    def __init__(self):
        pass
    def stack_data(self):
        stock_price = MyStocks.objects.all()
        my_stock = Prices.objects.all()

        start_date = [str(x["Buy_Date"]) for x in MyStocks.objects.values("Buy_Date")][0].split("-")
        current_date = str(datetime.datetime.now()).split(" ")[0].split("-")

        d1 = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))  #start date
        d2 = datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) #end date

        delta = d2 - d1
        date_list = []
        for i in range(delta.days + 1):
            date_list.append(d1 + datetime.timedelta(days=i))

        print(date_list)

