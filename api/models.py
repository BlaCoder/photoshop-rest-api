from django.db import models

class Imagem(models.Model):
    N_FEITO = 0
    FEITO = 1
    STATUS_OPCOES = (
        (N_FEITO, 'nao feito'),
        (FEITO, 'feito'),
    )

    usuario = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    ambiente = models.CharField(max_length=30)
    itens = models.CharField(max_length=10000)
    imagem = models.ImageField(default='placeholder.jpg')
    status = models.PositiveSmallIntegerField(choices=STATUS_OPCOES)

    def __str__(self):
        return self.codigo

    def nome_imagem(self):
        self.imagem = self.codigo + "_" + self.usuario + "_" + self.ambiente + ".jpg"

    def save(self, *args, **kwargs):
        self.nome_imagem()
        return super(Imagem, self).save(*args, **kwargs)