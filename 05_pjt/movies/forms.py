from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        label_suffix= ' ',
        widget = forms.TextInput(
            attrs = {
                'class': 'movie_title form-control',
                'placeholder': 'Title',
                'maxlength': 20,
            }
        )        
    )

    audience = forms.IntegerField(
        label='Audience',
        label_suffix= ' ',
        widget = forms.NumberInput( #TextInput으로 할지 고민
            attrs = {
                'class': 'movie_audience form-control', # form control: 줄바꾸고 자동으로 만들어줌
                'placeholder': 'Audience',
            }
        )        
    )

    release_date = forms.DateField(
        # label='Release date',
        # label_suffix= ' ',
        #input_formats=['%Y-%m-%d'],
        widget = forms.DateInput(
                        # format = '%Y-%m-%d',
            attrs = {
                # 'class': 'movie_release_date form-control',
                'type': 'date',
            }
        )        
    )

    genre_list = [('comedy','코미디'), ('romance','로맨스'), ('horor','공포')]
    genre = forms.CharField(
        label='Genre',
        label_suffix= ' ',
        widget = forms.Select(
            choices= genre_list,
            attrs = {
                'class': 'Genre form-control',                
            }
        )        
    )

    score = forms.FloatField(
        label='Score',
        label_suffix= ' ',
        widget = forms.NumberInput(
            attrs = {
                'class': 'movie_score form-control',
                'step': 0.5,
                'min': 0.0,
                'max': 5.0,
                'placeholder': 'Score',
            }
        )        
    )

    poster_url = forms.CharField(
        label='Poster_url',
        label_suffix= ' ',
        widget = forms.Textarea(
            attrs = {
                'class': 'movie_poster_url form-control',
                'placeholder': 'Poster_url',
            }
        )        
    )

    description = forms.CharField(
        label='Description',
        label_suffix= ' ',
        widget = forms.Textarea(
            attrs = {
                'class': 'movie_description form-control',
                'placeholder': 'Description',
            }
        )        
    )
    
    class Meta:
        model = Movie
        fields = '__all__'