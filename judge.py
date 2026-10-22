import json

def parse_answer(text):
    try:
        data = json.loads(text)
        return data["requires_german"]
    except (json.JSONDecodeError, KeyError): 
        return None

print("result:", parse_answer('{"requires_german": true}'))
print("result:", parse_answer('{"requires_german": false}'))
print("result:", parse_answer('Yes, German is required.'))
print("result:", parse_answer(''))
print("result:", parse_answer('{"answer": true}'))