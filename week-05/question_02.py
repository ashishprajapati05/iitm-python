# Implement the below functions as per the docstrings.





def total_price(fruit_prices: dict, purchases) -> float:
    '''
    Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

    Arguments:
    fruit_prices: dict - fruit name as key and price as value
    purchases: list[tuple] - as list of tuples of (fruit, quantity)

    Return:
    total_price: float
    '''
    total = 0
    for fruits, quantity in purchases:
        total += fruit_prices[fruits] * quantity
    return total

def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    '''
    Compute the total price without loops.
    '''
    return sum(map(lambda x: fruit_prices[x[0]] * x[1], purchases))

def find_cheapest_fruit(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit from the fruit_prices dict, do not use min function

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    cheapest_fruit: str - the fruit with the lowest price
    '''
    cheapest = None
    cheapest_price = None
    
    for fruit in fruit_prices:
        if cheapest is None or fruit_prices[fruit] < cheapest_price:
            cheapest = fruit
            cheapest_price = fruit_prices[fruit]
    return cheapest    

def find_cheapest_fruit_no_loops(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit using min function. Do not use loops
    '''
    return min (fruit_prices, key=fruit_prices.get)

# grouping
def group_fruits(fruits:list):
    '''
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    '''
    group = {}
    
    for fruit in sorted(fruits):
        first = fruit[0]
        
        if first not in group:
            group[first] = []
            
        group[first].append(fruit)
        
    return group  
                
   
# binning
def bin_fruits(fruit_prices):
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''
    binned = {
        "cheap": set(),
        "affordable": set(),
        "costly": set()
    }
    for fruit, price in fruit_prices.items():
        if price < 3:
            binned["cheap"].add(fruit)
        elif price <= 6:
            binned["affordable"].add(fruit)
        else:
            binned["costly"].add(fruit)
    return binned        
