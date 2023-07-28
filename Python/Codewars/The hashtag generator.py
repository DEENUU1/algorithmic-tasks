def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    
    lst = []
    
    words = s.split()
    
    for word in words:
        lst.append(word.title())
        
    new_text = "".join(lst)
    return f"#{new_text}"