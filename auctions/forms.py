from django import forms

class newListingForm(forms.Form):
    title = forms.CharField(label = 'Title: ', max_length = 64)
    description = forms.CharField(label = 'Description: ', max_length = 1024)
    price = forms.IntegerField(label='Price in Dollars: ')
    image_url = forms.CharField(label='Image URL: ', max_length = 1024)