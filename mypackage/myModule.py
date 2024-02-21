def top_n(items, n):
    """returns the top n items in an array, in descending order

    Args:
        items (array): List or array-like object containing numerical values
        n (int): The number of top n values to return

    Return: 
        array: top n values, in descending order

    Example:
        >>>top_n([8,5,17,9,11], 2)
        [17,11]
        """
    for i in range(n):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j] , items[j + 1] = items[j + 1], items[j]
        #get the first n values
    top_n = items[-n:]

    return top_n[::-1] 
