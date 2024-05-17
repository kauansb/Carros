from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta: # Reescrita da classe Meta
        model = Car
        fields = '__all__' # Uso de todos os campos disponíveis em Car

    def clean_value(self): # Regra para o campo de value com uso de validação automática do django
        value = self.cleaned_data.get['value']
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser R$20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get['factory_year']
        if factory_year < 1980:
            self.add_error('factoy_year', 'Não é possível cadastrar carros fabricados antes de 1980')
            return factory_year