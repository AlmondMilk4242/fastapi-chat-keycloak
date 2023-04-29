# main.py
from fastapi import FastAPI
from app import config
from app.models.kanban_box import Base as KanbanBase, get_all_kanban_boxes, get_user_kanban_boxes
from app.models.organization import Base as OrganizationBase, create_tables
from app.database import database, engine
from app.routers.routes import router as routes_router
from app.routers.organization import router as organization_router


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(routes_router)
app.include_router(organization_router)
