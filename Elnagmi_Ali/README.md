# Coffee Chats Matching Algorithm and Test Case Generator

## How to test the solution

* To test the solution you first must run the "gencases.py" file to generate a new test case. The generated data will be saved in the "testcase.txt" file. After that you can run the "strictalgo.py" to generate a list of coffee chats with the given data.

## How the algorithm works

* The basis of the matching algorithm is the calculated "matching score". The matching score is created based on various properties that are common between an aspiring professional
and executive.
<br> <br>

* Matching scores are calculated for every aspiring professional against an executive, a list is then compiled ranking the aspiring professionals by matching score from greatest to least. Every executive has their own sorted list of aspiring professionals in order of matching score.
<br> <br>

* Once all the lists are compiled, each executive goes down the list from highest matching score to lowest, and schedules the highest matching scores on the list with the same availability as the executive.
<br> <br>

* If an aspiring professional selected on the list fails to have the same availability as the executive, the next highest matching score on the list is selected.
Availability is listed as days Monday - Friday described in military time in the code.
<br> <br>

The image below is a visual representation of the selection algorithm after matching scores are calculated:

<a>
<img src="https://i.imgur.com/DJsDnT9.jpeg"
alt="visual" width="600" height = "300" border = "10"/>
</a>



