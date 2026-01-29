from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import src.models,src.schemas
from src.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import defer, joinedload, selectinload

# Create all tables in the database
#app.models.Base.metadata.create_all(bind=engine)

# Create the FastAPI application
app = FastAPI()

# Add CORS middleware to allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React's default port
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# READ - Get all publishers
@app.get("/publishers/", response_model=list[src.schemas.Publisher])
def read_items(db: Session = Depends(get_db)):
    
    publishers = db.query(src.models.Publisher).options(
        selectinload(src.models.Publisher.competitions)
    ).all()

    return publishers

# READ - Get all competitions
@app.get("/competitions/", response_model=list[src.schemas.Competition])
def read_items(db: Session = Depends(get_db)):

    competitions = (
        db.query(src.models.Competition)
        .options(
            # Pour améliorer les performances, on va charger toutes les tables nécessaires en 1 requête pour en mémoire aller tous chercher facilement
            selectinload(src.models.Competition.projects) # Charge tous les projets en 1 requête
            .joinedload(src.models.Project.company),       # Joint la compagnie
            selectinload(src.models.Competition.projects)
            .joinedload(src.models.Project.theme)         # Joint le thème
        )
        .all()
    )
    
    return competitions

# READ - Get all regions
@app.get("/regions/", response_model=list[src.schemas.Region])
def read_items(db: Session = Depends(get_db)):
    regions = (
    db.query(src.models.Region)
    .options(
        selectinload(src.models.Region.deps)
        .joinedload(src.models.Department.projects)
        .joinedload(src.models.Project.theme)
    )
    .all()
    )
    return regions

# READ - Get all departments
@app.get("/departments/", response_model=list[src.schemas.Department])
def read_items(db: Session = Depends(get_db)):
    regions = (
    db.query(src.models.Department)
    .options(
        selectinload(src.models.Department.projects)
        .joinedload(src.models.Project.theme)
    )
    .all()
    )
    return regions

# READ - Get all company
@app.get("/companies/", response_model=list[src.schemas.Company])
def read_items(db: Session = Depends(get_db)):
    companies = (db.query(src.models.Company)
                 .options(
                     selectinload(src.models.Company.projects)
                     .joinedload(src.models.Project.department)
                     .joinedload(src.models.Department.region)
                     ,
                     selectinload(src.models.Company.projects)
                     .joinedload(src.models.Project.theme)
                 )
                 .all())
    
    return companies

# READ - Get all publishers
@app.get("/projects/", response_model=list[src.schemas.Project])
async def read_items(db: Session = Depends(get_db)):
    
    projects = db.query(src.models.Project).options(
        selectinload(src.models.Project.theme)
    ).all()

    return projects

# READ - Get all publishers
@app.get("/themes/", response_model=list[src.schemas.Theme])
async def read_items(db: Session = Depends(get_db)):
    
    themes = db.query(src.models.Theme).options(
        selectinload(src.models.Theme.projects)
    ).all()

    return themes

# READ - Get all publishers
@app.get("/general_theme/", response_model=list[src.schemas.Theme])
async def read_items(db: Session = Depends(get_db)):
    
    themes = db.query(src.models.Theme).options(
        selectinload(src.models.Theme.projects)
    )

    return themes