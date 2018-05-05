from django import forms


class PostForm(forms.Form):
    Course = forms.CharField()
    Tariff = forms.IntegerField()
