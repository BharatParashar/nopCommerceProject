import configparser


def getvaluefromconfig(sectionname, parameter):
    config = configparser.ConfigParser()
    config.read("Configuration/config.ini")
    return config.get(sectionname, parameter)
