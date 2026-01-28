from pydantic import BaseModel
import datetime

# Base schema with common attributes
class PublisherBase(BaseModel):
    name: str
    web_url: str = ""

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
    id: int

    class Config:
        orm_mode = True

# Base schema with common attributes
class ThemeBase(BaseModel):
    theme: str
    general_theme: str

# Schema for reading/returning an item (includes id)
class Theme(ThemeBase):
    id: int

    class Config:
        orm_mode = True

# Base schema with common attributes
class DepartmentBase(BaseModel):
    name: str
    dep_number: str

# Schema for reading/returning an item (includes id)
class Department(DepartmentBase):
    id: int

    class Config:
        orm_mode = True

# Base schema with common attributes
class ProjectBase(BaseModel):
    name: str

# Schema for reading/returning an item (includes id)
class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

# Base schema with common attributes
class CompanyBase(BaseModel):
    name: str
    activity: str

# Schema for reading/returning an item (includes id)
class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True