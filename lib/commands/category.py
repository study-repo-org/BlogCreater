from sqlalchemy.orm import Session
from database import Session
from models import Category

def create_category(name):
    """Create a category."""
    session = Session()
    
    if not name:
        print("category name must not be null.")
        return
    
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("Category created successfully.")


def get_all_categories():
    """get all categories."""
    session = Session()
    categories = session.query(Category).all()

    if not categories:
        print("No categories found.")
        return

    print("\n--- List of All Categories ---")
    for category in categories:
        print(f"Category ID: {category.category_id}, Name: {category.name}")

    print()



