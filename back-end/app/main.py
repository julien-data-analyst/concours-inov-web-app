from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import defer, joinedload, selectinload

# Create all tables in the database
#models.Base.metadata.create_all(bind=engine)

# Create the FastAPI application
app = FastAPI()

# Add CORS middleware to allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React's default port
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
@app.get("/publishers/", response_model=list[schemas.Publisher])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    publishers = db.query(models.Publisher).offset(skip).limit(limit).all()
    return publishers

# READ - Get all competitions
@app.get("/competitions/", response_model=list[schemas.Competition])
def read_items(db: Session = Depends(get_db)):

    competitions = (
        db.query(models.Competition)
        .options(
            # Pour améliorer les performances, on va charger toutes les tables nécessaires en 1 requête pour en mémoire aller tous chercher facilement
            selectinload(models.Competition.projects) # Charge tous les projets en 1 requête
            .joinedload(models.Project.company),       # Joint la compagnie
            selectinload(models.Competition.projects)
            .joinedload(models.Project.theme)         # Joint le thème
        )
        .all()
    )
    
    return competitions

# READ - Get all regions
@app.get("/regions/", response_model=list[schemas.Region])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    publishers = db.query(models.Region).offset(skip).limit(limit).all()
    return publishers

# READ - Get all company
@app.get("/companies/", response_model=list[schemas.Company])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    publishers = db.query(models.Company).offset(skip).limit(limit).all()
    return publishers