from django.shortcuts import render
from myapp.models import Post

# Create your views here.


def get_post(request):
    a = Post.objects.all()
    return (request, a)


def create_post(request):
    pass


def update_post(request, id):
    a = Post.objects.get(id=id)
    if a.is_valid():
        return a


def delete_post(request, id):
    a = Post.objects.get(id=id)
    a.delete()
