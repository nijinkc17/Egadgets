from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['review']
        widgets={
            'review':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your review'})
        }