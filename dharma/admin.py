from django.contrib import admin

from dharma.nature.admin.admin import NatureAdmin
from dharma.nature.models.nature import Nature


admin.site.register(Nature, NatureAdmin)
