# pylint: disable=no-member
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Administrador(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,
                              unique=True)
    telefone = models.CharField(max_length=15,
                                unique=True,
                                help_text="(XX)XXXXX-XXXX")
    dataNascimento = models.DateTimeField(verbose_name="Data de Nascimento")
    documento = models.CharField(max_length=14,
                                 unique=True,
                                 help_text="Insira seu CPF")
    senha = models.CharField(max_length=50)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.telefone}"


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

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return f"[#{self.id}] ({self.nome} - {self.documento})"


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,
                              unique=True)
    telefone = models.CharField(max_length=15,
                                unique=True,
                                help_text="(XX)XXXXX-XXXX")
    dataNascimento = models.DateTimeField(verbose_name="Data de Nascimento")
    documento = models.CharField(max_length=14,
                                 unique=True,
                                 help_text="Insira seu CPF")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=50,verbose_name="UF")
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=50, verbose_name="Número")
    senha = models.CharField(max_length=50)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] ({self.nome} - {self.telefone})"


class Marca(models.Model):
    nome = models.CharField(max_length=80)
    pais = models.CharField(max_length=50, verbose_name="País")

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] ({self.nome} - {self.pais})"


class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] ({self.nome} - {self.marca.nome})"


class Moto(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    dataFabricacao = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    preco = models.FloatField(verbose_name="Preço Unitário")

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] ({self.modelo.nome} - {self.preco})"


class Venda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    valor = models.FloatField(default=0.0)
    dataVenda = models.DateTimeField(auto_now_add=True)

    # cadastrado por
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] ({self.cliente.nome} - {self.valor})"
    
    def delete(self, *args, **kwargs):
        # First, delete associated MotoVenda records.
        MotoVenda.objects.filter(venda=self.id).delete()
        # Call the parent class' delete method to delete the Venda.
        super().delete(*args, **kwargs)


class MotoVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT)
    moto = models.ForeignKey(Moto, on_delete=models.PROTECT)
    preco = models.FloatField(verbose_name="Preço Unitário")
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.moto.modelo.nome} - {self.moto.preco}"


class Carrinho(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)

    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] ({self.moto.modelo.nome} - {self.quantidade})"
