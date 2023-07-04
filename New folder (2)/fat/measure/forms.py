from django import forms

class BodyFatPredictionForm(forms.Form):
    density = forms.FloatField(label='Density')
    age = forms.IntegerField(label='Age')
    weight = forms.FloatField(label='Weight')
    height = forms.FloatField(label='Height')
    neck = forms.FloatField(label='Neck')
    chest = forms.FloatField(label='Chest')
    abdomen = forms.FloatField(label='Abdomen')
    hip = forms.FloatField(label='Hip')
    thigh = forms.FloatField(label='Thigh')
    knee = forms.FloatField(label='Knee')
    ankle = forms.FloatField(label='Ankle')
    biceps = forms.FloatField(label='Biceps')
    forearm = forms.FloatField(label='Forearm')
    wrist = forms.FloatField(label='Wrist')
