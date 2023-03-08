from django import forms


class Search(forms.Form):
    intitle = forms.CharField(max_length=100, required=True)
    inauthor = forms.CharField(max_length=100, blank=True, null=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['title'].widget.attrs['class'] = 'input'
