from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'photo',
            'difficulty',
            'reading_time',
            'category'
        )


        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title ...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description ...'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-control'
            }),
            'reading_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reading time ...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }


