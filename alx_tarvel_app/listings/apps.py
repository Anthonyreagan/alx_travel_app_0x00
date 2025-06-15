from django.apps import AppConfig

class ListingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alx_travel_app.listings'  # ← Must match INSTALLED_APPS prefix!