import json

def is_CMD_exist(CMD_name):
    filename = 'Raspberry/Resource/requestCMD.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
            return CMD_name in data
    except FileNotFoundError:
        return False

def replace_CMD_name(CMD_name, access_phrases):
    replaced_phrases = [[phrase.replace('google', CMD_name) for phrase in phrases] for phrases in access_phrases]
    return replaced_phrases

access_phrases = [
    ["mở","bật","vào","open"],
    ["google"]
]

def update_json_file(CMD_name, replaced_phrases):
    filename = 'Raspberry/Resource/requestCMD.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    if CMD_name not in data:
        data[CMD_name] = replaced_phrases
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def addNewCMDRequest(CMD_name):
    if not is_CMD_exist(CMD_name):
        replaced_phrases = replace_CMD_name(CMD_name, access_phrases)
        update_json_file(CMD_name, replaced_phrases)


