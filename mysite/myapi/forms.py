from django import forms
class CoordinatesForm(forms.Form):
    point1 = forms.CharField(max_length=50)
    point2 = forms.CharField(max_length=50)
    point3 = forms.CharField(max_length=50)
    point4 = forms.CharField(max_length=50)