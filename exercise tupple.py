#1
#a
tup1: tuple[int] = (99,)
print('tuple 1=',tup1)
#b
tup2: tuple[int, int, int] = (77, 88, 99)
print('tuple 2=',tup2)
#c
tup3: tuple[int, int, int, int] = (10, 20, 30, 40)
print('tuple 3=',(len(tup3)))
#d
tuple_1 : tuple[int, int] = (10, 20)
tuple_2 : tuple[int, int] = (30, 40)
print('tuple 4=',tuple_1 + tuple_2)

#e
def the_common_organs(tuple_3 , tuple_4):
    common_organs = [item for item in tuple_3 if item in tuple_4]
    return tuple(common_organs)

tuple_3 : tuple[int, int, int, int] = (10, 20, 30, 40)
tuple_4 : tuple[int, int, int, int] = (30, 40, 50, 60)

common_organs = the_common_organs(tuple_3 , tuple_4)
print('The common organs are =', common_organs)

#f
def the_different_organs(tuple_5, tuple_6):
    different_5 =[item for item in tuple_5 if item not in tuple_6]
    different_6 =[item for item in tuple_6 if item not in tuple_5]

    return tuple(different_5 + different_6)

tuple_5 : tuple[int, int, int, int] = (10, 20, 30, 40)
tuple_6 : tuple[int, int, int, int] = (30, 40, 50, 60)

different = the_different_organs(tuple_5, tuple_6)
print('The different organs are =', different)
#g
def tuple_index(i, index):
        if 0 <= index < len(i):
            return i[index]

tup4: tuple= (1, 2, 3, 4, 5)
index=7
repentance=tuple_index(tup4,index)
print('the tuple index is =', repentance)

#h
tup_6: tuple[int, int, int, int] = (10, 20, 30, 40)
print('Flipped tuple =', tup_6[::-1])

#i
def duplicate_tuple(x, y):
    return x*y

tup_7=(10, 20)
Duplicate=4
repentance= duplicate_tuple(tup_7, Duplicate)
print('Duplicate_tuple =', repentance)

#j
def tuple_without_the_number(a,b):
    return tuple(item for item in a if item != b)

tup_8=(10, 40 ,30 ,10 ,50 ,2 ,3 ,5 ,5 ,8)
pop_number=10
repentance= tuple_without_the_number(tup_8,pop_number)
print('Tuple without the number =',repentance)

#k
def tuple_without_duplicates(w):
    the_list=[]
    for item in w:
        if item not in the_list:
            the_list.append(item)
    return tuple(the_list)

tup_9=(10,20,30,40,30,10,50,60,70,60)
repentance=tuple_without_duplicates(tup_9)
print('Tuple without duplicates =', repentance)

#l *בונוס*
def tuple_return_indexes(x,indexes):
    index_i =[]
    for i in range(len(x)):
        if x[i] == indexes:
            index_i.append(i)
    return tuple(index_i)

tup_10=(10,40 ,30 ,10 ,5 ,2 ,3 ,5 ,5 ,8 )
return_number = 5
repentance=tuple_return_indexes(tup_10, return_number)
print('Tuple return indexes =', repentance)


#m
def  names_and_grades():

    names=[]
    while True:
        name:str=str(input('give me name:'))
        if name == "done":
            break
        names.append(name)
    while True:
        grades = []
        grade: str = str(input('give me grade:'))
        if grade == -999:
            break
        grades.append(grade)

    list_combined = tuple(zip(names, grades))
    return list_combined

repentance= names_and_grades
print(repentance)

#2
#מה ההבדל בין tuple ל- list ? מתי תעדיף להשתמש בכל אחד מהם?
# .ניתן כל הזמן למחוק ולשנות. הבדל נוסף הוא שחייב לכתוב את כמות הערכים שאני נותנת לטאפל ובליסט לא צריך. הבדל נוסף וקריטי הוא שטאפל לוקח פחות מקום בזיכרון לעומת הליסט list-לא ניתן למחוק את הקוד לאחר שהוא נכתב והודפס ולעומת זאת ב- tupleההבדל בין השניים הוא שב
#העדיף להשתמש בטאפל כאשר אני יודעת בוודאות שלא אצטרך לשנות את הקוד שנכתב והעדיף בליסט כאשר יהיה לי ידוע שאני ארצה באיזשהו שלב לשנות את הקוד שלי

#3
data_tuple = (
{"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0] ["age"] = 31
data_tuple[0] .clear()

#קוד זה מתאפשר ולא מתקבל שגיאה כיוון שהוא הוכנס לתוך רשימה/מילון
