#!/usr/bin/python3
'''
Script that adds the State Louisiana" to database hbtn_0e_6_usa
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
    new = State(name='Louisiana')
    Sess.add(new)
    Sess.commit()
    for i in Sess.query(State).filter(State.name == 'Louisiana'):
        print(i.id)
