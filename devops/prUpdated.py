import os
import json

import requests  # Add this import

GREEN_TEXT = '\033[32m'
YELLOW_TEXT = '\033[33m'
RED_TEXT = '\033[31m'
BOLD_TEXT = '\033[1m'
RESET = '\033[0m'
CYAN_BG = '\033[46m'



pr_number = os.environ.get('PR_NUMBER')
github_repository = os.environ.get('GITHUB_REPOSITORY')
github_token = os.environ.get('TOKEN_GITHUB')
commit_id = os.environ.get('COMMIT_ID')


print(f"GitHub Repository: {github_repository}")
print(f"GitHub Token: {github_token}")
print(f"PR Number: {pr_number}")
print(f"commit_id: {commit_id}")

# Get the path to the PMD violations file
deployment_file = "deploymentResult.json"

try:
    with open(deployment_file, "r") as file:
        validation_result = json.load(file)
        print(json.dumps(validation_result))
except FileNotFoundError:
    print(f"{CYAN_BG}{RED_TEXT}Error: The file {deployment_file} was not found.{RESET}")
    exit(1)
except json.JSONDecodeError:
    print(f"{CYAN_BG}{RED_TEXT}Error: The file {deployment_file} is not a valid JSON file.{RESET}")
    exit(1)

