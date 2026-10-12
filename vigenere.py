alphabet = ["A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","W","X"]

clear_text = input("Please enter a sentence or a word. ").upper()
key_text = input("Please enter a word for encryption ").upper()
temporary_text = list(clear_text)

length = len(clear_text)

#? We will generate a new dummy text from the main text and translate the code based on that; then, 
#? we will combine the two and extract the letters from the final sentence of the sequence.
a = 0
i = 0

for letter in temporary_text:
    if i==3:
        i = 0
    if temporary_text[a] == " ":
        temporary_text[a] = " "
    else:
        temporary_text[a] = key_text[i]
        i = i+1
    a = a+1

encrypted_text = []

for c_char, k_char in zip(clear_text, temporary_text):
  if c_char == " " or c_char not in alphabet:   
    encrypted_text.append(c_char)  
  else:
    c_index = alphabet.index(c_char)

    k_index = alphabet.index(k_char)

    new_index = (c_index + k_index) % len(alphabet)

    encrypted_text.append(alphabet[new_index])

final_result = "".join(encrypted_text)
print("encrypted text:", final_result)
    
    

    
