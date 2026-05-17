import streamlit as st
from groq import Groq
import os

# ✅ Load Groq API key from Hugging Face Secrets
api_key = os.getenv("apikey")
client = Groq(api_key=api_key)

# 🌐 Supported Languages
LANGUAGES = {
    "French": "French",
    "Spanish": "Spanish",
    "Urdu": "Urdu",
    "German": "German",
    "Chinese": "Chinese",
    "Arabic": "Arabic",
    "Turkish": "Turkish",
    "Russian": "Russian",
    "Japanese": "Japanese",
    "Korean": "Korean"
}

# ✅ Streamlit App UI
st.set_page_config(page_title="🌍 Translation App", layout="centered")
st.title("🌍 English to Any Language Translator")
st.markdown("🚀 Powered by **Groq LLaMA 3.3 70B**")

text = st.text_area("✍️ Enter English text:")
target_lang = st.selectbox("🌐 Choose target language:", list(LANGUAGES.keys()))

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some English text.")
    else:
        prompt = f"Translate the following English sentence to {LANGUAGES[target_lang]}:\n\n'{text}'\n\nTranslation:"
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-70b-8192"
            )
            translation = response.choices[0].message.content.strip()
            st.success("✅ Translation completed!")
            st.markdown(f"**🔄 Translated Text ({LANGUAGES[target_lang]}):**")
            st.markdown(f"> {translation}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")
st.caption("Made with ❤️ by Maheen Touqeer")
