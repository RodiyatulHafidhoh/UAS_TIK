from django.forms import ModelForm
from untirta.models import Buku

class FormBuku(ModelForm):
    class meta:
        model = Buku 
        fields = '__all__'