# test1
Parking Lot Challenge:

Create a parking lot class that takes in a square footage size as input and creates an array of empty values based on the input square footage size. 
Assume every parking spot is 8x12 (96 ft2) for this program, but have the algorithm that calculates the array size be able to account for different parking spot sizes.
For example, a parking lot of size 2000ft2 can fit 20 cars, but if the parking spots were 10x12 (120 ft2), it could only fit 16 cars. 
The size of the array will determine how many cars can fit in the parking lot.

Create a car class that takes in a 7 digit license plate and sets it as a property. The car will have 2 methods:

1.        A magic method to output the license plate when converting the class instance to a string.

2.        A "park" method that will take a parking lot and spot # as input and fill in the selected spot in the parking lot.
If another car is parked in that spot, return a status indicating the car was not parked successfully. If no car is parked in that spot, 
return a status indicating the car was successfully parked.

Have a main method take an array of cars with random license plates and have them park in a random spot in the parking lot array until the input
array is empty or the parking lot is full. If a car tries to park in an occupied spot, have it try to park in a different spot instead until it successfully parks.
Once the parking lot is full, exit the program.

Output when a car does or does not park successfully to the terminal (Ex. "Car with license plate [LICENSE_PLATE] parked successfully in spot [SPOT #]").

OPTIONAL/BONUS - Create a method for the parking lot class that maps vehicles to parked spots in a JSON object. Call this method at the end of the program,
save the object to a file, and upload the file to an input S3 bucket.
