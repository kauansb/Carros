from django.db import models 

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model): # Classe carro com herança da classe model
    id = models.AutoField(primary_key=True) # chave id com geração automática
    model = models.CharField(max_length=200) # modelo do carro
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True) # ano do modelo
    plate = models.CharField(max_length=10, blank=True, null=True) # placa do carro
    value = models.FloatField(blank=True, null=True) # valor do carro
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # imagem do carro por referência

    def __str__(self): # Método para criar objeto do carro com nome do modelo
        return self.model