from django import forms
from announcements.models import Announcement


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AnnouncementForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'body', 'image', 'stop_date')
        widgets = {

           'stop_date': forms.DateInput(attrs={'type': 'date'}),
        }

