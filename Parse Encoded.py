def parse_encoded_string(s):
    parts = s.split('0')
    filtered = [p for p in parts if p != '']
    return {
        "first_name": filtered[0],
        "last_name": filtered[1],
        "id": filtered[2]
    }

print(parse_encoded_string("John000Doe000123"))  # Output: {'first_name':'John', 'last_name':'Doe', 'id':'123'}
