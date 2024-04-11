from sys import argv, exit


def read_input_file(filename: str):
    try:
        with open(filename, "r") as file:
            data = list(map(int, file.read().split()))[1:]
            return data

    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit(1)
    except IOError as e:
        print(f"Error reading the file: {e}")
        exit(1)


def write_output_file(filename: str, *results):
    try:
        with open(filename, "w") as file:
            for result in results:
                file.write(' '.join(map(str, result)) + '\n')

    except IOError as e:
        print(f"Error writing the file: {e}")
        exit(1)

def count_comparisons(arr):

    comp_quick_sort = quick_sort(arr.copy(), 0, len(arr) - 1)
    comp_median_quick_sort = median_quick_sort(arr.copy(), 0, len(arr) - 1)
    comp_multi_quick_sort = multi_quick_sort(arr.copy(), 0, len(arr) - 1)

    return comp_quick_sort, comp_median_quick_sort, comp_multi_quick_sort


def quick_sort(arr, p, r, comparisons=0):

    if p < r:
        comparisons, q = partition(arr, p, r, comparisons)
        comparisons += quick_sort(arr, p, q - 1)
        comparisons += quick_sort(arr, q + 1, r)

    return comparisons


def median_quick_sort(arr, p, r, comparisons=0):
    if p < r:
        if r - p + 1 <= 3:
            comparisons += insertion_sort(arr, p, r, comparisons)
        else:
            comparisons, q = median_partition(arr, p, r, comparisons)
            comparisons += median_quick_sort(arr, p, q - 1)
            comparisons += median_quick_sort(arr, q + 1, r)

    return comparisons


def multi_quick_sort(arr, p, r, comparisons=0):
    if p < r:
        if r - p + 1 <= 3:
            comparisons += insertion_sort(arr, p, r, comparisons)
        else:
            arr[p], arr[p + 1], arr[r] = sorted([arr[p], arr[p + 1], arr[r]])

            comparisons, a, b, c = multi_partition(arr, p, r, comparisons)
            comparisons += multi_quick_sort(arr, p, a - 1)
            comparisons += multi_quick_sort(arr, a + 1, b - 1)
            comparisons += multi_quick_sort(arr, b + 1, c - 1)
            comparisons += multi_quick_sort(arr, c + 1, r)

    return comparisons


def insertion_sort(arr, p, r, comparisons):
    for i in range(p + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= p:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = key

    return comparisons


def partition(arr, p, r, comparisons):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        comparisons += 1
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return comparisons, i + 1


def median_partition(arr, p, r, comparisons):
    q = median_pivot(arr, p, r)
    i = p - 1
    for j in range(p, r):
        comparisons += 1
        if arr[j] <= q:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return comparisons, i + 1


def median_pivot(arr, p, r):
    mid = (p + r) // 2
    x, y, z = arr[p], arr[mid], arr[r]

    if (x <= y <= z) or (z <= y <= x):
        q = y
        qi = mid
    elif (y <= x <= z) or (z <= x <= y):
        q = x
        qi = p
    else:
        q = z
        qi = r

    arr[qi], arr[r] = arr[r], arr[qi]
    return q


def multi_partition(arr, left, right, comparisons):
    a, b = left + 2, left + 2
    c, d = right - 1, right - 1
    p, q, r = arr[left], arr[left + 1], arr[right]

    while b <= c:
        while arr[b] < q and b <= c:
            comparisons += 1
            if arr[b] < p:
                arr[a], arr[b] = arr[b], arr[a]
                a += 1
            b += 1
            comparisons += 1

        comparisons += 1
        while arr[c] > q and b <= c:
            comparisons += 1
            if arr[c] > r:
                arr[c], arr[d] = arr[d], arr[c]
                d -= 1
            c -= 1
            comparisons += 1

        comparisons += 1
        if b <= c:
            comparisons += 1
            if arr[b] > r:
                comparisons += 1
                if arr[c] < p:
                    arr[b], arr[a] = arr[a], arr[b]
                    arr[a], arr[c] = arr[c], arr[a]
                    a += 1
                else:
                    arr[b], arr[c] = arr[c], arr[b]
                arr[c], arr[d] = arr[d], arr[c]
                b += 1
                c -= 1
                d -= 1
            else:
                comparisons += 1
                if arr[c] < p:
                    arr[b], arr[a] = arr[a], arr[b]
                    arr[a], arr[c] = arr[c], arr[a]
                    a += 1
                else:
                    arr[b], arr[c] = arr[c], arr[b]
                b += 1
                c -= 1

    a -= 1
    b -= 1
    c += 1
    d += 1
    arr[left + 1], arr[a] = arr[a], arr[left + 1]
    arr[a], arr[b] = arr[b], arr[a]
    a -= 1
    arr[left], arr[a] = arr[a], arr[left]
    arr[right], arr[d] = arr[d], arr[right]

    return comparisons, a, b, d


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python main.py <input_file>")
        exit(1)

    array = read_input_file(argv[1])
    write_output_file("output.txt", count_comparisons(array))
