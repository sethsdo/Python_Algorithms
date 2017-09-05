#Assignment: Making and Reading from Dictionaries
#Create a dictionary containing some information about yourself. 
# The keys should include name, age, country of birth, favorite language.
#, 'age': '20', "country of birth": "United States", "favorite language": "python"
about = {'name': 'Seth', 'age': 20, "country of birth": "United States", "favorite language": "python"}

def personal_dictionary(content):
    for keys, value in content.iteritems():
        print ('My '+ keys +' is '+ str(value)+ ".")
personal_dictionary(about)