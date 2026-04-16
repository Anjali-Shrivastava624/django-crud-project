from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )


class Meta:
    model = User
    fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Already registered with this email address!")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken!")
        return username


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "course", "gender", "phone"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Student Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter Email"}
            ),
            "age": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Age"}
            ),
            "course": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Course Name"}
            ),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone Number"}
            ),
        }
