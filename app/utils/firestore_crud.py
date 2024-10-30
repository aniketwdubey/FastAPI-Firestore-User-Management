from unittest import mock
from google.cloud import firestore
from app.schemas.user import UserCreate


db = firestore.Client.from_service_account_json('/Users/aniketdubey/Downloads/buoyant-ceiling-440212-a6-86758dd7c004.json')


def create_user(user: UserCreate) -> dict:
    doc_ref = db.collection("users").document()
    user_data = user.dict()
    user_data["user_id"] = doc_ref.id
    doc_ref.set(user_data)
    return user_data

def get_users() -> list:
    users = [doc.to_dict() for doc in db.collection("users").stream()]
    return users

def update_user(user_id: str, user_data: UserCreate) -> dict:
    doc_ref = db.collection("users").document(user_id)
    if not doc_ref.get().exists:
        return None
    doc_ref.update(user_data.dict())
    return doc_ref.get().to_dict()

def delete_user(user_id: str) -> None:
    db.collection("users").document(user_id).delete()
