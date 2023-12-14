from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.id};" \
               f" {self.name};" \
               f" {self.image};" \
               f" {self.price};" \
               f" {self.release_date};" \
               f" {self.lte_exists};" \
               f" {self.slug}"