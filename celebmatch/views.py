from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .management import methods
import os
from io import BytesIO
from PIL import Image
import re
import base64
import pandas as pd
import random

# Create your views here.
def home(request):
    m = methods.Methods()
    current_folder = os.path.dirname(__file__)
    if os.path.isfile((current_folder+"/management/trained_knn_model.clf")):
        pass
    else:
        m.train_classifier()

    context={
    }
    return render(request,'celebmatch/home.html',context)

@csrf_exempt
def retrieve_image(request):
    m = methods.Methods()
    current_folder = os.path.dirname(__file__)

    # if request.POST:
    #     os.system('echo there is post data '+str(list(request.POST.keys())[0])+' > /root/text.txt')
    # elif request.GET:
    #     os.system('echo there is get data > /root/text.txt')
    # elif request.FILES:
    #     os.system('echo there is files data > /root/text.txt')
    # else:
    #     os.system('echo there is not data > /root/text.txt')

    if request.POST:
        image_data = request.POST['data_url']
        image_data = re.sub("^data:image/png;base64,", "", image_data)
        image_data = base64.b64decode(image_data)
        image_data = BytesIO(image_data)
        im = Image.open(image_data)
        im.save(current_folder+'/static/celebmatch/images/user_submitted.bmp')
        rating, celeb = m.get_lookalike()
        # os.remove(current_folder+'/static/celebmatch/images/user_submitted.bmp')
    else:
        pass

    pd.set_option('display.max_colwidth', -1)
    if len(list(celeb))>=5:
        df = pd.DataFrame([list(celeb)[0:5]]).T
        df["rating"] = list(rating)[0:5]

    else:
        df = pd.DataFrame([list(celeb)]).T
        df["rating"] = list(rating)

    df.columns = ['Name', 'Rating']

    image_path = []
    for x in list(celeb):
        image_path.append(get_image(x))
    image_temp_text = []
    for x in range(0,len(df["Name"].tolist())):
        image_temp_text.append("image_"+str(x))

    df['img_path'] = image_temp_text


    context = {
        'celeb_arr': ','.join(celeb),
        # 'rating_arr': ','.join([ str(x) for x in rating ]),
        'table': df.to_html(index=False, classes= 'table table-striped table-bordered table-hover table-responsive" id = "my_table'),
        'image_path': image_path,
        'original_photo': '<img class="icon centered-image" src="/static/celebmatch/images/user_submitted.bmp" alt="micron">'
    }
    return JsonResponse(json.loads(json.dumps(context)))

def get_image(name):
    return ('<img class="icon centered-image" src="/static/celebmatch/images/'+name+'.bmp" alt="micron">')
