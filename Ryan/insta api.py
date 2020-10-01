import requests
import json
import webbrowser

"""
stuff im going to ignore:
#token = requests.get("https://api.instagram.com/oauth/authorize", client_id=app_ID, redirect_uri=redirect_url,
#                     response_type=response_type, scope=scope)
#auth = requests.get("https://api.instagram.com/oauth/authorize", client_id=app_ID, redirect_uri=redirect_uri,
#                    response_type="code", scope=scope)

#response = requests.get("https://graph.instagram.com/me", access_token=token)
#print(response.text)

"""

app_ID = "1004426776670453"
app_secret = "e6bd17669d0319334884ed26293acd08"
redirect_uri = "https://essentialsandypercent.ryno8.repl.co/"

def get_code():
    """returns https://developers.facebook.com/docs/instagram-basic-display-api/overview#authorization-window"""
    """https://developers.facebook.com/docs/instagram-basic-display-api/reference/oauth-authorize"""
    allData = {"client_id": app_ID,
               "redirect_uri": redirect_uri,
               "response_type": "code",
               "scope": "user_profile"}
    url = "https://api.instagram.com/oauth/authorize?" + "&".join([k+"="+v for k, v in allData.items()])
    webbrowser.open(url)
    return input("Enter the code received: ")[:-2]

def get_short_access_token(code):
    """returns {"access_token": str, ???}"""
    """https://developers.facebook.com/docs/instagram-basic-display-api/reference/oauth-access-token"""
    allData = {"client_id": app_ID,
               "client_secret": app_secret,
               "code": code,
               "grant_type": "authorization_code",
               "redirect_uri": redirect_uri}
    short_access = requests.post("https://api.instagram.com/oauth/access_token", data=allData)
    return json.loads(short_access.text)

def get_long_access_token(short_access_token):
    """returns {"access_token": str, "token_type": str, "expires_in": str}"""
    """https://developers.facebook.com/docs/instagram-basic-display-api/reference/access_token"""
    allData = {"grant_type": "ig_exchange_token",
               "client_secret": app_secret,
               "access_token": short_access_token}
    long_access = requests.get("https://graph.instagram.com/access_token", params=allData)
    return json.loads(long_access.text)

def get_profile(user_id, access_token):
    """returns ..."""
    """https://developers.facebook.com/docs/instagram-basic-display-api/reference/user"""
    allData = {"fields": "account_type,id,ig_id,media_count,username",
               "access_token": access_token}
    media = requests.get(f"https://graph.instagram.com/{user_id}/?", params=allData)
    return json.loads(media.text)

def get_media(user_id, access_token):
    """returns {"data": [...], "paging": {...}}"""
    """https://developers.facebook.com/docs/instagram-basic-display-api/reference/user/media"""
    allData = {"fields": "caption,id,media_type,media_url,permalink,thumbnail_url,timestamp,username",
               "access_token": access_token}
    media = requests.get(f"https://graph.instagram.com/{user_id}/media?", params=allData)
    return json.loads(media.text)


#code = get_code()
code = "AQAG4ZXALCjSwUf64PhjSE4yER6re9w4wWjnvPtn89koteQK1-aggH3ETQR5ytdfW1GL1Ad7EiOj39TENhGqFh29Ejk5jAqifnpL0iAnLx86xQ4AH2-7_Bgk_bpwLb8vE0MAXTnA5nOOcKHtwqq-qGhYqGubKw72NYwS6-wW40ZvxYhH824I7CwuAyb0GtgjwmKI6QYtofAtjB6fSrQ370tDonCgkZ5nYxs0TeItE0ibbA"
print("CODE:", code)


#short_access = get_short_access_token(code)
#short_access_token = short_access["access_token"]
short_access_token = "IGQVJXc0JOWllodkdrbmtOMzdMSTN4amN2V3hBbTN1YVFNVEs2U21sa0lEdG91a0hzZATkwUklaWVdVaTdaY21ZAYnlEcnpqT3VBcll2cjBCemctZAENsNElyS1UzNDFEcV9kQXF6TmZAsLXQ4LUVoeExTMWlTT2dUZAkZADMTYw"
print("ACCESS TOKEN:", short_access_token)
#user_id = short_access["user_id"]
user_id = "17841407758337629"
print("USER ID:", user_id)

#long_access_token = get_long_access_token(short_access_token)["access_token"]
long_access_token = "IGQVJVeTNhLXN4ZAUdSa1BoTDFFNTgxVXU2VEd6dENwRC1XVmZAlUmxKRDRfTTFPQmNuWG5yVU1XV0FvLS1fWGF2aXNmWG1GdEpsOV9YUkZApNXZAXUlBfMGhNc2lVeUJYVUNKUzNxZAXNn"
print("LONG ACCESS TOKEN:", long_access_token)

print(get_profile("17841405793187218", long_access_token))
#print(get_media(user_id, long_access_token))
