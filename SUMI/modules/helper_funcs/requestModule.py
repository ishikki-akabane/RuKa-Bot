#!/usr/bin/env python3


"""Extracting IDs from document"""
def idExtractor(channelID, document):
    for key in document:
        try:
            if document[key][0] == channelID:
                return key, document[key][1]
        except TypeError:
            continue
    return

def getAllGroupID(document):
    groupIDList = []
    for key in document:
        if key in ("groupID", "_id"):
            continue
        else:
            groupIDList.append(int(key))
    else:
        return groupIDList
