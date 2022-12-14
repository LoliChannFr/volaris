import yaml
import discord

class Player():
    def __init__(self, id):
        self.id = id

    
        

class Character():
    """The characters are the entity players play.
    
    The class of a character register all is data."""
    def __init__(self, id):
        """At the creation of a character, he get his data by the information in the database"""
        self.character_data = yaml.safe_load(open(f"./database/characters/{id[:-0]}/{id}.yml"))

        self.id = id

        self.player_id = id[:-2]

        self.name = self.character_data.get("name")
        self.age = self.character_data.get("age")
        self.sexe = self.character_data.get("sexe")

        #change to the race data
        self.race_id = self.character_data.get("race")
        self.race = Race(self.character_data.get("race"))

        #change to the classe data
        self.classe_id = self.character_data.get("classe")
        self.classe = self.character_data.get("classe")

        self.stats = self.character_data.get("stats")

        self.level = self.character_data.get("level")
        self.xp = self.character_data.get("xp")
        self.hp = self.character_data.get("hp")

        self.zone = self.character_data.get("zone")

    def save(self):
        """He save all his data in the database"""
        self.character_data["name"] = self.name
        self.character_data["age"] = self.age
        self.character_data["sexe"] = self.sexe
        self.character_data["race"] = self.race
        self.character_data["classe"] = self.classe
        self.character_data["stats"] = self.stats
        self.character_data["level"] = self.level
        self.character_data["xp"] = self.xp
        self.character_data["hp"] = self.hp
        self.character_data["zone"] = self.zone

        with open (f"./database/characters/{self.id[:-2]}/{self.id}.yml"):
            yaml.dump(self.character_data, f)
            print(f"character data of {self.name} saved")
        
class Race():
    def __init__(self, id):
        self.id = id

        self.race_data = yaml.safe_load(open(f"./database/Races/{id}.yml"))

        self.name = self.race_data["name"]
        self.bonus = self.race_data["bonus"]
        self.competence = self.race_data["competence"]
        self.average_age = self.race_data["average_age"]
        self.average_stats = self.race_data["average_stats"]

    def save(self):
        self.race_data["name"] = self.name
        self.race_data["bonus"] = self.bonus
        self.race_data["competence"] = self.competence
        self.race_data["average_age"] = self.average_age
        self.race_data["average_stats"] = self.average_stats

        with open (f"./database/Races/{self.id}.yml"):
            yaml.dump(self.race_data, f)
            print(f"Race data of {self.name} saved")
        