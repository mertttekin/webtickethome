from django.contrib import admin
from.models import Firma, Status, Ariza, Paylasim, Category


class TicketAdmin(admin.ModelAdmin):
    list_display = ("gelenAdSoyad", "gelenMail", "gelenTelefon")
    #list_editable = ("gelenMail", "gelenTelefon")
    search_fields = ("gelenAdSoyad",)
    readonly_fields = ("gelenAdSoyad",
                       "gelenMail", "gelenTelefon", "gelenAciklama",)

# class PaylasimAdmin(admin.ModelAdmin):
    # list_filter=()
    # filtreleme olursa 165


admin.site.register(Status)
admin.site.register(Ariza, TicketAdmin)
admin.site.register(Paylasim)
admin.site.register(Category)
admin.site.register(Firma)
