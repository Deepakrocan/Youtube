eng_month=["jan","feb","march","april","may","june","july","Aug","sep","oct","Nov","dec"]
user_input=input("Type the current month :")
is_puratasi=True
for puratasi in eng_month:
    if puratasi=="sep" or puratasi=="oct":
       if user_input=="puratasi": 
           is_puratasi=True
    else:
        is_puratasi=False

if is_puratasi==True:
    print("tha mooditu samiya kumbudo da")