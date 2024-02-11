def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter name and phone."
        except KeyError:
            return "Please enter existing contact."
        except IndexError:
            return "Please enter existing contact."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, dict):
    name, phone = args
    dict[name] = phone
    return "Contact added."

@input_error
def change_contact(args, dict):
    name, phone = args
    value = dict.get(name)
    if value is None:
        raise KeyError()
    dict[name] = phone
    return "Contact changed."

@input_error
def show_phone(contact, dict):
    return dict[contact[0]]

def show_all(dict):
    return dict

def main ():
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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))      
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()