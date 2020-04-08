from django import forms
from .models import *

class CafeCreateForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Cafe
        fields = ("title",
                  "address",
                  "city",
                  "phone",
                  "email",
                  "content",
                  "date_posted",
                  "image")


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields = ("comment",)


class CafeUpdateForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ("title",
                  "address",
                  "city",
                  "phone",
                  "email",
                  "content",
                  "date_posted",
                  "image")
