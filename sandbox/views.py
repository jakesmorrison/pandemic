from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
counter = 0
def micron_slider_test(request):
    context={}
    return(render(request, 'sandbox/micron_slider_test.html',context))

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
