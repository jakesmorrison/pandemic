import datetime
from ..models import MyStocks, Prices
import pandas as pd

class Stock_Tracker_Methods(object):
    def __init__(self):
        pass
    def stack_data(self):
        my_stock = MyStocks.objects.all().values()
        stock_price = Prices.objects.all().values()

        df_stock_price = pd.DataFrame(list(stock_price))
        df_my_stock = pd.DataFrame(list(my_stock))



        start_date = [str(x["Buy_Date"]) for x in MyStocks.objects.values("Buy_Date")][0].split("-")
        current_date = str(datetime.datetime.now()).split(" ")[0].split("-")

        d1 = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))  #start date
        d2 = datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) #end date

        delta = d2 - d1
        date_list = []
        stack_list = []
        for index, row in df_my_stock.iterrows():
            data = []
            for i in range(delta.days + 1):
                date = d1 + datetime.timedelta(days=i)
                if row["Sell_Date"] == None:
                    if date >= row["Buy_Date"]:
                        todays_cost = df_stock_price[(df_stock_price["Symbol"] == row["Symbol"]) & (df_stock_price["Date"] == date)]
                        todays_cost = todays_cost["Price"].tolist()
                        if todays_cost:
                            data.append({'y':round(float((todays_cost[0]-row["Cost"])*row["Quanity"]),2),"transaction":int(row["id"]),
                                         "cost":round(float(row["Cost"]),2),"buydate":str(row["Buy_Date"]),"selldate":str(row["Sell_Date"]),
                                         "quanity": int(row["Quanity"])})
                            date_list.append(str(date))
                    else:
                        if df_stock_price[df_stock_price["Date"] == date].empty == False:
                            date_list.append(str(date))
                            data.append(0)
                        else:
                            pass

                else:
                    if date >= row["Buy_Date"] and row["Sell_Date"] >= date:
                        todays_cost = df_stock_price[(df_stock_price["Symbol"] == row["Symbol"]) & (df_stock_price["Date"] == date)]
                        todays_cost = todays_cost["Price"].tolist()
                        if todays_cost:
                            data.append({'y':round(float((todays_cost[0]-row["Cost"])*row["Quanity"]),2),"transaction":int(row["id"]),
                                         "cost":round(float(row["Cost"]),2),"buydate":str(row["Buy_Date"]),"selldate":str(row["Sell_Date"]),
                                         "quanity": int(row["Quanity"])})
                            date_list.append(str(date))
                    else:
                        if df_stock_price[df_stock_price["Date"] == date].empty == False:
                            date_list.append(str(date))
                            data.append(0)
                        else:
                            pass

            stack_list.append({"name":row["Symbol"],"data":data,"threshold": 0,"negativeColor": '#ff5f5f', "color": '#5fff5f'})


        return stack_list, sorted(list(set(date_list)))


    def get_money_in_market(self):
        my_stock = MyStocks.objects.all().values()
        stock_price = Prices.objects.all().values()

        df_stock_price = pd.DataFrame(list(stock_price))
        df_my_stock = pd.DataFrame(list(my_stock))

        total_money_in_market = 0
        for index, row in df_my_stock.iterrows():
            stock = row["Symbol"]
            quanity = row["Quanity"]
            sold = row["Sell_Date"]
            try:
                if sold == None:
                    newest_price = df_stock_price[df_stock_price["Symbol"]==stock]
                    newest_price = newest_price.sort_values(by=['Date'])["Price"].tolist()[-1]
                    total_money_in_market = total_money_in_market + newest_price*quanity
            except:
                pass

        return total_money_in_market


    def get_table(self):
        my_stock = MyStocks.objects.all().values()
        stock_price = Prices.objects.all().values()


        df_stock_price = pd.DataFrame(list(stock_price))
        df_stock_price = df_stock_price.sort_values(by=['Date'])

        df_my_stock = pd.DataFrame(list(my_stock))

        df_my_stock = df_my_stock["id,Symbol,Quanity,Buy_Date,Cost,Sell_Date".split(",")]

        total_price_list = []
        total_gain_list = []
        for index,row in df_my_stock.iterrows():
            symbol = row["Symbol"]
            quanity = row["Quanity"]
            cost = row["Cost"]
            if row["Sell_Date"] == None:
                current_price = df_stock_price[df_stock_price["Symbol"]==symbol]["Price"].tolist()[-1]
                total_price = current_price
                gain = ((total_price-cost)/cost)*100
                total_price_list.append(total_price)
                total_gain_list.append(gain)
            else:
                sale_price = df_stock_price[(df_stock_price["Symbol"] == symbol) & (df_stock_price["Date"] == row["Sell_Date"])]
                sale_price = sale_price["Price"]
                total_price = sale_price
                gain = ((sale_price-cost)/cost)*100
                total_price_list.append(total_price)
                total_gain_list.append(gain)

        df_my_stock["Price"] = total_price_list
        df_my_stock["% Gain/Loss"] = total_gain_list
        df_my_stock["$ Gain/Loss"] = (df_my_stock["Price"]-df_my_stock["Cost"])*df_my_stock["Quanity"]

        test = pd.DataFrame()
        test["buying"] = (df_my_stock["Cost"]*df_my_stock["Quanity"])
        test["selling"] = (df_my_stock["Price"]*df_my_stock["Quanity"])

        print(test)


        buying = float(test["buying"].sum())
        selling = float(test["selling"].sum())


        gain_loss_percent = ((selling-buying)/buying)*100
        gain_loss_cash = float(df_my_stock["$ Gain/Loss"].sum().tolist()[0])

        gain_loss_percent = "{:0.2f}%".format(gain_loss_percent)
        gain_loss_cash =  "${:0.2f}".format(gain_loss_cash)

        df_my_stock["Price"] = df_my_stock["Price"].apply(lambda x: "{:0.2f}".format(float(x)))
        df_my_stock["% Gain/Loss"] = df_my_stock["% Gain/Loss"].apply(lambda x: "{:0.2f}%".format(float(x)))
        df_my_stock["$ Gain/Loss"] = df_my_stock["$ Gain/Loss"].apply(lambda x: "${:0.2f}".format(float(x)))

        return df_my_stock, gain_loss_percent, gain_loss_cash

