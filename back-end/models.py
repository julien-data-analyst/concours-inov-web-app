from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from database import Base

class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    web_url = Column(String, nullable=False)

    competitions = relationship('Competition',
                                secondary="competition_publisher",
                                backref='publisher',
                                lazy="dynamic")
    
class Competition(Base):
    __tablename__ = "competition"

    vague = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True, nullable=False)
    web_url = Column(Text, nullable=False)
    pdf_url = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    presentation = Column(Text, nullable=False)
    parution = Column(Date, nullable=False)

    projects = relationship('Project',
                            backref='competition',
                            lazy='dynamic')

class Region(Base):
    __tablename__ = "region"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)

    deps = relationship('Department', 
                        backref='region', 
                        lazy='dynamic')
    
class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    theme = Column(String, index=True, nullable=False)
    general_theme = Column(String, index=True, nullable=False)

    projects = relationship('Project', 
                        backref='theme', 
                        lazy='dynamic')
    
class Company(Base):
    __tablename__ = "company"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    activity = Column(String, nullable=True)

    projects = relationship('Project', 
                        backref='company', 
                        lazy='dynamic')
    
class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    dep_number = Column(String, index=True, nullable=False)

    id_reg = Column(Integer,
                    ForeignKey("region.id"))

    projects = relationship('Project',
                            secondary='location',
                            backref='department',
                            lazy='dynamic')
    
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    pdf_page = Column(Integer, index=True, nullable=False)
    description = Column(Text, nullable=True)
    project_amount = Column(BigInteger, nullable=True)
    project_allowance = Column(BigInteger, nullable=True)
    beginning_year = Column(Integer, nullable=True)
    ending_year = Column(Integer, nullable=True)
    month_dury = Column(Integer, nullable=True)

    id_them = Column(Integer,
                     ForeignKey("theme.id"))
    
    vague = Column(Integer,
                   ForeignKey('competition.vague'))
    
    id_comp = Column(Integer,
                     ForeignKey('company.id'))
    
##############################
# ---- Création des tables d'associations (*-*) ----
##############################

# Pour competition et publisher
competition_publisher = Table('competition_publisher',
                        Base.metadata,
                        Column('id_pu', Integer,
                               ForeignKey("publisher.id")),
                        
                        Column('vague_comp', Integer,
                               ForeignKey('competition.vague')))

# Pour project et department
location = Table('location',
                 Base.metadata,
                 Column('id_dep', Integer,
                        ForeignKey("department.id")),
                 
                 Column('id_proj', Integer,
                        ForeignKey('project.id')))