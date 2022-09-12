## Linked List

> O(n^2) time
>   - we run an iteration over the input list, then at each iteration, we insert an element into the resulting list. 
>   
> O(1) space
>   - We used some pointers within the algorithm. However, their memory consumption is constant regardless of the input. Note, we did not create new nodes to hold the values of input list, but simply reorder the existing nodes.
>
> The first trick is that we will create a `dummy (pseudo_head) node` which serves as a pointer pointing to the resulting list.
> More precisely, this node facilitates us to always get a hold on the resulting list, especially when we need to insert a new element to the head of the resulting list.
> Given the above insight, in order to insert a new element into a singly-linked list, we apply another trick.
>
> The idea is that we use a pair of pointers (namely `prev -> next`) which serve as place-holders to guard the position where in-between we would insert a new element (i.e. `prev -> new_node -> next`).

| Item | Topic | Remark | Link(s) |
|  ----  |  ----  | ----  | ----  |
| 1 | Algorithm: Insertion Sort |  | [Leet147](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) |
| 2 | Partition | two linked list -> merge | [Leet86](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) |
