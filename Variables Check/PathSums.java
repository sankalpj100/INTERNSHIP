/* You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes). */

class PathSums {
	public static class TreeNode {
		public int data;      
		public TreeNode left;    
		public TreeNode right; 
		public TreeNode parent;
		public TreeNode(int d) {
			this.data = d;
			left = null;
			right = null;
		}
	}
	public static int countPathsWithSum(TreeNode rootOfTree, int checkPathForThisSum) {
		if (rootOfTree == null) return 0;
		int pathsFromrootOfTree = countPathsWithSumFromNode(rootOfTree, checkPathForThisSum, 0);
		int pathsOnLeft = countPathsWithSum(rootOfTree.left, checkPathForThisSum);
		int pathsOnRight = countPathsWithSum(rootOfTree.right, checkPathForThisSum);
		
		return pathsFromrootOfTree + pathsOnLeft + pathsOnRight;
	}	
	public static int countPathsWithSumFromNode(TreeNode currNode, int checkPathForThisSum, int currentSum) {
		if (currNode == null) return 0;
		currentSum += currNode.data;
		int totalPaths = 0;
		if (currentSum == checkPathForThisSum) { // Found a path from the rootOfTree
			totalPaths++;
		}
		totalPaths += countPathsWithSumFromNode(currNode.left, checkPathForThisSum, currentSum); // Go left
		totalPaths += countPathsWithSumFromNode(currNode.right, checkPathForThisSum, currentSum); // Go right
		return totalPaths;
	}	

	public static void main(String [] args) {
		
		TreeNode rootOfTree = new TreeNode(5);
		rootOfTree.left = new TreeNode(3);		
		rootOfTree.right = new TreeNode(1);
		rootOfTree.left.left = new TreeNode(-8);
		rootOfTree.left.right = new TreeNode(8);
		rootOfTree.right.left = new TreeNode(2);
		rootOfTree.right.right = new TreeNode(6);	
		System.out.println(countPathsWithSum(rootOfTree, 0));
	}
}
