#!/usr/bin/python3
'''
Script that edits the name of a State object in hbtn_0e_6_usa database
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
    for i in Sess.query(State).filter(State.id == 2):
        i.name = 'New Mexico'
        Sess.commit()
