from django.contrib import admin

from .models import Article , Comment , Like

## register the 3 models for the admin page
admin.site.register( Article )
admin.site.register( Comment )
admin.site.register( Like )
