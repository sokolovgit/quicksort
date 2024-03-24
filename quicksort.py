def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


def median_quick_sort(arr, p, r):
    if p < r:
        if r - p + 1 <= 3:
            insertion_sort(arr, p, r)
        else:
            q = median_of_three(arr, p, r)
            median_quick_sort(arr, p, q - 1)
            median_quick_sort(arr, q + 1, r)


def multi_quick_sort(arr, p, r):
    if p < r:
        if r - p + 1 <= 3:
            insertion_sort(arr, p, r)
        else:
            arr[p], arr[p + 1], arr[r] = sorted([arr[p], arr[p + 1], arr[r]])

            a, b, c = multi_partition(arr, p, r)
            multi_quick_sort(arr, p, a - 1)
            multi_quick_sort(arr, a + 1, b - 1)
            multi_quick_sort(arr, b + 1, c - 1)
            multi_quick_sort(arr, c + 1, r)


def insertion_sort(arr, p, r):
    for i in range(p + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= p and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def median_of_three(array, p, r):
    mid = (p + r) // 2

    if array[mid] < array[p]:
        array[mid], array[p] = array[p], array[mid]
    if array[r] < array[p]:
        array[r], array[p] = array[p], array[r]
    if array[r] < array[mid]:
        array[r], array[mid] = array[mid], array[r]

    array[mid], array[r - 1] = array[r - 1], array[mid]
    return partition(array, p, r)


def multi_partition(arr, left, right):
    a, b = left + 2, left + 2
    c, d = right - 1, right - 1
    p, q, r = arr[left], arr[left + 1], arr[right]

    while b <= c:
        while arr[b] < q and b <= c:
            if arr[b] < p:
                arr[a], arr[b] = arr[b], arr[a]
                a += 1
            b += 1

        while arr[c] > q and b <= c:
            if arr[c] > r:
                arr[c], arr[d] = arr[d], arr[c]
                d -= 1
            c -= 1

        if b <= c:
            if arr[b] > r:
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

    return p, q, r
