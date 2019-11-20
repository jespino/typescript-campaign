import requests
import click
from requests.auth import HTTPBasicAuth

@click.command()
@click.option('--username', prompt='Your username', help='Username of the user to publish the new user story.')
@click.option('--token', prompt='Your user token', help='The token used to authenticate the user.')
@click.option('--path', prompt='Path', help='Path')
def cli(username, token, path):
    template = open("template.md").read()

    summary = "Migrate '{}' module and associated tests to TypeScript".format(path)

    description = template.replace("{{path}}", path)

    data = {
        "fields": {
            "project": {"key": "MM"},
            "assignee": {"name": "5bb21f2d7b7a444735b36e7c"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Story"},
            "customfield_11101": {"value": "Apps"},
            "customfield_10007": "MM-18907",
        }
    }

    resp = requests.post(
        "https://mattermost.atlassian.net/rest/api/2/issue/",
        json=data,
        auth=HTTPBasicAuth(username, token)
    )
    print(resp.json())
    print("https://mattermost.atlassian.net/browse/{}".format(resp.json()['key']))

if __name__ == "__main__":
    cli()
