from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    nombre_completo = forms.CharField(max_length=100, label='Nombre Completo')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.nombre_completo = self.cleaned_data['nombre_completo']
        user.save()
        return user