#!/usr/bin/env python3
import os, googleapiclient.discovery

token_json = os.environ["GSC_TOKEN"]
# token_json should be a service-account JSON string stored as a secret
import json, tempfile
with tempfile.NamedTemporaryFile("w", delete=False) as f:
    f.write(token_json)
    cred_file = f.name

from google.oauth2 import service_account
creds = service_account.Credentials.from_service_account_file(
    cred_file, scopes=["https://www.googleapis.com/auth/webmasters"]
)
service = googleapiclient.discovery.build("searchconsole", "v1", credentials=creds)

SITE = "https://www.pciprinciple.org"
SITEMAP = "https://www.pciprinciple.org/sitemap.xml"

service.sitemaps().submit(siteUrl=SITE, feedpath=SITEMAP).execute()
print("Sitemap submitted to GSC")
