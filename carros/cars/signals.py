from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio

def car_inventory_update():
    cars_count = Car.objects.all().count() # Contagem de registros
    cars_value = Car.objects.aggregate( # Retorna uma query que soma todos os values dos carros
        total_value=Sum('value')
    )['total_value'] # Retorna apenas o valor, ao invés do padrão de 'campo:valor'
    CarInventory.objects.create( 
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs): # campo bio será alimentado automaticamente caso seja nula, porém sempre persiste a que o usuário informa
    """ Execução da API de IA
    if not instance.bio: # Usando IA para criar biografias personalizadas para cada registro
        ai_bio = get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        instance.bio = ai_bio
    """
    """""" 
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente' 
   
    

@receiver(post_save, sender=Car) # Para cada carro salvo, será contado quantos carros há no estoque e qual o valor total
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
