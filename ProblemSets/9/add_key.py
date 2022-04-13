import json

sampleDictionary = {
    0: 10,
    1: 20
}

print(json.dumps(sampleDictionary, indent = 4))

sampleDictionary[2] = 30

print(json.dumps(sampleDictionary, indent = 4))