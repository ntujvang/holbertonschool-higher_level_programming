#!/usr/bin/python3
'''
Script that prints all City objects from the database hbtn_0e_14_usa
using SQLAlchemy
'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Sess = Session()
    for i, j in Sess.query(State, City).join(City).order_by(City.id).all():
        print("{}: ({}) {}".format(i.name, j.id, j.name))
