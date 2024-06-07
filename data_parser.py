import json
from collections import defaultdict

# uni => major
offers_major = defaultdict(set)
# uni => class
offers_class = defaultdict(set)

and_id = 0
or_id = 0
unis = set()
ccs = set()
majors = set()
with open("data2") as file:
    for line in file.read().splitlines():
        obj = json.loads(line)

        result = obj["result"]

        major = result["name"]

        recv = json.loads(result["receivingInstitution"])
        recv_name = recv["names"][0]["name"]

        send = json.loads(result["sendingInstitution"])
        send_name = send["names"][0]["name"]

        if send_name == "Kings River College":
            send_name = "Reedley College"

        offers_major[recv_name].add(major)

        tmpl = json.loads(result["articulations"])

        unis.add(recv_name)
        ccs.add(send_name)
        majors.add(major)

        for elem in tmpl:
            art = elem["articulation"]
            and_ids = []

            or_group = []
            for item in art["sendingArticulation"]["items"]:
                group = []
                for req in item["items"]:
                    name = req["prefix"] + " " + req["courseNumber"]

                    offers_class[send_name].add(name)

                    group.append('"' + name + '"')

                if group:
                    for course in group:
                        print(f"req_and({and_id},{course})")
                    and_ids.append(str(and_id))
                    and_id += 1

            for aid in and_ids:
                print(f"req_or({or_id},{aid})")

            print(f'requires("{send_name}", "{recv_name}", "{major}", {or_id})')

            or_id += 1

for cc in offers_class.keys():
    for cls in offers_class[cc]:
        print(f'offers_class("{cc}", "{cls}")')

for uni in offers_major.keys():
    for major in offers_major[uni]:
        print(f'offers_major("{uni}", "{major}")')

for uni in unis:
    print(f'university("{uni}")')

for cc in ccs:
    print(f'college("{cc}")')

for major in majors:
    print(f'major("{major}")')
