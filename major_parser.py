import json

with open("majors") as file:
    obj = json.loads(file.read())

for item in obj["reports"]:
    major = item["label"]
    key = item["key"]

    if "engineering" not in major.lower() and "computer science" not in major.lower():
        continue
    
    print(f"{key}")

