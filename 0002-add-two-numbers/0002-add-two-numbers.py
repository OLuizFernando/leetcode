# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, l: Optional[ListNode]) -> int:
        length = 1 # non-empty linked lists have at least 1 node
        while True:
            if l.next: # checks if it isn't the last node
                length += 1
                l = l.next # moves to the next node
            else:
                return length


    def turnIntoReversedLinkedList(self, num: int) -> Optional[ListNode]:
        str_num = str(num) # turns into a string to access the digits individually
        current_node = None 
        for i in range(len(str_num)):
            # on the first iteration, current_node == None, so it starts at the last node
            current_node = ListNode(val=int(str_num[i]), next=current_node)

        return current_node


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked_lists = [l1, l2] # add the parameters to a list to iterate over them
        num_sum = 0

        for linked_list in linked_lists:
            # the variable "linked_list" points to the first node
            current_node = linked_list

            # "mult_val" helps convert the "linked_list" into an "int" by organizing numbers as units, tens, hundreds, and so on
            mult_val = 1

            for _ in range(self.get_length(linked_list)):
                num_sum += current_node.val * mult_val
                current_node = current_node.next # moves to the next node
                mult_val *= 10

        return self.turnIntoReversedLinkedList(num_sum) # turns the result of the linked lists sum into a reversed linked list
