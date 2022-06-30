import glob
import os

NEW_EXTENSION = '.txt'

class RenameOperation:
    def __init__(self, old_filename: str, new_filename: str):
        self.old = old_filename
        self.new = new_filename
    
    def __str__(self):
        """Return operations witch will be processing"""
        return f"{self.old} --> {self.new}"

    def __repr__(self):
        return f"RenameOperation(old_name={self.old!r}, new_name={self.new!r}"

    def execute(self) -> None:
        """Process operations"""
        os.rename(self.old, self.new)
        print(self.old, '-->', self.new)

    def __eq__(self,other):
        return self.old == other.old and self.new == other.new


def split_filename(filename: str) -> list:
    if '.' in filename:
        tokens = filename.rsplit('.', maxsplit = 1)
        name, extension = tokens
    else:
        name = filename
        extension = ''
    
    return [name, extension]


def collect_operations(filename: str) -> RenameOperation:
    name, extension = split_filename(filename)
    new_filename = name + NEW_EXTENSION
    operations = RenameOperation(filename, new_filename)
    return operations


def print_proposal_result(operations: list) -> None:
    print('Zostaną dokonane następujące zmiany:')
    for op in operations:
        print(op) _
        

def execute_operations(operations: list) -> None:
    for op in operations:
        op.execute()


def agreement(agreement: str, operations: list) -> None:
    if agreement.lower() == 't':
       execute_operations(operations)
       print('Sukces :)')
    else:
        print('Anulowano :(')


def main() -> None:
    file = input('Podaj nazwę pliku: ')
    filenames = glob.glob(file)
    
    operations = [collect_operations(filename) for filename in filenames]
    
    print_proposal_result(operations)
    
    choice = input('Czy kontynuować? [t/n] ')

    agreement(choice, operations)


if __name__ == '__main__':
    main()
