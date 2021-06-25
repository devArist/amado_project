from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    image = models.FileField(upload_to='img')
    name = models.CharField(max_length=200, verbose_name='nom')
    price = models.FloatField(verbose_name='prix')
    description = models.TextField()
    brand = models.ForeignKey(
        'Brand', 
        verbose_name='marque',
        on_delete=models.CASCADE,
        related_name='products'
        )
    category = models.ForeignKey(
        'Category', 
        verbose_name='catégorie',
        on_delete=models.CASCADE,
        related_name='products'
        )
    colors = models.ManyToManyField("Color", verbose_name='couleur')
    date_add = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='date d\'ajout'
        )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='dernière modification'
        )
    status = models.BooleanField(default=True, verbose_name='disponible')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'produit'


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    date_add = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='date d\'ajout'
        )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='dernière modification'
        )
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'marque'


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    date_add = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='date d\'ajout'
        )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='dernière modification'
        )
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'catégorie'


class Color(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    date_add = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='date d\'ajout'
        )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='dernière modification'
        )
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'couleur'


class Discount(models.Model):
    value = models.IntegerField(
        verbose_name='valeur',
        validators=[MinValueValidator(0)]
        )
    date_add = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='date d\'ajout'
        )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='dernière modification'
        )
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'taux de réduction'


class Delivery(models.Model):
    value = models.IntegerField(
        verbose_name='valeur',
        validators=[MinValueValidator(0)]
        )
    date_add = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='date d\'ajout'
        )
    date_update = models.DateTimeField(
        auto_now=True,
        verbose_name='dernière modification'
        )
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'coût de livraison'
        verbose_name_plural = 'coûts de livraison'