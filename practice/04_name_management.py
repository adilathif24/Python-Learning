# My mini-project: Name Management
# Current data is stored in lists, so it will reset when the program exits.

names = []
deleted = []
restore = []


def addname(name):
    if name not in names:
        names.append(name)
        print("New name added =", name)
    else:
        print("Name already exists")


def removename(name):
    if name in names:
        names.remove(name)
        deleted.append(name)
        print("Name deleted successfully =", name)
    else:
        print("No suitable name to delete")


def restoreName(name):
    if name in names:
        print("Name already exists in active names")
    elif name in deleted:
        deleted.remove(name)
        names.append(name)
        restore.append(name)
        print("Restored successfully =", name)
    else:
        print("Name not found in deleted list")


def viewname():
    print("Active names:", names)
    print("Total active names:", len(names))
    print("Deleted names:", deleted)
    print("Total currently deleted:", len(deleted))
    print("Restoration history:", restore)


# Sample run: change these values and test other cases.
addname("syed adil")
addname("syed")
addname("adil")
addname("ali")
addname("athif")
removename("syed adil")
removename("adil")
viewname()
restoreName("syed adil")
restoreName("adil")
viewname()
