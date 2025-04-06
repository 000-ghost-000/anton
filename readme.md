### this is anton a chatbot powered my mistral api to be my perosnal assistant 

to run anton a chatbot you need to have python installed on your computer. you can download the latest version of
python from the official python website. once you have python installed, you can install the required libraries by
running the following command in your terminal:
``` bash
pip install -r requirements.txt
```
create a virtual environment if you want to

the file structure of the codebase looks like this:
```grpgql
anton/
|---- .venv/
|------- |----- requirements.txt
|------- |----- .env
|--------|----- main.py
|--------|----- readme.md
```
the .env file looks like
```.env
MISTRAL_API_KEY="your api key"
MISTRAL_API_URL=https://api.mistral.ai/v1/chat/completions
QDRANT_HOST=localhost
QDRANT_PORT=6333
python-dotenv=1.0.1
```
