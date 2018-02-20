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
        # Get data from db
        my_stock = MyStocks.objects.all().values()
        stock_price = Prices.objects.all().values()

        #Convert into dataframe
        df_stock_price = pd.DataFrame(list(stock_price))
        df_stock_price = df_stock_price.sort_values(by=['Date'])

        market_dates = df_stock_price["Date"].tolist()



        df_my_stock = pd.DataFrame(list(my_stock))
        df_my_stock = df_my_stock["id,Symbol,Quanity,Buy_Date,Buy_Price,Sell_Date,Sell_Price".split(",")]

        # Convert to Float
        df_my_stock["Buy_Price"] = df_my_stock["Buy_Price"].apply(lambda x: float(x))
        df_my_stock["Sell_Price"] = df_my_stock["Sell_Price"].apply(lambda x: float(x))
        df_my_stock["Quanity"] = df_my_stock["Quanity"].apply(lambda x: float(x))
        df_stock_price["Price"] = df_stock_price["Price"].apply(lambda x: float(x))

        # get data for pie chart
        pie_data = df_my_stock.copy()
        pie_data["Sell_Date"] = pie_data["Sell_Date"].apply(lambda x: str(x))
        pie_data = pie_data[pie_data["Sell_Date"]=="None"]
        pie_data = pie_data.groupby(["Symbol"]).sum().reset_index()
        pie_data_list=[]
        for index, row in pie_data.iterrows():
            pie_data_list.append({'name':row["Symbol"],'y':row["Quanity"]})
        pie_series = [{'name': 'Stock','colorByPoint': "true", 'data': pie_data_list}]


        # Stack data
        # Get dates
        start_date = [str(x["Buy_Date"]) for x in MyStocks.objects.values("Buy_Date")][0].split("-")
        current_date = str(datetime.datetime.now()).split(" ")[0].split("-")

        d1 = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))  #start date
        d2 = datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2])) #end date

        color_pos = "#79ffbc"
        color_neg = "#ff7979"

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


                if date in market_dates:
                    # If not sold and current date is greater than buy date.
                    # If stock has not been sold.
                    if row["Sell_Date"] == None:
                        # If the current date is equal or past the buy date
                        if date >= row["Buy_Date"]:
                            # Get data stock price data.
                            todays_cost = df_stock_price[(df_stock_price["Symbol"] == row["Symbol"]) & (df_stock_price["Date"] == date)]
                            todays_cost = todays_cost["Price"].tolist()
                            if todays_cost:
                                # get the value of the stock based on current price.
                                portfolio_data.append({"x": epoch, "y": todays_cost[0]*row["Quanity"]})
                                # get diff between buy price and current price.
                                val = float('{0:.2f}'.format((todays_cost[0]-row["Buy_Price"])*row["Quanity"]))
                                if val>0:
                                    data.append({"x": epoch, "y": val, 'color': color_pos, "name": row["Symbol"], "id": row["id"]})
                                else:
                                    data.append({"x": epoch, "y": val, 'color': color_neg, "name": row["Symbol"], "id": row["id"]})

                    # If stock did sell
                    else:
                        # before sell date
                        if date >= row["Buy_Date"] and date < row["Sell_Date"]:
                            todays_cost = df_stock_price[(df_stock_price["Symbol"] == row["Symbol"]) & (df_stock_price["Date"] == date)]
                            todays_cost = todays_cost["Price"].tolist()
                            #val = float('{0:.2f}'.format((row["Sell_Price"]-row["Buy_Price"])*row["Quanity"]))
                            val = float('{0:.2f}'.format((todays_cost[0] - row["Buy_Price"]) * row["Quanity"]))
                            portfolio_data.append({"x": epoch, "y": todays_cost[0]*row["Quanity"]})
                            if val>0:
                                data.append({"x": epoch, "y": val, 'color': color_pos, "name": row["Symbol"], "id": row["id"]})
                            else:
                                data.append({"x": epoch, "y": val, 'color': color_neg, "name": row["Symbol"], "id": row["id"]})
                        # on sale date
                        elif date >= row["Buy_Date"] and date <= row["Sell_Date"]:
                            val = float('{0:.2f}'.format((row["Sell_Price"]-row["Buy_Price"])*row["Quanity"]))
                            if val>0:
                                data.append({"x": epoch, "y": val, 'color': color_pos, "name": row["Symbol"], "id": row["id"]})
                            else:
                                data.append({"x": epoch, "y": val, 'color': color_neg, "name": row["Symbol"], "id": row["id"]})




        # FOR STACK: Creating temp dataframe,sorting and then putting it back into dictionary form.
        df = pd.DataFrame(data)
        df = df.sort_values(by=['x', 'name'])
        stack_data_list=[]
        for index, row in df.iterrows():
            stack_data_list.append({"x": row["x"], "y": row["y"], 'color': row["color"], 'name': row["name"], 'id': row["id"]})

        # FOR PORTFOLIOJ: Creating temp dataframe,sorting and then putting it back into dictionary form.
        df_p = pd.DataFrame(portfolio_data)
        df_p = df_p.groupby(["x"]).sum().reset_index()
        df_p = df_p.sort_values(by='x')
        port_data_list = []
        for index, row in df_p.iterrows():
            port_data_list.append({"x": row["x"], "y": float('{0:.2f}'.format(row["y"]))})

        return stack_data_list, port_data_list, pie_series


    def get_table(self):
        stock_price = Prices.objects.all().values()
        df_stock_price = pd.DataFrame(list(stock_price))
        df_stock_price = df_stock_price.sort_values(by=['Date'])

        my_stock = MyStocks.objects.all().values()
        df_my_stock = pd.DataFrame(list(my_stock))
        df_my_stock = df_my_stock["id,Symbol,Quanity,Buy_Date,Buy_Price,Sell_Date,Sell_Price".split(",")]

        #Convert to Float
        df_my_stock["Buy_Price"] = df_my_stock["Buy_Price"].apply(lambda x: float(x))
        df_my_stock["Sell_Price"] = df_my_stock["Sell_Price"].apply(lambda x: float(x))
        df_my_stock["Quanity"] = df_my_stock["Quanity"].apply(lambda x: float(x))
        df_stock_price["Price"] = df_stock_price["Price"].apply(lambda x: float(x))

        # df_my_stock["$ Gain/Loss"] = (df_my_stock["Sell_Price"]-df_my_stock["Buy_Price"])*df_my_stock["Quanity"]
        # df_my_stock["% Gain/Loss"] = ((df_my_stock["Sell_Price"]-df_my_stock["Buy_Price"])/df_my_stock["Sell_Price"])*100

        total_price_list = []
        total_gain_list = []
        for index,row in df_my_stock.iterrows():
            symbol = row["Symbol"]
            cost = row["Buy_Price"]
            if row["Sell_Date"] == None:
                current_price = df_stock_price[df_stock_price["Symbol"]==symbol]["Price"].tolist()[-1]
                total_price = current_price
                gain = ((total_price-cost)/cost)*100
                total_price_list.append(total_price)
                total_gain_list.append(gain)
            else:
                gain = ((row["Sell_Price"]-row["Buy_Price"])/row["Buy_Price"])*100
                total_price_list.append(row["Sell_Price"])
                total_gain_list.append(gain)

        df_my_stock["Price"] = total_price_list
        df_my_stock["% Gain/Loss"] = total_gain_list
        df_my_stock["$ Gain/Loss"] = (df_my_stock["Price"]-df_my_stock["Buy_Price"])*df_my_stock["Quanity"]

        test = pd.DataFrame()
        test["buying"] = (df_my_stock["Buy_Price"]*df_my_stock["Quanity"])
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

        del df_my_stock["Sell_Price"]
        return df_my_stock, gain_loss_percent, gain_loss_cash

