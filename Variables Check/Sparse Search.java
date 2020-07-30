/*Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: b a l l , { " a t " , "", "", "", "ball", "", "car", "", "", "dad", ""}
Output: 4*/
public class SS{
	public static int modifiedBinarySearch(String[] arrOfStrings, String searchString, int lowerBound, int upperBound) {
		if (lowerBound > upperBound) {
			return -1;
		}
		int midpoint = (upperBound + lowerBound) / 2;
		if (arrOfStrings[midpoint].isEmpty()) { 
			int newLB = midpoint - 1;
			int newUB = midpoint + 1;
			while (true) {
				if (newLB < lowerBound && newUB > upperBound) {
					return -1;
				} else if (newUB <= upperBound && !arrOfStrings[newUB].isEmpty()) {
					midpoint = newUB;
					break;
				} else if (newLB >= lowerBound && !arrOfStrings[newLB].isEmpty()) {
					midpoint = newLB;
					break;
				}
				newUB++;
				newLB--;
			}
		}
		if (searchString.equals(arrOfStrings[midpoint])) { // Found the String!
			return midpoint;
		} else if (arrOfStrings[midpoint].compareTo(searchString) < 0) { 
			return modifiedBinarySearch(arrOfStrings, searchString, midpoint + 1, upperBound);
		} else { 
			return modifiedBinarySearch(arrOfStrings, searchString, lowerBound, midpoint - 1);
		}
	}	
		
	public static int sparseSearch(String[] arrOfStrings, String searchString) {
		return modifiedBinarySearch(arrOfStrings, searchString, 0, arrOfStrings.length - 1);
	}
	
	public static void main(String[] args) {
        String[] stringList = {"apple", "", "", "banana", "", "", "", "carrot", "duck", "", "", "eel", "", "flower"};
        System.out.println(sparseSearch(stringList, "flower"));
    }
}
