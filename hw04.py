'''
Assistant bot module
'''

from functools import wraps

class BotException(Exception):
    '''
    Bot exception handling class
    '''

def input_error(func):
    '''
    Inputs error handling decorator
    '''
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "There should be two arguments: name and phone."
        except IndexError:
            return "There should be one argument: user's name"
        except KeyError:
            return "The contact is not present in the phonebook"
        except BotException as e:
            return e.args[0]

    return inner

def parse_input(user_input: str) -> str:
    '''
    Parses the user input from the command line
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: slice, contacts: dict) -> str:
    '''
    Adds a phone for a specific user
    '''
    name, phone = args
    if contacts.get(name) is not None:
        raise BotException(f"The contact {name} already exists")
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: slice, contacts: dict) -> str:
    '''
    Changes a phone for a specific user
    '''
    name, phone = args
    if contacts.get(name) is None:
        raise BotException("Contact is not created yet")
    contacts[name] = phone
    return "Contact changed."

@input_error
def get_phone(args: slice, contacts: dict) -> str:
    '''
    Lists a phone for a specific user
    '''
    name = args[0]
    return contacts[name]

def get_all_phones(contacts: dict) -> str:
    '''
    Lists all the phones in the contacts
    '''
    phones = ""
    for name, phone in contacts.items():
        phones += f"Name: {name}, Phone: {phone}\n"
    return phones

def main():
    '''
    Main function
    '''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_phones(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
