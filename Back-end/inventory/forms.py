from django import forms
from django.contrib.auth import authenticate
from inventory.models import Product
""" quand ce sera en mode api
from django.http import JsonResponse

def get_logged_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not authenticated"}, status=401)

    return JsonResponse({
        "id": request.user.id,
        "username": request.user.username,
        "role": request.user.role,
    })

"""
class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Identifiants incorrects")

            self.user = user  # on stocke l'utilisateur validé

        return cleaned_data
    
class productRegister(forms.ModelForm):
    

    class Meta:
        model = Product
        exclude = ('is_active')
        fields = ['name', 'reference', 'category', 'purchase_price', 'sale_price', 'alert_threshold']

