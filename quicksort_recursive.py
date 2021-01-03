def partition(S, low, high):
    i = (low - 1)       
    pivot = S[high]    

    for j in range(low, high):

        if S[j] <= pivot:

            i += 1
            S[i], S[j] = S[j], S[i]

    S[i + 1], S[high] = S[high], S[i + 1]
    return (i + 1)

def quickSort(S, low, high):
    if low < high:

        pi = partition(S, low, high)

        quickSort(S, low, pi-1)
        quickSort(S, pi + 1, high)


# Driver Code
if __name__ == '__main__':

    S = [4, 2, 6, 9, 2]
    n = len(S)

    # Calling quickSort function
    quickSort(S, 0, n - 1)

    for i in range(n):
        print(S[i], end=" ")
