class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""You are provided with two singly linked lists, where each linked list represents a positive integer. Each node in the list contains a 
single digit, and the digits are arranged such that the head node of the list holds the most significant digit (i.e., the digit with the 
highest place value).

Your task is to compare the two numbers represented by these linked lists and return an integer that is the maximum of the two.

Note: The numbers may include leading zeroes.
 """

class LinkedList:
    def counterlen(self, head):
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        return n

    def max_list(self, num1, num2):
        n1 = self.counterlen(num1)
        n2 = self.counterlen(num2)

        if n1 > n2:
            return num1
        elif n2 > n1:
            return num2
        else:
            return num1

