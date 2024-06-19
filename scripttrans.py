import re
from googletrans import Translator
import time

def translate_text(text, target_language='fr'):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original text if translation fails

def translate_document(input_file, output_file, target_language='fr'):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if ':' in line:
                key, value = line.split(':', 1)
                # Check if the value is quoted
                match = re.search(r"'(.*?)'", value)
                if match:
                    value_content = match.group(1)
                    translated_value = translate_text(value_content.strip(), target_language)
                    translated_line = f"{key}: '{translated_value}'\n"
                else:
                    translated_value = translate_text(value.strip(), target_language)
                    translated_line = f"{key}: {translated_value}\n"
                outfile.write(translated_line)
                # Print progress
                print(translated_line.strip())
                # Optional: add a small delay to avoid hitting API rate limits
                time.sleep(0.1)
            else:
                outfile.write(line)

# Specify input and output file paths
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# Call the function to translate the document
translate_document(input_file_path, output_file_path)
