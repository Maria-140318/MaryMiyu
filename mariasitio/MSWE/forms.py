from django import forms
from MSWE.models import empresa

class empresaform(forms.ModelForm):
    class Meta:
        model = empresa
        fields = [
            'EmpresaId',
            'Nombre',
            'Fecha',
            'Tipo',
            'Comentarios',
            'Favorita',
        ]
        OPTIONS = [
        ('Distribuidores', 'Distribuidores'),
        ('Mayorista', 'Mayorista'),
        ('Usuario Final', 'Usuario Final'),
    ]
        labels = {
            
            'EmpresaId': 'Empresa' ,
            'Nombre':'Nombre' ,
            'Fecha': 'Fecha',
            'Tipo': 'Tipo',
            'Comentarios': 'Comentarios',
            'Favorita':'Favorita',
        }
        #
        widgets = {
            'EmpresaId':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Fecha':forms.SelectDateWidget(years=range(1000, 3000)),
            'Tipo': forms.Select(choices=OPTIONS,attrs={'class':'form-control'}),
            'Comentarios':forms.TextInput(attrs={'class':'form-control'}),
            #'Favorita':forms.CheckboxInput(attrs='class':'form-control'),
            #'Favorita':forms.BooleanField(required=True),
            #'Favorita':forms.BooleanField(wid=forms.CheckboxInput({'class': 'my-checkbox-class'})),
            #'Favorita':forms.BooleanField( widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class', 'id': 'accept-terms'}))                     
        }
