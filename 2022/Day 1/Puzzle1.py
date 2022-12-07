def ReadInputs():
    File = open("./Inputs.txt", "r")
    GroupedData = []
    
    data = []
    
    for Line in File:
    	if Line == "\n":
    	    GroupedData.append(data)
    	    data = []
    	    continue
    	data.append(int(Line.strip()))
    GroupedData.append(data)
 
    return GroupedData
    
def solveA(GroupedData):
    max = 0
    for Group in GroupedData:
        sum = 0
        for Calorie in Group:
            sum += Calorie
        if sum > max:
            max = sum;
            
        
    return max
    
def solveB(GroupedData):
    ordered_sums = []
    
    for Group in GroupedData:
        sum = 0
        for Calorie in Group:
            sum +=Calorie
        ordered_sums.append(sum)
        
    ordered_sums.sort(reverse = True)
   
    max = ordered_sums[0:3]
   
    answer = 0
    for x in max:
        answer += x
   
    return answer
        

                    
    
 
def main():

    Inputs=ReadInputs()
    Part1=solveA(Inputs)
    print("Answer: ", Part1)
    Part2=solveB(Inputs)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
