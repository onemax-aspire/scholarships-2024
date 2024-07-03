# Project Name: Max Scholarships Coffee Chat Simulation
Overview
This project implements an algorithm in Python to facilitate weekly coffee chats for Aspiring Professionals and Senior Executives on a platform. The algorithm considers various factors such as industry alignment, the interests of Aspiring Professionals, and the availability of Senior Executives.

# Installation
Run PowerShell, Command Prompt, or Terminal as administrator.
Clone the repository using the following URL: https://github.com/onemax-aspire/scholarships-2024.git and name the directory scholarships-2024.
Navigate to the project directory scholarships-2024/Katyal_Dev.
Install Python 3.9.
Create a virtual environment and activate it.
Install dependencies listed in the requirements.txt file.
If access is denied and the virtual environment is unable to be activated, simply install pytest as it is the only dependency.
Usage
Run the main program to see the solution method and logs of the coffee chat simulations in action. Parameters can be modified as per user preference.
Run the test cases to account for edge cases and see how the algorithm behaves. A large test case at the bottom simulates how the algorithm might behave given a sufficient user base.
#Architecture
Classes
The solution is structured as follows:

Person Class: Represents both Aspiring Professionals and Senior Executives with attributes like name and industry, with Aspiring Professionals and Senior Executives being child classes.

AspiringProfessional Class: Inherits from Person, includes additional attributes such as interests and professionals met.
SeniorExecutive Class: Inherits from Person, includes attributes for years of experience and appearance count.
Platform Class: Manages the platform operations, including adding professionals, creating industry-specific heaps, and generating coffee chats based on the algorithm. The platform class also manages the algorithm. The platform class attributes store the number of industries and a map of heaps, allowing us to map an industry to its heap. This heap contains Senior Executives.

#Solution Architecture
The solution function is designed to take five variables: aspiring professionals per industry, senior executives per industry, interests per aspiring professional, weeks to simulate, and industries. Each of these variables is important in determining the longevity and efficiency of the algorithm below.

These variables were chosen as they might represent the data points when extracting from a database. We assume that a full-fledged platform would store users in a database. The ratio of these users (Aspiring Professionals, Senior Executives) is important, as well as their industries.

Here, we have perfect data where there are the same number of senior executives per industry and aspiring professionals per industry across all industries, which may not always be the case. However, we can assume that when extracting from the database, these values can be overridden with the minimum amount for each. This is important because it helps us calculate how long our algorithm can last.

For example, if we have a minimum of 5 aspiring professionals per industry and a minimum of 2 senior executives per industry, and we've set the parameters for our platform to make users select 5 industries out of 10, we can schedule aspiring professionals per industry times the number of industries (5x10) coffee chats for approximately interests per aspiring professional times senior executives per industry (2x5) weeks. This would mean 50 coffee chats per week for 10 weeks. With there being only 20 (2 executives per industry) executives, each executive, on average, is doing 2.5 coffee chats per week.

#Benefits
For every week, we can schedule a coffee chat for every single aspiring professional on the platform. However, with higher ratios of aspiring professionals to professional executives, we end up with the senior executives being spread thin.

Having the interests per aspiring professional and industries be an argument to the method also has tradeoffs. It allows us to customize our solution, allowing many industries or a few to be looked at. Additionally, it allows more industries to be added later on. In an actual platform, the number of interests for an individual might vary. We have opted to use a set amount. However, the user experience might take a hit if a user only wants to meet individuals from one industry.

Additionally, we opted for the appearance count to be total and not weekly. We are much more interested in a total appearance count for a Senior Executive than seeing week by week who appeared the most.

#Algorithm
The algorithm matches Aspiring Professionals with Senior Executives based on their industry and interests. It ensures fair distribution of coffee chats among Senior Executives so that one senior executive does not appear too often compared to the rest. It accounts for the frequency of appearances by Senior Executives in a greedy approach. The algorithm is greedy because it finds the first best possible choice in terms of a coffee chat. It randomly chooses an Aspiring Professional's interest, and then finds the heap of Senior Executives for this industry/interest. From this, it greedily chooses the Senior Executive from the top of the heap.

A heap in Python stores a list of objects by default in a minimum order by some attribute. For example, given a random order of elements [5,3,7,1,2], if we added these to a heap and sequentially extracted them, we'd get in order 1,2,3,5,7, where the smallest elements are processed first, hence minimum order.

The attribute we chose was appearance count. With this, popping from the heap ensures we get Senior Executives who have appeared the least. From here, we just continue on until we can find one this Aspiring Professional has not met with before. If we find it, we return the Senior Executive, and reorder the heap after incrementing the appearance count by 1. Then we must add the elements we popped back into our heap.

If none is found for this industry/interest, we move on to the next, until we find a valid coffee chat. It's possible for no coffee chats to be found. In that case, nothing is returned, and an optional print statement exists to specify that a coffee chat could not be found for this individual.

#Tradeoffs
The shuffling mentioned before allows us to randomly select an industry. This ensures that we aren't always choosing, for example, technology coffee chats before finance, etc. This allows a more random distribution and less predictability. This is a tradeoff because it means our solution will be harder to test, so we don't actually look at which individuals meet with which senior executives as both the industries for selection are shuffled, and the order of senior executives and aspiring professionals are shuffled.

Another tradeoff is using a heap. A heap is an important data structure for keeping track of elements. However, since we use a map of heaps, we are storing a significant amount of heaps in memory. Every time we access the heap, we are processing elements greedily. We are at least doing log(n) operations where n is the number of aspiring professionals we need to provide with coffee chats per week. And this is the minimum most likely. We can pop from the heaps n log(k) (k) where k is the total number of senior executives and n is the number of aspiring professionals. However, I chose this over the other option of maintaining a heap of valid senior executives for every aspiring professional, as then we would have to construct a heap for every aspiring professional, which of course would use a lot more memory. However, since it would get each pop down to log(k) for each professional, we would still need to store up to O(k) memory per aspiring professional, where k is the total number of senior executives total.

#Improvements
Previously we discussed coffee chat ratios. If we increase the number of executives and aspiring professionals, let's say at a ratio of 10:1 which is a conservative estimate, we can get up to 100 Aspiring Professionals per industry and 10 Senior Executives, letting us simulate for 50 weeks. Senior executives per industry being the limiting factor for the amount of simulations we can do per week. However, there will then be 1000 coffee chats per week and 100 Senior Executives, which means every senior executive has to do 10 coffee chats, which is not realistic.

The solution was architected in this way as per the requirements for this task. However, further improvements would cap the number of coffee chats to a reasonable number. The solution was architected in this way as per the requirements for this task. However, further improvements would cap the number of coffee chats to the number of senior executives on the platform, ensuring that a senior executive was at maximum meeting with only one individual per week. This would, of course, mean in a biased user distribution where there are many young professionals, not all of them would be able to have a coffee chat per week.

I would restructure the algorithm to also contain a heap containing aspiring professionals. Then I would pop from the heap professionals who have the lowest appearance count, and then I would attempt to find a coffee chat for them. I would do this for how many senior executives there are, or a predefined cap on coffee chats as determined by the limits of our system. This way, we can still find some coffee chats without feeling too thin.

Additionally, every couple of months or maybe a year, the appearance count should be reset, and the algorithm should start fresh.

Finally, given more time and significantly more funding, it would be important to have more attributes to classify Senior Executives and Aspiring Professionals such as location, hobbies, education, etc. With time, we could use artificial intelligence to recommend coffee chats based on interests, these new attributes, and previous chats.
