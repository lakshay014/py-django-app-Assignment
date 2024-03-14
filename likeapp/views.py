from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request

from likeapp.models import Events


# Create your views here.



#for adding a element in view
def add_new(request):
    if request.method == "POST":
        data = {"event_name":request.POST['event_name'],
                "data":request.POST['data'],
                "image":request.POST['image'],
                "location":request.POST['location'],
                "time":request.POST["time"],
                "sno":Events.objects.count()+1,
                "is_liked":0
        }

        event = Events(event_name=data["event_name"],
                        sno=data["sno"],
                        data=data["data"], 
                        image=data["image"], 
                        location=data["location"],
                        time=data["time"],
                        is_liked=data["is_liked"])
        event.save()  #saving data to database 
        return HttpResponseRedirect('/')


#for liking the image
def like_event(request):
    event= Events.objects.get(sno = request.POST['id'])
    #chenking for pervious starte of the event is_liked
    if event.is_liked:
       event.is_liked = 0
    else:
        event.is_liked=1
    event.save()#saving data to database
    return HttpResponseRedirect('/') 

#fetching events from database
def main_page(request): 
    events = Events.objects.all()
    context = {
        'events':events}
    return render(request, "index.html", context)
