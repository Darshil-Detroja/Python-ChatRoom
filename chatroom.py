# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print("You are already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(self.username, "joined", chatroom.name)

    def leave_chatroom(self):
        if not self.chatroom:
            print("You are not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(self.username, "left", self.chatroom.name)
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print("Join a chatroom first.")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print("\nChat History:")
        for msg in self.messages:
            print(msg)
        print()


# -------------------------------
# Dynamic Menu Program
# -------------------------------
room = ChatRoom("Python Lounge")
users = {}

while True:
    print("\n--- CHAT MENU ---")
    print("1. Create User")
    print("2. Join Chatroom")
    print("3. Send Message")
    print("4. Show Chat History")
    print("5. Leave Chatroom")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter username: ")
        if name in users:
            print("User already exists.")
        else:
            users[name] = User(name)
            print("User created successfully.")

    elif choice == "2":
        name = input("Enter username: ")
        if name in users:
            users[name].join_chatroom(room)
        else:
            print("User not found.")

    elif choice == "3":
        name = input("Enter username: ")
        if name in users:
            msg = input("Enter message: ")
            users[name].send_message(msg)
        else:
            print("User not found.")

    elif choice == "4":
        room.show_chat_history()

    elif choice == "5":
        name = input("Enter username: ")
        if name in users:
            users[name].leave_chatroom()
        else:
            print("User not found.")

    elif choice == "6":
        print("Exiting chat system.")
        break

    else:
        print("Invalid choice.")
