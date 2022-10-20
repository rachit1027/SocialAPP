from django.shortcuts import render,redirect
from. models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def home(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        user = request.user
        user = Post(caption = caption,image = image, user = user)
        user.save()
        messages.success(request,"Post done successfully")
    allPost = Post.objects.all()
    data = {
        'posts': allPost
    }
    return render(request,'user/feed.html',data)

def delete_view(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    messages.info(request,"Post deleted")
    return redirect("home_page")


def profile_view(request,username):
    getUser = User.objects.filter(username = username) #query set mil jaaega
    if getUser:
        profile = Profile.objects.get(user=getUser[0])
        data ={
            'profile': profile
        }
        return render (request,'user/profile.html',data)
    else:
        messages.error(request,f"No such user named {username}")
        return redirect("home_page")
    