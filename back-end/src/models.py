from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from src.database import Base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func
from src.schemas import ProjectBase

class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    web_url = Column(String, nullable=False)

    competitions = relationship('Competition',
                                secondary="competition_publisher",
                                backref='publisher',
                                lazy="selectin")
    
    @hybrid_property
    def competitions_participated(self) -> list:
        return [c.vague for c in self.competitions]
    
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
                            lazy='selectin') # dynamic <> selectin, l'un nous permet d'aller dans l'étape Query (Filtres, pagination, etcPeu) (Objet Query) 
                                            # <> l'autre nous permet de récupérer directement la liste (list object) : privilégier pour de la performance
    
    # Version selectin
    @hybrid_property
    def project_count(self) -> int:
        return len(self.projects) # On Compte le nombre de projets

    @hybrid_property
    def themes(self) -> list[str]:
        return list({p.theme.theme for p in self.projects if p.theme}) # Le set est utilisé pour supprimer les doublons

    @hybrid_property
    def companies(self) -> list[str]:
        return list({p.company.name for p in self.projects if p.company})
    
    # Pour avoir l'expression SQL
    @companies.expression
    def companies(cls):
        from .models import Project, Company

        return (
            select(func.array_agg(func.distinct(Company.name)))
            .where(Project.vague == cls.vague)
            .join(Company, Project.id_comp == Company.id)
            .scalar_subquery()
        )
    
class Region(Base):
    __tablename__ = "region"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)

    deps = relationship('Department', 
                        backref='region', 
                        lazy='selectin')
    
    @hybrid_property
    def listdeps(self) -> list:
        return [[d.name, d.dep_number] for d in self.deps]
    
    @hybrid_property
    def project_count(self) -> int:
        return sum([len(d.projects) for d in self.deps])
            
    @hybrid_property
    def vague_participated(self) -> list[int]:
        return list({
        proj.vague
        for dep in self.deps
        for proj in dep.projects
        })

    @hybrid_property
    def themes(self) -> list[str]:
        return list({
        proj.theme.theme
        for dep in self.deps
        for proj in dep.projects
        })

    @hybrid_property
    def themes_gen(self) -> list[str]:
        return list({
        proj.theme.general_theme
        for dep in self.deps
        for proj in dep.projects
        })
    
class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    theme = Column(String, index=True, nullable=False)
    general_theme = Column(String, index=True, nullable=False)

    projects = relationship('Project', 
                        backref='theme', 
                        lazy='selectin')
    
class Company(Base):
    __tablename__ = "company"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    activity = Column(String, nullable=True)

    projects = relationship('Project', 
                        backref='company', 
                        lazy='selectin')
    
    @hybrid_property
    def regions_dep_list(self):
        dict_regions_dep = {}

        for p in self.projects:
            for d in p.department:
                if not d.region.name in dict_regions_dep:
                    dict_regions_dep[d.region.name] = [d.name]
                else:
                    dict_regions_dep[d.region.name].append(d.name)
        
        return dict_regions_dep
    
    @hybrid_property
    def themes_list(self):
        return list({
            proj.theme.general_theme
            for proj in self.projects
            })

    # @hybrid_property
    # def project_details(self):
    #     return [
    #     ProjectBase.model_validate(proj).model_dump()
    #     for proj in self.projects
    # ]
    
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
                            lazy='selectin')
    
    @hybrid_property
    def project_count(self) -> int:
        return len(self.projects)
            
    @hybrid_property
    def vague_participated(self) -> list[int]:
        return list({
        proj.vague
        for proj in self.projects
        })

    @hybrid_property
    def themes(self) -> list[str]:
        return list({
        proj.theme.theme
        for proj in self.projects
        })

    @hybrid_property
    def themes_gen(self) -> list[str]:
        return list({
        proj.theme.general_theme
        for proj in self.projects
        })
    
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
                     ForeignKey("theme.id"),
                     index=True)
    
    vague = Column(Integer,
                   ForeignKey('competition.vague'))
    
    id_comp = Column(Integer,
                     ForeignKey('company.id'),
                     index=True)
    
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
