from django import forms
from django.views.generic import CreateView, UpdateView
from main.models import Client, MailingSetting, Blog, Message, MailingLogs

exclusion_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class FormStyleMixin:
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'



    def clean_product_name (self):
        cleaned_data = self.cleaned_data['email']
        for i in exclusion_list:
            if i.lower() in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова в наименовании: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['client']
        for i in exclusion_list:
            if i.lower() in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова в описании: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар')

        return cleaned_data
#
#

class MessageForm(FormStyleMixin, forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Message
        fields = '__all__'


class MailingSettingForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = MailingSetting
        fields = '__all__'



    def clean_product_name (self):
        cleaned_data = self.cleaned_data['email']
        for i in exclusion_list:
            if i.lower() in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова в наименовании: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['start_time']
        for i in exclusion_list:
            if i.lower() in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые слова в описании: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар')

        return cleaned_data



class MailingLogsForm(FormStyleMixin, forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MailingLogs
        fields = '__all__'

