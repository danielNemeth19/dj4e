# Go to https://github.com/settings/developers

# Add a New OAuth2 App

# Application name: ChuckList PythonAnywhere
# Homepage Url: https://drchuck.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://drchuck.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file
import os
SOCIAL_AUTH_GITHUB_KEY = os.getenv("GH_KEY", None)
SOCIAL_AUTH_GITHUB_SECRET = os.getenv("GH_SECRET", None)

# For detail: https://readthedocs.org/projects/python-social-auth/downloads/pdf/latest/

