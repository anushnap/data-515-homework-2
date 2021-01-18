# Anushna Prakash
# DATA 515
# Homework 2: Programming
# January 21, 2021

# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol. Let's call the first part *personal* and the latter part *domain*, i.e., personal@domain. The length of the personal part may be up to 64 characters long and domain name may be up to 253 characters.

# The personal and domain parts contains the following ASCII characters:

# - Uppercase (`A-Z`) and lowercase (`a-z`) English letters.
# - Digits (`0-9`).
# - Character `-` (dash).
# - Character `.` (period, dot or fullstop) provided that it is not the first or last character and it will not come one after the other.

# Additionally, the personal part can contain:

# - Characters `! # $ % & ' * + / = ? ^ _ { | } ~`

# Example of valid emails:

#     mysite@ourearth.com
#     my.ownsite@ourearth.org
#     mysite@you.me.net
#     mysite123@gmail.b [This is valid, discussion in Canvas]

# Example of invalid emails:

#     mysite.ourearth.com [@ is not present]
#     mysite@.com.my [domain can not start with dot "."]
#     @you.me.net [No character before @]
#     mysite@.org.org [domain can not start with dot "."]
#     .mysite@mysite.org [Personal part can not start with "."]
#     mysite()*@gmail.com [Invalid due to parentheses in personal part, asterisk acceptable]
#     mysite..1234@yahoo.com [double dots are not allowed]


# Takes an string arg email and returns whether the email is valid based on requirements for valid emails
def check_email_validity(email):
    # If email does not contain @ symbol, not valid
    # If email contains more than 1 @ symbol, not valid
    # Separate email into personal part and domain, and check validity of each
    # check_personal_validity(personal_comp)
    # check_domain_validity(domain_comp)
      

def check_personal_validity(personal_comp):
    pass

def check_domain_validity(domain_comp):
    pass
