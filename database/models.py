from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer, String

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)

    created_on = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_on = Column(TIMESTAMP)

    name = Column(String)
    discord_id = Column(String)
    discord_code = Column(String)

    verified_by = Column(ForeignKey('moderator.id'))



class Moderator(Base):
    __tablename__ = 'moderator'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    token = Column(String)

    permission_level = Column(ForeignKey('moderatorPermission.id'))


class Server(Base):
    '''
        this server has the token that the server needs to send to authenticate to the api
    '''
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    token = Column(String)


class ModeratorPermission(Base):
    '''
        this table has the permissions of a moderator
    '''
    __tablename__ = 'moderatorPermission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    

class UserPermission(Base):
    '''
        This table has the token that the user needs to send to the server to authenticate
    '''
    __tablename__ = 'userPermission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(ForeignKey('server.id'))
    user_id = Column(ForeignKey('user.id'))
    token = Column(String)
