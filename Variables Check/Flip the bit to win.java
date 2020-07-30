class FB {
	public static int flipTheBit(int inputInteger) {		
		int onesCurrLength = 0;
		int onesPrevLength = 0;
		int maxLengthOfOnes = 1; 
		while (inputInteger != 0) {
			if ((inputInteger & 1) == 1) {
				onesCurrLength++;
			} else if ((inputInteger & 1) == 0) {
				if ((inputInteger & 2) == 0) {
					onesPrevLength = 0;
				}
				else {
					onesPrevLength = onesCurrLength;
				}
				onesCurrLength = 0;
			}
			maxLengthOfOnes = Math.max(onesPrevLength + onesCurrLength + 1, maxLengthOfOnes);
			inputInteger >>>= 1;
		}
		return maxLengthOfOnes;
	}
	
	public static void main(String[] args) {
		int inputInteger = 1775;
		System.out.println(flipBit(a));
	}
}