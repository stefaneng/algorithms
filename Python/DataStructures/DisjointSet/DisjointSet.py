from sets import Set

class DisjointSet(object):
    """
    Disjoint-Set Data Structure with a list as collection
    """
    def __init__(self):
        self.collection = []

    def find_set(self, x):
        "Returns the set that contains `x`"
        for s in self.collection:
            if x in s:
                return s
        # Object x is not in collection
        return None

    def _delete_set(self, x):
        """
        Deletes a set from colletion, and returns the deleted set.
        Note: This is not part of disjoint-set api.
        """
        for i,s in enumerate(self.collection):
            if x in s:
                del self.collection[i]
                return s

    def make_set(self, x):
        """
        Creates a new set in collection whose only member is `x`.
        Returns the set if `x` was not in collection already,
        and returns `None` if `x` was already in set.
        """
        if not self.find_set(x):
            new_set = Set([x])
            self.collection.append(new_set)
            return new_set

    def union(self, x, y):
        "Unites the sets that contain `x` and `y` in the collection."
        set_x = self._delete_set(x)
        set_y = self._delete_set(y)

        if set_x and set_y:
            # Union of set_x and set_y
            new_set = set_x | set_y
        elif set_x:
            new_set = set_x
        elif set_y:
            new_set = set_y
        else:
            new_set = None

        if new_set:
            self.collection.append(new_set)
        return new_set

    def __str__(self):
        return self.collection.__str__()
