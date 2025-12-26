import requests
import time
import json

# slow_type فنکشن - آہستہ آہستہ ٹیکسٹ دکھانے کے لیے 
API_KEY = "AIzaSyDCcQn7u54B6JI6ILBK9Igo8ry7NSVBjdA"
URL = URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def ask_gemini(prompt):
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(URL, json=data)
        result = response.json()
        
        # Ye line humein terminal mein bataye gi ke Google bhej kya raha hai
        print("\n--- DEBUG INFO ---")
        print(result) 
        print("------------------\n")

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Google ne 'candidates' nahi bhejay. Debug info check karein."
            
    except Exception as e:
        return f"Oho! Thora masla aa gaya hai: {e}"

# --- MAIN PROGRAM ---
print("🤖 Umar Ka Bot Tayyar Hai! (Exit likh kar band karein)")

while True:
    user_input = input("\n👤 Aap: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("🤖 Bot: Allah Hafiz! Phir milte hain.")
        break
    
    print("🤖 Bot soch raha hai...", end="\r")
    bot_response = ask_gemini(user_input)
    
    # Typing effect ke saath jawab dikhana
    print("🤖 Bot: ", end="")
    for char in bot_response:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()
    

