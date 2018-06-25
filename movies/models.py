from django.db import models


class Movies(models.Model):
    m_id = models.AutoField(primary_key=True, db_column='m_id')
    m_title = models.TextField(db_column='m_title', default='')
    m_director = models.TextField(db_column='m_director', default='')
    m_genre = models.TextField(db_column='m_genre', default='')
    m_imdb_score = models.DecimalField(max_digits=50, decimal_places=1, default="")#.PositiveIntegerField(db_column='m_imdb_score', default='')
    m_99popularity = models.DecimalField(max_digits=50, decimal_places=1, default="")#PositiveIntegerField(db_column='m_99popularity', default='')

    def __unicode__(self):
        return unicode(self.m_id) + " - " + unicode(self.m_title)
