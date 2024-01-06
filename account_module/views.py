from django.shortcuts import render
from . import form
from . import models
import datetime
# Create your views here.


def register(request):
    form_reg=form.registerform(request.POST)
    if request.method=='POST':
        if form_reg.is_valid():
            print(form_reg.cleaned_data['username'])
            print(form_reg.cleaned_data['email'])
            print(form_reg.cleaned_data['desc'])
            new_message=models.register_model()
            new_message.username =form_reg.cleaned_data['username']
            new_message.email = form_reg.cleaned_data['email']
            new_message.desc = form_reg.cleaned_data['desc']
            new_message.date = datetime.datetime.now()
            new_message.save()








    return render(request,'call/contact.html',context={"form":form_reg})