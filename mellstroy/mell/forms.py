from django.forms import ModelForm
from .models import *

class QuoteForm(ModelForm):
    class Meta:
        model = Quotes
        fields = ['quote', 'author']
    
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    
class Q_CForm(ModelForm):
    class Meta:
        model = Quote_Category
        fields = ['quote', 'category']
    
class TagForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['name']
    
class Q_TForm(ModelForm):
    class Meta:
        model = Quote_Tag
        fields = ['quote', 'tag']