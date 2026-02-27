from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control con-validate',
                'id': 'contact-name',
                'placeholder': 'نام',
                'minlength': 3
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control con-validate',
                'id': 'contact-email',
                'placeholder': 'ایمیل'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control con-validate',
                'id': 'contact-message',
                'placeholder': 'چگونه ما میتوانیم به شما کمک کنیم؟',
                'rows': 6
            }),
        }