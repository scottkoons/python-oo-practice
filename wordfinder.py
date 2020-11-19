# """Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, path):
        self.path = path

    # Reads a random line from a file passed into it
    def random_line(self):
        # lines = open(self.path).read().splitlines()
        lines = random.choice(open(self.path).readlines())
        # return random.choice(lines)
        return lines.strip()


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
        # self.full_lines = path

    def remove_special(self):
        find_line = super().random_line()

        if find_line == "" or find_line[0] == '#':
            return "I could not find a list item. Please run the app again."
        else:
            return find_line.strip()


# wf = WordFinder('lots_of_words.txt')
# wf = SpecialWordFinder('special.txt')

wf = WordFinder('words.txt')
print(wf.random_line())
# wf = SpecialWordFinder('special.txt')
# print(wf.remove_special())
