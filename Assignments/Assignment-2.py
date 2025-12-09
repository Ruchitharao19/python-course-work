n = int(input("Enter the number of messages: "))
data = {}
messages = [] 
for i in range(n):
    raw = input()
    name, msg = raw.split(":", 1)
    name = name.strip()
    msg = msg.strip()
    messages.append((name, msg))
    if name in data:
        data[name].append(msg)
    else:
        data[name] = [msg]
choices = {
    1: 'Count total number of messages',
    2: 'Identify unique users in the chat',
    3: 'Count total words in the chat',
    4: 'Calculate average words per message',
    5: 'Find the longest message sent',
    6: 'Find the most active user',
    7: 'Get message count for a specific user',
    8: 'Find the most frequently used word by a specific user',
    9: 'Retrieve the first and last message sent by a user',
    10: 'Check if a user is present in the chat',
    11: 'Find commonly repeated words',
    12: 'Identify the user with the longest average message length',
    13: 'Count how many messages mention a specific user',
    14: 'Remove duplicate messages',
    15: 'Sort messages alphabetically',
    16: 'Extract all questions asked in the chat',
    17: 'Calculate the reply ratio between two users',
    18: 'Check for deleted messages',
    20: 'Exit'
}

from collections import Counter
while True:
    print("\n----- Analysis Options -----")
    for i in choices:
        print(f"{i}. {choices[i]}")

    ch = int(input("Enter the choice: "))

    # -------------------- 1 --------------------
    if ch == 1:
        print(f"Total messages: {len(messages)}")

    # -------------------- 2 --------------------
    elif ch == 2:
        print("Unique users in the chat:", set(data.keys()))

    # -------------------- 3 --------------------
    elif ch == 3:
        total_words = sum(len(msg.split()) for _, msg in messages)
        print("Total words in the chat:", total_words)

    # -------------------- 4 --------------------
    elif ch == 4:
        total_words = sum(len(msg.split()) for _, msg in messages)
        avg = total_words / len(messages)
        print(f"Average words per message: {avg:.2f}")

    # -------------------- 5 --------------------
    elif ch == 5:
        longest = max(messages, key=lambda x: len(x[1]))
        print(f'Longest message: "{longest[0]}: {longest[1]}"')

    # -------------------- 6 --------------------
    elif ch == 6:
        most_active = max(data, key=lambda x: len(data[x]))
        print(f"Most active user: {most_active} ({len(data[most_active])} messages)")

    # -------------------- 7 --------------------
    elif ch == 7:
        user = input("Enter user name: ").strip()
        if user in data:
            print(f"Messages sent by {user}: {len(data[user])}")
        else:
            print(f"User '{user}' not found in the chat.")

    # -------------------- 8 --------------------
    elif ch == 8:
        user = input("Enter user name: ").strip()
        if user not in data:
            print(f"User '{user}' not found in the chat.")
        else:
            words = []
            for msg in data[user]:
                words.extend(msg.lower().split())

            if words:
                freq = Counter(words).most_common(1)[0][0]
                print(f'Most frequent word used by {user}: "{freq}"')
            else:
                print(f"No words found for {user}.")

    # -------------------- 9 --------------------
    elif ch == 9:
        user = input("Enter user name: ").strip()
        if user not in data:
            print(f"User '{user}' not found in the chat.")
        else:
            msgs = data[user]
            print(f'First message by {user}: "{user}: {msgs[0]}"')
            print(f'Last message by {user}: "{user}: {msgs[-1]}"')

    # -------------------- 10 --------------------
    elif ch == 10:
        user = input("Enter user name: ").strip()
        if user in data:
            print(f"User '{user}' is present in the chat.")
        else:
            print(f"User '{user}' not found in the chat.")

    # -------------------- 11 --------------------
    elif ch == 11:
        all_words = []
        for _, msg in messages:
            all_words.extend(msg.lower().split())
        repeated = {w for w, c in Counter(all_words).items() if c > 1}
        print("Common repeated words:", repeated)

    # -------------------- 12 --------------------
    elif ch == 12:
        avg_len = {}
        for user in data:
            total = sum(len(msg.split()) for msg in data[user])
            avg_len[user] = total / len(data[user])

        best = max(avg_len, key=avg_len.get)
        print(f"User with longest average message: {best} (avg {avg_len[best]:.2f} words)")

    # -------------------- 13 --------------------
    elif ch == 13:
        target = input("Enter user name to search in messages: ").lower()
        count = sum(1 for _, msg in messages if target in msg.lower())
        print(f"Messages mentioning '{target}': {count}")

    # -------------------- 14 --------------------
    elif ch == 14:
        unique = list(dict.fromkeys(messages))
        print(f"Unique messages count: {len(unique)}")
        for name, msg in unique:
            print(f"{name}: {msg}")

    # -------------------- 15 --------------------
    elif ch == 15:
        sorted_msgs = sorted([f"{name}: {msg}" for name, msg in messages])
        print("Messages sorted alphabetically:")
        for m in sorted_msgs:
            print(m)

    # -------------------- 16 --------------------
    elif ch == 16:
        questions = [f"{name}: {msg}" for name, msg in messages if "?" in msg]
        print("Questions in the chat:")
        for q in questions:
            print(q)

    # -------------------- 17 --------------------
    elif ch == 17:
        user1 = input("Enter User A: ").strip()
        user2 = input("Enter User B: ").strip()

        replies = sum(1 for _, msg in messages if msg.lower().startswith(user1.lower()))
        print(f"Reply ratio from {user2} to {user1}: {replies} replies")

    # -------------------- 18 --------------------
    elif ch == 18:
        deleted_count = sum(1 for _, msg in messages if msg == "This message was deleted")
        print(f"Deleted messages found: {deleted_count}")

    # -------------------- EXIT --------------------
    elif ch == 20:
        print("End of program.")
        break

    else:
        print("Invalid choice. Try again.")
