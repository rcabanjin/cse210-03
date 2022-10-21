import random

class SecretWord():
    """The person choosing the Secret Word that the Player must guess in order to dave the Jumper.
    
    Attriibutes:
        word (str): The random 5 letter word.
    """

    def __init__(self):

        list = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis"
        , "Beach", "Birth", "Block", "Blood", "Board", "Brain", "Bread"
        , "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest"
        , "Chief", "Child", "China", "Claim", "Class", "Clock", "Coach"
        , "Coast", "Court", "Cover", "Cream", "Crime", "Cross", "Crowd"
        , "Crown", "Cycle", "Dance", "Death", "Depth", "Doubt", "Draft"
        , "Drama", "Dream", "Dress", "Drink", "Drive", "Earth", "Enemy"
        , "Entry", "Error", "Event", "Faith", "Fault", "Field", "Fight"
        , "Final", "Floor", "Focus", "Force", "Frame", "Frank", "Front"
        , "Fruit", "Glass", "Grant", "Grass", "Green", "Group", "Guide"
        , "Heart", "Henry", "Horse", "Hotel", "House", "Image", "Index"
        , "Input", "Issue", "Japan", "Jones", "Judge", "Knife", "Laura"
        , "Layer", "Level", "Lewis", "Light", "Limit", "Lunch", "Major"
        , "March", "Match", "Metal", "Model", "Money", "Month", "Motor"
        , "Mouth", "Music", "Night", "Noise", "North", "Novel", "Nurse"
        , "Offer", "Order", "Other", "Owner", "Panel", "Paper", "Party"
        , "Peace", "Peter", "Phase", "Phone", "Piece", "Pilot", "Pitch"
        , "Place", "Plane", "Plant", "Plate", "Point", "Pound", "Power"
        , "Press", "Price", "Pride", "Prize", "Proof", "Queen", "Radio"
        , "Range", "Ratio", "Reply", "Right", "River", "Round", "Route"
        , "Rugby", "Scale", "Scene", "Scope", "Score", "Sense", "Shape"
        , "Share", "Sheep", "Sheet", "Shift", "Shirt", "Shock", "Sight"
        , "Simon", "Skill", "Sleep", "Smile", "Smith", "Smoke", "Sound"
        , "South", "Space", "Speed", "Spite", "Sport", "Squad", "Staff"
        , "Stage", "Start", "State", "Steam", "Steel", "Stock", "Stone"
        , "Store", "Study", "Stuff", "Style", "Sugar", "Table", "Taste"
        , "Terry", "Theme", "Thing", "Title", "Total", "Touch", "Tower"
        , "Track", "Trade", "Train", "Trend", "Trial", "Trust", "Truth"
        , "Uncle", "Union", "Unity", "Value", "Video", "Visit", "Voice"
        , "Waste", "Watch", "Water", "While", "White", "Whole", "Woman"
        , "World", "Youth"]

        self.word = random.choice(list).lower()

    


random_word = SecretWord()