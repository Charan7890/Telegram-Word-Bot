import json

def get_current_index():

    with open("../data/progress.josn","r") as file:
        data = json.load(file)

    return data["current_index"]

def update_current_index(index):

    data = {"current_index":index}
    
    with open("../data/progress.json","w") as file:
        json.dump(data,file)
