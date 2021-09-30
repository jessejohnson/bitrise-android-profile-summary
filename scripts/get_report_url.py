import sys, os, requests

BITRISE_API_ACCESS_TOKEN = sys.argv[1]
APP_SLUG = sys.argv[2]
BUILD_SLUG = sys.argv[3]
ARTIFACT_URL_MAP = os.environ['BITRISE_PERMANENT_DOWNLOAD_URL_MAP']

BASE_URL = "https://api.bitrise.io/v0.1"
ARTIFACT_BASE_URL = BASE_URL + "/apps/" + APP_SLUG + "/builds/" + BUILD_SLUG + "/artifacts"
HEADERS = {
    "Authorization": BITRISE_API_ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def get_permanent_download_url():
    if ARTIFACT_URL_MAP is not None:
        artifacts = ARTIFACT_URL_MAP.split("|")
        for artifact in artifacts:
            if "profile.zip" in artifact:
                return artifact.split("=>")[1]
    return None

def get_profile_artifact_slug():
    response = requests.get(ARTIFACT_BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        artifact_list_response = response.json()
        for artifact in artifact_list_response['data']:
            if artifact['title'] == 'profile.zip':
                return artifact['slug']

def get_artifact_url(slug):
    if slug is None:
        print("We could not get the artifact slug. Did you `--profile` your Gradle task?")
    artifact_url = ARTIFACT_BASE_URL + "/" + slug
    response = requests.get(artifact_url, headers=HEADERS)
    if response.status_code == 200:
        artifact_response = response.json()
        return artifact_response['data']['expiring_download_url']

download_url = get_permanent_download_url()
if download_url is None:
    artifact_slug = get_profile_artifact_slug()
    download_url = get_artifact_url(artifact_slug)

print(download_url)