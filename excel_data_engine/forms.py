from django import forms

class ExcelForm(forms.Form):
    name = forms.CharField(label="Nombre del Excel", widget=forms.TextInput(attrs={"class": "py-1.5 px-3 w-full [background:#212332] outline-none rounded-md focus:[outline-color:#605BFF] focus:outline-1 focus:outline-offset-0 transition-all", "placeholder":"Ejemplo: Mi primer hoja de Excel", "autocomplete":"off"}))
    url = forms.CharField(label="Url del Excel (Formato CSV)", widget=forms.TextInput(attrs={"class": "py-1.5 px-3 w-full [background:#212332] outline-none rounded-md focus:[outline-color:#605BFF] focus:outline-1 focus:outline-offset-0 transition-all", "placeholder":"Ejemplo: https://docs.google.com/spreadsheets/d/e/2PACX-1vTsguMxjTn6cgROHODYdLOhnDlEFjCOkglShKEtfvi27sn6dh3bQv1dJOcWtqAVXg/pub?output=csv", "autocomplete":"off"}))