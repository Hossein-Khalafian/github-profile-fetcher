import requests

def get_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    if "name" not in data:
        return None
    return data

def build_report(username):
    data = get_user(username)
    if data is None:
        return f"{username} - not found"
    return f"{data['name']} - {data['public_repos']} repos"

def save_report(lines, filename):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

names = ["Hossein-Khalafian", "torvalds", "gvanrossum"]

reports = []
for n in names:
    reports.append(build_report(n))

for r in reports:
    print(r)

save_report(reports, "report.txt")