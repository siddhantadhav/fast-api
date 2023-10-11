from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Service(Base):
    __tablename__= "services" 
    id = Column(Integer, primary_key= True, index= True)
    main_issue= Column(String)
    sub_issue= Column(String)
    priority= Column(String)
    comment= Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator= relationship("User", back_populates= "services")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index= True)
    name= Column(String)
    email= Column(String)
    password= Column(String)
    services= relationship("Service", back_populates= "creator")