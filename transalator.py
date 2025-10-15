from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.core.exceptions import HttpResponseError

apiKey="REPLACE_WITH_YOUR_KEY"
region = "westus"
endpoint = "https://api.cognitive.microsofttranslator.com/"

credential = TranslatorCredential(apiKey, region)
text_translator = TextTranslationClient(region=region, credential=credential)

def translate_text(text, to_language):
    try:
    to_language = ["cs", "es", "de"]
    input_text_elements = [{"text": "Hello Alians!!"}]

    response = text_translator.translate(content=input_text_elements, to=to_language)
    translation = response[0] if response else None

    if translation:
        detected_language = translation.detected_language
        if detected_language:
            print(f"Source input text : {input_text_elements}" )
            print(
                f"Detected languages of the input text: {detected_language.language} with score: {detected_language.score}."
            )
        for translated_text in translation.translations:
            print(f"Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")

except HttpResponseError as exception:
    if exception.error is not None:
        print(f"Error Code: {exception.error.code}")
        print(f"Message: {exception.error.message}")