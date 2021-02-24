from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        #"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "time": strftime("%B %d, %Y %H:%M %p %Z", gmtime())
    }
    return render(request,'index.html', context)