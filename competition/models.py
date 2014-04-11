from django.db import models


class Competition(models.Model):
    name = models.CharField('Name', max_length=255)
    url = models.URLField('Competition URL', blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.name


class Challenge(models.Model):
    name = models.CharField('Name', max_length=255)
    progress = models.FloatField(default=0)
    competition = models.ForeignKey(Competition, related_name='challenges')

    def __unicode__(self):
        return self.name