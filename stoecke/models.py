from django.db import models

# Create your models here.

class Stoecke(models.Model):
    COLONY_TYPES = [
            ("W", "Wirtschaftsvolk"),
            ("A", "Ableger"),
            ("J", "Jungvolk"),
            ("S", "Schwarm"),
            ("F", "Flugling"),
        ]
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    colony_type = models.CharField(max_length=1, choices=COLONY_TYPES)
    date_created = models.DateField()
    date_queen_added = models.DateField()
    queen_color = models.CharField(max_length=20)
    queen_number = models.IntegerField()
    bee_race = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock_detail', args=[str(self.id)])

