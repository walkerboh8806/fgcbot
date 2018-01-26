#!/usr/python3

import urllib
import requests
import json
import os                   

# need a way to force remove and download data

# checks if tournament exists at all
# checks if tournament has already been added
# creates directory for tournament, and dumps raw files
def tournament_add_raw(tournament_name):
    url = "https://api.smash.gg/tournament/"+str(tournament_name)+"?expand[]=event"
    response = json.loads(requests.get(url).content.decode('utf-8'))
    #print(response)
    keys = list(response.keys())
    if "message" in keys:
        print("not found")
        return "Unable to find Tournament with name: " + str(tournament_name)
    elif response['resultEntity'] == "tournament":
        if os.path.isdir("data/tournaments/" + str(tournament_name)):
            return "Tournament has already been added."
        directory = "/home/samc/Dropbox/PycharmProjects/discord-bot/data/tournaments/" + str(tournament_name)
        os.mkdir(directory)
        os.mkdir(directory + "/raw")
        t_json_raw = response
        # print(json.loads(response.content.decode('utf-8')))
        directory = "/home/samc/Dropbox/PycharmProjects/discord-bot/data/tournaments/" + str(tournament_name)
        with(open(directory + "/raw/tournament.json", 'w+')) as f:
            json.dump(t_json_raw, f)
        eventids = get_eventids(t_json_raw)
        for event in eventids:
            event_json_raw = get_event_raw(event)
            with(open(directory + "/raw/event" + str(event) + ".json", 'w+')) as f:
                json.dump(event_json_raw, f)
            groupids = get_groupids(event_json_raw)
            for group in groupids:
                group_json_raw = get_group_raw(group)
                with(open(directory + "/raw/group_" + str(event) + "_" + str(group) + ".json", 'w+')) as f:
                    json.dump(group_json_raw, f)
        return ["TournamentID: "+str(response['result'])+" found and added."]
    else:
        return "Unknown error occurred, check log."


# creates list of eventids from raw tournament json
def get_eventids(t_json_raw):
    eventids = []
    for event in t_json_raw['entities']['event']:
        eventids.append(event['id'])
    return eventids

# creates json file with raw data for each event in the tournament (SFV, I2,
def get_event_raw(eventid):
    url = "https://api.smash.gg/event/" + str(eventid) + "?expand[]=groups"
    response = requests.get(url)
    # need to create folder per event
    return json.loads(response.content.decode('utf-8'))


def get_groupids(e_json_raw):
    groupids = []
    for group in e_json_raw['entities']['groups']:
        groupids.append(group['id'])
    return groupids

def get_group_raw(groupid):
    url = "https://api.smash.gg/phase_group/" + str(groupid) + "?expand[]=entrants&expand[]=seeds&expand[]=sets"
    response = requests.get(url)
    return json.loads(response.content.decode('utf-8'))