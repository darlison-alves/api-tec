from rest_framework import serializers
from .models import Computador, PlacaMae, Processador

class MontagemSerializer(serializers.HyperlinkedModelSerializer):
    processador = serializers.StringRelatedField()
    placa_mae = serializers.StringRelatedField()
    class Meta:
        model = Computador
        fields = ('id', 'url', 'processador', 'placa_mae', 'menoria_ram', 'placa_video')


class PlacaMaeSerializer(serializers.HyperlinkedModelSerializer):
    processadores = serializers.StringRelatedField(many= True)
    class Meta:
        model = PlacaMae
        fields = ('id','url','produto', 'processadores', 'qtd_slots_memoria_ram', 'total_memoria_ram_suportada', 'video_integrado')

class ProcessadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processador
        fields = ('id', 'url', 'produto','marca')