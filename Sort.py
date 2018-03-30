
class Sort:
    def insertion_sort(nums):
        for i in range(1, len(nums)):
            aux = nums[i]
            j = i-1
            while j>=0 and aux < nums[j]:
                nums[j+1] = nums[j]
                j=j-1
            nums[j+1] = aux
        return nums

    def shell_sort(nums):
        gap = len(nums)//2

        while gap > 0:
            for i in range(gap, len(nums)):
                c = nums[i]
                j = i
                while (j >= gap) and nums[j-gap] > c:
                    nums[j] = nums[j-gap]
                    j = j-gap
                nums[j] = c
            gap = gap//2
        return nums

    def selection_sort(nums):
        tamanho = len(nums)

        for i in range(tamanho-1):
            index_min = i
            j= i+1
            while j < tamanho:
                if nums[j] < nums[index_min]:
                    index_min = j
                j += 1
            if(index_min != i):
                nums[index_min],nums[i] = nums[i],nums[index_min]
        return nums

    def bubble_sort(nums):
        troca = True
        while troca == True:
            troca = False

            for i in range(len(nums)-2):
                if nums[i] > nums[i+1]:
                    troca = True
                    nums[i+1],nums[i] = nums[i],nums[i+1]
        return nums
            


print(Sort.bubble_sort([2,5,1,4,3]))
