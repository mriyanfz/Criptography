"from string import maketrans"
        
rot18trans ="". maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234')

# Function to translate plain text
def rot18(text):
    return text.translate(rot18trans)
def main():
    txt = input("text :")
    print (rot18(txt))
    
if _name_ == "_main_":
    main()