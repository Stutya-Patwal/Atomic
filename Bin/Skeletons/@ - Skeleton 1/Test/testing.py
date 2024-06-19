def enclose_word_after_double_ampersand(string):   
    index_of_double_ampersand = string.find('&&')
    
    if index_of_double_ampersand != -1:
        start_index = index_of_double_ampersand + 2
        end_index = start_index
        while end_index < len(string) and string[end_index].isalnum():
            end_index += 1
        new_string = string[:start_index] + '{' + string[start_index:end_index] + '}' + string[end_index:]

        new_string = new_string.replace("&&","")
        
        return new_string
    else:
        return string

# Test the function
x = 'print("hey &&name how are you?")'
x = enclose_word_after_double_ampersand(x)
print(x)
