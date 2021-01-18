# Anushna Prakash
# DATA 515
# Homework 2: Programming
# January 21, 2021
import string

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
    email_components = email.split('@')
    
    if ((len(email_components) == 1) | len(email_components) > 2):
        # If email does not contain @ or has more than one @, it is not valid
        return False
    else:
        # When there is exactly 1 @, then check the personal and domain components of the email
        personal_comp = email_components[0]
        domain_comp = email_components[1]

        # check_personal_validity(personal_comp)
        # check_domain_validity(domain_comp)

        return ((check_personal_validity == True) & (check_domain_validity == True))
      
# Takes the personal component of an email address string and returns whether the component is valid
def check_personal_validity(personal_comp):
    # Set of valid characters for personal component
    s = {'!', '#', '$', '%', '&', '\'', '*', '+', '/', '=', '?', '^', '_', '{', '|', '}', '~'}    
    allowed = set(string.ascii_letters + string.digits)
    allowed.update(s)
    
    if (check_fullstop(personal_comp) == False):
        return False

    for c in personal_comp:
        if (c not in allowed):
            return False
    
    return True


# Takes domain component of an email address string and returns whether the component is valid
def check_domain_validity(domain_comp):
    allowed = set(string.ascii_letters + string.digits + "." + "-")
    
    if (check_fullstop(domain_comp) == False):
        return False
        
    # Check that domain component does not contain invalid characters
    for c in domain_comp:
        if (c not in allowed):
            return False
    
    return True
    
    
    # Domain component cannot contain ".." and cannot start or end with "."

# Takes email address component and returns if component has valid usage of "." character
def check_fullstop(component):
    if ((component[0] == ".") | (component[-1] == ".")):
        return False
    elif (".." in component):
        return False
    else:
        return True

# #2 in homework requirements
def process_newsgroup_file(filepath, word_counts):
    pass

# #3 in homework requirements
def process_newsgroup_topic():
    pass


if __name__ == "__main__":
    test = 'mysite!!'
    print("Personal: ", check_personal_validity(test))
    print("Domain: ", check_domain_validity(test))