from django import forms
from myapp.models import BLogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BLogPost
        fields = "__all__"
