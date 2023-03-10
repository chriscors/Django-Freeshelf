from django import forms
from .models import Resource


class SearchForm(forms.Form):
    intitle = forms.CharField(max_length=100, required=True)
    inauthor = forms.CharField(max_length=100, required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['title'].widget.attrs['class'] = 'input'


class SortForm(forms.Form):
    SORT_CHOICES = (('Newest Added', "Newest Added"),
                    ('Oldest Added', 'Oldest Added'),
                    ('Name', 'Name'))

    order = forms.ChoiceField(choices=SORT_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['order'].widget.attrs['onchange'] = 'this.form.submit()'


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'author', 'description', 'url', 'category']
