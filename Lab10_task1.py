import redis


class SocialNetwork:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        self.username = None

    def create_user(self):
        username = input("Enter a new username: ")
        if self.r.hexists(f"user:{username}", "password"):
            print("Username already exists.")
            return
        password = input("Enter a new password: ")
        name = input("Enter your full name: ")
        age = input("Enter your age: ")
        country = input("Enter your country: ")

        self.r.hset(f"user:{username}", mapping={
            "password": password,
            "name": name,
            "age": age,
            "country": country
        })
        print(f"User {username} created successfully.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        stored_password = self.r.hget(f"user:{username}", "password")
        if stored_password and stored_password == password:
            print("Login successful!")
            self.username = username
        else:
            print("Invalid username or password.")

    def delete_user(self):
        if not self.username:
            print("You must login first.")
            return
        self.r.delete(f"user:{self.username}")
        self.r.delete(f"friends:{self.username}")
        self.r.delete(f"posts:{self.username}")
        print(f"User {self.username} deleted successfully.")
        self.username = None

    def edit_user(self):
        if not self.username:
            print("You must login first.")
            return
        name = input("Enter your new full name: ")
        if not name:
            name = self.r.hget(f"user:{self.username}", "name")
        age = input("Enter your new age: ")
        if not age:
            age = self.r.hget(f"user:{self.username}", "age")
        country = input("Enter your new country: ")
        if not country:
            country = self.r.hget(f"user:{self.username}", "country")
        self.r.hset(f"user:{self.username}", mapping={
            "name": name,
            "age": age,
            "country": country
        })
        print("User information updated successfully.")

    def search_user(self):
        name = input("Enter the full name to search: ")
        for key in self.r.scan_iter("user:*"):
            if self.r.hget(key, "name") == name:
                print(f"User found: {key.split(':')[1]}")
                return
        print("User not found.")

    def view_user_info(self):
        if not self.username:
            print("You must login first.")
            return
        user_info = self.r.hgetall(f"user:{self.username}")
        if user_info:
            print(f"User Information for {self.username}:")
            for key, value in user_info.items():
                print(f"{key}: {value}")
        else:
            print("No information found for this user.")

    def view_friends(self):
        if not self.username:
            print("You must login first.")
            return
        friends = self.r.smembers(f"friends:{self.username}")
        if friends:
            print(f"Friends of {self.username}:")
            for friend in friends:
                print(friend)
        else:
            print("No friends found.")

    def view_posts(self):
        if not self.username:
            print("You must login first.")
            return
        posts = self.r.lrange(f"posts:{self.username}", 0, -1)
        if posts:
            print(f"Posts of {self.username}:")
            for post in posts:
                print(post)
        else:
            print("No posts found.")

    def add_friend(self):
        if not self.username:
            print("You must login first.")
            return
        friend_username = input("Enter the username of the friend to add: ")
        if self.r.hexists(f"user:{friend_username}", "password"):
            self.r.sadd(f"friends:{self.username}", friend_username)
            self.r.sadd(f"friends:{friend_username}", self.username)
            print(f"{friend_username} has been added to your friends list.")
        else:
            print("User not found.")

    def create_post(self):
        if not self.username:
            print("You must login first.")
            return
        post_content = input("Enter your post content: ")
        self.r.rpush(f"posts:{self.username}", post_content)
        print("Post created successfully.")


    def run(self):
        while True:
            print("\nSocial Network Menu:")
            print("1. Create new user")
            print("2. Login")
            print("3. Delete user")
            print("4. Edit user info")
            print("5. Search user by name")
            print("6. View user info")
            print("7. Add friend")
            print("8. Add post")
            print("9. View friends")
            print("10. View posts")
            print("enter. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.delete_user()
            elif choice == '4':
                self.edit_user()
            elif choice == '5':
                self.search_user()
            elif choice == '6':
                self.view_user_info()
            elif choice == '7':
                self.add_friend()
            elif choice == '8':
                self.create_post()
            elif choice == '9':
                self.view_friends()
            elif choice == '10':
                self.view_posts()
            elif choice == '':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    social_network = SocialNetwork()
    social_network.run()
