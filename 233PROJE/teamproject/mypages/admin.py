from django.contrib import admin
from .models import Posts
from .models import Messages
from .models import FormName


# Register your models here.
admin.site.register(Posts)
admin.site.register(Messages)
admin.site.register(FormName)

