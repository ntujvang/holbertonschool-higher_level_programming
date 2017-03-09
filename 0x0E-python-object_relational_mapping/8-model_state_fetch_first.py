#!/usr/bin/python3
'''
Script that prints out the first State object from hbtn_0e_6_usa using
SQLAlchemy!!
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Sess = Session()
    first = Sess.query(State).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
