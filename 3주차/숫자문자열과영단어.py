def solution(s):
    answer=''
    alphabet=['zero','one','two','three','four','five','six','seven','eight','nine']
    numbers=[0,1,2,3,4,5,6,7,8,9]
    numlist=list(s)
    temp=''
    for i in numlist:
        temp+=i
        if i.isdigit():
            answer+=i
            temp=''
        if temp in alphabet:
            answer+=str(numbers[alphabet.index(temp)])
            temp=''
    return int(answer)
  
  #popular answer
  
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"} 
def solution(s): 
	answer = s 
	for key, value in num_dic.items(): 
		answer = answer.replace(key, value) 
	return int(answer)
