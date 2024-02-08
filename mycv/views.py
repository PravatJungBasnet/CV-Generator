from django.shortcuts import render,HttpResponseRedirect,reverse
from django.http import HttpResponse
from .models import Profile
from .forms import generate,Signup
from django.contrib import messages








# Create your views here.
def resume(request):
    if request.method=='POST':
        fm=generate(request.POST,request.FILES)
        if fm.is_valid():
            profile=fm.save()
            return HttpResponseRedirect(reverse('res', args=[profile.id]))
    
        else:
            messages.warning(request,'Invalid please enter a valid information')

    else:
        fm=generate()
    
    return render(request,'mycv/home.html',{'fm':fm})
def showres(request,id):
    res=Profile.objects.get(id=id)
    return render(request,'mycv/cv.html',{'res':res})





