import json

def judge_job(description, ask):
    answer = ask(description)
    return parse_answer(answer)

def parse_answer(text):
    try:
        data = json.loads(text)
        return data["requires_german"]
    except (json.JSONDecodeError, KeyError): 
        return None
