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
        return f"{self.nome} ({self.telefone})"


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
    senha = models.CharField(max_length=50)
    administrador = models.ForeignKey(Administrador, on_delete=models.PROTECT)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.documento})"
