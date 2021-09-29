import sys, requests

BITRISE_API_ACCESS_TOKEN = sys.argv[1]
APP_SLUG = sys.argv[2]
BUILD_SLUG = sys.argv[3]

BASE_URL = "https://api.bitrise.io/v0.1"
ARTIFACT_BASE_URL = BASE_URL + "/apps/" + APP_SLUG + "/builds/" + BUILD_SLUG + "/artifacts"
HEADERS = {
    "Authorization": BITRISE_API_ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def get_profile_artifact_slug():
    response = requests.get(ARTIFACT_BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        artifact_list_response = response.json()
        for artifact in artifact_list_response['data']:
            if artifact['title'] == 'profile.zip':
                return artifact['slug']

def print_artifact_url(slug):
    if slug is None:
        print("We could not get the artifact slug. Did you `--profile` your Gradle task?")
        return
    artifact_url = ARTIFACT_BASE_URL + "/" + slug
    response = requests.get(artifact_url, headers=HEADERS)
    if response.status_code == 200:
        artifact_response = response.json()
        print(artifact_response['expiring_download_url'])

artifact_slug = get_profile_artifact_slug()
print_artifact_url(artifact_slug)