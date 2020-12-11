from django import forms
from mainapp.models import Speciality, Group, Student
from user_auth.models import User

from django.contrib.auth import password_validation

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SpecialityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'





class StudentUserForm(forms.ModelForm):
    password_help_text = '''
            Ваш пароль не может быть слишком похож на вашу другую личную информацию. <br>
            Ваш пароль должен содержать как минимум 8 символов.<br>
            Ваш пароль не может быть обычным паролем.<br>
            Ваш пароль не может быть полностью числовым.<br>
            '''
    error_messages = {
        'password_mismatch': 'Два поля пароля не совпадают.',
    }
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_help_text,
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Введите тот же пароль, что и раньше, для проверки.",
    )

    group = forms.ChoiceField(label='Группа',choices=[(group.pk, group) for group in Group.objects.all()])
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'city', 'phone', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    def __init__(self, *args, **kwargs):
        super(StudentUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        group = Group.objects.get(id=self.cleaned_data['group'])
        Student.objects.create(user=user, group=group)
        return user