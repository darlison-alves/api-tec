from django.db import models

class Processador(models.Model):
    produto = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    
    def __str__(self):
        return self.produto

    
class PlacaMae(models.Model):
    produto = models.CharField(max_length=200)
    processadores = models.ManyToManyField(Processador)
    qtd_slots_memoria_ram = models.IntegerField()
    total_memoria_ram_suportada = models.IntegerField()
    video_integrado = models.BooleanField()

    def __str__(self):
        return self.produto

class Computador(models.Model):
    
    processador = models.ForeignKey(Processador, on_delete=models.CASCADE)
    placa_mae = models.ForeignKey(PlacaMae, on_delete=models.CASCADE)
    menoria_ram = models.CharField(max_length=200)
    placa_video = models.CharField(max_length=200)

    