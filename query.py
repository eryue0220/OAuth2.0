# !/usr/bin/env python3
# -*- coding: utf-8 -*

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

result = session.query(User).filter_by(email = 'eryue0220@gmail.com').one_or_none()
print(result)
