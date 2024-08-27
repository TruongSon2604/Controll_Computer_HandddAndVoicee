import json

def is_website_exist(website_name):
    filename = 'Raspberry/Resource/requestWebsite.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
            return website_name in data
    except FileNotFoundError:
        return False

def replace_website_name(website_name, access_phrases):
    replaced_phrases = [[phrase.replace('google', website_name) for phrase in phrases] for phrases in access_phrases]
    return replaced_phrases

access_phrases = [
    ["mở","bật","vào","open","truy cập"],
    ["google"],
    []
]

def update_json_file(website_name, replaced_phrases):
    filename = 'Resource/requestWebsite.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    if website_name not in data:
        data[website_name] = replaced_phrases
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def addNewWebsiteRequest(website_name):
    if not is_website_exist(website_name):
        replaced_phrases = replace_website_name(website_name, access_phrases)
        update_json_file(website_name, replaced_phrases)
addNewWebsiteRequest('zingmp3')