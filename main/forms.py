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
        fields = ('office_id', 'description', 'urgency', 'status', 'comments')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if not self.request.user.is_staff:
            self.fields['comments'].widget = forms.HiddenInput()



class BookingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'duration', 'status')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

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
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if not self.request.user.is_manager:
            self.fields['price'].widget = forms.HiddenInput()
            self.fields['status'].widget = forms.HiddenInput()

    class Meta:
        model = Cars
        fields = ('car_id', 'model', 'start_date', 'end_date', 'period', 'status', 'price')
        widgets = {
            # Виджеты для даты
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


