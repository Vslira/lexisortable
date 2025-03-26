from lexisortable.lexisortable import delexisort, lexisort


def lexiver(semver: str) -> str:
    return ".".join(map(lambda x: lexisort(int(x)), semver.split(".")))


def delexiver(lexiversion: str) -> str:
    return ".".join(map(lambda x: str(delexisort(x)), lexiversion.split(".")))
