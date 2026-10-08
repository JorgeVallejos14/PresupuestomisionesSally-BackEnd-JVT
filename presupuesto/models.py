from django.db import models

# Create your models here.
class Mision(models.Model):
    nombre = models.CharField(max_length=100)
    lider = models.CharField(max_length=60)
    zona = models.CharField(max_length=60)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Gasto(models.Model):
    mision = models.ForeignKey(
        Mision,
        on_delete=models.PROTECT,
        related_name='gastos',
    )
    concepto = models.CharField(max_length=120)
    categoria = models.CharField(max_length=40)
    registrado = models.DateField(auto_now_add=True)
    monto = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.concepto} - {self.mision}"