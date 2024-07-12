"""
1 - Receive an  int
2 - Know if number is multiple of 3 and 5:
    Bacon & eggs
3 - Know if number is multiple of 3
    Bacon
3 - Know if number is multiple of 5
    eggs
4 - Know if number is not multiple of 3 & 5
    starving

"""

def bacon_with_eggs(num):
    assert isinstance(num,int), 'number must be int'

    if num %3  == 0 and num % 5==0:
        return 'Bacon & eggs'
    
    if num %3  == 0 :
        return 'Bacon'
    
    if num %5  == 0 :
        return 'eggs'

    return 'starving'