def sort(lists):
    lists = [sorted(l) for l in lists]
    l1 = [(lists[i][0],i,0) for i in range(len(lists))]
    
    new_list = [[]]
    index = (0,0)
    
    while(len(l1)):
        minval,row,col = min(l1)
        l1.remove((minval,row,col))
        if (index[1] == len(lists[index[0]])):
            index = (index[0]+1,0)
            new_list += [[]]
        new_list[-1] += [minval]
        index = (index[0],index[1] + 1)
        
        if (col+1 < len(lists[row])):
            l1 += [(lists[row][col+1],row,col+1)]
        else:
            continue
   
    return new_list
       


#The idea is first sort each list inside the lists, then put the fisrt element of
#each list into a list, then get the min of it, then remove this and add the one in lists that
#is right after the min.

print(sort([[3,2,4],[7,1],[6,4,8],[3,4,5,6,2,1]]))
print(sort([[1,2,3],[5,7],[2,4,8],[6,2,1,]]))
print(sort([[3,4,5,6,2,1],[1,2,3],[5,7],[2,4,8],[6,2,1,]]))