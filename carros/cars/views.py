from django.shortcuts import render
from cars.models import Car


def cars_view(request): 
    cars = Car.objects.all().order_by('model')  # busca da tabela carros pela camada model para poder ser utilizado pelo template
    search = request.GET.get('search') 

    if search: # Verifica se há uso do parâmetro de busca, se não, renderiza todos os carros
        cars = Car.objects.filter(model__icontains=search)
    # print(cars)

    return render(request, 'cars.html', # Render usa a requisição e o template para que seja enviado pela view. A pasta templates ao ser criada é vista automaticamente pelo django
        {'cars': cars}) 