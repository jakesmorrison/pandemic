from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
counter = 0
def micron_slider_test(request):
    context={}
    return(render(request, 'sandbox/micron_slide_show.html',context))

def change_led(request):
    params = request.GET
    print(params["slide"])

    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))

def new_demo_front_end(request):
    global counter
    counter = 0
    context={}
    return(render(request, 'sandbox/new_demo_front_end.html',context))

def get_data(request):
    data_ssd_arr = 20*[7]
    data_nvme_arr = 20*[11]
    data_nvdimm_arr = 20*[15]
    all_data = data_ssd_arr + data_nvme_arr + data_nvdimm_arr

    global counter
    if counter>59:
        counter=0
    new_val = all_data[counter]
    counter = counter+1

    context = {
        'val': [counter,new_val]
    }
    return JsonResponse(json.loads(json.dumps(context)))

def gary_spelling(request):
    context={}
    return(render(request, 'sandbox/gary_spelling.html',context))

def vmworld(request):
    context={}
    return(render(request, 'sandbox/vmworld.html',context))

def career_day(request):
    context={}
    return(render(request, 'sandbox/career_day.html',context))

import subprocess
import pandas as pd
import json
from django.http import JsonResponse
import random

def linely_demo(request):
    context = {}
    return (render(request, 'sandbox/linely_demo.html', context))

def get_data_linely_demo(request):
    # Get first value from file (header).
    cmd = "head -1 /Users/jakesmorrison/Downloads/demo.csv"
    first_data = subprocess.check_output('{}'.format(cmd), shell=True)
    first_data = first_data.decode("utf-8").replace("\n", "0").replace('"', "")
    first_data = first_data.split(",")

    # Get last value from file (most recent data).
    cmd = "tail -1 /Users/jakesmorrison/Downloads/demo.csv"
    last_data = subprocess.check_output('{}'.format(cmd), shell=True)
    last_data = last_data.decode("utf-8").replace("\n", "0")
    last_data = last_data.split(",")
    last_data = [int(x) for x in last_data]

    # Put into dataframe and rename columns.
    df = pd.DataFrame(data=last_data)
    df = df.transpose()
    df.columns = first_data

    # Node (processor socket).
    N_val = "0"
    # HomeAgent or Group of Memory Channels.
    H_val = "0"
    # Channel Number within Home Agent.
    C_val = "0"

    # Calculating values needed for plotting.
    read_bw = (df["iMC:N" + N_val + "_H" + H_val + "_C" + C_val + "[1]-Read"] * 64) / (df["Time"] / 1000)
    write_bw = (df["iMC:N" + N_val + "_H" + H_val + "_C" + C_val + "[2]-Write"] * 64) / (df["Time"] / 1000)
    read_bw = float(read_bw.tolist()[0]) + random.randrange(0, 101, 2)
    write_bw = float(write_bw.tolist()[0]) + random.randrange(0, 101, 2)
    errors = float(df["iMC:N" + N_val + "_H" + H_val + "_C" + C_val + "[4]-Errs"].tolist()[0])

    context = {
        'read_bw': read_bw,
        'write_bw': write_bw,
        'errors': errors
    }
    return JsonResponse(json.loads(json.dumps(context)))


import pandas as pd
import math
from collections import Counter, OrderedDict
import string
import re

# Get color based on letter
def get_color(x):
    x = x[-1]
    if x == "Y":
        return "#696969"
    elif x == "E":
        return "#ff5f5f"
    elif x== "D":
        return "#5fffaf"
    elif x == "F":
        return "#5fafff"
    else:
        return "rgb(134, 107, 181)"

def remove_f(x):
    if "F" in x:
        return True
    else:
        return False

def speed_grade(request):

    # Reading in CSV.
    #df = pd.read_csv("/Users/jakesmorrison/Google Drive/Pycharm/pandemic/sandbox/static/sandbox/csv/Book1.csv")
    df = pd.read_csv("/root/pandemic/sandbox/static/sandbox/csv/Book1.csv")

    # Reverseing DataFrame for display purposes.
    df = df.iloc[::-1]

    # Clean Up
    df["SpeedGrade"] = df["SpeedGrade"].apply(lambda x: x.replace("?", ""))
    df["SpeedGrade"] = df["SpeedGrade"].apply(lambda x: x.replace("-", ""))

    # Create new DF without any of the speed colums.
    df_new = df.loc[:, 'SpeedGrade':'tRC*']

    # Get correct color
    df_new["Color"] = df_new["SpeedGrade"].apply(lambda x: get_color(x))

    # Fix order
    df_new["num"] = df_new["SpeedGrade"].apply(lambda x: re.sub("\D", "", x))
    df_new["letter"] = df_new["SpeedGrade"].apply(lambda x: re.sub("\d", "", x))
    df_new = df_new.sort_values(['num', 'letter'], ascending=[True, False])

    # Iterate through main dataframe and get which speedgrades have no coflicts.
    # If a speedgrade has no conflict save it to an array to be used later.
    speed_grades = list(df.loc[:, "-062F":].columns)
    no_conflicts_array = []
    for index, row in df.iterrows():
        no_conflicts = []
        for y in speed_grades:
            if (math.isnan(row[y]) == False):
                if (int(row[y]) == 0 ): #and "F" not in y
                    no_conflicts.append(y)
        no_conflicts = ",".join(no_conflicts)
        no_conflicts_array.append(no_conflicts)

    # Add array to new df.
    df_new["no_conflicts"] = no_conflicts_array
    # df_new["delete"] = df_new["SpeedGrade"].apply(lambda x: remove_f(x))
    # df_new = df_new[df_new["delete"] == False]

    # Get data for javascript.
    top_and_bottom_row = df_new["SpeedGrade"].tolist()
    column_count = len(top_and_bottom_row)
    connections = df_new["no_conflicts"].tolist()
    line_colors = df_new["Color"].tolist()
    data_rate = Counter(df_new["DataRate"].tolist())
    data_rate_keys = list(OrderedDict(reversed(sorted(data_rate.items()))).keys())
    data_rate_values = list(OrderedDict(reversed(sorted(data_rate.items()))).values())

    color_and_rows = []
    for x in range(0,len(line_colors)):
        color_and_rows.append([top_and_bottom_row[x],line_colors[x]])


    context = {
        'top_and_bottom_row':top_and_bottom_row,
        'connections': connections,
        'column_count':column_count,
        'line_colors': line_colors,
        'data_rate_keys': data_rate_keys,
        'data_rate_values': data_rate_values,
        'color_and_rows': color_and_rows,

    }
    return(render(request, 'sandbox/speed_grade.html',context))

def cnbu_dash(request):
    context={}
    return(render(request, 'sandbox/cnbu_dash.html', context))

def get_region_data(request):

    region = request.GET['region']
    if region == "americas":
        region_title = "Americas"
        qtd_rev = "$"+str(963)
        through_qtr = str(91)+"%"
        to_plan = str(80)+"%"
        ship_out = str(87)+"%"
        cp = "$"+str(1206)
    elif region == "asia":
        region_title = "Asia"
        qtd_rev = "$" + str(947)
        through_qtr = str(91) + "%"
        to_plan = str(77) + "%"
        ship_out = str(90) + "%"
        cp = "$" + str(1224)

    d = {'col1': ["HP INC", "APPLE"], 'col2': ["80%", "70%"], 'col3': ["$115.4", "$64.7"] }
    df = pd.DataFrame(data=d)
    html_table = df.to_html(index=False, classes='table table-striped table-bordered table-hover table-responsive" id = "my_table')

    context={
        'region_title': region_title,
        'qtd_rev': qtd_rev,
        'through_qtr': through_qtr,
        'to_plan': to_plan,
        'ship_out': ship_out,
        'cp': cp,
        'table': html_table
    }
    return JsonResponse(json.loads(json.dumps(context)))


# import threading
# import inspect
# import ctypes
# import time
# from neopixel import *
#
# def dna(request):
#     context = {}
#     return (render(request, 'sandbox/dna_2.html', context))
#
# threads = []
# def post_led(request):
#     global threads
#     setting = request.GET
#     setting = setting['setting']
#     if len(threads)>0:
#         for x in threads:
#             if x.isAlive():
#                 x.terminate()
#         threads = []
#
#     t = myThread(target=change_led, args=[setting])
#     t.setDaemon(True)
#     threads.append(t)
#     t.start()
#
#
#     context={
#     }
#     return JsonResponse(json.loads(json.dumps(context)))
#
#
# def change_led(args):
#     if args == "loop":
#         loop()
#     elif args == "slow":
#         slow()
#     elif args == "med":
#         pass
#     elif args == "fast":
#         pass
#
#
# def loop():
#     led = ledConfig()
#     while True:
#         print(led.strip1)
#         time.sleep(1)
#
#
# def slow():
#     for x in range(0,10):
#         time.sleep(1)
#         print(x)
#
#
# class ledConfig():
#     def __init__(self):
#         # LED strip configuration:
#         self.LED_COUNT = 234  # Number of LED pixels.
#         self.LED_PIN0 = 18  # GPIO pin connected to the pixels (18 uses PWM!).
#         self.LED_PIN1 = 13  # GPIO pin connected to the pixels (13 uses PWM!).
#         self.LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
#         self.LED_DMA = 10  # DMA channel to use for generating signal (try 10)
#         self.LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
#         self.LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
#         self.LED_CHANNEL0 = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
#         self.LED_CHANNEL1 = 1  # set to '1' for GPIOs 13, 19, 41, 45 or 53
#
#         self.strip1 = Adafruit_NeoPixel(LED_COUNT, LED_PIN0, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL0)
#         self.strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL1)
#
#
# class myThread(threading.Thread):
#     def _get_my_tid(self):
#         """determines this (self's) thread id"""
#         if not self.isAlive():
#             raise threading.ThreadError("the thread is not active")
#
#         # do we have it cached?
#         if hasattr(self, "_thread_id"):
#             return self._thread_id
#
#         # no, look for it in the _active dict
#         for tid, tobj in threading._active.items():
#             if tobj is self:
#                 self._thread_id = tid
#                 return tid
#
#         raise AssertionError("could not determine the thread's id")
#
#     def raise_exc(self, exctype):
#         """raises the given exception type in the context of this thread"""
#         _async_raise(self._get_my_tid(), exctype)
#
#     def terminate(self):
#         """raises SystemExit in the context of the given thread, which should
#         cause the thread to exit silently (unless caught)"""
#         self.raise_exc(SystemExit)
#
#
# def _async_raise(tid, exctype):
#     """raises the exception, performs cleanup if needed"""
#     if not inspect.isclass(exctype):
#         raise TypeError("Only types can be raised (not instances)")
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         # """if it returns a number greater than one, you're in trouble,
#         # and you should call it again with exc=NULL to revert the effect"""
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
#

from django.shortcuts import render
import json
from django.http import JsonResponse

from os import listdir
from os.path import isfile, join


def led_slider(request):
    mypath = "/Users/jakesmorrison/Documents/Movie/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    context={
        'video_file': onlyfiles[0]
    }
    return(render(request, 'sandbox/video.html',context))

def led_slider_change(request):
    # kill_all()

    # Use colors to set LEDs.
    print(request.GET)
    context={}
    return JsonResponse(json.loads(json.dumps(context)))
