from django import forms
from .models import Comments
from random import choice, seed, randint
from django.core.exceptions import ValidationError
from django.core import validators


class CommentForm(forms.ModelForm):

    comment_text = forms.CharField(label="Ваш отзыв", max_length=1000, help_text="(максисмум 1000 знаков)",
                                   strip=True,
                                   widget=forms.widgets.Textarea(attrs={'cols': 100, 'rows': 10}))

    comment_sign = forms.CharField(label='Представьтесь, пожалуйста', max_length=100,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}))

    comment_contact = forms.CharField(label='Ваш телефон или e-mail', max_length=100,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}))

    not_robot = forms.BooleanField(label="Подтвердите, что вы не робот", help_text="",
                                   widget=forms.widgets.CheckboxInput())

    captcha = forms.IntegerField(label="2x2", label_suffix='=', widget=forms.widgets.TextInput(attrs={'size': 3}))

    class Meta:
        model = Comments
        fields = ('comment_text', 'comment_sign', 'comment_contact', 'not_robot', 'captcha')


class CommentForm2(forms.ModelForm):

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

    comment_text = forms.CharField(label="Ваш отзыв:", min_length=4, max_length=1000, help_text="(максисмум 1000 знаков)",
                                   strip=True,
                                   widget=forms.widgets.Textarea(attrs={'cols': 100, 'rows': 10}),
                                   error_messages={'required': 'Напишите текст отзыва.',
                                                   'min_length': 'Очень короткие отзывы не принимаются!',
                                                   'max_length': 'Отзыв не должен превышать 1000 знаков!'})

    comment_sign = forms.CharField(label='Представьтесь, пожалуйста:', max_length=100,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size': 100}),
                                   error_messages={'required': 'Вы не написали свое имя.'})

    comment_contact = forms.CharField(label='Ваш телефон или e-mail:', max_length=100,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}),
                                   error_messages={'required': 'Введите номер вашего телефона или ваш e-mail.'})

    not_robot = forms.BooleanField(label="Подтвердите, что вы не робот:", help_text="",
                                   widget=forms.widgets.CheckboxInput(),
                                   error_messages={'required': 'Вы не подтвердили, что вы не робот.'})

    captcha_example = forms.CharField(label="", label_suffix='',disabled=True, required=False,
                                      widget=forms.widgets.TextInput(attrs={'size': 4, 'value': example}))

    captcha_entrance = forms.CharField(label='', help_text='', widget=forms.widgets.TextInput(),
                                       error_messages={'required': 'Введите решение несложного примера.'})

    captcha_result = forms.CharField(label='', help_text='', widget=forms.widgets.TextInput(attrs={'value': str(res)}))

    class Meta:
        model = Comments
        fields = ('comment_text', 'comment_sign', 'comment_contact', 'not_robot','captcha_example',
                  'captcha_entrance', 'captcha_result')

    def _clean_not_robot(self):
        if 'not_robot' not in self.cleaned_data.keys() or not self.cleaned_data['not_robot']:
            raise ValidationError('Вы не подтвердили, что вы не робот.')
        return None

    def _clean_captcha_entrance(self):
        if 'captcha_entrance' not in self.cleaned_data.keys() or self.cleaned_data['captcha_entrance'] != self.cleaned_data['captcha_result']:
            raise ValidationError('Ваше решение несложного примера неверно')
        return None