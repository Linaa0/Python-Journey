import requests
import json 
from IPython.display import Markdown, display

question="What is the weather today in Kigali?"

url= "https://api.ejplabs.com/api/v1/subiza"

headers= {
   "X-API-Key": ""
 }

data= {
    "messages":[
        {
          "role":"user",
          "content": question
       } 

    ]
}

response= requests.post(
    url,
    headers=headers,
    json=data
)

print(response.json())