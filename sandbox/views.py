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
