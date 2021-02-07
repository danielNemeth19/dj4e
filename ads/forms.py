from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.models import Ad
from ads.humanize import natural_size


class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = natural_size(max_upload_limit)
    picture = forms.FileField(required=False, label='File to Upload <= ' + max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Ad
        fields = ['title', 'text', 'price', 'picture']

    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")

    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        f = instance.picture
        if isinstance(f, InMemoryUploadedFile):
            byte_arr = f.read()
            instance.content_type = f.content_type
            instance.picture = byte_arr

        if commit:
            instance.save()

        return instance


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
