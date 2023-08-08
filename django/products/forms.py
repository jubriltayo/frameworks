from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    # This section is not needed, it only shows the default setup can be overwritten
    title       = forms.CharField(label='', # make label disappear
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Your title"
                                      }
                                  ))
    description = forms.CharField(required=False,# make field not compulsory
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Your description",
                                          "id": "my-id-for-text-area",
                                          "class": "new-class-name two",
                                          "rows": 20,
                                          "cols": 120
                                      }
                                  ))
    email = forms.EmailField()
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        """Method to check title input if it contains certain chars of interest
        majorly used in emails"""
        title = self.cleaned_data.get("title")
        # if not "CFE" in title:
        #     raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_email(self, *args, **kwargs):
        """Method to check title input if it contains certain chars of interest
        majorly used in emails"""
        email = self.cleaned_data.get("email")
        # if not email.endswith("edu"):
        #     raise forms.ValidationError("This is not a valid email")
        return email

class RawProductForm(forms.Form):
    """Pure django form"""
    title       = forms.CharField(label='', # make label disappear
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Your title"
                                      }
                                  ))
    description = forms.CharField(required=False,# make field not compulsory
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Your description",
                                          "id": "my-id-for-text-area",
                                          "class": "new-class-name two",
                                          "rows": 20,
                                          "cols": 120
                                      }
                                  )) 
    price       = forms.DecimalField(initial=20.00) # preset initial value
