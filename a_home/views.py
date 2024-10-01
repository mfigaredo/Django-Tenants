from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import Item

def home_view(request):
    items = Item.objects.all()
    context = {
        'items': items,
        'schema': connection.schema_name,
    }
    return render(request, 'home.html', context)

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        item = Item(name=name)
        item.save()
        return HttpResponse(f'<li class="text-6xl font-thin">{item.name}</li>')
    else:
        return redirect('home')