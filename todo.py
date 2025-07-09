from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import IntEnum

app = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class todo_schema(BaseModel):
    todo_name: str = Field(..., description = "Name of the todo")
    todo_description: str = Field(..., description = "Description of the todo")
    priority: Priority = Field(default=Priority.LOW, description = "Priority of the todo")

class todo_create(todo_schema):
    pass

class todo(todo_schema):
    todo_id: int = Field(..., description = "Unique Identifier")

class todo_update(todo_schema):
    todo_name: Optional[str] = Field(None)
    todo_description: Optional[str] = Field(None)
    priority: Optional[Priority] = Field(None)

all_todos = [
    todo(todo_id = 1, todo_name = 'sports', todo_description = 'Go to the GYM', priority = Priority.HIGH),
    todo(todo_id = 2, todo_name = 'Chores', todo_description = 'Clean The House', priority = Priority.MEDIUM),
    todo(todo_id = 3, todo_name = 'Study', todo_description = 'Revise the Lessons', priority = Priority.HIGH),
    todo(todo_id = 4, todo_name = 'Work', todo_description = 'Work on the Project', priority = Priority.MEDIUM),
    todo(todo_id = 5, todo_name = 'Meditate', todo_description = 'Meditate for 20 Mins', priority = Priority.LOW)
]

@app.get('/todos/{todo_id}', response_model = todo)
def get_todos(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail = "Todo Not Found")


@app.get('/todos', response_model = List[todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@app.post('/todos', response_model = todo)
def create_todo(todo: todo_create):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1

    new_todo = todo(
        todo_id= new_todo_id,
        todo_name= todo.todo_name,
        todo_description= todo.todo_description,
         priority = todo.priority
    )

    all_todos.append[new_todo]

    return new_todo

@app.put('/todos/{todo_id}', response_model = todo)
def update_todo(todo_id: int, updated_todo: todo_update):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
        raise HTTPException(status_code=404, detail = "Todo Not Found")
    
@app.delete('/todos/{todo_id}', response_model = todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
        
    raise HTTPException(status_code=404, detail = "Todo Not Found")
