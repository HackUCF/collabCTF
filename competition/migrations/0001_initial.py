# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Competition'
        db.create_table('competition_competition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('competition', ['Competition'])

        # Adding model 'Challenge'
        db.create_table('competition_challenge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_viewed', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('progress', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('num_progress', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('point_value', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='challenges', to=orm['competition.Competition'])),
        ))
        db.send_create_signal('competition', ['Challenge'])

        # Adding unique constraint on 'Challenge', fields ['name', 'competition']
        db.create_unique('competition_challenge', ['name', 'competition_id'])

        # Adding model 'ChallengeFile'
        db.create_table('competition_challengefile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ctime', self.gf('django.db.models.fields.DateTimeField')()),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('mtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('challenge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['competition.Challenge'])),
        ))
        db.send_create_signal('competition', ['ChallengeFile'])

        # Adding model 'Tag'
        db.create_table('competition_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('is_category', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('competition', ['Tag'])


    def backwards(self, orm):
        # Removing unique constraint on 'Challenge', fields ['name', 'competition']
        db.delete_unique('competition_challenge', ['name', 'competition_id'])

        # Deleting model 'Competition'
        db.delete_table('competition_competition')

        # Deleting model 'Challenge'
        db.delete_table('competition_challenge')

        # Deleting model 'ChallengeFile'
        db.delete_table('competition_challengefile')

        # Deleting model 'Tag'
        db.delete_table('competition_tag')


    models = {
        'competition.challenge': {
            'Meta': {'object_name': 'Challenge', 'ordering': "('progress',)", 'unique_together': "(('name', 'competition'),)"},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'challenges'", 'to': "orm['competition.Competition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_progress': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'point_value': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'progress': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'competition.challengefile': {
            'Meta': {'object_name': 'ChallengeFile'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': "orm['competition.Challenge']"}),
            'ctime': ('django.db.models.fields.DateTimeField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'competition.competition': {
            'Meta': {'object_name': 'Competition'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        },
        'competition.tag': {
            'Meta': {'object_name': 'Tag'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['competition']