from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # Lista todas as marcas cadastradas no banco.
    factory_year = forms.IntegerField() 
    model_year = forms.IntegerField()
    plate = forms.CharField() 
    value = forms.FloatField() 
    photo = forms.ImageField(allow_empty_file=True) 

    def save(self):
        car = Car( 
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        ) # Criação do objeto carro para que seja enviado ao banco
        car.save()
        return car