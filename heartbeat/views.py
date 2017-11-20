from django.shortcuts import render
from django.http import JsonResponse
import json
import time

# Create your views here.
def index(request):
    context={
    }
    return render(request,"heartbeat/index2.html",context)

def investment_analyzer(request):
    context={
    }
    return render(request,"heartbeat/index3.html",context)


def withdraw_analyzer(request):
    context={
    }
    return render(request,"heartbeat/index4.html",context)

def demo_dashboard(request):
    context={
    }
    return render(request,"heartbeat/demo_dashboard.html",context)


def gary1(request):
    context={
    }
    return render(request,"heartbeat/gary1.html",context)


counter = 0
import random
import subprocess
def get_data(request):
    global counter
    counter = counter+1

    sudo_password = 'BrettFavre13'

    # p = subprocess.Popen("sudo dd if=/dev/zero bs=512k of=tstfile count=1024 2>&1 | awk '/sec/ {print $1 / $5 / 1048576}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # my_line = ""
    # for line in p.stdout.readlines():
    #     my_line=line
    # my_line = float(str(my_line).replace("b","").replace("\'","").replace("n","").replace("\\",""))
    # print(my_line)


    context={
        #'arr': [counter,my_line],
        'arr': [counter, random.randint(740, 800)],
        'arr2': [counter, random.randint(400, 700)],

    }
    return JsonResponse(json.loads(json.dumps(context)))
