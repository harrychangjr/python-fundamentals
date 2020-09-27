def foobar(n): #return sum of all positive odd numbers <= n
    value, total = 1, 0
    while value <= n:
        if value%2 == 1:
            total = total + value
        value = value + 1
    return total

def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
def factorial_iterative(n):
    pdt, ctr = 1,1
    while ctr <= n:
        pdt = pdt * ctr
        ctr = ctr + 1
    return pdt

def exponentiation_recursive(x,e):
    if e == 0:
        return 1
    elif e >= 1:
        return x * exponentiation_recursive(x,e-1)
        
def exponentiation_iterative(x,e):
    number = 1
    for i in range(e):
        number = number * x
    return number

#Define recursive and iterative functions star_wars_<recursive or iterative> that takes an argument num_enemy_ships 
#and returns a string command to take down all the enemy ships.
#The string command will comprise of alternating beams: '*-' and '*--'
#For example:
#star_wars_<recursive or iterative>(3) will return '*-*--*-'
#star_wars_<recursive or iterative>(6) will return '*-*--*-*--*-*--'
#star_wars_<recursive or iterative>(0) will return ''

def star_wars_recursive(num_enemy_ships):
    n = num_enemy_ships    
    if n == 0:
        return ''
    elif n == 1:
        return '*-'
    elif n == 2:
        return star_wars_recursive(1) + '*--'
    else:
        string = n*star_wars_recursive(2)
        return string[:len(string)//2]
        
def star_wars_iterative(num_enemy_ships):
    n = num_enemy_ships
    count = 1
    pic1,pic2 = '*-','*--'
    if n == 0:
        return ''
    if n % 2 == 0:
        output = pic2
    else:
        output = pic1   
    while count < n: 
        output = pic1 + pic2
        pic1, pic2 = pic2, pic1
        count = count + 1
    if n%2==0:
        return (n//2)*output
    else:
        return pic1 + (n//2)*output
