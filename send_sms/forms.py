from django import forms


class MessageForm(forms.Form):
    file = forms.FileField(label='Upload a CSV file', widget=forms.FileInput(attrs={
        'class': 'form-control',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
    }))

    def clean_file(self):
        file_name = self.cleaned_data.get('file').name
        if not file_name.endswith('.csv'):
            raise forms.ValidationError('Sorry, CSV file is the only accepted!')
        return self.cleaned_data
