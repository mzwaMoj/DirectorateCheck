from PyPDF2 import PdfReader
# import docx
import textract
import pandas as pd

# List of director words in different languages
director_words = [
    "Direkteure",              # Afrikaans
    "director",                # English
    "diretor",                # Portuguese
    "gamdok",           # Korean
    "directeur",              # French (company)
    "director",              # Spanish
    "regista",                # Italian (film)
    "kantoku",                 # Japanese (director)
    "duàn zhǎng",             # Mandarin Chinese (director)
    "duan zhang",             # Mandarin Chinese (director)
    "rezhisser",              # Russian (film)
    "mudīr",                   # Arabic (director)
    "nideshak",                # Hindi (director)
    "dyrektor",               # Polish
    "regisseur",              # Dutch (film)
    "regissör",               # Swedish (film)
    "regissor",               # Swedish (film)
    "yönetmen",               # Turkish
    "yonetmen",               # Turkish
    "Direktur",               # Indonesian (director)
    "menahal",                # Hebrew (general manager)
    "johtaja",                # Finnish
    "đạo diễn",               # Vietnamese
    "dao dien",               # Vietnamese

    # African Languages
    "አስተዳዳሪ (astedaderi)",  # Amharic
    "mkurugenzi",             # Swahili
    "darakta",                 # Hausa
    "olórí ìgbó",              # Yoruba
    "olori igbo",              # Yoruba
    "onye nduzi",              # Igbo
    "umqondisi",              # Zulu
]

def check_keywords_in_document(file_path, keywords):
    try:
        if file_path.lower().endswith('.docx'):
            text = textract.process(file_path).decode('utf-8')
        elif file_path.lower().endswith('.pdf'):
            # Initialize a PDF reader
            reader = PdfReader(file_path)
            text = ""
            # Iterate over each page and extract text
            for page in reader.pages:
                text += page.extract_text() + "\n"
        else:
            return "Unsupported file format.", []

        found_keywords = [keyword for keyword in keywords if keyword.lower() in text.lower()]
        found_keywords = list(set(found_keywords))
        return "Keywords found." if found_keywords else "No keywords found.", found_keywords
    except Exception as e:
        return f"Error extracting text: {e}", []



