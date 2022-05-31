from django.contrib import admin
from.models import Status, Ariza, Paylasim


class TicketAdmin(admin.ModelAdmin):
    list_display = ("gelenAdSoyad", "gelenMail", "gelenTelefon")
    #list_editable = ("gelenMail", "gelenTelefon")
    search_fields = ("gelenAdSoyad",)
    readonly_fields = ("gelenAdSoyad",
                       "gelenMail", "gelenTelefon", "gelenAciklama",)


admin.site.register(Status)
admin.site.register(Ariza, TicketAdmin)
admin.site.register(Paylasim)
