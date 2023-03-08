from django.shortcuts import render
from .models import ChallengeAPI
from django.http import JsonResponse


def retrieve_data(request):
    data = ChallengeAPI.objects.all()
    data_list = []
    for item in data:
        data_list.append({
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'quantity': item.quantity,
        })
    context = {'data': data_list}
    return render(request, 'home.html', context)


def detail(request, pk):
    item = ChallengeAPI.objects.get(pk=pk)
    context = {
        'id': item.id,
        'name': item.name,
        'price': float(item.price),
        'quantity': item.quantity,
    }
    return render(request, 'detail.html', context)

def search(request):
    q = request.GET.get('q')
    if q:
        data = ChallengeAPI.objects.filter(id__icontains=q)
    else:
        data = ChallengeAPI.objects.all()
    data_list = []
    for item in data:
        data_list.append({
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'quantity': item.quantity,
        })
    return render(request, 'retrieve_data.html', {'data' : data_list})