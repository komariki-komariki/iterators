nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

multi_nested_list = [
    ['a', ['k', 'v', [15, 42],'v'], 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:

    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.list_iterator = iter(self.list)
        self.list_nested = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.list_nested) == self.cursor:
            self.list_nested = None
            self.cursor = 0
            while not self.list_nested:
                self.list_nested = next(self.list_iterator)
        return self.list_nested[self.cursor]

class Multi_flatIterator:

    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element


def flat_generator(my_list):
    for sub_list in my_list:
        for elem in sub_list:
            yield elem

def multi_flat_generator(my_list):
    for elem in my_list:
        if isinstance(elem, list):
            for sub_elem in multi_flat_generator(elem):
                yield sub_elem
        else:
            yield elem


def task_1(my_list):
    print('\nЗадание 1')
    for item in FlatIterator(my_list):
        print(item)
    flat_list = [item for item in FlatIterator(my_list)]
    print(flat_list)

def task_2(list):
    print('\nЗадание 2')
    for item in flat_generator(list):
        print(item)

def task_3(list):
    print('\nЗадание 3')
    for item in Multi_flatIterator(list):
        print(item)
    flat_list = [item for item in Multi_flatIterator(list)]
    print(flat_list)

def task_4(list):
    print('\nЗадание 4')
    for item in multi_flat_generator(list):
        print(item)

if __name__ == '__main__':
    task_1(nested_list)
    task_2(nested_list)
    task_3(multi_nested_list)
    task_4(multi_nested_list)
