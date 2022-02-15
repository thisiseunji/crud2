import json

from django.http  import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        try:
            data      = json.loads(request.body) #json을 dict처럼 쓰려고
            owner     = Owner.objects.create(
                name  = data['name'],
                email = data['email'],
                age   = data['age']
            )
            return JsonResponse({'message':'created'}, status = 201)
        
        except KeyError:
            return JsonResponse({'message':'key_error'}, status = 400)
# http -v GET  http://127.0.0.1:8000/owners   

    def get(self, request):
        owners  = Owner.objects.all()
        results = []
        for owner in owners:
            results.append(
                {
                    "name"  : owner.name,
                    "email" : owner.email,
                    "age"   : owner.age
                }
            )
        return JsonResponse({'results':results}, status=200)

class DogsView(View):
    def post(self, request):
        try:
            data      = json.loads(request.body)
            owner = Owner.objects.get(id = data['owner_id'])
            dog       = Dog.objects.create(
                name  = data['name'],
                age   = data['age'],
                owner = owner
            )
            return JsonResponse({'message':'created'}, status = 201)
        
        except KeyError:
            return JsonResponse({'message':'key_error'}, status = 400)
        
        except ValueError:
            return JsonResponse({'message':'value_error'}, status = 400)
            
    
    def get(self, request):
        dogs    = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "owner" : dog.owner.name,
                    "name"  : dog.name,
                    "age"   : dog.age
                }
            )
        return JsonResponse({'result':results}, status=200)

###다시해봅시다..?역참조생각해봅시다..?    
class OwnerAndDogsView(View):
    def get(self, request):
        try:
            owners  = Owner.objects.all()
            print(owners)
            dogs    = Dog.objects.all()
            print(dogs)
            results = []
            for owner in owners:
                pet = []
                for dog in dogs:
                    if owner.id == dog.owner.id:
                        pet.append(
                            {
                                'name' : dog.name,
                                'age'  : dog.age
                            }
                        )    
                results.append( 
                    {
                        "name"  : owner.name,
                        "email" : owner.email,
                        "age"   : owner.age,
                        "pet"   : pet
                            
                    }
                )
            print(results)            
            return JsonResponse({'result':results}, status= 200)
         
        except TypeError as e:
            print(e)
            return JsonResponse({'result': 'type_error'}, status=400)
