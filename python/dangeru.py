'''
dangeru.py - danger/u/ python API wrapper
@author prefetcher
'''

import requests
import json

'''
index a board
@param {string} board - the board
@param {string} limit - how many threads to show
@returns JSON formatted into a dictionary
'''
def index(board, limit):
    fetch = requests.get("https://boards.dangeru.us/api.php?type=index&board=" + board + "&ln=" + str(limit))
    fetch = fetch.text.replace('\n', ' ').replace('\r', '')
    json_f = json.loads(fetch)
    return json_f

'''
display a thread
@param {string} board - the board
@param {string} limit - how many threads to show
@param {string} threadid - the thread id
@returns JSON formatted into a dictionary
'''
def thread(board, limit, threadid):
    # if the thread id is a string and it starts with http, just get the ID
    if type(threadid) != type(0) and threadid.startswith("http"):
        threadid = threadid.partition("=")[2]

    fetch = requests.get("https://boards.dangeru.us/api.php?type=thread&board=" + board + "&ln=" + str(limit) + "&thread=" + str(threadid))
    fetch = fetch.text.replace('\n', ' ').replace('\r', '')
    try:
        idx = fetch.find("https://boards.dangeru.us/static")
        while fetch[idx] != '}': idx += 1
        fetch = fetch[:idx] + '"' + fetch[idx:]
    except:
        # dangeru/static wasn't found, he probably changed the api. Just try to decode the json without the fix
        pass
    json_f = json.loads(fetch)
    return json_f
