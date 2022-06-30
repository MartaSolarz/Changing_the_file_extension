# W poprzednim ćwiczeniu napisz testy funkcji collect_operation. Będzie to wymagało zaimplementowania metody RenameOperation.__eq__.

from M06L11 import collect_operations, RenameOperation

def test_collect_operations_casual_file():
    got = collect_operations('plik.pdf')
    expected = RenameOperation('plik.pdf', 'plik.txt')
    assert got == expected

def test_collect_operations_without_extension():
    got = collect_operations('plik')
    expected = RenameOperation('plik', 'plik.txt')
    assert got == expected

def test_collect_operations_with_punctations_in_name():
    got = collect_operations('pl.ik.pdf')
    expected = RenameOperation('pl.ik.pdf', 'pl.ik.txt')
    assert got == expected

def test_collect_operations_full_path():
    got = collect_operations('M03\pli.k\plik.pdf')
    expected = RenameOperation('M03\pli.k\plik.pdf', 'M03\pli.k\plik.txt')
    assert got == expected

