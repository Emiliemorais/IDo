from django.contrib import admin
from blog.models import Message, Questionnaire

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass
admin.site.register(Questionnaire, QuestionnaireAdmin)