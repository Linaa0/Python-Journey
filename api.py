import requests
import json 
# from IPython.display import Markdown, display

question="What is the weather today in Kigali?"

url= "https://api.ejolabs.com/api/v1/subiza"

headers= {
   "X-API-Key": "ejochat_1_E32pR40CaEQHL6e2zJ0M17LHxUxL-FFWKqYSrpmg8"
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
result = response.json()

clean_text = result['choices'][0]['message']['content']

print("\n--- AI Response ---")
print(clean_text)