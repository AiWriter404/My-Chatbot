import time

def slow_type(text: str, delay: float = 0.12) -> None:
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

if __name__ == "__main__":
    user_text = input("Type something to print slowly: ")
    slow_type(user_text)
    
    import time

def word_by_word(text: str, delay: float = 0.4) -> None:
    for word in text.split():
        print(word, end=" ")
        time.sleep(delay)
    print()

if __name__ == "__main__":
    user_text = input("Enter a sentence: ")
    word_by_word(user_text)
    
for char in user_text:
    print(char, end="", flush=True)
    time.sleep(0.12)
    