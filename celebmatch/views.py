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

# Create your views here.
def home(request):
    context={
    }
    return render(request,'celebmatch/home.html',context)

@csrf_exempt
def retrieve_image(request):
    m = methods.Methods()
    current_folder = os.path.dirname(__file__)

    if os.path.isfile((current_folder+"/management/trained_knn_model.clf")):
        pass
    else:
        m.train_classifier()

    if request.POST:
        os.system('echo there is post data > /root/text.txt')
    elif request.GET:
        os.system('echo there is get data > /root/text.txt')
    elif request.FILES:
        os.system('echo there is files data > /root/text.txt')
    else:
        os.system('echo there is not data > /root/text.txt')


    image_data = request.POST['data_url']
    image_data = re.sub("^data:image/png;base64,", "", image_data)
    image_data = base64.b64decode(image_data)
    image_data = BytesIO(image_data)
    im = Image.open(image_data)
    im.save(current_folder+'/static/celebmatch/images/user_submitted.bmp')
    predictions, closest_distances = m.get_lookalike()
    os.remove(current_folder+'/static/celebmatch/images/user_submitted.bmp')

    context = {
        'celeb': predictions,
    }
    return JsonResponse(json.loads(json.dumps(context)))
