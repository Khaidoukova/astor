from datetime import date

from django import forms
from .models import Company, Office, User_request, Booking, Cars


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CompanyForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'description', 'logo')


class OfficeForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Office
        fields = ('office_id', 'floor', 'sq_m', 'description', 'price')


class User_requestForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User_request
        fields = ('date', 'office_id', 'owner', 'description', 'urgency', 'status', 'comments')


class BookingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'duration', 'owner')

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError(
                'Выберите, пожалуйста, '
                'дату в будущем (завтра или позднее)',
                code='invalid'
            )
        return day

class CarsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Cars
        fields = ('car_id', 'model', 'description', 'price', 'owner')