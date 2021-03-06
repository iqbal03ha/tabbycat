from django.contrib import admin

from django_summernote.settings import get_attachment_model
from dynamic_preferences.admin import PerInstancePreferenceAdmin
from dynamic_preferences.models import GlobalPreferenceModel

from .models import TournamentPreferenceModel


# ==============================================================================
# Preferences
# ==============================================================================

@admin.register(TournamentPreferenceModel)
class TournamentPreferenceAdmin(PerInstancePreferenceAdmin):
    pass


admin.site.unregister(GlobalPreferenceModel)


# We don't use the attachment model; so hide it in the admin area
admin.site.unregister(get_attachment_model())
