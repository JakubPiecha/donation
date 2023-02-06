from django.contrib import admin, messages

# Register your models here.

from django.contrib import admin
from django.contrib.admin import helpers
from django.contrib.auth import get_user_model

from . import models

class CustomUserAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        selected = request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)
        if obj is None:
            if selected:
                if str(request.user.id) in selected:
                    self.message_user(request, 'Nie możesz usunąć samego siebie', level=messages.ERROR)
                    return False
                else:
                    return True
        else:
            user = get_user_model().objects.get(email=obj).id
            if user != request.user.id:
                return True
            else:
                return False
        return super(CustomUserAdmin, self).has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        else:
            user = get_user_model().objects.get(email=obj).id
            if user == request.user.id:
                return False
        return super(CustomUserAdmin, self).has_change_permission(request, obj)



admin.site.register(models.Category)
admin.site.register(models.Institution)
admin.site.register(models.Donation)
admin.site.register(models.CustomUser, CustomUserAdmin)
