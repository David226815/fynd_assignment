"""
Abstraction file for db support
"""


class MoviesAbs:
    """
    to save movie object
    """
    def __init__(self):
        self.m_id = 0
        self.m_title = ''
        self.m_director = ''
        self.m_genre = ''
        self.m_imdb_score = 0.0
        self.m_99popularity = 0.0
