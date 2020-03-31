"""Hash email adress"""
import hashlib
import uuid

# Available has algorithms in python
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# Example 1
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

# Example 2
mystring = 'Hello World'
# TO hash the string, you have to encode the string
mystring_b = mystring.encode()

hash_object = hashlib.sha1(mystring_b)
# hash_object = haslib.sha224(mystring_b)
# hash_object = haslib.sha256(mystring_b)
# hash_object = haslib.sha384(mystring_b)
# hash_object = haslib.sha512(mystring_b)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Update hashing method, replacing with a new algorithm to hash
hash_object = hashlib.new('sha512')
hash_object.update(b'Hello World')
print(hash_object.hexdigest())

def hash_user_data(data):
    """Take in a string, email adress or phone number, return a hashed string."""

    # uuid is used to generate a random number
    salt = uuid.uuid4().hex

    hashed_data_plus_salt = hashlib.sha1(salt.encode() + data.encode()).hexdigest() + ':' + salt
    print(hashed_data_plus_salt)
    return hashed_data_plus_salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_user_data(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')  


# if __name__ == "__main__":

#   if doctest.testmod().failed == 0:
#       print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")




