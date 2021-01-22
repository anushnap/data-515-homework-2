# Anushna Prakash
# DATA 515
# Homework 2: Programming
# January 21, 2021
import string
import glob
import pickle

# Takes an string arg email and returns whether the email is valid based on requirements for valid emails
def check_email_validity(email):
    email_components = email.split('@')
    
    if ((len(email_components) == 1) | (len(email_components) > 2)):
        # If email does not contain @ or has more than one @, it is not valid
        return False
    else:
        # When there is exactly 1 @, then check the personal and domain components of the email
        personal_comp = email_components[0]
        domain_comp = email_components[1]

        # If either domain or personal is empty string, then invalid
        if ((len(personal_comp) == 0) | (len(domain_comp) == 0)):
            return False

        return ((check_personal_validity(personal_comp) == True) & (check_domain_validity(domain_comp) == True))
      
# Takes the personal component of an email address string and returns whether the component is valid
def check_personal_validity(personal_comp):
    # Set of valid characters for personal component
    s = {'!', '#', '$', '%', '&', '\'', '*', '+', '/', '=', '?', '^', '_', '{', '|', '}', '~'}    
    allowed = set(string.ascii_letters + string.digits + "." + "-")
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
    
    if ("." not in domain_comp):
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

# Takes filepath and word_counts dictionary and returns tuple of valid email list and the word
# count dictionary with cleaned and tokenized words.
def process_newsgroup_file(filepath, word_counts):
    # Save each word into dictionary with words as keys and int counts as values
    valid_emails = []

    with open(filepath, encoding = 'windows-1252', mode = 'r') as file:
        read_data = file.read()
        tokens = read_data.split()
        allowed = set(string.ascii_letters + string.digits)

        for t in tokens:
            if (check_email_validity(t)):
                # Append into list
                valid_emails.append(t)
            else:           
                for c in t:
                    # Clean the token so it only has ascii and numbers, no punctuation or special characters
                    if c not in allowed:
                        t = t.replace(c, '')
                # Once cleaned, make each word lowercase only
                t = t.lower()
                if t in word_counts:
                    word_counts[t] += 1
                else:
                    word_counts[t] = 1
        
    # Return a tuple with first element being list of valid emails and then word_counts.
    return (valid_emails, word_counts)        


# Takes a directory file path, reads each file in the folder. Writes a list of valid emails in each file
# along with Pickle object of word counts dictionary from each file
def process_newsgroup_topic(dir_filepath):
    word_list = {}
    emails = []
    

    files = glob.glob(dir_filepath)
    for f in files:
        (temp_emails, temp_word_list) = process_newsgroup_file(f, word_list)
        emails.extend(temp_emails)
        word_list.update(temp_word_list)
    
    # Write emails to sci.crypt.emails.txt file
    with open('sci.crypt.emails.txt', 'w') as f:
        for e in emails:
            f.write('%s\n' % e)
    
    with open('sci.crypt.wordcounts.txt', 'wb') as p:
        pickle.dump(word_list, p)



if __name__ == "__main__":
    
    process_newsgroup_topic('/home/anushnap/data515/homework-2/20_newsgroups/sci.crypt/*')
