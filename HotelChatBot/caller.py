import json

def function_call(response,id_):

    
    function_call = response["choices"][0]["message"]["function_call"]
    function_name = function_call["name"]
    function_args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])
    

    with open("data.json", "r") as file:
            data = json.load(file)



    if function_name == "getDescription":
        arg = function_args["kind"]
        if arg == "title":
            return data["title"]
        if arg == "description":
            return data["description"]
        if arg == "history":
            return data["history"]
        if arg == "location":
            return data["location"]
        if arg == "rules":
            return data["rules"]
        if arg == "privacy policy":
            return data["privacy policy"]
        if arg == "safety & hazard":
            return data["safety & hazard"]
        if arg == "cancellation on booking":
            return data["cancellation on booking"]
        if arg == "contact":
            return data["contact"]
        if arg == "contact['email']":
            return data["contact"]["email"]
        if arg == "contact['twitter']":
            return data["contact"]["twitter"]
        if arg == "contact['telegram']":
            return data["contact"]["telegram"]
        if arg == "price['food']":
            return str(data["price"]["food"])
        if arg == "price['bed per day']":
            return str(data["[price"]["bed per day"])
        if arg == "price['gym per day']":
            return data["price"]["gym per day"]
        if arg == "price['hot shower']":
            return data["price"]["hot shower"]
        if arg == "price":
            return str(data["price"])
        if arg == "amneties":
            return str(data["amneties"])
        if arg == "amneties['livingroom']":
            return data["amneties"]["livingroom"]
        if arg == "amneties['bathroom']":
            return data["amneties"]["bathroom"]
        if arg == "amneties['bedroom']":
            return data["amneties"]["bedroom"]
        if arg == "amneties['kitchen']":
            return data["amneties"]["kitchen"]
        if arg == "amneties['balcony']":
            return data["amneties"]["balcony"]
        if arg == "room":
            return str(data["rooms"])
        if arg == "room['livingroom']":
            return data["rooms"]["livingroom"]
        if arg == "room['bedroom']":
            return data["rooms"]["bedroom"]
        if arg == "room['kitchen']":
            return data["rooms"]["kitchen"]
        if arg == "room['balcony']":
            return data["rooms"]["balcony"]
        if arg == "images":
            return data["images"]
    if function_name == "getService":
        arg = function_args["kind"]
        if arg == "overall":
            return data["services"]
        if arg == "food['fasting']":
            return data["food"]["fasting"]
        if arg == "food['non-fasting']":
            return data["food"]["non-fasting"]
        if arg == "food['drinks']":
            return str(data["food"]["drinks"])
        if arg == "bed":
            return data["bed"]
        if arg == "entertainment":
            return data["entertainment"]
        if arg == "availability":
            return data["availability"]

