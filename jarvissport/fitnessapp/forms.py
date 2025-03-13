from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import JarvisUser, Workout

class RegistrationForm(UserCreationForm):
  middle_name = forms.CharField(required=False, label="Отчество")
  GENDER_CHOICES = [
    ('male', 'Мужской'),
    ('female', 'Женский'),
  ]
  gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Пол")
  age = forms.IntegerField(required=False, label="Возраст", min_value=0)
  weight = forms.DecimalField(required=False, label="Вес (кг)", min_value=0, decimal_places=1)
  height = forms.DecimalField(required=False, label="Рост (см)", min_value=0, decimal_places=1)

  class Meta:
    model = JarvisUser
    fields = [
      'username', 'password1', 'password2',
      'first_name', 'last_name', 'middle_name',
      'gender', 'age', 'weight', 'height', 'email'
    ]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    #self.helper.add_input(Submit('submit', 'Зарегистрироваться'))

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Войти')) 
        # (Опционально, если хотите кнопку внутри самой формы)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = JarvisUser
        fields = ['first_name', 'last_name', 'middle_name', 'gender', 'age', 'weight', 'height', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))