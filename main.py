from secretkey import API_KEY
import requests
import json
import os
import openai
openai.api_key = os.getenv("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")
openai.Model.list()
