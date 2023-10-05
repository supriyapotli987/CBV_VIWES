from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView


def FBV_string(request):
    return HttpResponse('This data is fbv_string')



class CBV_string(View):
    def get(self,request):
        return HttpResponse('This data is cbv_string ')
    




#fbv_page by using template
def fbv_page(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    return HttpResponse('This is fbv_page',d)





class cbv_page(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return HttpResponse('This is cbv_page',d)
    

#insert fbv_data

def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is successfully inserted')
    return render(request,'insert_fbv.html',d)






class insert_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_fbv.html',d)
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is successfully inserted')



#template for fbv
class cbv_temp(TemplateView):
    template_name='cbv_temp.html'

