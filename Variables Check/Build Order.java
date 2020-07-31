/*Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). Ail of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: {"a", "b", "c", "d", "e", "f"}
dependencies:{{"a","d"}, {"f","b"}, {"b","d"}, {"f","a"},{"d","c"}}
Output: {"f", "e", "b", "a", "d", "c"}*/
import java.util.*;
class BuildOrder {

	public static class Graph{
		int numV;
		boolean[] visited;
		// boolean visited = true;
		HashMap<String,LinkedList<String>> adjList;
		public Graph() {
			adjList = new HashMap<String,LinkedList<String>>();
		}
		public void addProjects (String [] projects){
			for(String project : projects){
				LinkedList<String> deps = new LinkedList<String>();
				deps.add(project);
				adjList.put(project, deps);
			}
			
		}
		public void addDependencies (String [][] dependencies){
			for (String[] dependency : dependencies){
				adjList.get(dependency[0]).add(dependency[1]);
			}
		}
		public void print (){
			for (String key : adjList.keySet()){
				System.out.println("Vertex "+ key +":"+ adjList.get(key));
			}
		}
	}
	public static int[] buildOrder (HashMap<String,LinkedList<String>> depGraph, String[] projects){
		boolean[] visited = new boolean[depGraph.size()];
		for (int i = 0;i<visited.length ; i++) {
			visited[i] = false;
		}
		// System.out.println(depGraph.size());
		int[] order = new int[depGraph.size()];
		int n = (depGraph.size())-1;
		for (int v=0; v < visited.length; v++) {
			// System.out.println(v);
			if (!visited[v]) {
				n = topoSort(v, visited, order, n, depGraph, projects);
			}
		}
		return order;
	}
	public static int topoSort(int v, boolean[] visited, int[] order, int n, HashMap<String,LinkedList<String>> depGraph, String[] projects) {	
		visited[v] = true;
		LinkedList adjList = depGraph.get(projects[v]);
		// System.out.println(adjList);
		for(int num=0; num<adjList.size(); num++){
			// System.out.println(adjList.get(num));
			int indexOfdep =Arrays.asList(projects).indexOf(adjList.get(num));
			if (!visited[indexOfdep]){
				n = topoSort(indexOfdep, visited, order, n, depGraph, projects);
			}
	    }
	    order[n] = v;
	    return n - 1;
	}

	public static void main(String[] args) {
		String [] p = {"a", "b", "c", "d", "e"};
		String [][] d = {{"a","b"}, {"a","c"}, {"b","d"}, {"c","d"},{"d","e"}};
		Graph depg = new Graph();
		depg.addProjects(p);
		depg.addDependencies(d);
		depg.print();
		LinkedList l = new LinkedList();
		int [] a = buildOrder(depg.adjList, p);
		for (int i = 0;i < a.length ;i++ ) {
			l.add(p[a[i]]);
		}
		System.out.println(l);

	}


}
