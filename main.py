''' Python 3.6.5 '''

''' lib for vector '''
from Vector import Vector
from Sort import Sort
import time
import timeit


if __name__ == "__main__":
    vector = Vector.vector_unsorted(100)

    #Insertion sort --------------------------------------------
    vector = Vector.vector_unsorted(100)
    print('| Insertion sort com vetor desordenado de tamanho 100 |')
    tic = timeit.default_timer()
    nums1 = Sort.insertion_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(1000)
    print('| Insertion sort com vetor desordenado de tamanho 1000 |')
    tic = timeit.default_timer()
    nums2 = Sort.insertion_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(10000)
    print('| Insertion sort com vetor desordenado de tamanho 10000 |')
    tic = timeit.default_timer()
    nums2 = Sort.insertion_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))

    #Shell sort --------------------------------------------
    vector = Vector.vector_unsorted(100)
    print('| Shell sort com vetor desordenado de tamanho 100 |')
    tic = timeit.default_timer()
    nums1 = Sort.shell_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(1000)
    print('| Shell sort com vetor desordenado de tamanho 1000 |')
    tic = timeit.default_timer()
    nums2 = Sort.shell_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(10000)
    print('| Shell sort com vetor desordenado de tamanho 10000 |')
    tic = timeit.default_timer()
    nums2 = Sort.shell_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))

    #Selection sort --------------------------------------------
    vector = Vector.vector_unsorted(100)
    print('| Selection sort com vetor desordenado de tamanho 100 |')
    tic = timeit.default_timer()
    nums1 = Sort.selection_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(1000)
    print('| Selection sort com vetor desordenado de tamanho 1000 |')
    tic = timeit.default_timer()
    nums2 = Sort.selection_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(10000)
    print('| Selection sort com vetor desordenado de tamanho 10000 |')
    tic = timeit.default_timer()
    nums2 = Sort.selection_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))

    #Bubble sort --------------------------------------------
    vector = Vector.vector_unsorted(100)
    print('| Bubble sort com vetor desordenado de tamanho 100 |')
    tic = timeit.default_timer()
    nums1 = Sort.bubble_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(1000)
    print('| Bubble sort com vetor desordenado de tamanho 1000 |')
    tic = timeit.default_timer()
    nums2 = Sort.bubble_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))
    
    vector = Vector.vector_unsorted(10000)
    print('| Bubble sort com vetor desordenado de tamanho 10000 |')
    tic = timeit.default_timer()
    nums2 = Sort.bubble_sort(vector)
    toc = timeit.default_timer()
    print("| Tempo de execução: {} |\n\n".format(toc-tic))