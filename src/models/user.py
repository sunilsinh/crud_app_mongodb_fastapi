from pydantic import BaseModel

"""Schema for user model"""
class User(BaseModel):
    name: str 
    age: str
    salary: int
    contact: str

def fetchOne(item)->dict:
    return {
        "id":str(item["_id"]),
        "name": item["name"],
        "age": item["age"],
        "salary":item["salary"],
        "contact": item["contact"]
    }

def fetchList(datas)->list:
    return [fetchOne(data) for data in datas]




def responseModel(data, msg):
    return {
        "data":[data],
        "code": 200,
        "msg": msg
    }

def ErrorResponseModel(error, code, msg):
    return {
        "error": error, 
        "code": code, 
        "message": msg
    }