import os
import re

def remove_emojis(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002700-\U000027BF"
        u"\U0001F900-\U0001F9FF"
        u"\U00002600-\U000026FF"
        u"\U00002B00-\U00002BFF"
        u"\U0001FA70-\U0001FAFF"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith((".py", ".md", ".txt", ".ipynb")):
            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()
            cleaned = remove_emojis(data)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(cleaned)
