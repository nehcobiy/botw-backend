from django.db import models

class IngredientManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Ingredient(models.Model):
    category = models.CharField(max_length=200)
    duration = models.CharField(max_length=200, null=True, blank=True)
    effect = models.CharField(max_length=200, null=True, blank=True)
    hearts = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    resale = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    objects = IngredientManager()

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_name')]

    def __str__(self):
        return self.name

class Recipe(models.Model):
    category = models.CharField(max_length=200)
    duration = models.CharField(max_length=200, null=True, blank=True)
    hearts = models.CharField(max_length=200)
    ingredient1 = models.ForeignKey(Ingredient, related_name="i1", on_delete=models.CASCADE)
    ingredient2 =  models.ForeignKey(Ingredient, related_name="i2", on_delete=models.CASCADE, null=True, blank=True)
    ingredient3 = models.ForeignKey(Ingredient, related_name="i3", on_delete=models.CASCADE, null=True, blank=True)
    ingredient4 = models.ForeignKey(Ingredient, related_name="i4", on_delete=models.CASCADE, null=True, blank=True)
    ingredient5 = models.ForeignKey(Ingredient, related_name="i5", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=500, null=True, blank=True)
    resale = models.CharField(max_length=200)
    strength = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200)
    image = models.CharField(max_length=500, null=True, blank=True)
    type_image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name




