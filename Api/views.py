from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
dict = {"speed":50, "status":"P", "charge":45, "charging":0, "rpm": 55, "lineVoltage": 240.45325, "lineCurrent": -330.5345, "expectedRange": 50,"temperature": 66, "regen": 52, "odometer":76};

def Api(request):
    return JsonResponse(dict)

@csrf_exempt
def Chn(request):
    change = ""
    if request.method == 'POST':
        if "AC" in request.POST:
            dict["AC"] = request.POST.get("AC")
            change += " AC"

        if 'regen' in request.POST:
            dict['regen'] = request.POST.get('regen')
            change += ' regen'

        return HttpResponse(str(change) + 'has been changed successfully')



