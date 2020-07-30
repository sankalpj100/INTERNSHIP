/*Write a method to sort an array of strings so that all the anagrams are next to
each other.*/
import java.util.*;
public class GA {

	public static void anagramGrouper (String [] arrOfStrings){
		HashMap <String, ArrayList<String>> tableOfAnagrams = new HashMap <String, ArrayList<String>>();
		for (String inputString : arrOfStrings){
			String keyAnagram = sortTheString(inputString); 
			if (tableOfAnagrams.containsKey(keyAnagram)) { 
                tableOfAnagrams.get(keyAnagram).add(inputString); 
            } 
            else { 
                ArrayList<String> listOfAnagrams = new ArrayList<>(); 
                listOfAnagrams.add(inputString); 
                tableOfAnagrams.put(keyAnagram, listOfAnagrams); 
            } 
		}
		System.out.println(tableOfAnagrams);
	}

	public static String sortTheString(String stringForSort){
		char[] arrOfChars = stringForSort.toCharArray();
		Arrays.sort(arrOfChars);
		return new String(arrOfChars);

	}
	public static void main(String[] args) {
		String[] lol = {"acre", "race", "lol","llo","care", "oll", "acer"};
		anagramGrouper(lol);
	}
}
