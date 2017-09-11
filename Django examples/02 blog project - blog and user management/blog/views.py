from django.shortcuts import render

# Create your views here.
def show_list(request):
    context = "Yo"
    return HttpResponse("Here's the text of the Web page.")
    #return render(request,"",context)
    
    
def index(request):
    context = {}
    return render(request,"index.html",context)