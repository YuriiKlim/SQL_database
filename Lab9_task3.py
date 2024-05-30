import redis

class NewsFeed:
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

    def add_news(self):
        if not self.username:
            print("You must login first.")
            return
        news = input("Enter news content: ")
        timestamp = self.r.time()[0]
        self.r.zadd("news_feed", {news: timestamp})
        self._trim_news_feed()
        print("News added successfully.")

    def delete_news(self):
        if not self.username:
            print("You must login first.")
            return
        news = input("Enter the news content to delete: ")
        self.r.zrem("news_feed", news)
        print("News deleted successfully.")

    def update_news(self):
        if not self.username:
            print("You must login first.")
            return
        old_news = input("Enter the old news content to update: ")
        if self.r.zscore("news_feed", old_news):
            new_news = input("Enter the new news content: ")
            timestamp = self.r.time()[0]
            self.r.zrem("news_feed", old_news)
            self.r.zadd("news_feed", {new_news: timestamp})
            self._trim_news_feed()
            print("News updated successfully.")
        else:
            print("News not found.")

    def clear_news_feed(self):
        self.r.delete("news_feed")
        print("News feed cleared.")

    def view_news_feed(self):
        news = self.r.zrevrange("news_feed", 0, -1, withscores=False)
        print("News Feed:")
        for item in news:
            print(item)

    def view_latest_news(self):
        latest_news = self.r.zrevrange("news_feed", 0, 0, withscores=False)
        if latest_news:
            print("Latest News:")
            print(latest_news[0])
        else:
            print("No news available.")

    def _trim_news_feed(self):
        self.r.zremrangebyrank("news_feed", 0, -11)

    def run(self):
        while True:
            print("\nNews Feed Menu:")
            print("1. Create new user")
            print("2. Login")
            print("3. Add news")
            print("4. Delete news")
            print("5. Update news")
            print("6. Clear news feed")
            print("7. View news feed")
            print("8. View latest news")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.add_news()
            elif choice == '4':
                self.delete_news()
            elif choice == '5':
                self.update_news()
            elif choice == '6':
                self.clear_news_feed()
            elif choice == '7':
                self.view_news_feed()
            elif choice == '8':
                self.view_latest_news()
            elif choice == '9':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    news_feed = NewsFeed()
    news_feed.run()
