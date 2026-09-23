def calculate_team_total_rating(s: list) -> int:
    total = 0
    for el in s:
        result = el.get_rating()
        total += result
    return total


def elves_concert(list_elfs: list) -> None:
    for el in list_elfs:
        el.play_elf_song()


def feast_of_the_dwarves(list_dwarfs: list) -> None:
    for el in list_dwarfs:
        el.eat_favourite_dish()
