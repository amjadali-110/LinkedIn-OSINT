import requests
import json

api_key = "sk_live_65339138f5636605f1a0e307_key_6apvhou98vf"
target_email = input("Enter the target email: ")

url = f"https://api.reversecontact.com/enrichment?apikey={api_key}&mail={target_email}"
headers = {
    'accept': 'application/json',
    'content-type': 'application/json'
}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

if 'email' in data:
    print(f"Email: {data['email']}")
if 'publicIdentifier' in data['person']:
    print(f"Public Identifier: {data['person']['publicIdentifier']}")
if 'firstName' in data['person'] and 'lastName' in data['person']:
    print(f"Name: {data['person']['firstName']} {data['person']['lastName']}")
if 'linkedInUrl' in data['person']:
    print(f"LinkedIn URL: {data['person']['linkedInUrl']}")
if 'headline' in data['person']:
    print(f"Headline: {data['person']['headline']}")
if 'location' in data['person']:
    print(f"Location: {data['person']['location']}")
if 'photoUrl' in data['person']:
    print(f"Photo URL: {data['person']['photoUrl']}")
if 'positions' in data['person']:
    for position in data['person']['positions']['positionHistory']:
        if 'startEndDate' in position and 'title' in position and 'companyName' in position:
            print(f"Position: {position['title']}")
            print(f"Company: {position['companyName']}")
            if 'companyLocation' in position:
                print(f"Company Location: {position['companyLocation']}")
            if 'description' in position:
                print(f"Description: {position['description']}")
            if 'linkedInUrl' in position:
                print(f"LinkedIn URL: {position['linkedInUrl']}")
if 'schools' in data['person']:
    for school in data['person']['schools']['educationHistory']:
        if 'startEndDate' in school and 'schoolName' in school and 'degreeName' in school and 'fieldOfStudy' in school:
            print(f"School: {school['schoolName']}")
            print(f"Degree: {school['degreeName']}")
            print(f"Field of Study: {school['fieldOfStudy']}")