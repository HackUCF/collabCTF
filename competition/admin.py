from django.contrib import admin
from competition.models import Competition, Challenge, ChallengeFile

# Register your models here.


class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Competition


class ChallengeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Challenge

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(ChallengeFile)