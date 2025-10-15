**Azure AI Translator Service:**
This repository demonstrates how to integrate Azure AI Translator into your applications to perform real-time text translation, and language detection.

**Features:**

1. Translate text.
2. Detect languages.
3. Secure key management using Azure Key Vault and environment variables
4. Example scripts for Python SDKs

**Tech Stack:**

1. Azure AI Translator
2. Azure Key Vault
3. Python, Jupiter Notebook

**Examples taken in translator.ipynb file:**

1. Code | Language-Name | Native Name
2. cs | Czech | Čeština
3. de | German | Deutsch
4. es | Spanish | Español

**Quick Start:**

1. Create an Azure Translator resource in Azure Portal.
2. Set your API key, add it to jupiter python file.
3. Run the file.

**English Input String : en**
Hello Alians!!

**Translated Output String : cs,es,de**

1. Source input text : [{'text': 'Hello Alians!!'}]
2. Detected languages of the input text: en with score: 0.95.
3. Text was translated to: 'cs' and the result is: 'Ahoj Aliáni!!'.
4. Text was translated to: 'es' and the result is: '¡Hola Alians!'.
5. Text was translated to: 'de' and the result is: 'Hallo Alians!!'.
