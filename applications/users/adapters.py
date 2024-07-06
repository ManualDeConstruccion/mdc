from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super(MyAccountAdapter, self).save_user(request, user, form, False)
        data = form.cleaned_data
        user.nombre_completo = data.get('nombre_completo', '')
        user.save()
        return user