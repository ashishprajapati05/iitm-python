# A square metal plate in 2D space is the setup we are going to work with. The spatial extent of the metal plate is given by:

# 0≤x,y≤5
# The temperature at any point 

# (x,y) on the plate is given by the following equation. The temperature is measured in Celsius and can be negative:

# f(x,y)=30+x^2+y^2 −3x−4y

# A micro-organism lives on the surface of the metal plate. It occupies only those points on the plate where both the coordinates are integers. The organism cannot survive in high temperatures and instinctively moves to regions of low temperature that are less or equal to a threshold 
# T. If no such region is found, it can't survive. The terms high and low are used in a relative sense and should be compared with respect to the threshold.

# Write a function named survival that accepts the value of 
# T as argument and returns True if the organism can survive on the metal plate, and False otherwise.

# You do not have to accept input from the user or print the output to the console. You just have to write the function definition.

# ans

def survival(T):
    return T >= 24