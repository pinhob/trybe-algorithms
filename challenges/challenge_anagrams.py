def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    list_first_str = list(first_string.lower())
    list_second_str = list(second_string.lower())

    order_string(list_first_str, 0, len(list_first_str) - 1)
    order_string(list_second_str, 0, len(list_second_str) - 1)

    return list_first_str == list_second_str


# baseado no exemplo de quick sort do course
def order_string(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        order_string(array, low, partition_index - 1)
        order_string(array, partition_index + 1, high)


def partition(array, low, high):
    index_lower_element = low - 1
    pivot = array[high]

    for loop_index in range(low, high):
        if array[loop_index] <= pivot:

            index_lower_element += 1
            array[index_lower_element], array[loop_index] = (
                array[loop_index],
                array[index_lower_element],
            )

    array[index_lower_element + 1], array[high] = (
        array[high],
        array[index_lower_element + 1],
    )

    return index_lower_element + 1


if __name__ == "__main__":
    print(is_anagram("pedra", "perda"))
