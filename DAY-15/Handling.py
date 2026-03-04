'''

try:
    a=20
    if a>10
        print("GOOD")

except NameError:
    print(f"a is not defined")
except ValueError:
    print("Enter the requested data type")
except TypeError:
    print("Data types are different")
except ZeroDivisionError:
    print("Can't divide with zero")
except IndexError:
    print("The index is not present")
except KeyError:
    ("In dict this key is not present")

else:
    print("No Errors !!")

finally:
    print("End of th block")


'''



'''
try:
    
    '''
'''
    a={1:1,2:4,3:9}
    print("a[3]")
    '''
'''
    a=a+'8'
    print(a[4])
    '''


'''
except (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) as e:
    print(f"Error is occured: [e]")


else:
    print("No Errors !!")

finally:
    print("End of th block")


'''


'''
try:
    
    a=int(input())
    print(a[4])
    

except Exception as e:
    print("Error occured as: {e}")

else:
    print("No errors")
finally:
    print("End of block")

    '''


try:
    a = int(input())
    if a<0:
        raise Exception("Enter the positive value")

except Exception as e:
    print("Error occured as: {e}")

else:
    print("No errors")
finally:
    print("End of block")
















