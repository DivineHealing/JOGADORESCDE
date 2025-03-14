# Import dos utilitarios
from lib.utilitarios import *
# 
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Personagem, ConjuntoArmadura, Elmo, Peitoral, Manoplas, Calcas, Botas
from .serializers import PersonagemSerializer, ConjuntoArmaduraSerializer, ElmoSerializer # ... e os outros

#def conjunto(request):
#    resultado = 0  # Inicializa a variável resultado
#
#    if request.method == 'POST':
#        form = ConjuntoForm(request.POST)
#        print(lvlup(191275200))
#        if form.is_valid():
#            pegar_atributos('Aryah Astaris', 'forca')
#            for i in range(1, 7):  # Itera de 1 a 6 (incluindo 6)
#                numero = form.cleaned_data.get(f'numero{i}', 0)  # Obtém o valor do campo
#                if numero is not None:  # Verifica se o valor é válido
#                    resultado += numero
#    else:
#        form = ConjuntoForm()
#
#    
#    return render(request, 'conjunto.html', {'form': form, 'resultado': resultado})

class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

class ConjuntoArmaduraViewSet(viewsets.ModelViewSet):
    serializer_class = ConjuntoArmaduraSerializer

    def get_queryset(self):
        personagem_id = self.kwargs['personagem_pk']
        return ConjuntoArmadura.objects.filter(personagem_id=personagem_id)

    def perform_create(self, serializer):
        personagem_id = self.kwargs['personagem_pk']
        personagem = Personagem.objects.get(pk=personagem_id)
        serializer.save(personagem=personagem)

class PecaArmaduraViewSet(viewsets.ModelViewSet):
    # serializer_class e queryset são definidos dinamicamente

    def get_queryset(self):
        conjunto_id = self.kwargs['conjunto_pk']
        tipo = self.kwargs['tipo']

        model_class = {
            'elmo': Elmo,
            'peitoral': Peitoral,
            'manoplas': Manoplas,
            'calcas': Calcas,
            'botas': Botas,
            'conjuntoEquip': ConjuntoEquip,
        }[tipo]

        return model_class.objects.filter(conjunto_id=conjunto_id)

    def get_serializer_class(self):
        tipo = self.kwargs['tipo']
        serializer_map = {
            'elmo': ElmoSerializer,
            'peitoral': PeitoralSerializer,
            'manoplas': ManoplasSerializer,
            'calcas': CalcasSerializer,
            'botas': BotasSerializer,
             'conjuntoEquip': ConjuntoEquipSerializer,
        }
        return serializer_map[tipo]

    def perform_create(self, serializer):
        conjunto_id = self.kwargs['conjunto_pk']
        conjunto = ConjuntoArmadura.objects.get(pk=conjunto_id)
        # O tipo *já está* no serializer, porque o usuário o selecionou no formulário
        serializer.save(conjunto=conjunto)