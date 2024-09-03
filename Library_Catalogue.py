M=["PYTHON","C","C++","JAVA","SQL","OOPS IN PYTHON","NETWORKS"]
I=M.copy()
USER_ID=[1,3,5,7,9,"LIB"]
LIBRARIAN=[]
A=[]
B=[]
C=[]
D=[]
E=[]
PASSWORD="-*-LIBRARY-*-"
while True:
    print("\n1-DISPLAY THE BOOKS \n2-ISSUE THE BOOKS \n3-RETURN THE BOOK \n4-FOR LIBRARIAN USE \n0-STOP \n")
    T=eval(input("ENTER YOUR CHOICE: "))
    if(T==1):
        print("TOTAL BOOKS IN THE LIBRARY: ",len(M))
        print("THE AVAILABLE BOOKS IN THE LIBRARY ARE ",sorted(M))
    elif(T==2):
        USER=eval(input("ENTER YOUR USER ID: "))
        if USER in USER_ID:
            Q=str(input("ENTER THE BOOK NAME: "))
            L=Q.upper()
            if L in M:
                if(USER==1):
                    if(len(A)<3):
                        M.remove(L)
                        A.append(L)
                        print("THE BOOK '",L,"' WAS SUCCESSFULLY ISSUED")
                    else:
                        print("YOUR QUATA WAS ALREADY FULFILLED")
                    print("YOUR BOOK LIST:",sorted(A))
                elif(USER==3):
                    if(len(B)<3):
                        M.remove(L)
                        B.append(L)
                        print("THE BOOK '",L,"' WAS SUCCESSFULLY ISSUED")
                    else:
                        print("YOUR QUATA WAS ALREADY FULFILLED")
                    print("YOUR BOOK LIST:",sorted(B))
                elif(USER==5):
                    if(len(C)<3):
                        M.remove(L)
                        C.append(L)
                        print("THE BOOK '",L,"' WAS SUCCESSFULLY ISSUED")
                    else:
                        print("YOUR QUATA WAS ALREADY FULFILLED")
                    print("YOUR BOOK LIST:",sorted(C))
                elif(USER==7):
                    if(len(D)<3):
                        M.remove(L)
                        D.append(L)
                        print("THE BOOK '",L,"' WAS SUCCESSFULLY ISSUED")
                    else:
                        print("YOUR QUATA WAS ALREADY FULFILLED")
                    print("YOUR BOOK LIST:",sorted(D))
                elif(USER==9):
                    if(len(E)<3):
                        M.remove(L)
                        E.append(L)
                        print("THE BOOK '",L,"' WAS SUCCESSFULLY ISSUED")
                    else:
                        print("YOUR QUATA WAS ALREADY FULFILLED")
                    print("YOUR BOOK LIST:",sorted(E))
                elif(USER=="LIB"):
                    if(len(LIBRARIAN)<2):
                        M.remove(L)
                        LIBRARIAN.append(L)
                        print("THE BOOK '",L,"' WAS SUCCESSFULLY ISSUED")
                    else:
                        print("YOUR QUATA FOR BOOKS WAS ALREADY FULFILLED")
                    print("YOUR BOOK LIST:",sorted(LIBRARIAN))
                continue
            else:
                print("THE BOOK '",L,"' IS NOT AVAILABLE")
        else:
            print("PLEASE ENTER A VALID USER ID")
    elif(T==3):
        USER=eval(input("ENTER YOUR USER ID: "))
        if USER in USER_ID:
            Q=str(input("ENTER THE BOOK NAME: "))
            H=Q.upper()
            if(H not in M) and (H in I):
                if(USER==1):
                    if(H in A):
                        A.remove(H)
                        M.append(H)
                        print("THE BOOK '",H,"' IS SUCCESSFULLY RETURNED")
                        print("YOUR BOOK LIST:",sorted(A))
                    else:
                        print("INVALID USER")
                elif(USER==3):
                    if(H in B):
                        B.remove(H)
                        M.append(H)
                        print("THE BOOK '",H,"' IS SUCCESSFULLY RETURNED")
                        print("YOUR BOOK LIST:",sorted(B))
                    else:
                        print("INVALID USER")
                elif(USER==5):
                    if(H in C):
                        C.remove(H)
                        M.append(H)
                        print("THE BOOK '",H,"' IS SUCCESSFULLY RETURNED")
                        print("YOUR BOOK LIST:",sorted(C))
                    else:
                        print("INVALID USER")
                elif(USER==7):
                    if(H in D):
                        D.remove(H)
                        M.append(H)
                        print("THE BOOK '",H,"' IS SUCCESSFULLY RETURNED")
                        print("YOUR BOOK LIST:",sorted(D))
                    else:
                        print("INVALID USER")
                elif(USER==9):
                   if(H in E):
                        E.remove(H)
                        M.append(H)
                        print("THE BOOK '",H,"' IS SUCCESSFULLY RETURNED")
                        print("YOUR BOOK LIST:",sorted(E))
                   else:
                        print("INVALID USER")
                elif(USER=="LIB"):
                    if(H in LIBRARIAN):
                        LIBRARIAN.remove(H)
                        M.append(H)
                        print("THE BOOK '",H,"' IS SUCCESSFULLY RETURNED")
                        print("YOUR BOOK LIST:",sorted(LIBRARIAN))
                    else:
                        print("INVALID USER")
            else:
                print("IT IS NOT THE LIBRARY PROPERTY")
        else:
             print("PLEASE ENTER A VALID USER ID")
    elif(T==4):
        LIBRARIAN=str(input("ARE YOU A LIBRARIAN(YES/NO): "))
        L=LIBRARIAN.upper()
        if(L=="YES"):
            PASS_WORD=str(input("ENTER THE PASSWORD: "))
            if(PASS_WORD==PASSWORD):
                print("*-*-*-*-*-WELCOME MR/MRS LIBRARIAN-*-*-*-*-*")
                K=int(input("ENTER NUMBER OF BOOKS: "))
                for i in range(K):
                    N=str(input("ENTER THE BOOK NAME: "))
                    M.append(N)
                print("A LIST OF BOOKS WERE ADDED SUCCESSFULLY")
                continue
            else:
                print("YOU ARE NOT A LIBRARIAN")
        else:
            continue
    elif(T==0):
        print("THANK YOU !!!")
        break
    else:
        print("ENTER A VALID CHOICE \n")
        
