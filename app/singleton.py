"""
Singleton pattern
"""
import random
from model import UserAuth


def singleton(class_):
    """
    Singleton decorator
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    """
    Database class
    """
    def __init__(self):
        self.id = random.randint(0, 10000)
        self.user_storage: dict[str, UserAuth] = {}
        print(f"Instance ID: {self.id}")


db = Database()

if __name__ == "__main__":
    db = Database()
    # db.user_storage["test"] = User(email="test", age=20)
    # print(db.user_storage)
