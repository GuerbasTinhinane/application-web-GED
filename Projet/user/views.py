#redirect and render import
from audioop import reverse
from tkinter import Y
from django.shortcuts import redirect, render 
#modelsImport
from user.models import Documents
from user.models import DocumentContractuel
from user.models import History
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
from django.contrib.auth import get_user_model

#formsImport
from user.forms import ContratForm
from user.forms import SoitTransmisForm
from user.forms import PointDeSituationForm
from user.forms import AvisJuridiqueForm
from user.forms import PartenaireForm
from user.forms import FinancementDuPartenaireForm
from user.forms import AccordOperationForm
from user.forms import AccordForm
from user.forms import LettreAccordForm
from user.forms import AvenantForm
from user.forms import ConventionDeDetachementForm
from user.forms import UserForm
from .forms import DocumentsForm
from .forms import AccordSearchForm

#loginImport
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect

#fileImport
from django.core.files.storage import FileSystemStorage

from datetime import date,timedelta
# Create your views here.
from django.contrib import messages 
#**************** Password change*************
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangeForm
  success_url = reverse_lazy('home')




#**************** DASHBORD*************
#//////////////////////////////////////////////SQLITE////////////////////////////



# def readSqliteTable():
#     try:
#         sqliteConnection = sqlite3.connect('db.sqlite3')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         sqlite_select_query = """SELECT  partenaire ,count(*) from FinancementDuPartenaire group by partenaire"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Total rows are:  ", len(records))
#         print("Printing each row")

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read data from sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             print("The SQLite connection is closed")


#///////////////////////////////////////////////MYSQL////////////////////////////////

# import mysql.connector
# try:
#     dbConnexion = mysql.connector.connect(
#        host="localhost",
#        user="username",
#        password="password",
#        database="mydatabase"
#     )

#     cursor = dbConnexion.cursor()
#     print("Connected to MySQL")
#     cursor.execute("SELECT  partenaire ,count(*) from FinancementDuPartenaire group by partenaire")

#     result = cursor.fetchall()

#     for x in result:
#       print(x)
# except mysql.Error as error:
#         print("Failed to read data from mysql table", error)
# finally:
#     if dbConnexion:
#         dbConnexion.close()
#         print("The MySQL connection is closed")

# import sqlite3
def dashboard(request):
    if request.user.is_authenticated:
     current_user = request.user
     #Effectifs
     ct_nb = Contrat.objects.all().count()
     ct_nb = int(ct_nb)
     print('Nombre de contrats',ct_nb)

     st_nb = SoitTransmis.objects.all().count()
     st_nb = int(st_nb)
     print('Nombre de soit transmis',st_nb)

     pds_nb = PointDeSituation.objects.all().count()
     pds_nb = int(pds_nb)
     print('Nombre de points de situation',pds_nb)

     aj_nb = AvisJuridique.objects.all().count()
     aj_nb = int(aj_nb)
     print("Nombre d'avis juridiques",aj_nb)
    
     #Documents Contratuels par type
     av_nb = Avenant.objects.all().count()
     av_nb = int(av_nb)
     print("Nombre d'avenants",av_nb)

     ac_nb = Accord.objects.all().count()
     ac_nb = int(ac_nb)
     print("Nombre d'accords",ac_nb)

     la_nb = LettreAccord.objects.all().count()
     la_nb = int(la_nb)
     print("Nombre de lettres d'accord",la_nb)

     ao_nb = AccordOperation.objects.all().count()
     ao_nb = int(ao_nb)
     print("Nombre d'accords d'opération",ao_nb)

     cd_nb = ConventionDeDetachement.objects.all().count()
     cd_nb = int(cd_nb)
     print("Nombre de convention de détachement",cd_nb)

     dc_nb = av_nb + ac_nb + la_nb + ao_nb + cd_nb
     print('Nombre de documents contractuels',dc_nb)

     #Contrats par phase
     ctR_nb = Contrat.objects.filter(phase_contrat='Recherche').count()
     ctR_nb = int(ctR_nb)
     print('Nombre de contrats en phase de recherche',ctR_nb)

     ctD_nb = Contrat.objects.filter(phase_contrat='Développement').count()
     ctD_nb = int(ctD_nb)
     print('Nombre de contrats en phase de développement',ctD_nb)

     ctE_nb = Contrat.objects.filter(phase_contrat='Exploitation').count()
     ctE_nb = int(ctE_nb)
     print("Nombre de contrats en phase d'exploitation",ctE_nb)

    
    #tableau des partenaires
     print("methode raw iciiiiiiii")
     partenaire_list = FinancementDuPartenaire.objects.raw('''SELECT partenaire_id,
           x.code ,
           y.code as codep,
           y.pays,
           y.nom_partenaire as nom,
           count( * ) as nbct
      FROM user_financementdupartenaire x, user_partenaire y
      where x.partenaire_id = y.code
     GROUP BY partenaire_id''')
     for p in partenaire_list:
        print('*******************')
        print(p.code)
        print(p.pays)
        print(p.nom)
        print(p.nbct)
        print('*******************')
   

     doc_list = ['Contrat', 'Document contractel', 'Soit transmis', 'Point de situation', 'Avis juridique']
     doc_number = [ct_nb, dc_nb, st_nb, pds_nb, aj_nb]

     dc_list = ['Avenant', 'Accord', 'Lettre accord', "Accord d'opérations", "Convention de détachement"]
     dc_number = [av_nb, ac_nb, la_nb, ao_nb, cd_nb ]

     ct_list = ['Recherche', 'Développement', 'Exploitation']
     ct_number = [ctR_nb, ctD_nb, ctE_nb ]

     #Contrats par annees
     annee_list = []
     nbct_list = []
     ct = Contrat.objects.all()
     for x in ct:
         print('coucou')
         d = x.date_signature_contrat
         c = str(d)[0:4]
         print(c)
         annee_list.append(c)
     annee_list = list(set(annee_list))
     for y in annee_list:
         a = Contrat.objects.filter(date_signature_contrat__year= y)
         nb = len(a)
         nbct_list.append(nb)
         print (nb)

     #Contrats nb par phase par annee 
     #phase recherche
     nbctR_list =[]
     for y in annee_list:
         a = Contrat.objects.filter(date_signature_contrat__year= y ).filter(phase_contrat = 'Recherche')
         nb = len(a)
         nbctR_list.append(nb)
         print(y, '->',nb)
     #phase developppement
     print('------------')
     nbctD_list =[]
     for y in annee_list:
         a = Contrat.objects.filter(date_signature_contrat__year= y ).filter(phase_contrat = 'Développement')
         nb = len(a)
         nbctD_list.append(nb)
         print(y, '->',nb)
     #phase exploitation
     print('------------')
     nbctE_list =[]
     for y in annee_list:
         a = Contrat.objects.filter(date_signature_contrat__year= y ).filter(phase_contrat = 'Exploitation')
         nb = len(a)
         nbctE_list.append(nb)
         print(y, '->',nb)

     # Les cases si y (annee actuelle)
     current_date = date.today()
     y = str(current_date)[0:4]
     ct_nba = Contrat.objects.filter(date_signature_contrat__year= y).count()
     ct_nba = int(ct_nba)
     print('Nombre de contrats cette annnee',ct_nba)

     st_nba = SoitTransmis.objects.filter(date_arrivee_st__year= y).count()
     st_nba = int(st_nba)
     print('Nombre de soit transmis cette annnee',st_nba)

     pds_nba = PointDeSituation.objects.filter(date_pds__year= y).count()
     pds_nba = int(pds_nba)
     print('Nombre de points de situation cette annnee',pds_nba)

     aj_nba = AvisJuridique.objects.filter(date_avis__year= y).count()
     aj_nba = int(aj_nba)
     print("Nombre d'avis juridiques cette annnee",aj_nba)

     #Documents Contratuels par type
     av_nba = Avenant.objects.filter(date_de_signature__year= y).count()
     av_nba = int(av_nba)

     ac_nba = Accord.objects.filter(date_de_signature__year= y).count()
     ac_nba = int(ac_nba)

     la_nba = LettreAccord.objects.filter(date_de_signature__year= y).count()
     la_nba = int(la_nba)

     ao_nba = AccordOperation.objects.filter(date_de_signature__year= y).count()
     ao_nba = int(ao_nba)

     cd_nba = ConventionDeDetachement.objects.filter(date_de_signature__year= y).count()
     cd_nba = int(cd_nba)

     dc_nba = av_nba + ac_nba + la_nba + ao_nba + cd_nba
     print('Nombre de documents contractuels cette annee',dc_nba)


   
  
    

     context = {'doc_list':doc_list, 'doc_number':doc_number,
                'dc_list':dc_list, 'dc_number':dc_number, 
                'ct_list':ct_list, 'ct_number':ct_number,
                'dc_nb':dc_nb, 'ct_nb':ct_nb, 'aj_nb':aj_nb, 
                'pds_nb':pds_nb, 'st_nb':st_nb,
                'dc_list':dc_list, 'dc_number':dc_number, 
                'ct_list':ct_list, 'ct_number':ct_number,
                'dc_nba':dc_nba, 'ct_nba':ct_nba, 'aj_nba':aj_nba, 
                'pds_nba':pds_nba, 'st_nba':st_nba,
                'annee_list':annee_list ,'nbct_list':nbct_list,
                'nbctR_list':nbctR_list, 'nbctD_list':nbctD_list, 
                'nbctE_list':nbctE_list, 'partenaire_list':partenaire_list}
     if current_user.is_chefdep:
        return render( request,'chefdep/general/dashboard.html', context)
     else:
        return render(request, 'general/dashboard.html', context)
    else:
      return render(request, 'general/error.html')



# ************   SIG   *****************    

import folium
from folium import plugins

def index(request):
    if request.user.is_authenticated:
      current_user = request.user
      data = Partenaire.objects.all()
      data_list = Partenaire.objects.values_list('latitude', 'longitude')

      map1 = folium.Map(location=[19, -12],
                        tiles='stamentoner', zoom_start=2)

      plugins.MarkerCluster(data_list).add_to(map1)
      plugins.Fullscreen(position='topright').add_to(map1)
      map1 = map1._repr_html_()
      context = {
          'map1': map1
        }
      if current_user.is_chefdep:
        return render( request,'chefdep/dashboard/dashboard.html', context)
      else:
        return render(request, 'dashboard/dashboard.html', context)
    else:
      return render(request, 'general/error.html')


# *********Cryptage de la base de données*************
# def encrypt(txt):
#     try:
#         txt = str(txt)
#         cipher_suite = Fernet(settings.ENCRYPT_KEY) 
#         encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
#         encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
#         return encrypted_text
#     except Exception as e:
#         logging.getLogger("error_logger").error(traceback.format_exc())
#         return None

#********History************

def view_history(request):
    if request.user.is_authenticated:
      current_user = request.user
      hist1 = Contrat.history.all()
      hist3 = Partenaire.history.all()
      hist2 = Accord.history.all()
      hist5 = AccordOperation.history.all()
      hist4 = Avenant.history.all()
      hist6 = AvisJuridique.history.all()
      hist7 = LettreAccord.history.all()
      hist8 = ConventionDeDetachement.history.all()
      hist9 = PointDeSituation.history.all()
      hist10 = SoitTransmis.history.all()
      hist11 = FinancementDuPartenaire.history.all()
      if (current_user.is_chefdep or current_user.is_admin):
        return render( request,"chefdep/gestion/history.html", {'hist1':hist1, 'hist2':hist2, 'hist3':hist3, 'hist4':hist4,
                                                        'hist5':hist5, 'hist6':hist6, 'hist7':hist7, 'hist8':hist8,
                                                        'hist9':hist9, 'hist10':hist10, 'hist11':hist11})
      else:
        return render(request, 'general/error.html')
    else:
      return render(request, 'general/error.html')



#*******Home*******
def home(request):
    auth.logout(request)
    error = ''
    username =''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_chefdep:
                return redirect('chefdep')
            elif user.is_admin:
                return redirect('admin')
            else:
                return redirect('juriste')
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect Veuillez réessayer "
    return render(request, 'general/login.html', {'error':error})

def logoutUser(request):
    auth.logout(request)
    return redirect('/')

from django.contrib import messages 
def register(request):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_admin:
        form = UserForm()
        if request.method == "POST":
          form = UserForm(data=request.POST)
          if form.is_valid():
             form.save()
             messages.success(request, "Utilisateur ajouté avec succès!")
        return render( request,'general/register.html', {'form':form})
      else:
        return render(request, 'general/error.html')
    else:
      return render(request, 'general/error.html')


import html
def chefdep(request):
    if request.user.is_authenticated:
      current_user = request.user
      if (current_user.is_chefdep or current_user.is_admin):
        
        return render( request,'general/chefdep.html')
        return redirect(dashboard)
      else:
        return render(request, 'general/juriste.html')
    else:
        return render(request, 'general/error.html')

def juriste(request):
    if request.user.is_authenticated:
      current_user = request.user
      hist1 = Contrat.history.filter( history_user_id=current_user.id)
      hist2 = Accord.history.filter( history_user_id=current_user.id)
      hist3 = Partenaire.history.filter( history_user_id=current_user.id)
      hist4 = Avenant.history.filter( history_user_id=current_user.id)
      hist5 = AccordOperation.history.filter( history_user_id=current_user.id)
      hist6 = AvisJuridique.history.filter( history_user_id=current_user.id)
      hist7 = LettreAccord.history.filter( history_user_id=current_user.id)
      hist8 = ConventionDeDetachement.history.filter(history_user_id=current_user.id)
      hist9 = PointDeSituation.history.filter(history_user_id=current_user.id)
      hist10 = SoitTransmis.history.filter(history_user_id=current_user.id)
      hist11 = FinancementDuPartenaire.history.filter(history_user_id=current_user.id)
      
      current_date = date.today()
      list_ct = Contrat.objects.all()
      ct_died = []
      bool_list= []
      for c in list_ct:
            eccart = c.date_fin_contrat - current_date
            afteran = current_date + timedelta(365)
            afteran = afteran - current_date
            print(eccart)
            if ( eccart < afteran ):
              list_av = Avenant.objects.filter(contrat= c.code)
              trouve = False
              for a in list_av:
                 titre = a.titre
                 if (titre.find('prorogation') != -1):
                     trouve = True
                     break
              if ( trouve == False ):
               print('yes')
               ct_died.append(c)
               bool_list.append(str(trouve))
        
      if 'False' in bool_list:
            messages.warning(request, html.unescape("Un ou plusieurs contrats vont expiré dans moins"))
      if current_user.is_juriste or current_user.is_admin:
          return render(request, 'general/juriste.html', {'hist1':hist1, 'hist2':hist2, 'hist3':hist3, 'hist4':hist4,
                                                        'hist5':hist5, 'hist6':hist6, 'hist7':hist7, 'hist8':hist8,
                                                        'hist9':hist9, 'hist10':hist10 , 'hist11':hist11,'ct_died':ct_died})
      else:
          return render(request, 'general/error.html')
    else:
      return render(request, 'general/error.html')


def admin(request):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_admin:
          return render(request, 'general/admin.html')
      else:
          return render(request, 'general/error.html')
    else:
      return render(request, 'general/error.html')





#Gestion des formulaires ajout modification suppression affichage

#***************Ajout***********
def accord_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
         accord = Accord.objects.all()
         form = AccordForm()
         error=''
         if request.method == 'POST':
            form = AccordForm(request.POST, request.FILES)
            n = request.POST['titre']
            qs = Accord.objects.filter(titre=n)
            if qs.exists():
             n = '"'+n+'"'
             error = "Accord avec le titre: "+n+" existe déjà."
            if form.is_valid():
                n1 = request.POST['titre'] 
                n2 = request.POST['date_de_signature'] 
                n3 = request.FILES['doc_pdf'] 
                n4 = request.POST['contrat']          

                c = Contrat.objects.filter(code=n4)
                print(c)
                for i in c:
                 print(i.nom_perimetre)
                 a = (i.nom_perimetre).upper()
                 m = Accord.objects.all()
                 n = str(len(m) + 1)
                 d = str(n2)[2:4]
    
                accord = Accord.objects.create(
                   code="-".join([("".join([("_".join(['ACC', a])), d])), n]),
                   titre = n1,
                   date_de_signature=n2,
                   doc_pdf=n3,
                   contrat=i
                )
                accord.save()
                messages.success(request, "Accord ajouté avec succès!")
                # return redirect(update_accord, '0')
         return render(request, "models/accord.html",{"form": form, 'accord': accord, 'error':error})
    else:
      return render(request, 'general/error.html')

def contrat_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        contrat = Contrat.objects.all()
        form_contrat = ContratForm()
        fdup = FinancementDuPartenaire.objects.all() 
        form_fdup = FinancementDuPartenaireForm()
        partenaire = Partenaire.objects.all()
        error=''
        error1=''
        error2=''
        error3=''
        error4=''
        num=''
        fin=''
        form = PartenaireForm()
        if request.method == 'POST':
           print(request.POST)
           if 'contrath' in request.POST: 
               print('oh nooo')
               form_contrat = ContratForm(request.POST, request.FILES)
               num = request.POST['num_decret']
               fin = request.POST['financement_SH']
               n = request.POST['titre_contrat']
               qs = Contrat.objects.filter(titre_contrat=n)
               if qs.exists():
                 n = '"'+n+'"'
                 error = "Contrat avec le titre: "+n+" existe déjà."
               n1 = request.POST['nom_op']
               qs = Contrat.objects.filter(nom_op=n1)
               if qs.exists():
                 n1 = '"'+n1+'"'
                 error1 = "Contrat avec opérateur: "+n1+" existe déjà."
               n2 = request.POST['nom_perimetre']
               qs = Contrat.objects.filter(nom_perimetre=n2)
               if qs.exists():
                 n2 = '"'+n2+'"'
                 error2 = "Contrat sur le périmètre "+n2+" existe déjà."
               if form_contrat.is_valid():
                 n1 = request.POST['titre_contrat'] 
                 n2 = request.POST['loi']
                 n3 = request.POST['date_signature_contrat'] 
                 n4 = request.POST['num_decret']
                 n5 = request.POST['date_decret']
                 n6 = request.POST['date_debut_contrat']
                 n8 = request.POST['date_approbation_pod']
                 n9 = request.POST['financement_SH']
                 n10 = request.POST['phase_contrat']
                 n11 = request.POST['date_fin_contrat']
                 n12 = request.FILES['contrat_pdf'] 
                 n13 = request.POST['nom_op']
                 n14 = request.POST['nom_perimetre'] 
                 n15 = request.user.username
                 n16 = request.POST['date_fin_recherche']
                 n17 = request.POST['date_debut_exploitation']
                 contrat = Contrat.objects.create(
                     code="".join([("_".join(['CT', n14.upper()])), str(n3)[2:4]]),
                     titre_contrat = n1,
                     loi=n2,
                     date_signature_contrat=n3,
                     num_decret=n4,
                     date_decret=n5,
                     date_debut_contrat=n6,
                     date_approbation_pod=n8,
                     financement_SH=n9,
                     phase_contrat=n10,
                     date_fin_contrat=n11,
                     contrat_pdf=n12,
                     nom_op=n13,
                     nom_perimetre=n14,
                     user = n15,
                     date_fin_recherche=n16,
                     date_debut_exploitation=n17
                   )
                 contrat.save()
                 messages.success(request, "Contrat ajouté avec succès!")
                #  return redirect(update_contrat, '0')
           if 'fdup' in request.POST:
                form_fdup = FinancementDuPartenaireForm(request.POST)
                n3 = request.POST['contrat']
                n4 = request.POST['partenaire']
                qs = FinancementDuPartenaire.objects.filter(contrat=n3).filter(partenaire=n4)
                if qs.exists():
                 for w in qs:
                   n4 = str(w.partenaire)
                 error3 = "Financement du contrat: "+n3+" effectué par: "+n4+" existe déjà."

                 return render(request, 'models/contrat.html', {"form_contrat": form_contrat,
        'contrat': contrat, "form_fdup": form_fdup, 'fdup': fdup, "form": form, 'partenaire': partenaire, 
        'fin':fin, 'num':num, 'error':error, 'error1':error1, 'error2':error2, 'error3':error3, 'n3':n3, 'n4':n4})
                if form_fdup.is_valid():
                 n0 = request.POST['pourcentage_fin'] 
                 n1 = request.POST['contrat'] 
                 n2 = request.POST['partenaire'] 
                 p = Partenaire.objects.get(code=n2)
                 co = Contrat.objects.get(code=n1)
                 a = (p.nom_partenaire).upper()
                 b = (co.nom_perimetre).upper()
                 t = (co.date_signature_contrat)
                 c = str(t)[2:4]
                 a = "_".join(['F', a])
                 fdup = FinancementDuPartenaire.objects.create(
                     code="".join([("_".join([a, b])), c]),
                     pourcentage_fin=n0,
                     contrat = co,
                     partenaire=p
                    )
                 fdup.save()
                 messages.success(request, "Financement ajouté avec succès!")
           if 'partenaire' in request.POST:
               form = PartenaireForm(request.POST)
               n = request.POST['nom_partenaire']
               qs = Partenaire.objects.filter(nom_partenaire=n)
               if qs.exists():
                 n = '"'+n+'"'
                 error4 = "Partenaire avec le nom: "+n+" existe déjà."
               if form.is_valid():
                 n = request.POST['nom_partenaire']
                 p = request.POST['pays']
                 m = Partenaire.objects.filter(pays=p)
                 r = str(len(m) + 1)
                 partenaire = Partenaire.objects.create(nom_partenaire=n, pays=p, code="_".join([ (p.upper())[0:3], r]) )
                 partenaire.save()
                 messages.success(request, "Partenaire ajouté avec succès!")
              #  return redirect(update_partenaire, '0')
        return render(request, 'models/contrat.html', {"form_contrat": form_contrat,
        'contrat': contrat, "form_fdup": form_fdup, 'fdup': fdup, "form": form, 'partenaire': partenaire, 
        'fin':fin, 'num':num, 'error':error, 'error1':error1, 'error2':error2, 'error3':error3, 'error4':error4})
    else:
      return render(request, 'general/error.html')
   
def accordOperation_create(request):
    if request.user.is_authenticated:
      current_user = request.user 
      error=''
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
         accordop = AccordOperation.objects.all()
         form = AccordOperationForm()
         if request.method == 'POST':
           form = AccordOperationForm(request.POST, request.FILES)
           n = request.POST['titre']
           qs = AccordOperation.objects.filter(titre=n)
           if qs.exists():
             n = '"'+n+'"'
           error = "AOP avec le titre: "+n+" existe déjà."
           if form.is_valid():
               n1 = request.POST['titre'] 
               n2 = request.POST['date_de_signature'] 
               n3 = request.FILES['doc_pdf'] 
               n4 = request.POST['contrat']  
               n15 = request.user.username        

               c = Contrat.objects.get(code=n4)
               a = (c.nom_perimetre).upper()
               m = AccordOperation.objects.all()
               n = str(len(m) + 1)
               d = str(n2)[2:4]
    
               accordop = AccordOperation.objects.create(
                   code="-".join([("".join([("_".join(['AOP', a])), d])), n]),
                   titre = n1,
                   date_de_signature=n2,
                   doc_pdf=n3,
                   contrat=c, 
                   user = n15
                 )
               accordop.save()
               messages.success(request, "Accord d'opération ajouté avec succès!")
             #   return redirect(update_accordOp, '0')
         return render(request, "models/accordoperation.html",{"form": form, 'accordop': accordop, 'error':error})
    else:
      return render(request, 'general/error.html')

def avenant_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      error=''
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        avenant = Avenant.objects.all()
        form = AvenantForm()
        if request.method == 'POST':
           form = AvenantForm(request.POST, request.FILES)
           n = request.POST['titre']
           qs = Accord.objects.filter(titre=n)
           if qs.exists():
             n = '"'+n+'"'
           error = "Avenant avec le titre: "+n+" existe déjà."
           if form.is_valid():
             n1 = request.POST['titre'] 
             n2 = request.POST['date_de_signature'] 
             n3 = request.FILES['doc_pdf'] 
             n4 = request.POST['contrat'] 
             n15 = request.user.username         
 
             c = Contrat.objects.get(code=n4)
             a = (c.nom_perimetre).upper()
             m = Avenant.objects.filter(contrat=n4)
             n = str(len(m) + 1)
             d = str(n2)[2:4]
    
             avenant = Avenant.objects.create(
                 code="-".join([("".join([("_".join(['AVN', a])), d])), n]),
                 titre = n1,
                 date_de_signature=n2,
                 doc_pdf=n3,
                 contrat=c,
                 user=n15
                )
             avenant.save()
             messages.success(request, "Avenant ajouté avec succès!")
             # return redirect(update_avenant, '0')
        return render(request, "models/avenant.html",{"form": form, 'avenant': avenant, 'error':error})
    else:
      return render(request, 'general/error.html')

def avisJuridique_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      error=''
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        avis= AvisJuridique.objects.all()
        form = AvisJuridiqueForm()
        if request.method == 'POST':
         form = AvisJuridiqueForm(request.POST, request.FILES)
         n = request.POST['titre']
         qs = Accord.objects.filter(titre=n)
         if qs.exists():
             n = '"'+n+'"'
         error = "AVJ avec le titre: "+n+" existe déjà."
         if form.is_valid():
             n1 = request.POST['titre'] 
             n2 = request.POST['date_de_signature'] 
             n3 = request.POST['doc_pdf'] 
             n4 = request.POST['contrat']  
             n15 = request.user.username        

             c = Contrat.objects.filter(code=n4)
             a = (c.nom_perimetre).upper()
             m = AvisJuridique.objects.all()
             n = str(len(m) + 1)
             d = str(n2)[2:4]
    
             avis = AvisJuridique.objects.create(
                 code="-".join([("".join([("_".join(['AVJ', a])), d])), n]),
                 titre = n1,
                 date_de_signature=n2,
                 doc_pdf=n3,
                 contrat=n4,
                 user=n15
                )
             avis.save()
             messages.success(request, "Avis juridique ajouté avec succès!")
             # return redirect(update_avis, '0')
        return render(request,"models/avisjuridique.html",{"form": form, 'avis': avis, 'error':error})
    else:
      return render(request, 'general/error.html')

def convention_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      error=''
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        convention = ConventionDeDetachement.objects.all()
        form = ConventionDeDetachementForm()
        if request.method == 'POST':
           form = ConventionDeDetachementForm(request.POST, request.FILES)
           n = request.POST['titre']
           qs = Accord.objects.filter(titre=n)
           if qs.exists():
             n = '"'+n+'"'
           error = "Convention avec le titre: "+n+" existe déjà."
           if form.is_valid():
               n1 = request.POST['titre'] 
               n2 = request.POST['date_de_signature'] 
               n3 = request.FILES['doc_pdf'] 
               n4 = request.POST['contrat']   
               n15 = request.user.username       

               c = Contrat.objects.get(code=n4)
               a = (c.nom_perimetre).upper()
               m = ConventionDeDetachement.objects.all()
               n = str(len(m) + 1)
               d = str(n2)[2:4]
    
               convention = ConventionDeDetachement.objects.create(
                   code="-".join([("".join([("_".join(['COV', a])), d])), n]),
                   titre = n1,
                   date_de_signature=n2,
                   doc_pdf=n3,
                   contrat=c,
                   user=n15
                )
               convention.save()
               messages.success(request, "Convention ajoutée avec succès!")
               # return redirect(update_convention, '0')
        return render(request, "models/convention.html",{"form": form, 'convention': convention, 'error':error})
    else:
      return render(request, 'general/error.html')

def lettreAccord_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      error=''
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        laccord = LettreAccord.objects.all()
        form = LettreAccordForm()
        if request.method == 'POST':
          form = LettreAccordForm(request.POST, request.FILES)
          n = request.POST['titre']
          qs = Accord.objects.filter(titre=n)
          if qs.exists():
             n = '"'+n+'"'
          error = "Lettre Accord avec le titre: "+n+" existe déjà."
          if form.is_valid():
              n1 = request.POST['titre'] 
              n2 = request.POST['date_de_signature'] 
              n3 = request.FILES['doc_pdf'] 
              n4 = request.POST['contrat']    
              n15 = request.user.username      

              c = Contrat.objects.get(code=n4)
              a = (c.nom_perimetre).upper()
              m = LettreAccord.objects.all()
              n = str(len(m) + 1)
              d = str(n2)[2:4]
    
              laccord = LettreAccord.objects.create(
                 code="-".join([("".join([("_".join(['LAC', a])), d])), n]),
                 titre = n1,
                 date_de_signature=n2,
                 doc_pdf=n3,
                 contrat=c,
                 user=n15
                )
              laccord.save()
              messages.success(request, "Lettre accord ajoutée avec succès!")
              # return redirect(update_lettreAccord, '0')
        return render(request, "models/lettreaccord.html",{"form": form, 'laccord': laccord, 'error':error})
    else:
      return render(request, 'general/error.html')

def st_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      error=''
      e=''
      o=''
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        st = SoitTransmis.objects.all()
        form = SoitTransmisForm()
        if request.method == 'POST':
          form = SoitTransmisForm(request.POST, request.FILES)
          e = request.POST['expediteur']
          o = request.POST['objet']
          n = request.POST['id_document']
          qs = SoitTransmis.objects.filter(id_document=n)
          if qs.exists():
             n = '"'+n+'"'
             error = "ST avec id: "+n+" existe déjà."
          if form.is_valid():
              form.save()
              messages.success(request, "Soit transmis ajouté avec succès!")
              # return redirect(update_st, '0')
        return render(request, "models/st.html",{'e':e, 'o':o, "form": form, 'st': st, 'error':error})
    else:
      return render(request, 'general/error.html')

def pds_create(request):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        error = ''
        pds = PointDeSituation.objects.all()
        form = PointDeSituationForm()
        if request.method == 'POST':
         form = PointDeSituationForm(request.POST, request.FILES)
         n = request.POST['titre_pds']
         qs = PointDeSituation.objects.filter(titre_pds=n)
         if qs.exists():
          n = '"'+n+'"'
          error = "Pds avec le titre: "+n+" existe déjà."
         if form.is_valid():
             n1 = request.POST['titre_pds'] 
             n2 = request.POST['date_pds'] 
             n3 = request.FILES['pds_pdf'] 
             n4 = request.POST['contrat']   
             n15 = request.user.username       

             c = Contrat.objects.get(code=n4)
             a = (c.nom_perimetre).upper()
             m = PointDeSituation.objects.filter(contrat=n4)
             n = str(len(m) + 1)
             d = str(n2)[2:4]
    
             pds = PointDeSituation.objects.create(
                 code="-".join([("".join([("_".join(['PDS', a])), d])), n]),
                 titre_pds = n1,
                 date_pds=n2,
                 pds_pdf=n3,
                 contrat=c,
                 user=n15
                )
             pds.save()
             messages.success(request, "Point de situation ajouté avec succès!")
             # return redirect(update_pds, '0')
        return render(request, "models/pds.html",{"form": form, 'pds': pds, 'error':error})
    else:
      return render(request, 'general/error.html')



#***************************************
#************Affichage_Detaillé*********
def affiche_detail_accord(request, c): 
    accord = Accord.objects.filter(code=c) 
    return render(request,"tableau/tableaccord.html", {"accord": accord})



#**************************************
#***************Affichage + Modification***********

def update_partenaire_fdup(request, c):  
    if request.user.is_authenticated:
      current_user = request.user
      y=0
      x=0
      formP=PartenaireForm()
      formF= FinancementDuPartenaireForm()
      partenaire = Partenaire.objects.all()
      fdup = FinancementDuPartenaire.objects.all()
      if (c !='0'):
        if ( (len(str(c)) == 5) or (len(str(c)) == 6) ):
           x = Partenaire.objects.get(code=c)
           if request.method == 'POST':
              formP = PartenaireForm(request.POST, instance=x)
              if formP.is_valid():
                  formP.save()
                  messages.success(request, "Partenaire modifié avec succès!")
           else:
            formP = PartenaireForm(instance=x) 
        else:
           x = FinancementDuPartenaire.objects.get(code=c)
           y = Partenaire.objects.get(nom_partenaire=x.partenaire)
           y = y.code
           if request.method == 'POST':
               formF = FinancementDuPartenaireForm(request.POST, instance=x)
               if formF.is_valid():
                  formF.save()
                  messages.success(request, "Financement modifié avec succès!")
           else:
            formF = FinancementDuPartenaireForm(instance=x)
      if current_user.is_chefdep:
        return render(request,"chefdep/tableau/contrat2.html",{'formP': formP,'formF': formF, 'x':x, 'y':y, 'fdup': fdup, 'partenaire': partenaire})
      else:
        return render(request,"tableau/contrat2.html",{'formP': formP,'formF': formF, 'x':x, 'y':y, 'fdup': fdup, 'partenaire': partenaire})
    else:
      return render(request, 'general/error.html')




def update_accord(request, c): 
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= AccordForm()
      accord = Accord.objects.all()
      if (c !='0'):
         x = Accord.objects.get(code=c)
         if request.method == 'POST':
          form = AccordForm(request.POST, request.FILES, instance=x)
          if form.is_valid():
              form.save()
              messages.success(request, "Accord modifié avec succès!")
         else:
          form = AccordForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tableaccord.html", {'form': form, 'x':x, 'accord': accord})
      else:
        return render(request,"tableau/tableaccord.html", {'form': form, 'x':x, 'accord': accord}) 
    else:
      return render(request, 'general/error.html')  

def update_convention(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= ConventionDeDetachementForm()
      convention = ConventionDeDetachement.objects.all()
      if (c !='0'):
         x = ConventionDeDetachement.objects.get(code=c)
         if request.method == 'POST':
          form = ConventionDeDetachementForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
             form.save()
             messages.success(request, "Convention modifiée avec succès!")
         else:
          form = ConventionDeDetachementForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tableconvention.html", {'form': form, 'x':x,'convention': convention})
      else:
        return render(request, "tableau/tableconvention.html", {'form': form, 'x':x,'convention': convention}) 
    else:
      return render(request, 'general/error.html')  

def update_avenant(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= AvenantForm()
      avenant = Avenant.objects.all()
      if (c !='0'):
         x = Avenant.objects.get(code=c)
         if request.method == 'POST':
          form = AvenantForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
            form.save()
            messages.success(request, "Avenant modifié avec succès!")
         else:
           form = AccordForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tableavenant.html", {'form': form, 'x':x,'avenant': avenant})
      else:
        return render(request, "tableau/tableavenant.html", {'form': form, 'x':x,'avenant': avenant}) 
    else:
      return render(request, 'general/error.html')  
  

def update_lettreAccord(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= LettreAccordForm()
      lettreAccord = LettreAccord.objects.all()
      if (c !='0'):
         x = LettreAccord.objects.get(code=c)
         if request.method == 'POST':
          form = LettreAccordForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
            form.save()
            messages.success(request, "Lettre accord modifiée avec succès!")
         else:
          form = LettreAccordForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tablelettreaccord.html", {'form': form, 'x':x,'lettreAccord': lettreAccord})
      else:
        return render(request, "tableau/tablelettreaccord.html", {'form': form, 'x':x,'lettreAccord': lettreAccord}) 
    else:
      return render(request, 'general/error.html')  

def update_accordOp(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= AccordOperationForm()
      accordOp = AccordOperation.objects.all()
      if (c !='0'):
         x = AccordOperation.objects.get(code=c)
         if request.method == 'POST':
          form = AccordOperationForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
            form.save()
            messages.success(request, "Accord d'opérations modifié avec succès!")
         else:
          form = AccordOperationForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tableaccordoperation.html", {'form': form, 'x':x,'accordOp': accordOp})
      else:
        return render(request, "tableau/tableaccordoperation.html", {'form': form, 'x':x,'accordOp': accordOp}) 
    else:
      return render(request, 'general/error.html')  

def update_avis(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= AvisJuridiqueForm()
      avis = AvisJuridique.objects.all()
      if (c !='0'):
         x = AvisJuridique.objects.get(code=c)
         if request.method == 'POST':
          form = AvisJuridiqueForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
            form.save()
            messages.success(request, "Accord modifié avec succès!")
         else:
          form = AvisJuridiqueForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tableavisjuridique.html", {'form': form, 'x':x,'avis': avis})
      else:
        return render(request, "tableau/tableavisjuridique.html", {'form': form, 'x':x,'avis': avis}) 
    else:
      return render(request, 'general/error.html')  

def update_pds(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= PointDeSituationForm()
      pds = PointDeSituation.objects.all()
      if (c !='0'):
         x = PointDeSituation.objects.get(code=c)
         if request.method == 'POST':
          form = PointDeSituationForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
            form.save()
            messages.success(request, "Point de situation modifié avec succès!")
         else:
          form = PointDeSituationForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tablepds.html", {'form': form, 'x':x,'pds': pds})
      else:
        return render(request, "tableau/tablepds.html", {'form': form, 'x':x,'pds': pds}) 
    else:
      return render(request, 'general/error.html')  

def update_st(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= SoitTransmisForm()
      st = SoitTransmis.objects.all()
      if (c !='0'):
         x = SoitTransmis.objects.get(num_st=c)
         if request.method == 'POST':
          form = SoitTransmisForm(request.POST,request.FILES, instance=x)
          if form.is_valid():
            form.save()
            messages.success(request, "Soit transmis modifié avec succès!")
         else:
          form = SoitTransmisForm(instance=x)
      if current_user.is_chefdep:
        return render( request,"chefdep/tableau/tablest.html", {'form': form, 'x':x,'st': st})
      else:
        return render(request, "tableau/tablest.html", {'form': form, 'x':x,'st': st}) 
    else:
      return render(request, 'general/error.html')  

def update_contrat(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      x=[]
      aj=[]
      pds=[]
      ac=[]
      acop=[]
      cov=[]
      la=[]
      av=[]
      form= ContratForm()
      contrat = Contrat.objects.all()
      if (c !='0'):
         aj=AvisJuridique.objects.filter(contrat=c)
         pds=PointDeSituation.objects.filter(contrat=c)
         ac=Accord.objects.filter(contrat=c)
         acop=AccordOperation.objects.filter(contrat=c)
         cov=ConventionDeDetachement.objects.filter(contrat=c)
         la=LettreAccord.objects.filter(contrat=c)
         av=Avenant.objects.filter(contrat=c)
    
         x = Contrat.objects.get(code=c)
         if request.method == 'POST':
             form = ContratForm(request.POST, instance=x)
             if form.is_valid():
                form.save()
                messages.success(request, "Contrat modifié avec succès!")
         else:
          form = ContratForm(instance=x)
      if current_user.is_chefdep:
        return render(request,"chefdep/tableau/tablecontrat.html", {'form': form, 'x':x,'contrat': contrat,
           'aj':aj, 'pds':pds, 'ac':ac, 'acop':acop,
           'cov':cov, 'la':la, 'av':av})
      else:
        return render(request,"tableau/tablecontrat.html", {'form': form, 'x':x,'contrat': contrat,
           'aj':aj, 'pds':pds, 'ac':ac, 'acop':acop,
           'cov':cov, 'la':la, 'av':av}) 
    else:
      return render(request, 'general/error.html')  

def update_user(request, u):
    if request.user.is_authenticated:
      current_user = request.user
      x=0
      form= ContratForm()
      User = get_user_model()
      users = User.objects.all()
      if (u !='0'):
         x = User.objects.get(username=u)
         if request.method == 'POST':
             form = UserForm(request.POST, instance=x)
             print(form)
             if form.is_valid():
                form.save()
                messages.success(request, "Utilisateur modifié avec succès!")
         else:
             form = UserForm(instance=x)
      if current_user.is_admin:
        return render( request,"general/users.html", {'form': form, 'x':x, 'users': users})
      else:
        return render(request, 'general/error.html') 
    else:
      return render(request, 'general/error.html')  
   

#*************************************
#***************Suppression***********
def delete_partenaire(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        partenaire = Partenaire.objects.get(code=c) 
        partenaire.delete()
        print("hey")
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_partenaire_fdup, '0')
    else:
      return render(request, 'general/error.html')  
    

def delete_fdup(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        fdup = FinancementDuPartenaire.objects.get(code=c) 
        fdup.delete()
        print("heyhey")
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_partenaire_fdup, '0')
    else:
      return render(request, 'general/error.html') 

def delete_accord(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        accord = Accord.objects.get(code=c) 
        accord.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_accord, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_convention(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        convention = ConventionDeDetachement.objects.get(code=c) 
        convention.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_convention, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_avenant(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        avenant = Avenant.objects.get(code=c) 
        avenant.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_avenant, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_lettreAccord(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        lettreAccord = LettreAccord.objects.get(code=c) 
        lettreAccord.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_lettreAccord, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_accordOp(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        accordOp = AccordOperation.objects.get(code=c) 
        accordOp.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_accordOp, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_avis(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        avis = AvisJuridique.objects.get(code=c) 
        avis.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_avis, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_pds(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        pds = PointDeSituation.objects.get(code=c) 
        pds.delete()
        messages.success(request, 'Suppression du point de situation effectuée avec succés')
        return redirect(update_pds, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_st(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else: 
        st = SoitTransmis.objects.get(num_st=c) 
        st.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_st, '0')
    else:
      return render(request, 'general/error.html') 
    

def delete_contrat(request, c):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:
        contrat = Contrat.objects.get(code=c) 
        contrat.delete()
        messages.success(request, 'Suppression effectuée avec succés')
        return redirect(update_contrat, '0')
    else:
     return render(request, 'general/error.html') 

def delete_user(request, u):
    if request.user.is_authenticated:
      current_user = request.user
      if current_user.is_chefdep:
        return render( request,'general/error.html')
      else:  
       User = get_user_model()
       user = User.objects.get(username=u) 
       user.delete()
       messages.success(request, 'Suppression effectuée avec succés')
       return redirect(update_user, '0')
    else:
      return render(request, 'general/error.html') 
    