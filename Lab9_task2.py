import redis


class RecordTable:
    def __init__(self, host='localhost', port=6379, db=0, dr=True):
        self.r = redis.Redis(host=host, port=port, db=db, decode_responses=dr)
        self.username = None

    def create_user(self):
        username = input("Enter a new username: ")
        if self.r.hexists("users", username):
            print("Username already exists.")
            return
        password = input("Enter a new password: ")
        self.r.hset("users", username, password)
        print(f"User {username} created successfully.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        stored_password = self.r.hget("users", username)
        if stored_password and stored_password == password:
            print("Login successful!")
            self.username = username
        else:
            print("Invalid username or password.")

    def add_user_result(self):
        if not self.username:
            print("You must login first.")
            return
        score = int(input("Enter your score: "))
        self.r.zadd("highscores", {self.username: score})
        print(f"Added score {score} for user {self.username}.")

    def delete_user_result(self):
        if not self.username:
            print("You must login first.")
            return
        self.r.zrem("highscores", self.username)
        print(f"Deleted score for user {self.username}.")

    def update_user_result(self):
        if not self.username:
            print("You must login first.")
            return
        new_score = int(input("Enter your new score: "))
        self.r.zadd("highscores", {self.username: new_score})
        print(f"Updated score for user {self.username} to {new_score}.")

    def clear_table(self):
        self.r.delete("highscores")
        print("Cleared the high scores table.")

    def search_user_result(self):
        if not self.username:
            print("You must login first.")
            return
        score = self.r.zscore("highscores", self.username)
        if score:
            print(f"User {self.username} has a score of {score}.")
        else:
            print(f"No score found for user {self.username}.")

    def view_table(self):
        scores = self.r.zrange("highscores", 0, -1, withscores=True)
        print("High Scores Table:")
        for user, score in scores:
            print(f"{user}: {score}")

    def view_top_ten(self):
        top_scores = self.r.zrevrange("highscores", 0, 9, withscores=True)
        print("Top 10 High Scores:")
        for user, score in top_scores:
            print(f"{user}: {score}")

    def run(self):
        while True:
            print("\nRecord Table Menu:")
            print("1. Create new user")
            print("2. Login")
            print("3. Add result")
            print("4. Delete result")
            print("5. Update result")
            print("6. Clear table")
            print("7. Search result")
            print("8. View table")
            print("9. View top 10")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.add_user_result()
            elif choice == '4':
                self.delete_user_result()
            elif choice == '5':
                self.update_user_result()
            elif choice == '6':
                self.clear_table()
            elif choice == '7':
                self.search_user_result()
            elif choice == '8':
                self.view_table()
            elif choice == '9':
                self.view_top_ten()
            elif choice == '10':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    record_table = RecordTable()
    record_table.run()
