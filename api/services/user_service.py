from api.repositories import user_repository


def find_all(offset: int = None, limit: int = None):
    return user_repository.find_all(offset, limit)


def find_one(user_id):
    return user_repository.find_one(user_id)
