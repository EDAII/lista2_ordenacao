
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





