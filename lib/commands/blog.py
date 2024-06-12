from sqlalchemy.orm import Session
from database import Session
from models import User, Category, Post


def create_post(user_id, title, content, category_id):
    """Create a new post."""
    session = Session()
    
    if user_id == 0:
        print("user id must not be null .")
        return

    if category_id == 0:
        print("category id must not be null.")
        return

    user = session.query(User).filter_by(user_id=user_id).first()
    if not user:
        print("User not found.")
        return
    
    category = session.query(Category).filter_by(category_id=category_id).first()
    if not category:
        print("Category not found.")
        return
    
    post = Post(title=title, content=content, author=user, category=category)
    session.add(post)
    session.commit()
    print("Post created successfully.")



def get_all_posts():
    """Retrieve and print all posts with user information."""
    session = Session()
    posts = session.query(Post).all()

    if not posts:
        print("No posts found.")
        return

    print("\n--- List of All Posts ---")
    for post in posts:
        print(f"Post ID: {post.post_id}, Title: {post.title}, Content: {post.content}, Author: {post.author.username}")

    print()



def get_post_by_id(post_id):
    """Retrieve and print a post by its ID with user information."""
    session = Session()
    post = session.query(Post).filter_by(post_id=post_id).first()

    if not post:
        print("Post not found.")
        return

    print("\n--- Post Details ---")
    print(f"Post ID: {post.post_id}, Title: {post.title}, Content: {post.content}, Author: {post.author.username}")
    print()



def get_posts_by_category(category_id):
    """Retrieve and print all posts by a specific category with user information."""
    session = Session()
    category = session.query(Category).filter_by(category_id=category_id).first()

    if not category:
        print("Category not found.")
        return

    posts = category.posts
    if not posts:
        print("No posts found in this category.")
        return
    
    print(f"\n--- Posts in Category: {category.name} ---")
    for post in posts:
        print(f"Post ID: {post.post_id}, Title: {post.title}, Content: {post.content}, Author: {post.author.username}")

    print()


def get_posts_by_user(user_id):
    """Retrieve and print all posts by a specific user."""
    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()

    if not user:
        print("User not found.")
        return

    posts = user.posts
    if not posts:
        print("No posts found for this user.")
        return
    
    print(f"\n--- Posts by User: {user.username} ---")
    for post in posts:
        print(f"Post ID: {post.post_id}, Title: {post.title}, Content: {post.content}")

    print()

    
def delete_post(post_id):
    """Delete a post by its ID."""
    session = Session()
    post = session.query(Post).filter_by(post_id=post_id).first()

    if not post:
        print("Post not found.")
        return

    session.delete(post)
    session.commit()
    print("Post deleted successfully.")

