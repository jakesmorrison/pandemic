from django.shortcuts import render
import pandas as pd
import datetime
import holidays
import time
from .management import config as cfg
from .management import stock_tracker_methods

# Create your views here.
# Create your views here.
def index(request):
    context={
    }
    return render(request,"finance/home.html",context)

def investment_analyzer(request):
    context={
    }
    return render(request,"finance/investment_analyzer_1.html",context)


def retirement_withdrawl(request):
    context={
    }
    return render(request,"finance/retirement_withdrawl.html",context)

def sankey(request):
    context={
    }
    return render(request,"finance/sankey.html",context)


def calc_easter(year):
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return datetime.date(year, month, day) #- datetime.timedelta(2)


def top(request):
    start_date = datetime.date(2017, 9, 18)
    now = datetime.datetime.now().date() + datetime.timedelta(500)

    end_date = datetime.date(2019, 1, 1)
    end_date = now

    total_days = (end_date - start_date).days

    micron_holidays = ["New Year's Day", "Easter", "Memorial Day", "Independence Day", "Labor Day",
                       "Thanksgiving", "Day After", "Christmas Eve", "Christmas Day"]
    top_stuc = {0: 5.31, 1: 5.54, 2: 5.77, 3: 6, 4: 6.24, 5: 6.47, 6: 6.70, 7: 6.93}

    us_holidays = holidays.UnitedStates()

    top = {}

    for x in range(0, total_days):
        current_day = start_date + datetime.timedelta(x)

        vaca_day = 0
        if str(current_day) in cfg.Config.Vacation.keys():
            vaca_day = int(cfg.Config.Vacation[str(current_day)])

        week_day = current_day.weekday()
        t = 3.5
        if week_day in [5, 6]:
            t = 11.5
        years_worked = int(((current_day - start_date).days) / 365)
        if current_day.day == 1 or current_day.day == 15:
            if current_day in top.keys():
                top[current_day] = top[current_day] + top_stuc[years_worked]
            else:
                top[current_day] = top_stuc[years_worked]
        if us_holidays.get(current_day) in micron_holidays:
            if current_day in top.keys():
                top[current_day] = top[current_day] + t
            else:
                top[current_day] = t
            if us_holidays.get(current_day) == "Thanksgiving":
                top[current_day + datetime.timedelta(1)] = t
        elif current_day == (datetime.date(current_day.year, 12, 25) - datetime.timedelta(1)):
            if current_day in top.keys():
                top[current_day] = top[current_day] + t
            else:
                top[current_day] = t

        elif current_day == calc_easter(current_day.year):
            if current_day in top.keys():
                top[current_day] = top[current_day] + 3.5
            else:
                top[current_day] = 3.5
        else:
            if current_day in top.keys():
                top[current_day] = top[current_day] + 0
            else:
                top[current_day] = 0
        if vaca_day < 0:
            if current_day in top.keys():
                top[current_day] = top[current_day] + vaca_day
            else:
                top[current_day] = vaca_day


    df = pd.DataFrame(pd.Series(top, name='TOP'))
    df.index.name = "Date"
    df = df.reset_index()
    df = df.sort_values(by='Date')
    df["Date"] = df["Date"].apply(lambda x: str(x))

    date = df["Date"].tolist()
    top = df["TOP"].tolist()
    for n,x in enumerate(top):
        if n==0:
            pass
        else:
            top[n] = float(top[n-1])+float(top[n])
    data = [[date[n],top[n]]for n,x in enumerate(date)]

    context={
        'data': data
    }
    return render(request,"finance/top.html",context)

def stock_tracker(request):
    stm =stock_tracker_methods.Stock_Tracker_Methods()
    stack_data_list, port_data_list, pie_series = stm.stack_data()

    table, gain_loss_percent, gain_loss_cash = stm.get_table()

    html_table = table.to_html(index=False,classes='table table-striped table-bordered table-hover table-responsive')


    context = {
        "money_in_market": port_data_list[-1]["y"],
        "gain_loss_percent": gain_loss_percent,
        "gain_loss_cash": gain_loss_cash,
        "html_table": html_table,
        "data1": port_data_list,
        "data2": stack_data_list,
        "pie_series": pie_series
    }
    return render(request, "finance/stock_tracker.html", context)