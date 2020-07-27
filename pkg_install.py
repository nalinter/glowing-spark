import sys
import os
import json
import requests

def get_access_token(env_url, env_payload):
	oauth_url = env_url + "rest/v11_8/oauth2/token"
	oauth_body = json.dumps(env_payload)
	access_token_response = requests.post(oauth_url, data=oauth_body)
	return access_token_response

def upload_package(env_url, oauth_token, pkg_path):
	oauth_url = env_url + "rest/v11_8/Administration/packages"
	files = [
      ('upgrade_zip', open(pkg_path,'rb'))
    ]
	headers = {
	'OAuth-Token': oauth_token
	}
	upload_pkg_response = requests.post(oauth_url, headers= headers, files = files)
	return upload_pkg_response

def install_package(env_url, oauth_token, file_hash):
	oauth_url = env_url + "rest/v11_8/Administration/packages/" + file_hash + "/install/"
	headers = {
	'OAuth-Token': oauth_token
	}
	install_pkg_response = requests.get(oauth_url, headers =headers)
	return install_pkg_response

env_name = sys.argv[1]
pkg_name = sys.argv[2]

pkg_file_path = "/var/www/html/prpackages/module_" + pkg_name + "_modules_1.zip"
payload = json.load(open("/home/devin/secrets/environments.json"))

env_info = payload[env_name]
env_url = env_info['env_url']
env_payload = env_info['credentials']

print("Environment Name : ", env_name)
print("Environment URL : ", env_url)
print("Package Name : ", pkg_name)


#Access Token Generation 
access_response = get_access_token(env_url, env_payload)
if access_response.status_code == 200:
	print("Success, Access Token Generated, ", access_response.status_code)
	access_json = access_response.json()
	access_token = access_json['access_token']
else:
	print("Access Token Generation failure with status code, ",access_response.status_code)
	print("Reason for failure: ", access_response.json())
	exit()

#Uploading Package
upload_response = upload_package(env_url, access_token, pkg_file_path)
if upload_response.status_code == 200:
	print("Success, Package has been Uploaded, ", upload_response.status_code)
	upload_json = upload_response.json()
	file_hash = upload_json['file_install']
else:
	print("Uploading Package failure with status code, ",upload_response.status_code)
	print("Reason for failure: ", upload_response.json())
	exit()

#Installing Package
install_response = install_package(env_url, access_token, file_hash)
if install_response.status_code == 200:
	print("Success, Package has been Installed, ", install_response.status_code)
else:
	print("Installing Package failure due to status code, ", install_response.status_code)
	print("Reason for failure: ", install_response.json())
