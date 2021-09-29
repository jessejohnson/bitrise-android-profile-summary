import requests

BASE_URL = "https://api.bitrise.io/v0.1/"
BITRISE_API_ACCESS_TOKEN = sys.argv[1]
APP_SLUG = sys.argv[2]
BUILD_SLUG = sys.argv[3]

HEADERS = {
    "Authorization": BITRISE_API_ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def get_profile_artifact_slug():
    artifact_list_url = BASE_URL + "/apps/" + APP_SLUG + "/builds/" + BUILD_SLUG
    response = requests.get(artifact_list_url, headers=HEADERS)
    if response.status_code == 200:
        artifact_list_response = response.json()
        for artifact in artifact_list_response['data']:
            if artifact['title'] == 'profile.zip':
                return artifact['slug']

def print_artifact_url(slug):
    artifact_url = artifact_list_url + "/artifacts/" + slug
    response = requests.get(artifact_url, headers=HEADERS)
    if response.status_code == 200:
        artifact_response = response.json()
        print(artifact_response['expiring_download_url'])

artifact_slug = get_profile_artifact_slug()
print_artifact_url(artifact_slug)