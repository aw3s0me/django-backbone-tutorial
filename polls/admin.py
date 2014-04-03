from django.contrib import admin
from polls.models import Question
from polls.models import Choice

#Here we define the way how we wanna see fields

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


#1Version
#class PollAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question_text'] #just changed the order

#2Version. Divide fields
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'isPublished') #In the list we output all information


#register as default way
#admin.site.register(Question)

#register model in a new way
admin.site.register(Question, PollAdmin)
admin.site.register(Choice)

# Register your models here.
