# from django.http import HttpResponse
from django.shortcuts import render

from .models import Menu
from django.core import serializers
from .models import Booking
from .models import UserComments
from datetime import datetime
from .forms import CommentForm
from .forms import BookingForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
# from .forms import BookingForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message':'Success'
            })
        else:
            print(form.errors)
            return JsonResponse({
                'message':'Invalid form',
                'errors': form.errors
            })
    return render(request, 'book.html',{'form':form})

# Add code for the bookings() view


def formView(request):
    form = CommentForm()
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            uc=UserComments(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                comment=cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message':'Success'
            })
    return render(request,'blog.html',{'form':form})

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

@api_view(['GET', 'POST'])
def menuItems(request):
    return Response({
  "menu_items": [
    {
      "name": "Cheeseburger",
      "price": 8.99,
      "category": "Burgers"
    },
    {
      "name": "Margherita Pizza",
      "price": 12.99,
      "category": "Pizzas"
    },
    {
      "name": "Caesar Salad",
      "price": 6.49,
      "category": "Salads"
    }
  ]
}
)
    # if request.method == 'GET':
    #     allItems = MenuItem.objects.all()
    #     print("items: ", list(allItems.values()))
    #     return Response({'items': list(allItems.values())})
    # else:
    #     serializedItem = MenuItemSerializer(data=request.data)
    #     if (serializedItem.is_valid()):
    #         print("saving the data: ", request.data)
    #         serializedItem.save()
    #         return Response({'statusa': "saved"})
    #     else:
    #         return Response({'error': "Incorrect format"})


@api_view(['GET'])
def categories (request):
    return Response({
  "categories": [
    {
      "name": "Burgers"
    },
    {
      "name": "Pizzas"
    },
    {
      "name": "Salads"
    }
  ]
}
)
def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def reservations(request):
    all_bookings = Booking.objects.all()
    print('bookings: ',all_bookings)
    return render(request,'reservations.html',{'all_bookings': all_bookings})