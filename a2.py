class Find :
    d={}
    def __init__(self,arr,sum):
        key=1
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(arr[i]+arr[j]==sum):
                    self.d[key] = [i,j]
                    key=key+1
        print(self.d)
X = Find([10,20,40,50,10,20,30],50) 