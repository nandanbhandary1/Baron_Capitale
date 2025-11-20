from django.shortcuts import redirect, render
from myapp.models import BLogPost
from myapp.forms import BlogPostForm

# Create your views here.


def get_post(request):
    if request.method == "GET":
        a = BLogPost.objects.all()
        context = {"blog": a}
        return render(request, "home.html", context)


def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)

            blog_post.save()
            return redirect("blog_list")
    else:
        form = BlogPostForm()
    return render(request, "post.html", {"form": form})


def update_post(request, id):
    if request.method == "POST":
        a = BLogPost.objects.get(id=id)
        if a.is_valid():
            return a


def delete_post(request, id):
    a = BLogPost.objects.get(id=id)
    a.delete()
