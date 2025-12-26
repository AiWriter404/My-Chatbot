import os
import time
import google.generativeai as genai

# slow_type فنکشن - آہستہ آہستہ ٹیکسٹ دکھانے کے لیے
def slow_type(text: str, delay: float = 0.03) -> None:
    """ہر حرف کو تھوڑی دیر میں پرنٹ کرتا ہے ٹائپرائٹر_effect کے لیے"""
    for char in text:
        print(char, end="", flush=True)  # بغیر نئی لائن پرنٹ کریں
        time.sleep(delay)  # تھوڑی دیر رکیں
    print()  # آخری لائن کے لیے

# Gemini API کنفیگر کریں
# یہاں اپنا API key پیسٹ کریں 👇
genai.configure(api_key="AIzaSyDL1P1P_5R_2C7XB3cdRrnEEHjLwYFyOXQ")
# یا environment variable استعمال کریں:
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini ماڈل بنائیں
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# چیٹ سیشن شروع کریں (یہ میموری رکھتا ہے)
chat = model.start_chat(history=[])

print("🤖 Google Gemini AI Bot Is Start ! 'exit' Or 'quit' Leave the Model")

while True:  # لامحدود لوپ جب تک صارف باہر نہ نکلے
    user_input = input("\n👤 Welcome: ").strip()
    
    # چیک کریں کہ صارف باہر نکلنا چاہتا ہے
    if user_input.lower() in ['exit', 'quit']:
        print("👋Bye See You Later")
        break
    
    try:
        # Gemini API کو کال کریں
        response = chat.send_message(user_input)
        ai_response = response.text
        
        # آہستہ آہستہ AI کا جواب دکھائیں
        print("\n🤖 AI: ", end="")
        slow_type(ai_response)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print(" Meet Your GEMINI_API_KEY Try It Now")
# OpenAI (پہلے)
