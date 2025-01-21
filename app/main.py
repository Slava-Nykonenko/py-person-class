class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        instance = Person(name, age)
        result.append(instance)

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"]:
            Person.people[name].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            Person.people[name].husband = Person.people[person["husband"]]
    return result
