from django import forms

class ImageForm(forms.Form):
    id = forms.IntegerField(min_value=1, max_value=100, widget=forms.NumberInput(attrs={'class':'form-control'}))
    image = forms.ImageField()


