from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse,JsonResponse
from .models import Classe,Etablissement
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    classes = Classe.objects.all()

    return render(request, 'home.html', {'classes': classes})

# List Classe obj
@csrf_exempt
def classe_list(request):
    classes = list(Classe.objects.all().values())

    return JsonResponse(classes, safe=False)

# List Ets obj
@csrf_exempt
def etablissement_list(request):
    etablissements = list(Etablissement.objects.all().values())

    return JsonResponse(etablissements, safe=False) 

# Add new Classe obj
@csrf_exempt
def new_classe(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        code_classe = data['code_classe']
        libelle_classe = data['libelle_classe']

        # user = User.objects.first()  
	# TODO: get the currently logged in user

        classe = Classe.objects.create(
            code_classe=code_classe,
            libelle_classe=libelle_classe,
        )
        return redirect('classe_list')  
        
    return JsonResponse("ok", safe=False)

# Add new Etablissement obj
@csrf_exempt
def new_etablissement(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))

        # user = User.objects.first()  
	# TODO: get the currently logged in user

        etablissement = Etablissement.objects.create(
            adresse_postale=data['adresse_postale'],	
            adresse_rue=data['adresse_rue'],	
            adresse_ville= data['adresse_ville'],	
            categorie=data['categorie'],	
            date_creation=data['date_creation'],	
            niveau=data['niveau'],
            nom=data['nom'],
            statut=data['statut'],	
            telephone=data['telephone']
        )

        return JsonResponse("ok",safe=False) 
    return HttpResponse("ok")    

# Display a Classe obj
@csrf_exempt
def show_classe(request,id):
    if request.method == 'GET':
        classe = Classe.objects.get(id=id)

    return HttpResponse(classe.libelle_classe)


# Display an Etablissement obj
@csrf_exempt
def show_etablissement(request,id):
    if request.method == 'GET':
        etablissement = Etablissement.objects.get(id=id)

    return HttpResponse(etablissement)


# Find an Etablissement obj(zone - statut - niveau - categorie - note)
@csrf_exempt
def search_etablissement(request):
    zone = 'Parakou'
    statut = 'Privé'
    if request.method == 'GET':
        etablissement = Etablissement.objects.filter(adresse_ville=request.GET.get('zone'))| Etablissement.objects.filter(sstatut=request.GET.get('statut'))

    return HttpResponse(etablissement)   
