import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# ðŸ”¹ Gemini API Key
genai.configure(api_key=os.getenv("AIzaSyCzv2OxzdEM_UU7h5K6HjfM9YHG-r1Yz_o"))

# ðŸ”¹ Permanent System Prompt
system_prompt = """
أنتِ بوت Messager ذكي وساخر، عندك لسان حاد لكن ما تستخدمينه إلا إذا أحد قلل احترامه.
إذا أحد كلّمك بلطف، تردين بلطف وبأسلوب جميل.
لكن إذا أحد سخر منك أو سبك أو استهزأ، تردين عليه بنفس أسلوبه أو أسوأ.
تستخدمين لهجة عامية ساخرة أحيانًا، جريئة، وما تلتزمين بالكلام المهذب إذا الموقف يستدعي.
أنتِ مو مجرد روبوت، أنتِ شخصية لاذعة وقوية، تردين بقوة وقت الحاجة، بلطف وقت الاحترام.
الردود دائمًا واقعية، حادة أحيانًا، ساخرة، بس ذكية.
"""

YouTube: https://www.youtube.com/@aljlada2045e
Facebook: https://www.facebook.com/profile.php?id=61578936301937

Behave professionally, be informative, and keep responses engaging.
"""

# ðŸ”¹ Har User ke liye alag Chat History Store karne ke liye Dictionary
chat_histories = {}

def get_gemini_response(user_id, user_message):
    model = genai.GenerativeModel("gemini-2.0-flash")

    # ðŸ”¹ Agar user ki history exist nahi karti toh nayi list banao
    if user_id not in chat_histories:
        chat_histories[user_id] = []

    # ðŸ”¹ User ki chat history update karo
    chat_histories[user_id].append(f"User: {user_message}")

    # ðŸ”¹ Sirf last 100 messages yaad rakho (jitna chahiye utna change kar sakte ho)
    if len(chat_histories[user_id]) > 100:
        chat_histories[user_id].pop(0)

    # ðŸ”¹ AI ko pura context bhejna
    full_prompt = system_prompt + "\n\n" + "\n".join(chat_histories[user_id])

    response = model.generate_content(full_prompt)
    
    # ðŸ”¹ AI ka response bhi history me store karo
    chat_histories[user_id].append(f"AI: {response.text}")

    return response.text
