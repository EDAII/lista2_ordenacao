''' Python 3.6.5 '''

''' lib for vector '''
from Vector import Vector
from Sort import Sort
import sys
import timeit
import matplotlib.pyplot as plt


if __name__ == "__main__":
    while(1):
        print("Choose an option:\n1: Insertion_sort\n2: Shell_sort\n3: Selection_sort\n4: Bubble_sort\n0: exit")
        ans = int(input())
        if ans == 1:
            ''' Graph of insertion sort in time '''

            ''' Unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,50):
                vector = Vector.vector_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.insertion_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            f, axarr = plt.subplots(5, sharex=True)
            axarr[0].plot(list_index, list_result)
            axarr[0].set_title('Insertion sort unsorted vector')
            ''' Sorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_sorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.insertion_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[1].plot(list_index,list_result)
            axarr[1].set_title("Insertion sort in sorted vector")
            ''' Semi unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_semi_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.insertion_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[2].plot(list_index,list_result)
            axarr[2].set_title("Insertion sort in semi unsorted vector")

            ''' Decreasing Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_decreasing(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.insertion_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[3].plot(list_index,list_result)
            axarr[3].set_title("Insertion sort in decreasing vector")
            ''' Repeater Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_repeater(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.insertion_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[4].plot(list_index,list_result)
            axarr[4].set_title("Insertion sort in repeater vector")


            f.subplots_adjust(hspace=0.6,right= 0.5, left= 0.2,top=1.2)
            plt.show()
        if ans == 2:
            ''' Graph of shell sort in time '''

            ''' Unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,50):
                vector = Vector.vector_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.shell_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            f, axarr = plt.subplots(5, sharex=True)
            axarr[0].plot(list_index, list_result)
            axarr[0].set_title('Shell sort unsorted vector')
            ''' Sorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_sorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.shell_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[1].plot(list_index,list_result)
            axarr[1].set_title("Shell sort in sorted vector")
            ''' Semi unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_semi_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.shell_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[2].plot(list_index,list_result)
            axarr[2].set_title("Shell sort in semi unsorted vector")

            ''' Decreasing Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_decreasing(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.shell_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[3].plot(list_index,list_result)
            axarr[3].set_title("Shell sort in decreasing vector")
            ''' Repeater Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_repeater(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.shell_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[4].plot(list_index,list_result)
            axarr[4].set_title("Shell sort in repeater vector")


            f.subplots_adjust(hspace=0.6,right= 0.5, left= 0.2,top=1.2)
            plt.show()
        if ans == 3:
            ''' Graph of selection sort in time '''

            ''' Unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,50):
                vector = Vector.vector_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.selection_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            f, axarr = plt.subplots(5, sharex=True)
            axarr[0].plot(list_index, list_result)
            axarr[0].set_title('Selection sort unsorted vector')
            ''' Sorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_sorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.selection_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[1].plot(list_index,list_result)
            axarr[1].set_title("Selection sort in sorted vector")
            ''' Semi unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_semi_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.selection_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[2].plot(list_index,list_result)
            axarr[2].set_title("Selection sort in semi unsorted vector")

            ''' Decreasing Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_decreasing(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.selection_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[3].plot(list_index,list_result)
            axarr[3].set_title("Selection sort in decreasing vector")
            ''' Repeater Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_repeater(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.selection_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[4].plot(list_index,list_result)
            axarr[4].set_title("Selection sort in repeater vector")

            f.subplots_adjust(hspace=0.6,right= 0.5, left= 0.2,top=1.2)
            plt.show()
        if ans == 4:
            ''' Graph of bubble sort in time '''

            ''' Unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,50):
                vector = Vector.vector_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.bubble_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            f, axarr = plt.subplots(5, sharex=True)
            axarr[0].plot(list_index, list_result)
            axarr[0].set_title('bubble sort unsorted vector')
            ''' Sorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_sorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.bubble_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[1].plot(list_index,list_result)
            axarr[1].set_title("bubble sort in sorted vector")
            ''' Semi unsorted Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_semi_unsorted(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.bubble_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[2].plot(list_index,list_result)
            axarr[2].set_title("bubble sort in semi unsorted vector")

            ''' Decreasing Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_decreasing(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.bubble_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[3].plot(list_index,list_result)
            axarr[3].set_title("bubble sort in decreasing vector")
            ''' Repeater Vector '''
            list_result = []
            list_index = []
            for count in range(1,5000,100):
                vector = Vector.vector_repeater(count)
                list_index.append(count)
                tic = timeit.default_timer()
                vector_sorted = Sort.bubble_sort(vector)
                toc = timeit.default_timer()
                time = toc - tic
                list_result.append(time)
            #print("list_index : ",list_index)
            #print("list_result: ",list_result)
            axarr[4].plot(list_index,list_result)
            axarr[4].set_title("bubble sort in repeater vector")

            f.subplots_adjust(hspace=0.6,right= 0.5, left= 0.2,top=1.2)
            plt.show()
        else:
            sys.exit()
    # vector = Vector.vector_unsorted(100)
    #
    # #Insertion sort --------------------------------------------
    # vector = Vector.vector_unsorted(100)
    # print('| Insertion sort com vetor desordenado de tamanho 100 |')
    # tic = timeit.default_timer()
    # nums1 = Sort.insertion_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(1000)
    # print('| Insertion sort com vetor desordenado de tamanho 1000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.insertion_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(10000)
    # print('| Insertion sort com vetor desordenado de tamanho 10000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.insertion_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # #Shell sort --------------------------------------------
    # vector = Vector.vector_unsorted(100)
    # print('| Shell sort com vetor desordenado de tamanho 100 |')
    # tic = timeit.default_timer()
    # nums1 = Sort.shell_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(1000)
    # print('| Shell sort com vetor desordenado de tamanho 1000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.shell_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(10000)
    # print('| Shell sort com vetor desordenado de tamanho 10000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.shell_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # #Selection sort --------------------------------------------
    # vector = Vector.vector_unsorted(100)
    # print('| Selection sort com vetor desordenado de tamanho 100 |')
    # tic = timeit.default_timer()
    # nums1 = Sort.selection_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(1000)
    # print('| Selection sort com vetor desordenado de tamanho 1000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.selection_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(10000)
    # print('| Selection sort com vetor desordenado de tamanho 10000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.selection_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # #Bubble sort --------------------------------------------
    # vector = Vector.vector_unsorted(100)
    # print('| Bubble sort com vetor desordenado de tamanho 100 |')
    # tic = timeit.default_timer()
    # nums1 = Sort.bubble_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(1000)
    # print('| Bubble sort com vetor desordenado de tamanho 1000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.bubble_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
    #
    # vector = Vector.vector_unsorted(10000)
    # print('| Bubble sort com vetor desordenado de tamanho 10000 |')
    # tic = timeit.default_timer()
    # nums2 = Sort.bubble_sort(vector)
    # toc = timeit.default_timer()
    # print("| Tempo de execução: {} |\n\n".format(toc-tic))
