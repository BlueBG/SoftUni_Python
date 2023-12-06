from django.db import models


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        authors_with_article_count = (self.annotate(article_count=models.Count('article'))
                                      .order_by('-article_count', 'email'))
        return authors_with_article_count

    def get_authors_by_review_count(self):
        authors_with_review_count = (self.annotate(review_count=models.Count('review'))
                                     .order_by('-review_count', 'email'))
        return authors_with_review_count
