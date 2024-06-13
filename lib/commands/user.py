from database import Session
from models import User

def create_user(username):
    # Create a new user.
    session = Session()
    
    if not username:
        print("Username must not be null.")
        return
    
    user = User(username=username)
    session.add(user)
    session.commit()
    print("User created successfully.")


def get_all_users():
    # getting all users.
    session = Session()
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return

    print("\n--- List of All Users ---")
    for user in users:
        print(f"User ID: {user.user_id}, Username: {user.username}")

    print() 


def get_user_by_id(user_id):
    # get a user by ID.
    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()
    if not user:
        print("User not found.")
        return

    print("\n--- User ---")
    print(f"User ID: {user.user_id}, Username: {user.username}")


