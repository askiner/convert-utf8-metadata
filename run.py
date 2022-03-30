from sys import argv
from os import path, getenv 
from dotenv import load_dotenv

import subprocess
from json import loads

load_dotenv()

def run(filename):
    if path.exists(filename):
        if isUTF8Codepage(filename):
            print("UTF8 found")


def isUTF8Codepage(filename):
    exiftool = getenv("EXIFTOOL")
    if path.exists(exiftool) and path.exists(filename):
        result = subprocess.run([exiftool, "-j", "-codedcharacterset", filename], stdout=subprocess.PIPE)
        result_object = loads(result.stdout)
        return "CodedCharacterSet" in result_object[0] and result_object[0]["CodedCharacterSet"] == "UTF8"

        # result = subprocess.run("ping localhost", stdout=subprocess.PIPE)
        pass



if __name__ == "__main__":
    if len(argv) > 0:
        for arg in argv[1:]:
            run(arg)