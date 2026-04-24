def two_sum(num,target):
    seen = {}

    for i in range(len(num)):
        complement = target - num[i]

        if complement in seen :
            return [seen[complement],i]
        
        seen[num[i]] =i