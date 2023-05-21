from sqlalchemy import func
from dtos import get_engine
from dtos import Book, Rating, AuthorBook
from sqlalchemy.orm import sessionmaker
from dtos import CategoryAnalytics
import math


def categories_analytics():
    Session = sessionmaker(bind = get_engine())
    session = Session()
    categories = session.query(Book.publisher, Book.categories, func.sum(Book.ratingsCount)).\
            group_by(Book.publisher, Book.categories).\
            filter(Book.categories != None, Book.ratingsCount >= 0)
    
    categories_dtos = [CategoryAnalytics(publisher=r[0], categories=r[1], count_ratings=r[2]) for r in categories]
    categories_dtos = [cat for cat in categories_dtos if not math.isnan(cat.count_ratings)]
    for category in categories_dtos:
        print(f'Categories: {category.categories}   Count: {category.count_ratings}')
    

if __name__ == '__main__':
    categories_analytics()