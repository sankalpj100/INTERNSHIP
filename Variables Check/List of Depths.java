public class BO {

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

	public static ArrayList<TreeNode> buildOrder(TreeNode rootOfTree) {
		ArrayList<TreeNode> dependencyNodes = new ArrayList<TreeNode>();
		ArrayList<TreeNode> lessDepNodes = new ArrayList<TreeNode>();

		ArrayList<TreeNode> currList = new ArrayList<TreeNode>();
		if (rootOfTree != null) {
				currList.add(rootOfTree);
			}
			
		while (currList.size() > 0) {
			for (TreeNode currNode: currList) {
				if (!((currNode.left == null && currNode.right == null)) && dependencyNodes.contains(currNode)) {	
					dependencyNodes.add(currNode);
				} 
				else {
					lessDepNodes.add(currNode);
				}
			
				
			}
			ArrayList<TreeNode> parentList = currList; 
			currList = new ArrayList<TreeNode>(); 
			for (TreeNode parentNode : parentList) {
				if (parentNode.left != null) {
					currList.add(parentNode.left);
				}
				if (parentNode.right != null) {
					currList.add(parentNode.right);
				}
			}
		}
		dependencyNodes.addAll(lessDepNodes);
		return dependencyNodes; 
    }

    public static void printList(ArrayList<TreeNode> input) {
    	for (TreeNode node: input) {
    		System.out.println(node.data + " ")
    	}
    }

    public static void main(String[] args) {
    	
    }
}