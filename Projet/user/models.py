from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
import geocoder

# Create your models here.

class User(AbstractUser):
    is_chefdep = models.BooleanField(default=False)
    is_juriste = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    history = HistoricalRecords()

class History(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50)
    prev = models.CharField(max_length=50)
    new = models.CharField(max_length=50)
    field = models.CharField(max_length=50)


class Documents(models.Model):
    nom=models.CharField(max_length=25)
    typee=models.CharField(max_length=25, choices=[
    ('Contrat1', 'Contrat1'),
    ('Contrat2', 'Contrat2'),
    ('Contrat3', 'Contrat3'),
    ('Contrat4', 'Contrat4'),
    ('Contrat5', 'Contrat5'), ])
    document=models.FileField(upload_to='Documents')
    def __str__(self):
        return self.nom


class Contrat(models.Model):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    titre_contrat=models.CharField( max_length=50, unique=True)
    loi=models.CharField(max_length=25, choices=[
    ('86-14', '86-14'),
    ('05-07', '05-07'),
    ('19-13', '19-13'), ])
    date_signature_contrat=models.DateField()
    num_decret=models.IntegerField()
    date_decret=models.DateField()
    date_debut_contrat=models.DateField()
    date_approbation_pod=models.DateField()
    financement_SH=models.FloatField()
    phase_contrat=models.CharField(max_length=25, choices=[
    ('Recherche', 'Recherche'),
    ('Développement', 'Développement'),
    ('Exploitation', 'Exploitation'), ])
    date_fin_contrat=models.DateField()
    date_fin_recherche=models.DateField()
    date_debut_exploitation=models.DateField()
    contrat_pdf=models.FileField(upload_to='Documents/Contrats')
    nom_op=models.CharField(max_length=50, unique=True)
    nom_perimetre=models.CharField(max_length=50, unique=True)
    user = models.CharField(max_length=50, blank=True)
    history = HistoricalRecords()
    
    def __str__(self): 
        return self.code

      
class DocumentContractuel(models.Model):
    titre=models.CharField(max_length=50, unique=True)
    date_de_signature=models.DateField()
    contrat=models.ForeignKey(Contrat, on_delete=models.CASCADE, default=None)
    user = models.CharField(max_length=50, blank=True)
    history=HistoricalRecords(inherit=True)
    class Meta:
        abstract = True 

    def __str__(self):
        return self.code


class AvisJuridique(models.Model):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    titre_avis=models.CharField(max_length=50, unique=True)
    date_avis=models.DateField()
    avis_pdf=models.FileField(upload_to='Documents/Avis_juridiques')
    contrat=models.ForeignKey(Contrat, on_delete=models.CASCADE, default=None)
    user = models.CharField(max_length=50, blank=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.code

# creating a validator function
# def validate_titre_pds(value):
#     for instance in PointDeSituation.objects.all():
#         if instance.titre_pds == value:
#             raise ValidationError(value + ' is already added')
#         else:
#             return value

class PointDeSituation(models.Model):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    titre_pds=models.CharField(max_length=50, unique=True)
    date_pds=models.DateField()
    pds_pdf=models.FileField(upload_to='Documents/Point_de_situations')
    contrat=models.ForeignKey(Contrat, on_delete=models.CASCADE, default=None)
    user = models.CharField(max_length=50, blank=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.code
    

class Partenaire(models.Model):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    nom_partenaire=models.CharField(max_length=50, unique=True)
    pays=models.CharField(max_length=50)
    latitude = models.FloatField(default=0, blank=True)
    longitude = models.FloatField(default=0, blank=True)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name_plural = 'Partenaire'

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.pays).lat
        self.longitude = geocoder.osm(self.pays).lng
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nom_partenaire

class SoitTransmis(models.Model):
    num_st=models.IntegerField(primary_key=True, default=None)
    id_document=models.CharField(max_length=50, unique=True)
    date_arrivee_st=models.DateField()
    date_depart_st=models.DateField()
    objet=models.CharField(max_length=50)
    expediteur=models.CharField(max_length=50)
    st_pdf=models.FileField(upload_to='Documents/Soit_transmis')
    user = models.CharField(max_length=50, blank=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.id_document

class AccordOperation(DocumentContractuel):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    doc_pdf=models.FileField(upload_to='Documents/Documents_contractuels/Accords_operations')

class Accord(DocumentContractuel):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    doc_pdf=models.FileField(upload_to='Documents/Documents_contractuels/Accords')

class LettreAccord(DocumentContractuel):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    doc_pdf=models.FileField(upload_to='Documents/Documents_contractuels/Lettres_accords')

class Avenant(DocumentContractuel):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    doc_pdf=models.FileField(upload_to='Documents/Documents_contractuels/Avenant')

class ConventionDeDetachement(DocumentContractuel):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    doc_pdf=models.FileField(upload_to='Documents/Documents_contractuels/Conventions')


class FinancementDuPartenaire(models.Model):
    code=models.CharField(primary_key=True, blank=True, max_length=50)
    pourcentage_fin=models.FloatField()
    contrat=models.ForeignKey(Contrat, on_delete=models.CASCADE, default=None)
    partenaire=models.ForeignKey(Partenaire, on_delete=models.CASCADE, default=None)
    history = HistoricalRecords()
    def __str__(self):
        return self.code