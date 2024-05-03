from django.forms import ModelForm
from .models import Movies_list, Movies_pics

class Movies_form(ModelForm) :
    class Meta :
        model = Movies_list
        fields = "__all__"

class Movie_pic_form (ModelForm) :
    class Meta :
        model = Movies_pics
        fields = "__all__"