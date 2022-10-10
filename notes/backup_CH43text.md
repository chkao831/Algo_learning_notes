```
欢迎来到『九章算法班 2022版』的第43节课，今天我们一起来学习『后序遍历非递归与Morris算法』
在第13章的学习中，我们掌握了如何使用非递归形式获得二叉树的前序、中序遍历。而在这节课中，我们将继续使用非递归形式求出二叉树的后序遍历。然后我们将学习另外一类遍历二叉树的算法——Morris算法。
本章关键字：前序遍历（Preorder Traversal），中序遍历（Inorder Traversal），后序遍历（Postorder Traversal）。
与前序、中序的非递归方式相同，二叉树的非递归后序遍历也需要借助栈来完成，遍历顺序为左、右、根。
大致思路如下：
1、如果根节点非空，将根节点加入到栈中。
2、如果栈不空，取栈顶元素（暂时不弹出），
a.如果（左子树已访问过或者左子树为空），且（右子树已访问过或右子树为空），则弹出栈顶节点，将其值加入数组，
b.如果左子树不为空，且未访问过，则将左子节点加入栈中，并标左子树已访问过。
c.如果右子树不为空，且未访问过，则将右子节点加入栈中，并标右子树已访问过。
3、重复第二步，直到栈空。

java版本：
public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();
    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode prev = null; // previously traversed node
    TreeNode curr = root;
    if (root == null) {
        return result;
    }

    stack.push(root);
    while (!stack.empty()) {
        curr = stack.peek();
        if (prev == null || prev.left == curr || prev.right == curr) { // traverse down the tree
            if (curr.left != null) {
                stack.push(curr.left);
            } else if (curr.right != null) {
                stack.push(curr.right);
            }
        } else if (curr.left == prev) { // traverse up the tree from the left
            if (curr.right != null) {
                stack.push(curr.right);
            }
        } else { // traverse up the tree from the right
            result.add(curr.val);
            stack.pop();
        }
        prev = curr;
    }
    return result;
}

python版本
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        result = []
        stack = []
        prev, curr = None, root

        if not root:
            return result

        stack.append(root)
        while len(stack) > 0:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:  # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:  # traverse up the tree from the left
                if curr.right:
                    stack.append(curr.right)
            else:  # traverse up the tree from the right
                result.append(curr.val)
                stack.pop()
            prev = curr

        return result
        
请同学借助上面的模板，尝试完成相关的练习。

Binary Tree Postorder Traversal

下面我们将学习一种完全不同的思想，相比使用栈的思想（空间换时间）来说，Morris算法是一种使用时间换取空间的算法。

什么是 Morris 算法
与递归和使用栈空间遍历的思想不同，Morris 算法使用二叉树中的叶节点的right指针来保存后面将要访问的节点的信息，当这个right指针使用完成之后，再将它置为null，但是在访问过程中有些节点会访问两次，所以与递归的空间换时间的思路不同，Morris则是使用时间换空间的思想。

节点定义

Java:
class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    pubic TreeNode(int val) {
        this.val = val;
        this.left = this.right = null;
    }
}
Python:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
https://github.com/chkao831/Algo_learning_notes/blob/main/images/CH43_Morris1.jpg
用 Morris 算法进行中序遍历(Inorder Traversal)
思路

如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
重复1、2两步直到当前节点为空。
上图为每一步迭代的结果（从左至右，从上到下），cur代表当前节点，深色节点表示该节点已输出。
示例代码

Java:
public class Solution {
    /**
     * @param root: A Tree
     * @return: Inorder in ArrayList which contains node values.
     */

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;

        while (root != null) {
            if (root.left != null) {
                cur = root.left;
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }

                if (cur.right == root) {
                    nums.add(root.val);
                    cur.right = null;
                    root = root.right;
                } else {
                    cur.right = root;
                    root = root.left;
                }               
            } else {
                nums.add(root.val);
                root = root.right;
            }
        }

        return nums;
    } 

}
Python:


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        nums = []
        cur = None
    
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                
                if cur.right == root:
                    nums.append(root.val)
                    cur.right = None
                    root = root.right
                else:
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right
                
        return nums
        
https://github.com/chkao831/Algo_learning_notes/blob/main/images/CH43_Morris2.jpg
用 Morris 算法实现先序遍历(Preorder Traversal)
思路

如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。输出当前节点（与中序遍历唯一一点不同）。当前节点更新为当前节点的左孩子。
如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。当前节点更新为当前节点的右孩子。
重复1、2两步直到当前节点为空。
示例代码

Java:
public class Solution {
    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        // morris traversal
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;
        while (root != null) {
            if (root.left != null) {
                cur = root.left;
                // find the predecessor of root node
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }
                if (cur.right == root) {
                    cur.right = null;
                    root = root.right;
                } else {
                    nums.add(root.val);
                    cur.right = root;
                    root = root.left;
                }
            } else {
                nums.add(root.val);   
                root = root.right;
            }
        }
        return nums;
    } 
}
Python:
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        nums = []
        cur = None
        
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                if cur.right == root:
                    cur.right = None
                    root = root.right
                else:
                    nums.append(root.val)
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right
                
        return nums

用 Morris 算法实现后序遍历(Postorder Traversal)
思路

后序遍历其实可以看作是和前序遍历左右对称的，此处，我们同样可以利用这个性质，基于前序遍历的算法，可以很快得到后序遍历的结果。我们只需要将前序遍历中所有的左孩子和右孩子进行交换就可以了。
示例代码

Java:
public class Solution {
    /**
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;
        while (root != null) {
            if (root.right != null) {
                cur = root.right;
                while (cur.left != null && cur.left != root) {
                    cur = cur.left;
                }
                if (cur.left == root) {
                    cur.left = null;
                    root = root.left;
                } else {
                    nums.add(root.val);
                    cur.left = root;
                    root = root.right;
                }
            } else {
                nums.add(root.val);
                root = root.left;
            }
        }
        Collections.reverse(nums);
        return nums;
    } 
}
Python:
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        nums = []
        cur = None

        while root:
            if root.right != None:
                cur = root.right
                while cur.left and cur.left != root:
                    cur = cur.left
                if cur.left == root:
                    cur.left = None
                    root = root.left
                else:
                    nums.append(root.val)
                    cur.left = root
                    root = root.right
            else:
                nums.append(root.val)
                root = root.left
                
        nums.reverse()
        return nums
        
        
学有余力的同学，可以尝试使用Morris算法来分别AC二叉树的前中后序遍历问题。

Binary Tree Preorder Traversal
Binary Tree Inorder Traversal
Binary Tree Postorder Traversal

本章的学习就到这里，在下一章中我们将学习二叉搜索树（BST）的相关内容，还请同学努力学习哦~
```
