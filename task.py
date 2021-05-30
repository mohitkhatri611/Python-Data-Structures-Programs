import sys
#Few points
#IF you are running program in your id then need to press enter 2 times to after inputs
#If you are running program in any online id then it will be output directly.
#outputs are in list and program using dictionary so particular list items are in random Order
#But ouptuts were be same as required only poition of names are random
list_of_lists=[]
import ast
st=""
for line in sys.stdin:
    if line!="\n":
        st+=line
    else:
        st=st.replace("\n","")
        break

list_of_lists=ast.literal_eval(st)

dict = {}
i=0
for list in list_of_lists:
    for element in list:
        if str(element) in dict:
            if dict[str(element)] ==0:
                dict.update({str(element):2})
            else:
                new=dict[str(element)]
                new= new+1
                dict.update({str(element): new})
        else:
            if list_of_lists[0]!=list:
                dict[str(element)] = 1
            else:
                dict[str(element)] = 0


list1=[]
list2=[]
list3=[]
for key in dict:
    if dict[str(key)] == len(list_of_lists):
        list1.append(key)
    if dict[str(key)]<=1:
        list2.append(key)
    if dict[str(key)]==0:
        list3.append(key)


print(list1)
print(list2)
print(list3)
