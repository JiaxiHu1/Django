from django.shortcuts import render,redirect 
from .forms import TopicForm
from .models import Topic

#this will be our home page 
# Create your views here.

def index(request):
    return render(request, 'Mainapp/index.html')
    #last line will be a render - using this template 

def topics(request):
    #Topic is the object in the models.py file 
    topics = Topic.objects.order_by('-date_added') #decending order will be '-date_added'

    #dictionary called context
    context = {"topics":topics} #the value will be whatever you called up there 

    return render(request, "Mainapp/topics.html",context)
    #render the info from up there 

#url 
#view 
#template 

#this will be the chess or the rockclimbing page for individual topic 
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    entries = topic.entry_set.all()

    #context dictionary 
    #what kind of object is the context 
    #pass the information from the view to the - create the dicitonary and pass the dictionary 
    context = {'topic':topic,'entries':entries}

    return render(request, 'Mainapp/topic.html',context)


#get is request information to load the page - we just an empty form 
#post request - we want to save the information that the user submitted into the database 
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() #IF this is the GET request - then we just provide an empty form 
    else:
        form = TopicForm(data=request.POST)  #else, se want to post the request 

        if form.is_valid(): #validation phase 
            new_topic = form.save()
            return redirect('Mainapp:topics')
    
    context = {'form':form}
    return render(request,'Mainapp/new_topic.html',context)
