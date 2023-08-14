import re
def dynamic_split(user_input, delimiters):
    split_pattern = r'|'.join(delimiters)
    results= re.split(split_pattern, user_input)
    return [result for result in results if result]
user_input= "sdfkdjsadfsd diweiw; 1231:foo"
delimiters = [' ',':',';']
split_result =dynamic_split(user_input,delimiters)
print(split_result)