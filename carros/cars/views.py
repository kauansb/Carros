from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


def cars_view(request): 
    cars = Car.objects.all().order_by('model')  # busca da tabela carros pela camada model para poder ser utilizado pelo template
    search = request.GET.get('search') 

    if search: # Verifica se há uso do parâmetro de busca, se não, renderiza todos os carros
        cars = Car.objects.filter(model__icontains=search)
    # print(cars)

    return render(request, 'cars.html', # Render usa a requisição e o template para que seja enviado pela view. A pasta templates ao ser criada é vista automaticamente pelo django
        {'cars': cars}) 

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES) # Contém todos os dados enviados pelo form, incluindo arquivos
        # print(new_car_form.data) TESTE
        if new_car_form.is_valid(): # Verificando se os dados recebidos são válidos baseado em regras personalizadas
            new_car_form.save() # cadastra no banco de dados o objeto ligado ao modelform
            return redirect('cars_list')   
    else:
        new_car_form = CarModelForm() 
    return render(request, 'new_car.html', {'new_car_form': new_car_form}) # Ao ser chamada cria um formulário vazio 