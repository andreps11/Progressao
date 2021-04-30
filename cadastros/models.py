from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
# class Categoria(models.Model):
    
#     nome = models.CharField(
#         max_length=50, choices=NOME_CHOICES, default="Selecione")

#     class Meta:
#         verbose_name_plural = 'Categorias'

#     def __str__(self):
#         return self.name


# class Produto(models.Model):
#     nome = models.CharField(max_length=50)
#     usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="usuário")
#     quantidade = models.IntegerField(default=1)
#     preco = models.DecimalField(max_digits=20, decimal_places=2)

#     CATEGORIA_PRODUTO = (
#         ('Verdura', 'Verdura'),
#         ('Fruta', 'Fruta'),
#         ('Hortaliça', 'Hortaliça'),
#     )

#     categoria = models.CharField(max_length=50, choices=CATEGORIA_PRODUTO)

#     class Meta:
#         verbose_name_plural = "Produtos"

#     def __str__(self):
#         return "{} - R${}, quantidade: {}, Vendedor: {}".format(self.nome, self.preco, self.quantidade, self.usuario)


    # def save(self, *args, **kwargs):
    #     print(self.pk)
    #     is_new = self.pk is None
    #     print(is_new)
    #     if is_new:
    #         print("Entrou")
    #         super(Produto, self).save()
    #         # self.slug = '%s-%i' % (slugify(self.nome), self.id)
    #         print('%s-%i' % (slugify(self.nome), self.id))
    #     super(Produto, self).save(*args, **kwargs)



# class Estado(models.Model):
#     nome = models.CharField(max_length=50)
#     uf = models.CharField(max_length=2, verbose_name='UF')

#     def __str__(self):
#         return "{}".format(self.nome)


# class Cidade(models.Model):
#     nome = models.CharField(max_length=50)
#     estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

#     def __str__(self):
#         return "{} - {}".format(self.nome, self.estado.uf)


# class Escola(models.Model):
#     nome = models.CharField(max_length=50)
#     cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
#     endereco = models.CharField(max_length=150, verbose_name="endereço")
#     telefone = models.CharField(max_length=15)

#     def __str__(self):
#         return "{} ({})".format(self.nome, self.cidade)



# class Vendedor(models.Model):
#     nome_completo = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=14, verbose_name="CPF")
#     telefone = models.CharField(max_length=15)
#     cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
#     # usuario = models.ForeignKey(
#     #     User, on_delete=models.PROTECT, verbose_name="usuário")

#     def __str__(self):
#         return "{}".format(self.nome_completo)


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=5)

    CATEGORIA_PRODUTO = (
        ('Verdura', 'Verdura'),
        ('Fruta', 'Fruta'),
        ('Hortaliça', 'Hortaliça'),
    )

    categoria = models.CharField(max_length=50, choices=CATEGORIA_PRODUTO)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} R${}, quantidade: {}, categoria: {}".format(self.nome, self.preco, 
            self.quantidade, self.categoria)
