from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from models import User, Recipe
import schemas

router = APIRouter()

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/register")
async def register(login: str, password: str, db: Session = Depends(get_db)):
    user = User(login=login, password=password)
    db.add(user)
    db.commit()
    return {"msg": "Пользователь зарегистрирован!"}

@router.post("/login")
async def login(login: str, password: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.login == login).first()
        if user.password == password:
            return {"Успешный вход!": f"ID:{user.id}"}
        else:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный пароль!")
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль!")
    
@router.get("/recipes")
async def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()

@router.post("/add_recipe")
async def add_recipe(recipe: schemas.Recipe, db: Session = Depends(get_db)):
    new_recipe = Recipe(**recipe.model_dump())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return {"msg": f"Рецепт \'{recipe.name}\' успешно добавлен!"}