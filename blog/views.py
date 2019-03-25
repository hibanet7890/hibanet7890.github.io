from django.shortcuts import render
from .models import Post
def home(request):
	return render(request, 'pages/home.html')
def index(request):
    #posts = [
	    #{'id':1, 'Title':'First Post', 'body':'This is my First Post'}, 
        #{'id':2, 'Title':'Second Post', 'body':'This is my Second Post'},
        #{'id':3, 'Title':'Third Post', 'body':'This is my Third Post'},
        #{'id':4, 'Title':'Four Post', 'body':'This is my Four Post'},

	#]
    posts = Post.objects.all()
    return render(request, 'blog/index.html' , {'posts': posts})


def show(request , id):
    #posts = [
	    #{'id':1, 'Title':'First Post', 'body':'This is my First Post'}, 
        #{'id':2, 'Title':'Second Post', 'body':'This is my Second Post'},
        #{'id':3, 'Title':'Third Post', 'body':'This is my Third Post'},
        #{'id':4, 'Title':'Four Post', 'body':'This is my Four Post'},

	#]
	post = Post.objects.get(pk=id)
	return render(request, 'blog/show.html' , {'post': post}) 
    #return render(request, 'blog/show.html' , {'post': posts[int(id) -1]})

