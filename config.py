# config.py
import os

# Set your IBM WatsonX API credentials here
IBM_WATSON_API_KEY = os.getenv("IBM_WATSON_API_KEY", "Kvxo-7GDEUOp2tp9iAnVrdwzoUGmPoFT4NB67iZa772X")
IBM_WATSON_API_URL = os.getenv("IBM_WATSON_API_URL", "https://us-south.ml.cloud.ibm.com")

# You can set these as environment variables or directly in this file for simplicity
MODEL_NAME = "ibm/granite-13b-chat-v2"
