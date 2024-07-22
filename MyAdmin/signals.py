from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from MyAdmin.models import subscription_details



@receiver(post_migrate)
def plan_creation(sender, **kwargs ):
    
    if sender.name == 'MyAdmin':
        subscriptionModel = apps.get_model('MyAdmin', 'subscription_details')
        if not subscriptionModel.objects.exists() :
            types_of_plane = [
                {
                    's_name':'Basic',
                    's_max_problem_solve_qty':'10',
                    'price': 0 
                },
                {
                    's_name':'premium' ,
                    's_max_problem_solve_qty':'15',
                    'price': 250
                },
                {
                    's_name':'Deluxe', 
                    's_max_problem_solve_qty':'20',
                    'price':500
                },
            ]
            
            for plan in types_of_plane:
                subscriptionModel.objects.create(**plan)