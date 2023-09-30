function_descriptions = [
        {
            "name": "getDescription",
            "description": "general information of the hotel including the hotel's title, description, history, location and information about the rooms , amneties, images about the hotel and about the price of services and finally policy of the hotel contact you can get to the hotel and always remember when asked about price contact room and amnety always require specifically ask them that there is no general",
            "parameters" : {
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "enum": ["title", "description", "history", "location", "rules", "privacy policiy", "safety & Hazard", "cancellation on booking", "contact['email']", "contact['website']", "contact['phone number']", "contact['twitter']", "contact['telegram']", "price['food']", "price['bed per day']", "price['gym per day']", "price['hot shower']", "amneties['livingroom']", "amneties['bathroom']", "amneties['bedroom']", "amneties['kitchen']", "amneties['balcony']", "room['livingroom']", "room['balcony']", "room['kitchen']", "room['bedroom']", "images"],
                        "description": "the type of information about the hotel like title, description, history, location, rules, safety things that the user should know privacy policy information to cancel booking and price contact room amnety"
                        },
                    },
                "required": ["kind"],
                }
            },
            {
            "name": "getService",
            "description": "gives information about the services provied in the hotel like overall, bed, food, entertainment, cancelling a booking and cancelling a room, availabilty",
            "parameters" : {
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "enum": ["overall", "food['non-fasting']","food['fasting']","food['drinks']", "bed", "entertainment", "book", "cancel", "availability"],
                        "description": "the kind of service the hotel provides and the user wants could be cancelling or booking a room"
                        },
                    },
                "required": ["kind"],
                }
            },
] 
