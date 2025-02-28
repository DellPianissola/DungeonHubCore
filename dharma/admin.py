from django.contrib import admin

from .models import *

from dharma.nature.admin.admin import NatureAdmin
from dharma.technique.admin.admin import TechniqueAdmin
from .weapon.admin.admin import WeaponAdmin


admin.site.register(Nature, NatureAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Weapon, WeaponAdmin)
