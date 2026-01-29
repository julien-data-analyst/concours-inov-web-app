from pydantic import BaseModel
import datetime
from typing import Optional

# Base schema with common attributes
class PublisherBase(BaseModel):
    name: str
    web_url: str = ""
    competitions_participated: list[int]

# Schema for reading/returning an item (includes id)
class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True

# Base schema with common attributes
class CompetitionBase(BaseModel):
    vague: int
    description: str = ""
    web_url: str = ""
    pdf_url: str = ""
    description: str = ""
    presentation: str=""
    parution: datetime.datetime

# Schema for reading/returning an item (includes id)
class Competition(CompetitionBase):
    vague: int
    project_count: int
    themes: list[str]
    companies: list[str]

    class Config:
        orm_mode = True

# Base schema with common attributes
class RegionBase(BaseModel):
    name: str

# Schema for reading/returning an item (includes id)
class Region(RegionBase):
    listdeps: list
    project_count: int
    vague_participated: list[int]
    themes: list
    themes_gen: list

    class Config:
        orm_mode = True

# Base schema with common attributes
class ThemeBase(BaseModel):
    theme: str
    general_theme: str

# Schema for reading/returning an item (includes id)
class Theme(ThemeBase):
    project_count: int
    
    class Config:
        orm_mode = True

# Base schema with common attributes
class DepartmentBase(BaseModel):
    name: str
    dep_number: str

# Schema for reading/returning an item (includes id)
class Department(DepartmentBase):
    id: int
    project_count: int
    vague_participated: list[int]
    themes: list
    themes_gen: list
    
    class Config:
        orm_mode = True

# Base schema with common attributes
class ProjectBase(BaseModel):
    id: int
    name: str
    pdf_page: int
    description: Optional[str] = None
    project_amount: Optional[int] = None
    project_allowance: Optional[int] = None
    beginning_year: Optional[int] = None
    ending_year: Optional[int] = None
    month_dury: Optional[int] = None
    
# Schema for reading/returning an item (includes id)
class Project(ProjectBase):
    theme: Theme

    class Config:
        #from_attributes = True
        orm_mode = True

# Base schema with common attributes
class CompanyBase(BaseModel):
    name: str
    activity: str

# Schema for reading/returning an item (includes id)
class Company(CompanyBase):
    regions_dep_list: dict
    themes_list: list
    projects: list[Project]

    class Config:
        orm_mode = True