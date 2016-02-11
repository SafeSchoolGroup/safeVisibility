from django.db import models

# Create your models here.

class Classe(models.Model):
	code_classe = models.CharField(max_length=5)
	libelle_classe = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.code_classe

class Niveau(models.Model):
	TYPE_NIVEAU = (
		('GEN', 'Général'),
		('TECH', 'Technique')
	)
	code_niveau = models.CharField(max_length=5)
	description_niveau = models.CharField(max_length=40)
	type_niveau = models.CharField(max_length=15, choices=TYPE_NIVEAU)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.code_niveau		

class Etablissement (models.Model):
	# NIVEAU = (
    #     ('EM', 'Enseignement Maternel'),
    #     ('EP', 'Enseignement Primaire'),
    #     ('ES', 'Enseignement Secondaire'),
	# 	('ESup', 'Enseignement Supérieur'),
	# 	('FP','Formation Professionnelle')
    )
	
	STATUT = (
        ('PUBLIC', 'Public'),
        ('PRIVE', 'Privé'),
		('COMMUNAUTAIRE','Communautaire')
    )
	ORDRE_ENSEIGNEMENT = (
        ('Laic', 'Laic'),
        ('Catholique', 'Catholique'),
        ('Protestant', 'Protestant'),
    )

	nom = models.CharField(max_length=30, unique=True)
	adresse_rue = models.CharField(max_length=30)
	adresse_ville = models.CharField(max_length=30)		
	adresse_postale = models.CharField(max_length=30, unique=True)	
	telephone = models.CharField(max_length=15, unique=True)	
	date_creation = models.DateField()	
	statut = models.CharField(max_length=10, choices=STATUT)
	ordre_enseignement = models.CharField(max_length=15, choices=ORDRE_ENSEIGNEMENT)
	niveau = models.CharField(max_length=5, choices=NIVEAU)
	classes = models.ManyToManyField(Classe, through='EtablissementClasse')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nom


class EtablissementClasse(models.Model):
	etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
	classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
	frais_scolarite = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	


