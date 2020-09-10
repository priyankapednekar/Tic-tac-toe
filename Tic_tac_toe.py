
def print_matrix(list1):
    n=3
    i=0
    while i < 3:
        print(" --- "*n)
        print("|{}   |{}   |{}   |".format(list1[i][0],list1[i][1],list1[i][2]))
        i+=1
    print(" --- "*n)

def play():
    val=3*3
    list1=[[(" ") for i in range(3)] for i in range(3)]
    print_matrix(list1)

    while val > 0:
        r1,c1=input("please enter rwo,column for 1st player in this format (r,c)\n").split(",")
        list1[int(r1)][int(c1)]='x'
        print_matrix(list1)
        val-=1
        if val >0:
            r2,c2=input("please enter rwo,column for 2nd player in this format (r,c)\n").split(",")
            list1[int(r2)][int(c2)]='o'
            print_matrix(list1)
            val-=1
        else:
            break

    return list1


def decide_winner(list1,n):
    for i in range(n):
        for x in range(n):
            if list1[0][x]==list1[1][x]==list1[2][x]:
                return list1[1][x]
            elif list1[i][0]==list1[i][1]==list1[i][2]:
                return list1[i][1]

    i=0
    x=0
    if list1[i][x]==list1[i+1][x+1]==list1[i+2][x+2]:
        return list1[i][x]
    elif list1[0][2]==list1[0][0]==list1[2][0]:
        return list1[0][2]

    return 0


def main():
    print("Welcome to tic-tac-toe Game!!\n\n")
    list1=play()
    print_matrix(list1)
    print(list1)
    flag=decide_winner(list1,3)
    if flag=='o':
        print("{} player Won!!".format(2))
    elif flag=='x':
        print("{} player Won!!".format(1))
    else:
        print("No winner!!")



if __name__ == '__main__':
    main()
