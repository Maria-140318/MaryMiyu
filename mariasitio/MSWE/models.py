from django.db import models
# Create your models here.
#model django with table mysql
class empresa(models.Model):
    EmpresaId=models.AutoField(db_column='EmpresaId', primary_key=True, blank=False)
    Nombre=models.CharField(db_column='Nombre', max_length=50, blank=False)
    Fecha = models.DateField(db_column='Fecha', blank=False, )
    Tipo= models.CharField(db_column='Tipo', max_length=14,blank=False,null=True)
    Comentarios=models.CharField(db_column='Comentarios', max_length=1020, blank=True)
    Favorita=models.BooleanField(db_column='Favorita',blank=True)
    class Meta:
        managed = False
        db_table = 'empresa'