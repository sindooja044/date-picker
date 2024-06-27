from django.shortcuts import render
from .models import Hello

# Create your views here.
def home(request):
        hellos=Hello.objects.all()
        context= {
            'hellos':hellos
        }
        return render(request,'index.html',context)
