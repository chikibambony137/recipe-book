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
async def register(user: schemas.User, db: Session = Depends(get_db)):
    user = User(login=user.login, password=user.password)
    db.add(user)
    db.commit()
    return {"msg": "Пользователь зарегистрирован!"}

@router.post("/login")
async def login(user: schemas.User, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.login == user.login).first()
        if db_user.password == user.password:
            return {"Успешный вход!": f"ID:{db_user.id}"}
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

@router.get("/recipe")
async def find_recipe_by_name(search: str, db: Session = Depends(get_db)):
    return db.query(Recipe).where(Recipe.name.contains(search.lower().strip())).all()