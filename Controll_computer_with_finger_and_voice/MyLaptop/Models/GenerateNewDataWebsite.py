import json
def addNewWebsiteURL(website_name,url):
    filename = 'Resource/dict_website.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    data[website_name] = [url]
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
