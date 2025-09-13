from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'url', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': (
                    'peer w-full rounded-lg border border-gray-300 bg-gray-50 px-4 pt-5 pb-2 text-gray-900 '
                    'placeholder-transparent focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 '
                    'focus:outline-none transition-all'
                ),
                'placeholder': 'Enter a name for your link'
            }),
            'url': forms.URLInput(attrs={
                'class': (
                    'peer w-full rounded-lg border border-gray-300 bg-gray-50 px-4 pt-5 pb-2 text-gray-900 '
                    'placeholder-transparent focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 '
                    'focus:outline-none transition-all'
                ),
                'placeholder': 'Enter the URL to shorten'
            }),
            'slug': forms.TextInput(attrs={
                'class': (
                    'peer w-full rounded-lg border border-gray-300 bg-gray-50 px-4 pt-5 pb-2 text-gray-900 '
                    'placeholder-transparent focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 '
                    'focus:outline-none transition-all'
                ),
                'placeholder': 'Custom slug (optional)'
            }),
        }
        labels = {
            'name': 'Link Name',
            'url': 'Original URL',
            'slug': 'Custom Slug (Optional)',
        }
        
        """help_texts = {
            'name': 'A unique name for your shortened link.',
            'url': 'The original URL you want to shorten.',
            'slug': 'Optional: a custom short URL ending.',
        }"""
