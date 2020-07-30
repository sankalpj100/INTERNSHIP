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