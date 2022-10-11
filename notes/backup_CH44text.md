```
欢迎来到『九章算法班 2022版』的第44节课，今天我们一起来学习『二叉查找树的增删查改』
在这一章里，我们将学习二叉查找树以及它的增、删、查、改操作。
本章关键字：Divide and Conquer（分治法），BST（Binary Search Tree，二叉查找树）。

BST 的增删查改
什么是二叉搜索树(Binary Search Tree)

二叉搜索树可以是一棵空树或者是一棵满足下列条件的二叉树:
如果它的左子树不空，则左子树上所有节点值均小于它的根节点值。
如果它的右子树不空，则右子树上所有节点值均大于它的根节点值。
它的左右子树均为二叉搜索树(BST)。
严格定义下BST中是没有值相等的节点的(No duplicate nodes)。
根据上述特性，我们可以得到一个结论：BST中序遍历得到的序列是升序的。
BST基本操作——增删改查(CRUD)

对于树节点的定义如下：
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
        
        
基本操作之查找(Retrieve)
思路

查找值为val的节点，如果val小于根节点则在左子树中查找，反之在右子树中查找
代码实现

Java:
public TreeNode searchBST(TreeNode root, int val) {
	if (root == null) {
		return null;
	}// 未找到值为val的节点
	if (val < root.val) {
		return searchBST(root.left, val);//val小于根节点值，在左子树中查找
	} else if (val > root.val) {
		return searchBST(root.right, val);//val大于根节点值，在右子树中查找
	} else {
		return root;//找到了
	}
}

Python:
def searchBST(root, val):
    if not root:
        return None # 未找到值为val的节点
    if val < root.val:
        return searchBST(root.left, val) # val小于根节点值，在左子树中查找哦
    elif val > root.val:
        return searchBST(root.right, val) # val大于根节点值，在右子树中查找
    else:
        return root
        
        
基本操作之修改(Update)
思路

修改仅仅需要在查找到需要修改的节点之后，更新这个节点的值就可以了，(假如修改过后整棵树还满足BST的性质)
代码实现

Java:
public void updateBST(TreeNode root, int target, int val) {
	if (root == null) {
		return;
	}// 未找到target节点
	if (target < root.val) {
		updateBST(root.left, target, val);//target小于根节点值，在左子树中查找
	} else if (target > root.val) {
		updateBST(root.right, target, val);//target大于根节点值，在右子树中查找
	} else { //找到了
		root.val = val;
	}
}
Python:
def updateBSTBST(root, target, val):
    if not root:
        return  # 未找到target节点
    if target < root.val:
        updateBST(root.left, target, val) # target小于根节点值，在左子树中查找哦
    elif target > root.val:
        updateBST(root.right, target, val) # target大于根节点值，在右子树中查找
    else:  # 找到了
        root.val = val
        
        
基本操作之增加(Create)
思路

根节点为空，则待添加的节点为根节点
如果待添加的节点值小于根节点，则在左子树中添加
如果待添加的节点值大于根节点，则在右子树中添加
我们统一在树的叶子节点(Leaf Node)后添加
代码实现

Java:
public TreeNode insertNode(TreeNode root, TreeNode node) {
    if (root == null) {
        return node;
    }
    if (root.val > node.val) {
        root.left = insertNode(root.left, node);
    } else {
        root.right = insertNode(root.right, node);
    }
    return root;
}
Python:
def insertNode(root, node):
    if not root:
        return node
    if root.val > node.val:
        root.left = insertNode(root.left, node)
    else:
        root.right = insertNode(root.right, node)
    return root
    
    
基本操作之删除(Delete)
思路(最为复杂)

考虑待删除的节点为叶子节点，可以直接删除并修改父亲节点(Parent Node)的指针，需要区分待删节点是否为根节点
考虑待删除的节点为单支节点(只有一棵子树——左子树 or 右子树)，与删除链表节点操作类似，同样的需要区分待删节点是否为根节点
考虑待删节点有两棵子树，可以将待删节点与右子树中的最小节点进行交换，由于右子树中的最小节点一定为叶子节点，所以这时再删除待删的节点可以参考第一条
详细的解释可以看 http://www.algolist.net/Data_structures/Binary_search_tree/Removal
代码实现

Java:
public TreeNode removeNode(TreeNode root, int value) {
    TreeNode dummy = new TreeNode(0);
    dummy.left = root;
    TreeNode parent = findNode(dummy, root, value);
    TreeNode node;
    if (parent.left != null && parent.left.val == value) {
        node = parent.left;
    } else if (parent.right != null && parent.right.val == value) {
        node = parent.right;
    } else {
        return dummy.left;
    }
    deleteNode(parent, node);
    return dummy.left;
}

private TreeNode findNode(TreeNode parent, TreeNode node, int value) {
    if (node == null) {
        return parent;
    }
    if (node.val == value) {
        return parent;
    }
    if (value < node.val) {
        return findNode(node, node.left, value);
    } else {
        return findNode(node, node.right, value);
    }
}

private void deleteNode(TreeNode parent, TreeNode node) {
    if (node.right == null) {
        if (parent.left == node) {
            parent.left = node.left;
        } else {
            parent.right = node.left;
        }
    } else {
        TreeNode temp = node.right;
        TreeNode father = node;
        while (temp.left != null) {
            father = temp;
            temp = temp.left;
        }
        if (father.left == temp) {
            father.left = temp.right;
        } else {
            father.right = temp.right;
        }
        if (parent.left == node) {
            parent.left = temp;
        } else {
            parent.right = temp;
        }
        temp.left = node.left;
        temp.right = node.right;
    }
}
Python:
def removeNode(root, value):
    dummy = TreeNode(0)
    dummy.left = root
    parent = findNode(dummy, root, value)
    node = None
    if parent.left and parent.left.val == value:
        node = parent.left
    elif parent.right and parent.right.val == value:
        node = parent.right
    else:
        return dummy.left
    deleteNode(parent, node)
    return dummy.left

def findNode(parent, node, value):
    if not node:
        return parent
    if node.val == value:
        return parent
    if value < node.val:
        return findNode(node,node.left, value)
    else:
        return findNode(node, node.right, value)

def deleteNode(parent, node):
    if not node.right:
        if parent.left == node:
            parent.left = node.left
        else:
            parent.right = node.left
    else:
        temp = node.right
        father = node
        while temp.left:
            father = temp
            temp = temp.left
        if father.left == temp:
            father.left = temp.right
        else:
            father.right = temp.right
        if parent.left == node:
            parent.left = temp
        else:
            parent.right = temp
        temp.left = node.left
        temp.right = node.right
        
 
请同学在理解代码的基础上努力完成下面的习题哦~
Search Range in Binary Search Tree
Two Sum IV - Input is a BST
Trim a Binary Search Tree

本章内容到此结束了，是不是觉得意犹未尽呢，要记得好好复习学到的知识哦。在下一章中我们将利用之前学到的DFS，对组合问题进行求解，我们下一章见。
```