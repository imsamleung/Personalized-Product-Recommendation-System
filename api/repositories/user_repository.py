from api.datasource import get_users


def find_all(offset: int = None, limit: int = None):
    df_users = get_users()

    if offset is not None:
        if offset < 0:
            offset = 0
        df_users = df_users[offset:]

    if limit is not None:
        if limit < 1:
            limit = 1
        if limit > len(df_users):
            limit = len(df_users)
        df_users = df_users[:limit]

    return df_users


def find_one(user_id):
    df_users = find_all()
    return df_users[df_users["user_id"] == user_id]
