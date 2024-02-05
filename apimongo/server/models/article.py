from typing import Optional

from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    titre: str = Field(...)
    prix: str = Field(...)
    status: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "titre": "test_titre",
                "prix": "test_prix_",
                "status": 222,
            }
        }


class UpdateArticleModel(BaseModel):
    titre: str = Field(...)
    prix: str = Field(...)
    status: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "titre": "update_test_titre",
                "prix": "update_test_prix",
                "status": 222,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}