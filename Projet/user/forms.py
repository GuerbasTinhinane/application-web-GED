from django import forms
from .models import Documents
from user.models import Contrat 
from user.models import SoitTransmis
from user.models import PointDeSituation
from user.models import AvisJuridique
from user.models import Partenaire
from user.models import FinancementDuPartenaire
from user.models import AccordOperation
from user.models import Accord
from user.models import LettreAccord
from user.models import Avenant
from user.models import ConventionDeDetachement

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import CharField, IntegerField, DateField


User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
            'is_chefdep',
            'is_juriste',
            'is_admin',
        ]

class DocumentsForm(forms.ModelForm):
    class Meta:
       model = Documents
       fields = '__all__'
         
class ContratForm(forms.ModelForm):
   contrath = forms.BooleanField(widget=forms.HiddenInput, initial=True)
   class Meta:
       model = Contrat 
       fields = '__all__'
    #    def clean(self):
    #     cleaned_data = super().clean()
    #     date_signature_contrat = cleaned_data.get("date_signature_contrat")
    #     date_debut_contrat = cleaned_data.get("date_debut_contrat")
    #     date_fin_contrat = cleaned_data.get("date_fin_contrat")
    #     date_fin_recherche = cleaned_data.get("date_fin_recherche")
    #     date_debut_exploitation = cleaned_data.get("date_debut_exploitation")
    #     if date_fin_contrat < date_debut_contrat:
    #         raise forms.ValidationError("Date fin du contrat doit être supérieure à sa date de début.")
    #     if date_fin_recherche < date_debut_contrat:
    #         raise forms.ValidationError("Date fin de la phase de recherche doit être supérieure à la date de début du contrat.")
    #     if date_debut_exploitation < date_debut_contrat:
    #         raise forms.ValidationError("Date début de la phase exploitation doit être supérieure à la date de début du contrat.")
    #     if date_debut_exploitation < date_fin_recherche:
    #         raise forms.ValidationError("Date début de la phase exploitation doit être supérieure à la date de fin de la phase de recherche.")
    #     if  date_debut_contrat < date_signature_contrat :
    #         raise forms.ValidationError("Date début du contrat doit être supérieure à la date de sa signature.")

class SoitTransmisForm(forms.ModelForm):
   class Meta:
       model = SoitTransmis
       fields = '__all__'
       
class PointDeSituationForm(forms.ModelForm):
   class Meta:
       model = PointDeSituation
       fields = ['titre_pds',
       'code',
       'date_pds',
       'pds_pdf', 
       'contrat',
       'user'
       ]
       def clean(self):
        data = self.cleaned_data
        titre = data.get("titre_pds")
        qs = PointDeSituation.objects.filter(titre_pds=titre)
        if qs.exists():
            self.add_error("title", f"\"{titre}\" is already in use. Please pick another title.")
        return data
       
class AvisJuridiqueForm(forms.ModelForm):
   class Meta:
       model = AvisJuridique
       fields = '__all__'
       
     
class PartenaireForm(forms.ModelForm):
    partenaire = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Partenaire
        fields = '__all__'
    def set_nom_partenaire(self, nom_partenaire):
     data = self.data.copy()
     data['nom_partenaire'] = nom_partenaire
     self.data = data
    def clean_nom_partenaire(self):
      new1=self.cleaned_data['nom_partenaire']
      return new1

       
class FinancementDuPartenaireForm(forms.ModelForm):
   fdup = forms.BooleanField(widget=forms.HiddenInput, initial=True)
   class Meta:
       model = FinancementDuPartenaire
       fields = '__all__'
       
class AccordOperationForm(forms.ModelForm):
   class Meta:
       model = AccordOperation
       fields = '__all__'
       
class AccordForm(forms.ModelForm):
   class Meta:
       model = Accord 
       fields = '__all__'
       
class LettreAccordForm(forms.ModelForm):
   class Meta:
       model = LettreAccord
       fields = '__all__'


class AvenantForm(forms.ModelForm):
   class Meta:
       model = Avenant
       fields = '__all__'  

class ConventionDeDetachementForm(forms.ModelForm):
   class Meta:
       model = ConventionDeDetachement
       fields = '__all__'

class AccordSearchForm(forms.Form):
    num = IntegerField(required=False)
    titre = CharField( max_length=50, required=False)
    date_de_signature = DateField(required=False)