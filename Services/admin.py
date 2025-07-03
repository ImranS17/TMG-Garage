from django.contrib import admin
from .models import Feedback
from .models import Complaint
from .models import BookService


# Register your models here.

admin.site.register(Feedback)
admin.site.register(Complaint)
admin.site.register(BookService)

