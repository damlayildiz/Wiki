from django import forms

class searchForm(forms.Form):
    form = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    
class newPageForm(forms.Form):
    title = forms.CharField(label="Title", required = True, widget=forms.TextInput(
        attrs={'placeholder': 'New entry title', 'class':'col-sm-10','style':'bottom:1rem'}))
    text = forms.CharField(label="Content", required = True, widget=forms.Textarea(
        attrs={'placeholder': 'Enter the content here', 'class':'col-sm-10','style':'top:1rem'}))

class editPageForm(forms.Form):
    title = forms.CharField(label="Title", required = True, widget=forms.TextInput(
        attrs={'placeholder': 'New entry title', 'class':'col-sm-10','style':'bottom:1rem'}))
    text = forms.CharField(label="Content", required = True, widget=forms.Textarea(
        attrs={'placeholder': 'Enter the content here', 'class':'col-sm-10','style':'top:1rem'}))    
