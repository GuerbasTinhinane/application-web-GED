from django.contrib import admin
from .models import User
from user.models import Documents
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
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(User)
admin.site.register(Documents)

admin.site.register(Contrat, SimpleHistoryAdmin) 
admin.site.register(SoitTransmis, SimpleHistoryAdmin)
admin.site.register(PointDeSituation, SimpleHistoryAdmin)
admin.site.register(AvisJuridique, SimpleHistoryAdmin)
# admin.site.register(Partenaire, SimpleHistoryAdmin)
admin.site.register(FinancementDuPartenaire, SimpleHistoryAdmin)
# DocumentContractuel est une classe abstraite
admin.site.register(AccordOperation, SimpleHistoryAdmin)
admin.site.register(Accord, SimpleHistoryAdmin)
admin.site.register(LettreAccord, SimpleHistoryAdmin)
admin.site.register(Avenant, SimpleHistoryAdmin)
admin.site.register(ConventionDeDetachement, SimpleHistoryAdmin)

class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('pays', 'latitude', 'longitude', 'code', 'nom_partenaire')

admin.site.register(Partenaire, PartenaireAdmin)