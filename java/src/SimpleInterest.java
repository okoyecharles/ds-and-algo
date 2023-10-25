public class SimpleInterest {
    public static void main(String[] args) {
        // Declare the variables needed for calculation
        float principal, rate, time;
        float simple_interest;

        // Assign values to variables
        // 10,000 naira for 3 years at a rate of 2.5% per annum
        principal = 10000;
        rate = 2.5f;
        time = 3;

        // Calculate interest
        simple_interest = (principal * rate * time) / 100;

        // Print out the result of calculation
        System.out.println("The simple interest is: " + simple_interest);
    }
}
