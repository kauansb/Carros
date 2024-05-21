from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

def car_inventory_update():
    cars_count = Car.objects.all().count() # Contagem de registros
    cars_value = Car.objects.aaggregate( # Retorna uma query que soma todos os values dos carros
        total_value=Sum('value')
    )['total_value'] # Retorna apenas o valor, ao invés do padrão de 'campo:valor'
    CarInventory.objects.create( 
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car) # Para cada carro salvo, será contado quantos carros há no estoque e qual o valor total
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
