from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
import json
# Create your views here.
def list_of_cars(request):
    cars = Car.objects.all()
    repr = []
    for car in cars:
        data = {
            'id': car.id,
            'title': car.title,
            'price': float(car.price),
            'description': car.description,
            'owner': car.owner.username

        }
        repr.append(data)

    res = json.dumps(repr, ensure_ascii=False).encode('utf8')
    # print(cars, "!!!")
    return HttpResponse(res, content_type='text/json')