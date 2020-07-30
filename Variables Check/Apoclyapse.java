/*In the new post-apocalyptic world, the world queen is desperately concerned
about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or
else they face massive fines. If all families abide by this policy—that is, they have continue to have
children until they have one girl, at which point they immediately stop—what will the gender ratio
of the new generation be? (Assume that the odds of someone having a boy or a girl on any given
pregnancy is equal.) Solve this out logically and then write a computer simulation of it.*/
import java.util.Random;

class Apoclyapse{
	public static int[] addChildrenToPopulation() {
		Random random = new Random();
		int boys = 0;
		int girls = 0;
		while (girls == 0) { 
			if (random.nextBoolean()) { 
				girls += 1;
			} else { 
				boys += 1;
			}
		}
		int[] population = {girls, boys};
		return population;
	}
	
	public static double genderRatioForNfamilies(int numberOfFamilies) {
		int boys = 0;
		int girls = 0;
		for (int i = 0; i < numberOfFamilies; i++) {
			int[] population = addChildrenToPopulation();
			girls += population[0];
			boys += population[1];
		}
		return girls / (double) (boys + girls); 
	}
	
	public static void main(String[] args) {
		double ratio = genderRatioForNfamilies();
		System.out.println(ratio);

	}

}
