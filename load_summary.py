import json
from summary import print_summary

try:
    with open("requirements.json", "r") as file:
        requirements = json.load(file)

except FileNotFoundError:
    print("The file 'requirements.json' was not found.")

except json.JSONDecodeError as error:
    print(
        f"The file 'requirements.json' is not valid JSON. "
        f"Error at line {error.lineno}, column {error.colno}."
    )

except Exception:
    print("Something unexpected went wrong.")

else:
    print("Total requirements:", len(requirements))
    print_summary(requirements)