from django.db import models


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f'{self.rua}, {self.numero}'


class Cliente(models.Model):
    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Não Binário')
    )
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_PEDIDO = (
        ('R', 'Pedido realizado'),
        ('P', 'Em processamento'),
        ('E', 'Saiu para entrega'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos_cliente')
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_PEDIDO)
    produtos = models.ManyToManyField(Produto)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'Pedido {self.id} - cliente {self.cliente}'
