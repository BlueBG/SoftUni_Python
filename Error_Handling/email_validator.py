class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGHT = 5
VALID_DOMAINS = ["com", "bg", "net", "org"]

input_line = input()

while input_line != "End":
    if input_line.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")
    elif input_line.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol")
    else:
        valid_name = input_line.split("@")

    if len(valid_name[0]) < MIN_NAME_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")
    else:
        valid_name = input_line.split(".")

    if valid_name[-1] in VALID_DOMAINS:
        print("Email is valid")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    input_line = input()
