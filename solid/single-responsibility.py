# coding=utf-8
"""
SRC: single responsibility principle : every object should have a single responsibility, and that all its services should be narrowly aligned with that responsibility.

SOC: separation of concern: is the process of breaking a computer program into distinct features that overlap in functionality as little as possible

"""
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append("%s: %s" %(self.count, text))
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    # so fas so good all methods are related to entries
    # dont overload the Journal object with too many responsibilities
    # avoid making god objects
    # break SRP
    def save(self, filename):
        # irrelevant in current class
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        # irrelevant in current class
        pass

    def load_from_web(self, uri):
        # irrelevant in current class
        pass


class PersistenceManager:
    """
    create independent class to handle such operations
    """
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'./journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
