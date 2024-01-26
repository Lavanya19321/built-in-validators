from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def studentdata(request):
    ESFO=studentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SDFO=studentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save
            return HttpResponse('data inserted is done')
        else:
            return HttpResponse('invalid data')
    return render(request,'studentform.html',d)