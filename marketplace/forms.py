from django import forms
from .models import Job


languages = (
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend  Developer', 'Backend  Developer'),
        ('Android  Developer', 'Android  Developer'),
        ('Graphic Designer', 'Graphic Designer'),
        ('IOS Developer', 'IOS Developer'),
        ('Data Scientist', 'Data Scientist'),
    )

frameworks = (
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend  Developer', 'Backend  Developer'),
        ('Android  Developer', 'Android  Developer'),
        ('Graphic Designer', 'Graphic Designer'),
        ('IOS Developer', 'IOS Developer'),
        ('Data Scientist', 'Data Scientist'),
    )


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('posted_by', 'created', 'updated', 'position_filled',)


class SearchForm(forms.ModelForm):
    language = forms.ChoiceField(choices=languages)
    framework = forms.ChoiceField(choices=frameworks)

    class Meta:
        model = Job
        exclude = ('posted_by', 'created', 'updated', 'position_filled',)

