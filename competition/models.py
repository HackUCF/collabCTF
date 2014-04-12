from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models


class Competition(models.Model):
    name = models.CharField('Name', max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    url = models.URLField('Competition URL', blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

    def get_absolute_url(self):
        return reverse('view_ctf', kwargs={'ctf_slug': self.slug})


class Challenge(models.Model):
    PROGRESS_CHOICES = (
        (0, 'Not Started'),
        (1, 'In Progress'),
        (2, 'Finished')
    )

    name = models.CharField('Name', max_length=255)
    slug = models.SlugField()
    progress = models.PositiveSmallIntegerField(choices=PROGRESS_CHOICES)
    num_progress = models.FloatField('Progress %', default=0)
    point_value = models.FloatField(default=0)

    competition = models.ForeignKey(Competition, related_name='challenges')
    last_viewed = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.name

    __str__ = __unicode__

    def get_absolute_url(self):
        return reverse('view_challenge', kwargs={'ctf_slug': self.competition.slug, 'chall_slug': self.slug})

    def last_viewed_display(self):
        if self.last_viewed == 0:
            return 'Never'
        else:
            return self.last_viewed


class ChallengeFile(models.Model):
    file = models.FileField(upload_to='files/')
    ctime = models.DateTimeField(auto_created=True)
    mtime = models.DateTimeField(auto_now=True)
    challenge = models.ForeignKey(Challenge, related_name='files')

    def __unicode__(self):
        return self.file.name

    __str__ = __unicode__


class Tag(models.Model):
    tag = models.SlugField()
    is_category = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.tag

    __str__ = __unicode__