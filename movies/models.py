from django.contrib.auth.models import User
from django.db import models
from constants import *
from multiselectfield import MultiSelectField


class Movies(models.Model):
    m_id = models.AutoField(primary_key=True, db_column='m_id')
    m_title = models.TextField(db_column='m_title', default='')
    m_director = MultiSelectField(db_column='m_director', default='')
    m_genre = models.TextField(choices=MOVIES_GENRE)
    m_imdb_score = models.PositiveIntegerField(db_column='m_imdb_score', default='')
    m_99popularity = models.PositiveIntegerField(db_column='m_99popularity', default='')

    def __unicode__(self):
        return unicode(self.m_id) + " - " + unicode(self.m_title)
