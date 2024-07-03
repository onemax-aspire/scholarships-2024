# Project Name
Max Scholarships Coffee Chat Simulation
## Overview
This project implements an algorithm in Python to facilitate weekly coffee chats for Aspiring Professionals and Senior Executives on a platform. The algorithm considers various factors such as industry alignment, the interests of Aspiring Professionals, and the availability of Senior Executives.

## Installation
Run powershell, command prompt, or terminal as administrator
1. Clone the repository git clone https://github.com/onemax-aspire/scholarships-2024.git scholarships-2024
2. Navigate to this project: scholarships-2024/Rana_Taha
3. Install Python 3.9
4. Create a virtual enviroment python -m venv env
5. Run Virtual enviroment source env/bin/activate (Mac/Linux) .\env\Scripts\activate (Windows)
6. Install dependencies: pip install -r requirements.txt
7. 
If access is still denied and the virtual enviroment is unable to be activated simply run pip install pytest in the root directory Rana_Taha as thats it is the only dependency.


## Usage
1.
Run python main.py
For solution method and see logs of coffee chat simulations in action. Parameters can be modified as per users liking

2. Run pytest test_solution.py
For Testcases. The testcases are structured to account for edge cases to see how the algorithim behaves. A large testcase is at the bottom to simulate how the algorithm might behave given sufficient userbase.


# Architechture

## Classes
The solution is structured as follows:

Person Class: Represents both Aspiring Professionals and Senior Executives with attributes like name and industry, with Aspiring Professionals and Senior Executives being child classes.
AspiringProfessional Class: Inherits from Person, includes additional attributes such as interests and professionals met.
SeniorExecutive Class: Inherits from Person, includes attributes for years of experience and appearance count.

Platform Class: Manages the platform operations, including adding professionals, creating industry-specific heaps, and generating coffee chats based on the algorithm.
The platform class also manages the algorithm. The platform class attributes to store the number of industries and a map of heaps, allowing us to map an industry to its heap. This heap contains Senior Executives.

## Solution Arcitecture:
The solution was function was arcihtiected to take 5 variables, aspiring_professionals_per_industry, senior_executives_per_industry, interests_per_aspiring_professional, weeks_to_simulate, industries. Each of these variables is important, in determining the longevity and effieciency of the algorithm below. These variables were chosen as it might repersent the data points when extracting from a database. We can assume that a full fledged platform would store users in a database. The ratio of these users (Aspiring Professionals, Senior Executives) is important, but also there industries. Here we have perfect data where there are the same number of senior_executives_per_industry and aspiring_professionals_per_industry across all indudstries, this may not always be the case, but we can assume that when extracting from the database these values can be over ridden with the minimum amount for each. This is important because it helps us calculate how long our algorithm can last for, if we have a minimum of 5 aspiring_professionals_per_industry, a minimum of 2 senior_executives_per_industry, and we've set the paramaters for our platform to make users select 5 industries out of 10. In that case we can schedule aspiring_professionals_per_industry*num_industries (5x10) coffee chats for aproximately interests_per_aspiring_professional*senior_executives_per_industry (2x5)  weeks. This would mean 50 coffee chats per week for 10 weeks, with there being only 20 (2 executive per industry) executives, each executive on average is doing 2 and a half coffee chats per week.

The benefits of this method, are that for every week we can schedule a coffee chat for every single aspiring professional on the platform. However, with higher ratios of aspiring professionals to professional executives, we end up with the senior executives being spread then.

Having the interests_per_aspiring_professional and industries be an argument to the method also has tradeoffs. It allows use to customize our solution allowing many industries or a few to be looked at. Additionally it allows more industries to be added later on. In an actual platform, the number of interests for an individual might vary, we have opted to use a set amount, however the user experience might take a hit, what if a user only wants to meet individuals from 1 industry.

Additionally, we opted for the appearance count to be total and not weekly, we are much more interested in a total appearance count for a Senior Executive than to see week by week who appeared the most.



## Algorithm
The algorithm Matches Aspiring Professionals with Senior Executives based on their industry and interests.
it ensures fair distribution of coffee chats among Senior Executives so that one senior executive does not appear too often compared to the rest
Accounts for the frequency of appearances by Senior Executives in a greedy approach.
The Algorithm is greedy because it finds the first best possible choice in terms of a coffee chat. It randomly choose an Aspiring Professionals interest, and then find the heap of Senior Executive for this industry/interest. From this, it greedily chooses the Senior Executive from the top of the heap.

A heap in Python stores a list of objects by default in a minimum order by some attribute. For example, given a random order of elements [5,3,7,1,2] if we added these to a heap and sequentially extracted them we'd get in order 1,2,3,5,7, where the smallest elements are processed first. Hence, minimum order.

The attribute we chose was appearance count. with this popping from the heap ensures we get Senior Exectuvies who have appeared the list, from here we just continue on until we can find one this Aspiriing Professional has not met with before. If we find it, we return the seneior executive, and reorder the heap after incremenign the appearance count by 1. Then we must and add the elements we popped back into our heap.

If none is found for this industry/interest, we move on to the next, until we find a valid coffee chat. Its possible for no coffee chats to be found, in that case nothing is returned, and an option print statement exists to specify that a coffee chat could not be found for this individual.  


## Tradeoffs
The shuffling mentioned before allows us to randomly select an industry, this ensures that we aren't always choosing, for example, technology coffee chats before finance, etc. This allows a more random distribution and less predictability. This is a trade off because it means our solution will be harder to test, so we dont actually look at which individuals meet with which senior executives as both the industries for selection are shuffled, and the order of senior executives and aspiring professionals are shuffled.

Another tradeoff is using a heap. A heap is an important data structure for keeping track of elements, however since we use a map of heaps, we are storing a significant amount of heaps in memory. Every time we access the heap we are processing elements greedily, we are atleast doing Log(n) operations where n is the number of aspiring professionals we need to provide with coffee chats per week. And this is the minimum most likely, we can pop from the heaps n*Log(k)*(k) where k is the total number of senior executives and n is the number of aspiring professionals. However, I chose this over the other option of maintaining a heap of valid senior executives for every aspiring professional, as then we would have to construct a heap for every aspiring professional, which of course would use a lot more memory. However, since it would get our each pop down to log(k) for each professional, we would still need to store up to O(k) memory per aspiring professional, where k is the total number of senior exectutives total.


## Improvements
Previously we discussed coffee chat ratios.
If we increase the number of executives and aspiring_professionals, lets say at a ratio for 10:1 which is a conservative estimate, we can get up to 100 Aspiring Professionals per industry, 10 Senior Executives, letting us simulate for 50 weeks. Senior_executives_per_industry being the limiting factor for the amount of simulations we can do per week. However, there will then be 1000 Coffee chats per week and 100 Senior Executives, which means every senior executive has to do 10 Coffee Chats with is not realistic.

The solution was architected in this way as per the requirements for this task, however, further improvements would cap the amount of coffee chats to a reasonable number.

The solution was architected in this way as per the requirements for this task, however, further improvements would cap the number of coffee chats to the number of senior executives on the platform, ensuring that a senior executive was at maximum meeting with only 1 individual per week. This would, of course, mean, in a biased user distribution where there are many young professionals, not all of them would be able to have a coffee chat per week.

I would restructure the algorithm, to also contain a heap containing aspiring professionals, then I would pop from the heap, professionals who have the lowest appearance count, and then I would attempt to find a coffee chat for them. I would do this for how many senior executives there are, or a predefined cap on coffee chats as determined by the limits of our system. This way, we can still find some coffee chats without feeling too thin.

Additionally, every couple of months or maybe a year, the appearance count should be reset, and the algorithm should start fresh. 

Finally, given more time and significantly more funding, it would be important to have more attributes to classify Senior Executives and Aspiring Professionals such as Location, Hobbies, Education etc, and then, with time use artificial intelligence to recommend coffee chats based on interests, these new attributes, and previous chats.
