from django.contrib import admin

from apps.ava_test_email.models import *

admin.site.register(EmailTest)
admin.site.register(EmailTestTarget)
admin.site.register(EmailTemplate)
