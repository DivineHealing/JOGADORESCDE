from django.contrib import admin
from .models import Personagem, ConjuntoArmadura, Elmo, Peitoral, Manoplas, Calcas, Botas, ConjuntoEquip  # Importe todos

admin.site.register(Personagem)
admin.site.register(ConjuntoArmadura)
admin.site.register(Elmo)
admin.site.register(Peitoral)
admin.site.register(Manoplas)
admin.site.register(Calcas)
admin.site.register(Botas)
admin.site.register(ConjuntoEquip)