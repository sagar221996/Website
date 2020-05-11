from django.shortcuts import render
from .models import Desti

# Create your views here.


def index(request):

    #dest1=Desti()
    #dest1.name='Mumbai'
    #dest1.desc='The city that never sleeps'
    #dest1.img='destination_4.jpg'
    #dest1.price=1000
    #dest1.offer=True

    #dest2=Desti()
    #dest2.name='Hyderabad'
    #dest2.desc='First Biryani second sherwani'
    #dest2.img='destination_5.jpg'
    #dest2.price=1000
    #dest2.offer=False

    #dest3=Desti()
    #dest3.name='Delhi'
    #dest3.desc='The capital of india'
    #dest3.img='destination_6.jpg'
    #dest3.price=1000
    #dest3.offer=True

    #dests=[dest1, dest2, dest3] 
    dests = Desti.objects.all()
    return render(request,'index.html',{'dests': dests})
