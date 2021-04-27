from django.shortcuts import render
from .models import Album
# Create your views here.
def Home(request):
    data = Album.objects.all()
    context ={
        'data':data
    }
    return render(request,'index.html',context)