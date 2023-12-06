import os

import django
# Set up Django
from django.db.models import Avg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating',
                                                                                            'title').first()

    if top_rated_article and top_rated_article.avg_rating is not None:
        avg_rating_formatted = "{:.2f}".format(top_rated_article.avg_rating)

        num_reviews = top_rated_article.review_set.count()

        return (f"The top-rated article is: {top_rated_article.title}, with an average rating of "
                f"{avg_rating_formatted}, reviewed {num_reviews} times.")

    return ""


def get_latest_article():
    latest_article = Article.objects.order_by('-published_on').first()

    if latest_article:
        authors_names = ', '.join(sorted([author.full_name for author in latest_article.authors.all()]))

        num_reviews = latest_article.review_set.count()
        avg_rating = latest_article.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0

        avg_rating_formatted = "{:.2f}".format(avg_rating)

        return (f"The latest article is: {latest_article.title}. Authors: {authors_names}. "
                f"Reviewed: {num_reviews} times. Average Rating: {avg_rating_formatted}.")

    return ""


def ban_author(email=None):
    if email is not None:
        author = Author.objects.filter(email=email).first()

        if author:
            num_reviews = author.review_set.count()

            author.review_set.all().delete()

            author.is_banned = True
            author.save()

            return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."

        return "No authors banned."

    return "No authors banned."
