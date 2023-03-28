# pylint: disable=no-member
from django.db import models

# Create your models here.
class Administrador(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, 
                              unique=True)
    telefone = models.CharField(max_length=15, 
                                unique=True,  
                                help_text="(XX)XXXXX-XXXX")
    dataNascimento = models.DateField()
    documento = models.CharField(max_length=14, 
                                 unique=True,
                                 help_text="Insira seu CPF")
    senha = models.CharField(max_length=50)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - ({self.telefone})"


class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,
                              unique=True)
    telefone = models.CharField(max_length=15,
                                unique=True,
                                help_text="(XX)XXXXX-XXXX")
    documento = models.CharField(max_length=18,
                                 unique=True,
                                 help_text="Insira seu CNPJ")
    administrador = models.ForeignKey(Administrador, on_delete=models.PROTECT)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - ({self.documento})"


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, 
                              unique=True)
    telefone = models.CharField(max_length=15, 
                                unique=True,  
                                help_text="(XX)XXXXX-XXXX")
    dataNascimento = models.DateField()
    documento = models.CharField(max_length=14, 
                                 unique=True,
                                 help_text="Insira seu CPF")
    senha = models.CharField(max_length=50)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - ({self.telefone})"


class Marca(models.Model):
    nome = models.CharField(max_length=80)
    pais = models.CharField(max_length=50)
    status = models.IntegerField

    def __str__(self):
        return f"{self.nome} - ({self.pais})"


class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    status = models.IntegerField

    def __str__(self):
        return f"{self.nome} - ({self.marca.nome})"

class Moto(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    dataFabricacao = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField
    status = models.IntegerField
    preco = models.FloatField

    def __str__(self):
        return f"{self.modelo.nome} - ({self.preco})"

class Venda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete = models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    moto = models.ForeignKey(Moto, on_delete = models.PROTECT)
    dataVenda  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.moto.modelo.nome} - ({self.moto.preco})"