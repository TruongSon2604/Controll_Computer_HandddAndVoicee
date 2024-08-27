import json

access_phrases = [
    "mở google",
    "truy cập google",
    "vào google",
    "mở trang google",
    "bật google",
    "tìm kiếm trên google",
    "tìm kiếm trên trang google",
    "tìm kiếm trên google ngay",
    "mở google ngay",
    "vào trang google ngay",
    "bật trang google ngay",
    "truy cập google ngay",
    "mở trang google ra",
    "vào google ngay",
    "tìm kiếm trên google ngay bây giờ",
    "mở trang google ngay bây giờ",
    "vào google ngay bây giờ",
    "bật trang google ngay bây giờ",
    "truy cập google ngay bây giờ",
    "mở trang google lên"
]

def replace_website_name(website_name, access_phrases):
    replaced_phrases = [phrase.replace('google', website_name) for phrase in access_phrases]
    return replaced_phrases

def update_json_file(website_name, access_phrases):
    filename = 'Raspberry/Resource/request.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    # tại sao nó có thể tạo ra các file requestCMD.json
    if website_name not in data:
        data[website_name] = access_phrases
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def addNewWebsite(website_names):
    replaced_phrases = replace_website_name(website_names, access_phrases)
    update_json_file(website_names, replaced_phrases)
