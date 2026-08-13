import requests;
import json;

url="https://api.ejolabs.com/api/v1/subiza"

headers={
    "X-API-Key": "ejochat_1_E32pR40CaEQHL6e2zJ0M17LHxUxL-FFWKqYSrpmg8"
}

name= input("What is your name?: ")

print(f"Nice to meet you {name}!")
print("Ask EjoChat anything you want, or type exit to stop")

while True:
    question= input("Your question: ")

    if question.lower()== "exit":
        print(f"Goodbye {name}!")
        break
    data={
        "messages": [
            {
                "role":"user",
                "content":question
            }
        ]
    }

    response= requests.post(
        url,
        headers=headers,
        json=data
    )

    answer= response.json()["choices"][0]["message"]["content"]
    print(answer)

