from django.shortcuts import render
from myapp.models import BLogPost

# Create your views here.


def get_post(request):
    if request.method == "GET":
        a = BLogPost.objects.all()
        return (request, a)


def create_post(request):
    pass


def update_post(request, id):
    if request.method == "POST":
        a = BLogPost.objects.get(id=id)
        if a.is_valid():
            return a


def delete_post(request, id):
    a = BLogPost.objects.get(id=id)
    a.delete()
