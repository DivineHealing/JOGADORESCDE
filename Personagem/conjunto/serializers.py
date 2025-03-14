from rest_framework import serializers
from .models import Personagem, ConjuntoArmadura, Elmo, Peitoral, Manoplas, Calcas, Botas, ConjuntoEquip  # Importe todos os modelos

class PecaArmaduraSerializer(serializers.ModelSerializer):  # Serializer genérico
    class Meta:
        model = None  # Vai ser sobrescrito nas subclasses
        fields = '__all__'
        # read_only_fields = ('tipo',)  # O tipo *não* deve ser read_only, pois o usuário precisa selecioná-lo

class ElmoSerializer(PecaArmaduraSerializer):
    class Meta(PecaArmaduraSerializer.Meta):
        model = Elmo

class PeitoralSerializer(PecaArmaduraSerializer):
    class Meta(PecaArmaduraSerializer.Meta):
        model = Peitoral

class ManoplasSerializer(PecaArmaduraSerializer):  # Adicionei
    class Meta(PecaArmaduraSerializer.Meta):
        model = Manoplas

class CalcasSerializer(PecaArmaduraSerializer):  # Adicionei
    class Meta(PecaArmaduraSerializer.Meta):
        model = Calcas

class BotasSerializer(PecaArmaduraSerializer):  # Adicionei
    class Meta(PecaArmaduraSerializer.Meta):
        model = Botas
class ConjuntoEquipSerializer(PecaArmaduraSerializer):
    class Meta(PecaArmaduraSerializer.Meta):
      model = ConjuntoEquip

class ConjuntoArmaduraSerializer(serializers.ModelSerializer):
    # Use os serializers específicos para cada tipo de peça, não StringRelatedField
    elmos = ElmoSerializer(many=True, read_only=True)
    peitorais = PeitoralSerializer(many=True, read_only=True)
    manoplas = ManoplasSerializer(many=True, read_only=True)
    calcas = CalcasSerializer(many=True, read_only=True)
    botas = BotasSerializer(many=True, read_only=True)
    conjuntoEquip = ConjuntoEquipSerializer(many=True, read_only=True)

    class Meta:
        model = ConjuntoArmadura
        fields = '__all__'

class PersonagemSerializer(serializers.ModelSerializer):
    conjuntos = ConjuntoArmaduraSerializer(many=True, read_only=True)  # Lista os conjuntos do personagem

    class Meta:
        model = Personagem
        fields = '__all__'