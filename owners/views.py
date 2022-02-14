import json

from django.http  import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data      = json.loads(request.body) #json을 dict처럼 쓰려고
        owner     = Owner.objects.create(
            name  = data['owner_name'],
            email = data['owner_email'],
            age   = data['owner_age']
        )
        return JsonResponse({'message':'created'}, status = 201)
    
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
        data      = json.loads(request.body)
        owner     = owner.object.get(id = data['owner_id'])
        dog       = Dog.objects.create(
            name  = data['dog_name'],
            age   = data['dog_age'],
            owner = owner
        )
        return JsonResponse({'message' : 'created'}, status = 201)
    
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