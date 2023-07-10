from django import forms
from .models import Demands
from random import choice, seed, randint
from django.core.exceptions import ValidationError


class DemandForm(forms.ModelForm):

    seed()
    a = randint(1, 99)
    b = randint(1, 99)
    c = choice(["+", "-"])
    match c:
        case "+":
            res = a + b
        case "-":
            res = a - b
    example = str(a) + c + str(b) + '='

    demand_client = forms.CharField(label="Ваша организация, или, если вы частное лицо, напишите: частное лицо",
                                    max_length=50, help_text="(максисмум 50 знаков)", strip=True,
                                   widget=forms.widgets.TextInput(attrs={'cols': 50, 'rows': 1}),
                                   error_messages={'required': 'Напишите вашу организацию или "частное лицо"',
                                                   'max_length': 'Название не должно превышать 50 знаков!'})

    demand_address = forms.CharField(label="Ваш адрес:",
                                    max_length=80, help_text="(максисмум 50 знаков)", strip=True,
                                   widget=forms.widgets.TextInput(attrs={'cols': 80, 'rows': 1}),
                                   error_messages={'required': 'Укажите ваш адрес."',
                                                   'max_length': 'Адрес не должен превышать 80 знаков!'})

    demand_type = forms.CharField(label='Вид заявки:', max_length=25,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'cols': 25, 'rows': 1}),
                                   error_messages={'required': 'Введите номер вашего телефона или ваш e-mail.'})

    demand_tech = forms.CharField(label='Модель аппарата:', max_length=30,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size': 30}),
                                   error_messages={'required': 'Введите модель аппарата.'})

    demand_serial = forms.CharField(label='Серийный номер:', max_length=25, required=False, help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}),)

    demand_description = forms.CharField(label='Опишите признаки неисправности:', max_length=255, required=False,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':255}),
                                   error_messages={'required': 'Введите признаки неисправности.'})

    demand_telephone = forms.CharField(label='Ваш телефон:', max_length=12, help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}),
                                   error_messages={'required': 'Введите номер вашего телефона.'})

    demand_fio = forms.CharField(label='Ваше имя (желательно фамилия, имя, отчество:', max_length=50, help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size': 50}),
                                   error_messages={'required': 'Введите ваше имя.'})

    demand_email = forms.CharField(label='Ваш e-mail:', max_length=100, help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}),
                                   error_messages={'required': 'Введите ваш e-mail.'})

    not_robot = forms.BooleanField(label="Подтвердите, что вы не робот:", help_text="",
                                   widget=forms.widgets.CheckboxInput(),
                                   error_messages={'required': 'Вы не подтвердили, что вы не робот.'})

    captcha_example = forms.CharField(label="", label_suffix='',disabled=True, required=False,
                                      widget=forms.widgets.TextInput(attrs={'size': 4, 'value': example}))

    captcha_entrance = forms.CharField(label='', help_text='', widget=forms.widgets.TextInput(),
                                       error_messages={'required': 'Введите решение несложного примера.'})

    captcha_result = forms.CharField(label='', help_text='', widget=forms.widgets.TextInput(attrs={'value': str(res)}))

    class Meta:
        model = Demands
        fields = ('demand_client', 'demand_address', 'demand_type', 'demand_tech', 'demand_serial', 'demand_description', 'demand_telephone', 'demand_fio', 'demand_email', 'not_robot','captcha_example',
                  'captcha_entrance', 'captcha_result')

    def _clean_not_robot(self):
        if 'not_robot' not in self.cleaned_data.keys() or not self.cleaned_data['not_robot']:
            raise ValidationError('Вы не подтвердили, что вы не робот.')
        return None

    def _clean_captcha_entrance(self):
        if 'captcha_entrance' not in self.cleaned_data.keys() or self.cleaned_data['captcha_entrance'] != self.cleaned_data['captcha_result']:
            raise ValidationError('Ваше решение несложного примера неверно')
        return None