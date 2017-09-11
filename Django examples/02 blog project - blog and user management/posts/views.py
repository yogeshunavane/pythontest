from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404


# Create your views here.
def show_list(request):
    #if not request.user.is_staff or not request.user.is_superuser:
    if request.user.is_anonymous():
        return render(request,"please_login.html",{})
    queryset_list = Post.objects.order_by("-timestamp")#.all() #.order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    print(paginator.count)
    print(paginator.num_pages)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
    	queryset = paginator.page(page)
    except PageNotAnInteger:
    	# If page is not an integer, deliver first page.
    	queryset = paginator.page(1)
    except EmptyPage:
    	# If page is out of range (e.g. 9999), deliver last page of results.
    	queryset = paginator.page(paginator.num_pages)
    
    
    context = {
    	"data_all": queryset, 
    	"title": "List",
    	"page_request_var": page_request_var,
    }

    
    #return HttpResponse("Here's the text of the Web page.")
    return render(request,"show_list.html",context)
    
    
def post_create(request):
    if request.user.is_anonymous():
        return render(request,"please_login.html",{})
    if request.method == 'POST':
        form = PostForm(request.POST)
        print("inside Post")
        if form.is_valid():
            print("for is valid")
            print(form)
            instance = form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect('/posts/post_create/')
    else:
        form = PostForm()
    	context = {"form": form}
	return render(request,"post_create.html",context)
	
	
def post_detail(request,id):
	instance = get_object_or_404(Post, id=id)
	if request.user.is_anonymous():
	    return render(request,"please_login.html",{})
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)