from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

    def clean_file(self):
        file = self.cleaned_data['file']

        allowed_extensions = ['pdf', 'xlsx']

        extension = file.name.split('.')[-1].lower()

        if extension not in allowed_extensions:
            raise forms.ValidationError(
                'Разрешены только PDF и XLSX файлы.'
            )

        return file