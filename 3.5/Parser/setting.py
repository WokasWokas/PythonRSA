from Errors.parser import *
from Environment.env import *

def ParseSettings():
    with open("settings", "r", encoding='utf-8') as setting_file:
        return setting_file.readlines()

def GetSettingsDict():
    settings = {}
    data = ParseSettings()
    for line in data:
        line = line.split("#")[0]
        if StringIsEmptyOrWhitespace(line): continue
        setting, value = line.split('=')
        value = [v.strip('\n') for v in value.split(',')] if value != '' else None
        settings[setting] = value
    return settings
    

def ValidateSettings(settings):
    available_settings = ["resolution", "keylength"]
    for setting, value in settings.items():
        if not setting in available_settings: 
            return (InvalidSetting("{} is not available option!".format(setting)), False)
        if value is None:
            return (InvalidSettingValue("{seting} can't have value {value}!".format(setting, value)), False)
    return (None, True)
        

def Parse():
    settings = GetSettingsDict()
    validate_result = ValidateSettings(settings)
    if not validate_result[1]:
        raise validate_result[0]
    return settings