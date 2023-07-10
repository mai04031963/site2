from django import forms
from . models import Good
from django.forms import ModelChoiceField


class GoodsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Cat1ModelChoiceField(ModelChoiceField):

        def __init__(self):
            super().__init__(queryset=Good.objects.filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name'),
                             to_field_name='name')

        def has_changed(self, initial, data):
            print(self.choices)
            print(self.clean)
            print(self.bound_data)
            print(self.iterator)
            super().has_changed(self, initial)


    seek = forms.CharField(max_length=255, required=False, label='')

    #category1 = forms.ModelChoiceField(queryset=Good.objects.filter(is_good=False,cat1=0,cat2=0,cat3=0).order_by('name'),
    #                                   to_field_name='name', required=False)
    category1 = Cat1ModelChoiceField()

    id1 = 0

    cat1_id = forms.IntegerField(required=False, initial=0)

    #category2 = forms.ModelChoiceField(required=False, queryset=Good.objects.filter(is_good=False, cat1=id1, cat2=0, cat3=0).order_by('name'),
    #                                   to_field_name='name')

    #id2 = Good.objects.get(is_good=False, name=category2, cat1=id1, cat2=0, cat3=0).pk

    #cat2_id = forms.IntegerField(required=False, initial=0)

    #category3 = forms.ModelChoiceField(required=None, queryset=Good.objects.filter(is_good=False, cat1=11, cat2=0, cat3=0).order_by('name'),
    #                                   to_field_name='name')
    #id3 = Good.objects.get(is_good=False, name=category2, cat1=id1, cat2=id2, cat3=0).pk

    #cat3_id = forms.IntegerField(required=False, initial=0)

    class Meta:
        model = Good
        fields = ('seek', 'category1')
        #, 'cat1_id', 'category2', 'cat2_id', 'category3', 'cat3_id')

    def _clean_category1(self):
        cat1 = self.cleaned_data['category1']
        self.cat1_id = cat1
        self.id1 = Good.objects.get(is_good=False, name=cat1, cat1=0, cat2=0, cat3=0).pk

