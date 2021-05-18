from django import forms
from django.contrib.auth import get_user_model,authenticate

User=get_user_model()

class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            user=authenticate(username=username,password=password)
            print("authenticated")
            if not user:
                raise forms.ValidationError("The user does not Exist")
                print("error 1")
            if not user.check_password(password):
                raise forms.ValidationError("Password Entered it Is In Incorrect")
                print("error 2")
            
        return super(UserLoginForm,self).clean(*args,**kwargs)



class UserRegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    first_name=forms.CharField(widget=forms.TextInput())
    last_name=forms.CharField(widget=forms.TextInput())
    email=forms.EmailField(widget=forms.TextInput())
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        cleaned_data=self.cleaned_data
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if (password1 != password2):
            raise forms.ValidationError("PASSWIRD DOES NOT MATCH")
        return cleaned_data

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("USERBANE EXISTS FOR ANOTHER ACCOUNT")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("EMAIL EXISTS")
        return email


