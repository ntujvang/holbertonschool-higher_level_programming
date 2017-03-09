#!/usr/bin/python3
'''
Script that prints the State passed as argv[4]
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
    search = sys.argv[4]
    found = 0
    for i in Sess.query(State).filter(State.name == search):
            print(i.id)
            found = 1
    if found == 0:
        print("Not found")
