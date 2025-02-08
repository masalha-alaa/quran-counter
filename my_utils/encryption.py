import keyring

SERVICE_NAME = "QuranCounter"
USER_NAME = "QuranCounter"

def save_api_key(api_key):
    keyring.set_password(SERVICE_NAME, USER_NAME, api_key)

def get_api_key():
    return keyring.get_password(SERVICE_NAME, USER_NAME)
