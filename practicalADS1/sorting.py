class Sorter(object):
    """
    Base class for sorters. Defines the `sort` method.
    """
    def sort(self, elements):
        """
        Sorts the elements in the list.

        :param elements: The list of elements which has to be sorted
        :type elements: list
        :return: The sorted list of elements
        :rtype: list
        """
        raise NotImplementedError()


class InsertionSorter(Sorter):
    """
    Sorter implementation using the insertion sort strategy.
    """
    def sort(self, elements):
        for i in range(1, len(elements)):
            value = elements[i]
            j = i-1
            while j >= 0 and elements[j] > value:
                elements[j+1] = elements[j]
                j -= 1
            elements[j+1] = value
        return elements


class QuickSorter(Sorter):
    """
    Sorter implementation using the quick sort strategy.
    """
    def sort(self, elements):
        self.quicksort(elements, 0, len(elements)-1)
        return elements

    def quicksort(self, elements, left, right):
        if right > left:
            i = self.partition(elements, left, right)
            self.quicksort(elements, left, i -1)
            self.quicksort(elements, i + 1, right)

    def partition(self, elements, left, right):
        i, j = left,right
        pivot = elements[right]
        while i < j:
            while elements[i] < pivot and i < j:
                i += 1
            while elements[j-1] >= pivot and i < j:
                j -= 1
            if i < j:
                elements[i], elements[j-1] = elements[j-1], elements[i]
                i += 1
                j -= 1
        if pivot < elements[i]:
            elements[i], elements[right] = elements[right], elements[i]
        return i

