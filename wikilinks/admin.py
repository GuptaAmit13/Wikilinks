from django.contrib import admin
from 	.models import MyUser,Question
class questionAdmin(admin.ModelAdmin):
	list_display=('question_start','question_end')

class userAdmin(admin.ModelAdmin):
	list_display=('__unicode__','user_password','user_receiptno','attempt_no','user_status')
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Question)
