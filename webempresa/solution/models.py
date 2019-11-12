from django.db import models

# Create your models here.
#como una categoria de modelos del producto
class Recepmodel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
        ordering = ['-created']

    def __str__(self):
        return self.name
#class de las preguntas
class Query(models.Model):
    question = models.TextField(verbose_name="Pregunta")
    image = models.ImageField(null=True, blank=True, verbose_name="imagen", upload_to="solution")
    answer = models.TextField(verbose_name="Respuesta")
    recep_model = models.ForeignKey(Recepmodel, verbose_name="modelo", on_delete=models.CASCADE, null=True)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "pregunta"
        verbose_name_plural = "preguntas"
        ordering = ['-created']

    def __str__(self):
        return self.question



""""
/////////////Modelo de respuesta la idea era relacionar este modelo con las preguyntas y iterar cada respuesta a su 
////////////respectiva pregunta
class Answer(models.Model):
    answer = models.TextField(verbose_name="Respuesta")
    recep_model = models.ManyToManyField(Recepmodel, verbose_name="modelos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ['-created']

    def __str__(self):
        return self.answer
"""