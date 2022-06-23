from django.contrib import admin
from.models import Firma, Status, Ariza, Paylasim, Category, Comment


class TicketAdmin(admin.ModelAdmin):
    list_display = ("gelenAdSoyad", "gelenMail", "gelenTelefon", "gelenKonu")
    #list_editable = ("gelenMail", "gelenTelefon")
    search_fields = ("gelenAdSoyad",)
    readonly_fields = ("gelenAdSoyad",
                       "gelenMail", "gelenTelefon", "gelenAciklama",)


class PaylasimAdmin(admin.ModelAdmin):
    list_display = ("göndericiAdi", "cameUrunumu",
                    "yazılımUrunumu", "gönderiDurumu", "gönderiFoto")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('hangi_ariza', 'göndericiUser', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Status)
admin.site.register(Ariza, TicketAdmin)
admin.site.register(Paylasim, PaylasimAdmin)
admin.site.register(Category)
admin.site.register(Firma)
