from django import forms


class SearchForm(forms.Form):
    origin = forms.CharField(max_length=72, label="Miejsce wylotu", min_length=3)
    destination = forms.CharField(max_length=72, label="Miejsce przylotu")
    departure_date = forms.DateField(label="Data wylotu", widget=forms.DateInput(attrs={'type': 'date'}))
    return_date = forms.DateField(label="Data przylotu", widget=forms.DateInput(attrs={'type': 'date'}))
