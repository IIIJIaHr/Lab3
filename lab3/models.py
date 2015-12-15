from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Manufacture(models.Model):
    country = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        result = (
            u'{name} {country}'
        ).format(name=self.name, country=self.country)
        return result


class Category(models.Model):
    name = models.CharField(max_length=30)
    floor = models.IntegerField()

    def __unicode__(self):
        result = (
            u'{name}'
        ).format(name=self.name)
        return result


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    weight = models.IntegerField()
    manufacture = models.ForeignKey(Manufacture)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        result = (
            u'{name}'
        ).format(name=self.name)
        return result


class Recall(models.Model):
    text = models.TextField(max_length=200)
    user_id = models.ForeignKey(AUTH_USER_MODEL)
    product_id = models.ForeignKey(Product)

    def __unicode__(self):
        result = (
            u'{text}'
        ).format(text=self.text[:10])
        return result
