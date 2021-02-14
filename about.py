import json
from rich import print

def about():
    f = open('license.json')
    data = json.load(f)

    print("[bold red]Developer: [/bold red]" + data.get("developer"))
    print("[bold red]Version: [/bold red]" + str(data.get("version")))
    print("[bold red]Programming Language: [/bold red]" + data.get("programming language"))

    f.close()