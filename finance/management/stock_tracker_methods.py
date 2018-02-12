import datetime
from ..models import MyStocks, Prices
import pandas as pd
import time
import datetime
import pytz

class Stock_Tracker_Methods(object):
    def __init__(self):
        pass
    def stack_data(self):
        my_stock = MyStocks.objects.all().values()
        stock_price = Prices.objects.all().values()

        df_stock_price = pd.DataFrame(list(stock_price))
        df_stock_price = df_stock_price.sort_values(by=['Date'])

        df_my_stock = pd.DataFrame(list(my_stock))
        df_my_stock = df_my_stock["id,Symbol,Quanity,Buy_Date,Cost,Sell_Date".split(",")]

        # Convert to Float
        df_my_stock["Cost"] = df_my_stock["Cost"].apply(lambda x: float(x))
        df_my_stock["Quanity"] = df_my_stock["Quanity"].apply(lambda x: float(x))
        df_stock_price["Price"] = df_stock_price["Price"].apply(lambda x: float(x))

        pie_data = df_my_stock.copy()
        pie_data["Sell_Date"] = pie_data["Sell_Date"].apply(lambda x: str(x))
        pie_data = pie_data[pie_data["Sell_Date"]=="None"]
        pie_data = pie_data.groupby(["Symbol"]).sum().reset_index()
        pie_data_list=[]
        for index, row in pie_data.iterrows():
            pie_data_list.append({'name':row["Symbol"],'y':row["Quanity"]})
        pie_series = [{'name': 'Stock','colorByPoint': "true", 'data': pie_data_list}]

        start_date = [str(x["Buy_Date"]) for x in MyStocks.objects.values("Buy_Date")][0].split("-")
        current_date = str(datetime.datetime.now()).split(" ")[0].split("-")

        d1 = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))  #start date
        d2 = datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) #end date

        color_pos = "#007800"
        color_neg = "#b30000"

        delta = d2 - d1
        data = []
        portfolio_data = []
        for index, row in df_my_stock.iterrows():
            for i in range(delta.days + 1):
                date = d1 + datetime.timedelta(days=i)
                new_date = str(date).split("-")
                tz = pytz.timezone('America/Boise')
                dt_with_tz = tz.localize(datetime.datetime(int(new_date[0]), int(new_date[1]), int(new_date[2]), 0, 0, 0), is_dst=None)
                ts = (dt_with_tz - datetime.datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()
                epoch = int(ts*1000)

                # If not sold and current date is greater than buy date.
                if row["Sell_Date"] == None:
                    if date >= row["Buy_Date"]:
                        todays_cost = df_stock_price[(df_stock_price["Symbol"] == row["Symbol"]) & (df_stock_price["Date"] == date)]
                        todays_cost = todays_cost["Price"].tolist()
                        if todays_cost:
                            val = float('{0:.2f}'.format((todays_cost[0]-row["Cost"])*row["Quanity"]))
                            portfolio_data.append({"x": epoch, "y": todays_cost[0]*row["Quanity"]})
                            if val>0:
                                data.append({"x": epoch, "y": val, 'color': color_pos, "name": row["Symbol"]})
                            else:
                                data.append({"x": epoch, "y": val, 'color': color_neg, "name": row["Symbol"]})

                            # data.append({'x':epoch,'y':,"transaction":int(row["id"]),
                            #              "cost":round(float(row["Cost"]),2),"buydate":str(row["Buy_Date"]),"selldate":str(row["Sell_Date"]),
                            #              "quanity": int(row["Quanity"]),'color':'#5fffaf'})
                else:
                    if date >= row["Buy_Date"] and row["Sell_Date"] >= date:
                        todays_cost = df_stock_price[(df_stock_price["Symbol"] == row["Symbol"]) & (df_stock_price["Date"] == date)]
                        todays_cost = todays_cost["Price"].tolist()
                        if todays_cost:
                            val = float('{0:.2f}'.format((todays_cost[0]-row["Cost"])*row["Quanity"]))
                            portfolio_data.append({"x": epoch, "y": todays_cost[0]*row["Quanity"]})
                            if val>0:
                                data.append({"x": epoch, "y": val, 'color': color_pos, "name": row["Symbol"]})
                            else:
                                data.append({"x": epoch, "y": val, 'color': color_neg, "name": row["Symbol"]})


        df = pd.DataFrame(data)
        df = df.sort_values(by='x')
        stack_data_list=[]
        for index, row in df.iterrows():
            stack_data_list.append({"x": row["x"], "y": row["y"], 'color': row["color"], 'name': row["name"]})

        df_p = pd.DataFrame(portfolio_data)
        df_p = df_p.groupby(["x"]).sum().reset_index()
        df_p = df_p.sort_values(by='x')

        port_data_list = []
        for index, row in df_p.iterrows():
            port_data_list.append({"x": row["x"], "y": float('{0:.2f}'.format(row["y"]))})

        return stack_data_list, port_data_list, pie_series

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

        #Convert to Float
        df_my_stock["Cost"] = df_my_stock["Cost"].apply(lambda x: float(x))
        df_my_stock["Quanity"] = df_my_stock["Quanity"].apply(lambda x: float(x))
        df_stock_price["Price"] = df_stock_price["Price"].apply(lambda x: float(x))

        total_price_list = []
        total_gain_list = []
        for index,row in df_my_stock.iterrows():
            symbol = row["Symbol"]
            cost = row["Cost"]
            if row["Sell_Date"] == None:
                current_price = df_stock_price[df_stock_price["Symbol"]==symbol]["Price"].tolist()[-1]
                total_price = current_price
                gain = ((total_price-cost)/cost)*100
                total_price_list.append(total_price)
                total_gain_list.append(gain)
            else:
                sale_price = df_stock_price[(df_stock_price["Symbol"] == symbol) & (df_stock_price["Date"] == row["Sell_Date"])]
                sale_price = sale_price["Price"].tolist()[0]
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

        buying = test["buying"].sum()
        selling = test["selling"].sum()

        gain_loss_percent = ((selling-buying)/buying)*100
        gain_loss_cash = df_my_stock["$ Gain/Loss"].sum()

        gain_loss_percent = "{:0.2f}".format(gain_loss_percent)
        gain_loss_cash =  "{:0.2f}".format(gain_loss_cash)

        df_my_stock["Price"] = df_my_stock["Price"].apply(lambda x: "{:0.2f}".format(float(x)))
        df_my_stock["% Gain/Loss"] = df_my_stock["% Gain/Loss"].apply(lambda x: "{:0.2f}%".format(float(x)))
        df_my_stock["$ Gain/Loss"] = df_my_stock["$ Gain/Loss"].apply(lambda x: "${:0.2f}".format(float(x)))

        df_my_stock = df_my_stock.rename(index=str, columns={"id":"ID","Symbol":"Ticker","Quanity":"Quanity",
                                                             "Buy_Date":"Purchase Date","Cost":"Initial Price","Sell_Date":"Sell Date",
                                                             "Price":"Current/Sell Price","% Gain/Loss": "Return %","$ Gain/Loss": "Return $"})


        return df_my_stock, gain_loss_percent, gain_loss_cash


    def area_chart(self):
        my_stock = MyStocks.objects.all().values()
        stock_price = Prices.objects.all().values()

        df_stock_price = pd.DataFrame(list(stock_price))
        df_stock_price = df_stock_price.sort_values(by=['Date'])

        df_my_stock = pd.DataFrame(list(my_stock))
        df_my_stock = df_my_stock["id,Symbol,Quanity,Buy_Date,Cost,Sell_Date".split(",")]

        # Convert to Float
        df_my_stock["Cost"] = df_my_stock["Cost"].apply(lambda x: float(x))
        df_my_stock["Quanity"] = df_my_stock["Quanity"].apply(lambda x: float(x))
        df_stock_price["Price"] = df_stock_price["Price"].apply(lambda x: float(x))

        new_df = pd.merge(df_stock_price, df_my_stock, how='left', on=['Symbol'])
        new_df["Price"] = new_df["Price"] * new_df["Quanity"]
        new_df["Cost"] = new_df["Cost"] * new_df["Quanity"]

        new_df = new_df.groupby(["Date"]).sum().reset_index()

        date_list = new_df["Date"].tolist()
        price_list = new_df["Price"].tolist()
        data1 = []
        for n, x in enumerate(date_list):
            new_date = str(x).split("-")
            tz = pytz.timezone('America/Boise')
            dt_with_tz = tz.localize(datetime.datetime(int(new_date[0]), int(new_date[1]), int(new_date[2]), 0, 0, 0),is_dst=None)
            ts = (dt_with_tz - datetime.datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()
            epoch = int(ts * 1000)
            data1.append({"x":epoch,"y":float('{0:.2f}'.format(price_list[n]))})

        return data1

