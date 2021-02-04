from django.db import models

class Categoria(models.Model):
    nombre = models.CharField('Nombre de categoria', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField('Nombre del proyecto', max_length=100, blank=True, null=True)
    img_principal = models.ImageField(upload_to='principales/%Y/%m/%d', null=True, blank=True)
    ubicacion = models.CharField('Ubicacion', max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    arquitecto = models.CharField('Arquitecto',max_length=300, blank=True, null=True)
    descripcion = models.TextField('Memoria',blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'

    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,blank=True, null=True )
    img = models.ImageField(upload_to='imagenes/%Y/%m/%d', null=True)
    resumen = models.CharField('Explicacion',max_length=500, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.proyecto.nombre

    class Meta:
        verbose_name='Imagen'
        verbose_name_plural='Imagenes'
        ordering=['-id']

        
class Fofografia(models.Model):
    foto = models.ImageField(upload_to='fotos')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name='Foto'
        verbose_name_plural='Fotos'
        ordering=['-id']


    



    