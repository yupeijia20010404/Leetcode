nums1 = [4,0,0,0,0,0]
nums2 = [1,2,3,5,6]
m = 1
n = 5

j = 0
if n > 0 and nums1[0] > nums2[0]:
    nums1[j + 1 : j + 1 + m] = nums1[j : j + m]
    nums1[0] = nums2[j]
    j += 1
    n -= 1

num1_p = 0
for k in range(j, len(nums2)):
    num = nums2[k]
    for i in range(num1_p, len(nums1) - 1):
        if nums1[i] <= num and nums1[i + 1] > num:
            nums1[i + 2 :] = nums1[i + 1 : len(nums1) - 1]
            nums1[i + 1] = num
            num1_p = i + 1
            n -= 1
            break
nums1[len(nums1) - n : len(nums1)] = nums2[len(nums2) - n : len(nums2)]

print(nums1)