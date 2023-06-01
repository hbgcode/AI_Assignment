from langdetect import detect

def identify_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unable to identify language"
text1 = "Hello Wolrd?"
text2 = "ギーク向けのコンピューターサイエンスポータルです。"
text3 = "это компьютерный портал для гиков"
language1 = identify_language(text1)
print("Detected language:", language1)
language2 = identify_language(text2)
print("Detected language:", language2)
language3 = identify_language(text3)
print("Detected language:", language3)



