class Person:

    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        # If already exists, skip creation but update age
        if person["name"] in Person.people:
            Person.people[person["name"]].age = person["age"]
            continue

        person_object = Person(person["name"], person["age"])
        if person.get("husband"):
            husband_name = person.get("husband")
            if husband_name in Person.people:
                husband_object = Person.people[husband_name]
            else:
                husband_object = Person(husband_name, 0)
            person_object.husband = husband_object
            husband_object.wife = person_object
        elif person.get("wife"):
            wife_name = person.get("wife")
            if wife_name in Person.people:
                wife_object = Person.people[wife_name]
            else:
                wife_object = Person(wife_name, 0)
            person_object.wife = wife_object
            wife_object.husband = person_object
    return list(Person.people.values())
