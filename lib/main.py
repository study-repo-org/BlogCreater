from database import create_db
from blog.user import create_user, get_all_users, get_user_by_id
from blog.category import create_category , get_all_categories
from blog.blog import create_post, get_all_posts, get_post_by_id, get_posts_by_category, get_posts_by_user, delete_post
from art import text2art

def welcome_message(color="red"):
    # Generate ASCII art
    art = text2art("Blog Creater")
    
    # ANSI escape codes for color
    color_code = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }
    
    # Print ASCII art with color
    print(color_code[color] + art + color_code["reset"])

def main():
    welcome_message("green")

    create_db()
    # Main menu for Blog Creater.
    while True:
        print("1. Create a user")
        print("2. Create a category")
        print("3. Create a post")
        print("4. Get all users")
        print("5. Get user by ID")
        print("6. Get all categories")
        print("7. Get all posts")
        print("8. Get post by ID")
        print("9. Get posts by category")
        print("10. Get posts by user")
        print("11. Delete a post")
        print("12. Exit")
        choice = input("Enter a number: ")

        if choice == '1':
            create_user_prompt()
        elif choice == '2':
            create_category_prompt()
        elif choice == '3':
            create_post_prompt()
        elif choice == '4':
            get_all_users()
        elif choice == '5':
            get_user_by_id_prompt()
        elif choice == '6':
            get_all_categories()
        elif choice == '7':
            get_all_posts()
        elif choice == '8':
            get_post_by_id_prompt()
        elif choice == '9':
            get_posts_by_category_prompt()
        elif choice == '10':
            get_posts_by_user_prompt()
        elif choice == '11':
            delete_post_prompt()
        elif choice == '12':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")


def create_user_prompt():
    # Prompting user to create a user.
    username = input("Enter username: ")
    create_user(username=username)
    print()

def create_category_prompt():
    # Prompting user to create a category.
    name = input("Enter category name: ")
    create_category(name=name)
    print()

def create_post_prompt():
    # Prompting user to create a post.
    user_id = input("Enter user ID: ")
    title = input("Enter post title: ")
    content = input("Enter content: ")
    category_id = input("Enter category ID: ")
    create_post(user_id=user_id, title=title, content=content, category_id=category_id)
    print()

def get_user_by_id_prompt():
    # Prompting user for input and retrieve a user by their ID.
    user_id = int(input("Enter user ID: "))
    get_user_by_id(user_id)
    print()

def get_post_by_id_prompt():
    # Prompting user for input and retrieve a post by its ID.
    post_id = int(input("Enter post ID: "))
    get_post_by_id(post_id)
    print()

def get_posts_by_category_prompt():
    # Prompting user for input and retrieve posts by category.
    category_id = int(input("Enter category ID: "))
    get_posts_by_category(category_id)
    print()

def get_posts_by_user_prompt():
    # Prompting user for input and retrieve posts by user.
    user_id = int(input("Enter user ID: "))
    get_posts_by_user(user_id)
    print()

def delete_post_prompt():
    # Prompting user for input and delete a post.
    post_id = int(input("Enter post ID to delete: "))
    delete_post(post_id)
    print()

if __name__ == '__main__':
    main()
