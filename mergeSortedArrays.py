def merge(nums1, nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0, len(nums1)-1):
            if i is not len(nums1)-1:
                if  nums1[i] > nums1[i+1]:
                    nums1 = nums1[0:i+1]
                    break

        for i in range(0,len(nums2)-1):
            if i != len(nums2)-1:
                if nums2[i] > nums2[i+1] :
                    nums1 = nums1[0:i+1]
                    break

        nums1.sort()
        nums2.sort()

        for num in nums2:
            nums1.append(num)
        print(nums1)

        nums1.sort()
        print("Sorted and Merged Array:",nums1)

        ## Actual leetcode code
        # p1 = m - 1
        # p2 = n - 1
    
        # # And move p backwards through the array, each time writing
        # # the smallest value pointed at by p1 or p2.
        # for p in range(n + m - 1, -1, -1):
        #     if p2 < 0:
        #         break
        #     if p1 >= 0 and nums1[p1] > nums2[p2]:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1


numbers1 = [1,2,3,0,0,0]
numbers2 =  [2,5,6]
result = merge(numbers1, numbers2)
print(result)
               