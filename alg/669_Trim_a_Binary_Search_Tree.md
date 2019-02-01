### 669. Trim a Binary Search Tree

如果一个点不在范围内，不代表它的子树不在范围内，所以有中间那两个if，用来返回满足条件的子树结构。

```java
public TreeNode trimBST(TreeNode root, int L, int R) {
    if (root == null) return null;
    
    if (root.val < L) return trimBST(root.right, L, R);
    if (root.val > R) return trimBST(root.left, L, R);
    
    root.left = trimBST(root.left, L, R);
    root.right = trimBST(root.right, L, R);
    
    return root;
}
```