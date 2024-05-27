from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta: # Reescrita da classe Meta
        model = Car
        fields = '__all__' # Uso de todos os campos disponíveis em Car

    def clean_value(self): # Regra para o campo de value com uso de validação automática do django
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser R$20.000')
        return value