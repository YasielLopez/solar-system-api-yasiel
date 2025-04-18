
''' 
1. Define a `Planet` class with the attributes `id`, `name`, and `description`, 
and one additional attribute
1. Create a list of `Planet` instances
'''
class Planet():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

# Declare instances of Planet for Demon slayer universe
planets = [
            Planet(1,"Gitara", "A collaborative world where every citizen lives in branches and merges ideas into a unified reality. Conflicts are resolved through pull requests."),
            Planet(2, "Stacktron", "A knowledge-rich planet where questions power the economy and answers are the main currency. The atmosphere is made of floating documentation."),
            Planet(3, "Debugonia", "A mysterious world shrouded in bugs and logs. Its inhabitants spend lifetimes hunting elusive errors with sacred print statements and ancient breakpoints.")
]
