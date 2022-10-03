class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if self._data.__len__() == 0:
            raise IndexError("The queue is empty")

        return self._data.pop(0)

    def search(self, index):
        list_length = self.__len__()
        if index < 0:
            raise IndexError("Index must be equal or greater then 0")

        if index > list_length - 1:
            raise IndexError("Index higher then list length")

        return self._data[index]
