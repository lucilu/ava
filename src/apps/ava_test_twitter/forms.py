from django.forms import ModelForm

from apps.ava_test_twitter.models import *


class TwitterTestForm(ModelForm):
    class Meta:
        model = TwitterTest
        exclude = []
