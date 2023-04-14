from api.repositories import user_repository


def find_all():
    return user_repository.find_all()


def find_one(user_id):
    return user_repository.find_one(user_id)
