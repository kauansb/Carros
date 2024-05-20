from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView

# Class Based Views
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars' # objeto que irá para template

    def get_queryset(self): # aponta que o filtro será feito pelo modelo do carro, ao invés do padrão.
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' # redireciona para a url ao cadastrar um carro com sucesso

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
