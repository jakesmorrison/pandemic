from django.shortcuts import render

# Create your views here.

def micron_slider_test(request):
    context={}
    return(render(request, 'sandbox/micron_slider_test.html',context))
