from api.datasource import get_users


def find_all():
    return get_users()


def find_one(user_id):
    df_users = find_all()
    return df_users[df_users["user_id"] == user_id]
