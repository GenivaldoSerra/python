from django.db import models
from datetime import date

# Create your models here.


class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name="Descrição", max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(verbose_name="Data de Entrega", null=False, blank=False)
    finished_at = models.DateField(null=True, blank=True)


    class Meta:
        ordering = ["deadline"]
        
    def mark_has_completed(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()