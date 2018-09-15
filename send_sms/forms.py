from django import forms


# def validate_file_extension(file):
#     print('ok')
#     if not file.name.endswith('.csv'):
#         print('Not CSV')
#         raise forms.ValidationError('Sorry, CSV file is only accepted')


class MessageForm(forms.Form):
    file = forms.FileField(label='Select a file', required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={
        "rows": 30,
        'cols': 120,
    }))

    def clean_file(self):
        file_name = self.cleaned_data.get('file').name
        if not file_name.endswith('.csv'):
            raise forms.ValidationError('Sorry, CSV file is the only accepted!')
        return self.cleaned_data