
import pymongo
from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
router = APIRouter()
from models.user import fetchList, User, fetchOne
from bson.objectid import ObjectId
from config.settings import userCollection

"""
add user 
"""
@router.post('/add')
def add(request: Request, user: User):
    try:
        result = userCollection.insert_one(dict(user))
        # return all_task(request.app.database["users"].find())
        print(f"inserted id {result.inserted_id}")
        """note: very important that _id is not iterable in python
        so if you want to get result without it then need to exclude
        or use above all task function because using that we made _id as id in response
        """
        new_user = userCollection.find_one(
            {"_id": result.inserted_id}, {'_id': 0} 
        )
        return {"status_code":200, "data": new_user}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"some error occured {e} ")
    return {'msg':'new data added successfully'}

"""
fetch user
"""
@router.get('/fetch')
def fetch(request: Request):
   return fetchList(userCollection.find())


@router.get('/fetch/{id}')
async def fetch_one(request:Request, id):
    if ObjectId.is_valid(id):
        return fetchOne(userCollection.find_one({"_id":ObjectId(id)}))
    else:
        return {
            "msg":f"no data found base on {id}"
        }

"""update user"""
@router.put('/update/{id}')
def update(request:Request,id, user:User): 
    if ObjectId.is_valid(id):
        fetchOne(userCollection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)}))
        return fetchOne(userCollection.find_one({"_id":ObjectId(id)}))

    else:
        return {
            "msg":f"no data found base on {id}"
        }

"""
delete user
"""
@router.delete('/delete/{id}')
def delete(request:Request, id):
    if ObjectId.is_valid(id):
        fetchOne(userCollection.find_one_and_delete({"_id":ObjectId(id)}))
        return fetchList(userCollection.find())

    else:
        return {
            "msg":f"no data found base on {id}"
        }