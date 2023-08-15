from django.contrib import admin

from main.models import Client, MailingSetting, Blog, Message, MailingLogs


# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'client','client_comment',)
    search_fields = ('email', 'client',)
    list_filter = ('is_active', )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'head_message','body_message', )
    search_fields = ('email', 'head_message','body_message',)
    list_filter = ('head_message', )

@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time','end_time', 'status_mailing', )
    search_fields = ('email', 'start_time','end_time',)
    list_filter = ('status_mailing', )

@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = ('email_id', 'log_time','status_mailing', 'get_server_mail', )
    search_fields = ('email_id', 'log_time','status_mailing',)
    list_filter = ('get_server_mail', )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('message_preview', 'message_heading','message_content', 'date_of_creation', 'date_of_change', )
    search_fields = ('message_preview', 'message_heading', 'message_content', 'date_of_creation', 'date_of_change',)
    list_filter = ('is_publication', )
    prepopulated_fields = {"slug": ("message_heading",)}

