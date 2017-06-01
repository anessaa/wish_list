# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Item

# Create your views here.
def index(request):
    context = {
    "users" : User.objects.all()
    }
    print context
    return render(request, 'wishList_app/index.html')
def validate(request):
    if request.method == "POST":
        errors = User.objects.validate(request)
        if (errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        else:
            request.session['name']=request.POST['name']
            User.objects.create(name=request.POST['name'], username=request.POST['username'],
            password=request.POST['password'], created_at=request.POST['member_since'])
            return redirect('/dashboard')
def login(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST['username'])
        if user:
            user = user[0]
            if user:
                request.session['user_id'] = user.id
                return redirect('/dashboard')
            else:
                messages.error(request, 'Username is not regisered')
                return redirect('/')
        else:
            messages.error(request, 'Username is not registered')
            return redirect('/')

def dashboard(request):
    user_id = request.session.get('user_id')

    user = User.objects.get(pk=user_id)
    items = Item.objects.all()
    context = {
        "user": user,
        "items": items
    }
    return render(request, 'wishList_app/dashboard.html', context)

def wish_items(request):

    return render(request, 'wishList_app/wish_items.html')

def create_item(request):
    # if request.method == "POST":
    #     errors = Item.objects.item_validate(request)
    #     if (errors):
    #         for error in errors:
    #             messages.error(request, error)
    #         return redirect('/wish_items')
    # else:
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    Item.objects.create(name=request.POST['name'], user=user)
    return redirect('/dashboard')

def display(request, id):
    context = {
    "item" : Item.objects.get(id=id)
    }

    return render(request, 'wishList_app/display_item.html', context)
def remove(request, id):
    query = Item.objects.get(id=id)

    return redirect('/dashboard')
def delete(request, id):
    query = Item.objects.get(id=id)
    query.delete()
    return redirect('/dashboard')
def logout(request):
    del request.session['user_id']
    return redirect('/')
