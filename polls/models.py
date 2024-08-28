from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(("Pergunta"), max_length=200)
    pub_date = models.DateField("Data da Publicação")
    
    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

class CadClientes(models.Model):
    nome_cli = models.CharField(("Nome do Cliente"), max_length=80)
    doc_cli = models.CharField(("Documento"), max_length=20)
    fone_cli = models.CharField(("Telefone"), max_length=12)

