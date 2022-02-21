from socket import forms

class EmailPostForms(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmaiField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


