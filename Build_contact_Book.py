cont=[]
while(True):
    print("1.Add new contact\n2.View all contact\n3.Search contact\n4.Delete contact\n5.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        cnt={}
        name=input("Enter contact name:")
        num=input("Enter contact number:")
        cnt['Name']=name
        cnt['Number']=num
        cont.append(cnt)
    elif ch==2:
        for i in cont:
            print("Name:",i['Name'],"Number:",i['Number'])
    elif ch==3:
        se=input("Enter contact name which is to be searched:")
        for i in cont:
            if i['Name']==se:
                print(i['Number'])
                break
        else:
            print("No such contact")
    elif ch==4:
        del1=input("Enter contact name which is to be deleted:")
        for i in cont:
            if i['Name']== del1:
                cont.remove(i)
                print("Deleted contact")
                break
        else:
            print("No such contact")
    elif ch==5:
        break
    else:
        print("Invalid choice")
