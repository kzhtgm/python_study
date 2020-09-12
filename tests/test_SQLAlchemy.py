import sqlite3
from typing import List

import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BaseEntity = declarative_base()


class User(BaseEntity):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birthday = Column(String(10))

    def __repr__(self):
        return '<User(id="%s", name="%s", birthday="%s")>' % (self.id, self.name, self.birthday)


@pytest.fixture(scope='class', autouse=True)
def build_session():
    engine = create_engine('sqlite:///test_SQLAlchemy')
    BaseEntity.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    try:
        session.add_all([
            User(id=1, name='かず', birthday='1978-01-20'),
            User(id=2, name='さき', birthday='1985-11-11'),
            User(id=3, name='あおい', birthday='2018-11-17')
        ])

        session.commit()
        yield session
    finally:
        session.query(User).delete()
        session.commit()
        session.close()


# class の方がスコープが広いので、function スコープの fixture に値が渡せる
# @pytest.fixture(scope='function', autouse=True)
# def before_function(self, create_engine):
#     self.engine = create_engine

# このメソッドより先に build_session が実行される
def test_select_specify_name(build_session):
    session = build_session

    user = session.query(User).filter_by(name='あおい').one()
    assert user.name == 'あおい'
    assert user.birthday == '2018-11-17'


def test_select_specify_index(build_session):
    session = build_session

    user = session.query(User).order_by(User.birthday.asc()).get(2)
    assert user.name == 'さき'
    assert user.birthday == '1985-11-11'


def test_select_order_by(build_session):
    session = build_session

    user = session.query(User).order_by(User.birthday.desc()).all()[0]
    assert user.name == 'あおい'

    users = session.query(User).order_by(User.birthday.desc()).all()[1:2]
    assert len(users) == 1
    assert users[0].name == 'さき'

    users = session.query(User).filter(User.birthday < '2000-01-01').order_by(User.birthday.asc()).all()
    assert len(users) == 2
    assert users[0].name == 'かず'
    assert users[1].name == 'さき'


def test_select_where(build_session):
    session = build_session

    users = session.query(User).filter(User.birthday > '1980-01-01', User.birthday < '2000-01-01').order_by(
        User.birthday.asc()).all()
    assert len(users) == 1
    assert users[0].name == 'さき'

    users = session.query(User).filter(User.birthday > '1980-01-01').filter(User.birthday < '2000-01-01').order_by(
        User.birthday.asc()).all()
    assert len(users) == 1
    assert users[0].name == 'さき'

    users = session.query(User).filter((User.birthday > '1980-01-01') | (User.birthday < '2000-01-01')).order_by(
        User.birthday.asc()).all()
    assert len(users) == 3
    assert users[0].name == 'かず'
    assert users[1].name == 'さき'
    assert users[2].name == 'あおい'


def test_select_in(build_session):
    session = build_session

    users = session.query(User).filter(User.name.in_(['かず', 'あおい'])).order_by(User.birthday.asc()).all()
    assert len(users) == 2
    assert users[0].name == 'かず'
    assert users[1].name == 'あおい'


def test_select_all(build_session):
    session = build_session

    users = session.query(User.name).order_by(User.birthday.asc()).all()
    assert users[0].name == 'かず'
    assert users[1].name == 'さき'
    assert users[2].name == 'あおい'


def test_update(build_session):
    session = build_session

    user = session.query(User).filter_by(name='かず').one()
    user.name = 'kaz'
    session.add(user)
    session.commit()

    assert session.query(User).get(1).name == 'kaz'
