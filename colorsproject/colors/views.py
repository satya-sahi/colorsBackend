import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .colors import colors
import random

# Create your views here.
@api_view(['GET'])
def get_colour_swatches_view(request):
        random_colors= random.sample(colors,5) # type: ignore
        return JsonResponse(random_colors, safe=False)

@api_view(['GET'])
def get_brgb_values_view(request):
        color=request.param.get('color')
        rgbValues=colors[color].rgb
        brgbValues=[]
        for i in rgbValues:
            brgbValues.append(i/10000)*255
        color['brgb']=brgbValues;
        return JsonResponse(color,safe=False)
                
