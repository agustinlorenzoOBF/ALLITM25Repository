'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
    is_upper = letter.isupper()
    num_letter = ord(letter)
    total = shift + num_letter
    if letter == " ":
            return " "
    elif letter == "_":
            return " "
    elif is_upper:
        max = 90
        if total > max:
            remainder = int(total - 90 + 65)
            new_letter = (chr(remainder-1))
            return(new_letter)
        else: 
            new_letter = chr(num_letter+shift)
            return (new_letter)
    else:
        max = 122
        if total > max:
            remainder = int(total - 122 + 97)
            new_letter = (chr(remainder-1))
            return(new_letter)
        else: 
            new_letter = chr(num_letter+shift)
            return (new_letter)
        

    
    
    
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    list=[]
    for i in message: 
        list.append(i)
    new=[]
  
    for i in list:
        letter = i
        is_upper = letter.isupper()
        if is_upper:
            num_letter = ord(i)
            total = shift + num_letter
            max = 90
            if i == " ":
                new.append(" ")
            elif i == "_":
                new.append("_")
            else:
                if total > max:
                    remainder = int(total - 90 + 65)
                    new_letter = (chr(remainder-1))
                    new.append(new_letter)
                else: 
                    new_letter = chr(num_letter+shift)
                    new.append(new_letter)
                c_cipher =""
                c_cipher =c_cipher.join(new)
        else:
            num_letter = ord(i)
            total = shift + num_letter
            max = 122
            if i == " ":
                new.append(" ")
            elif i == "_":
                new.append("_")
            else:
                if total > max:
                    remainder = int(total - 122 + 97)
                    new_letter = (chr(remainder-1))
                    new.append(new_letter)
                else: 
                    new_letter = chr(num_letter+shift)
                    new.append(new_letter)
                c_cipher =""
                c_cipher =c_cipher.join(new)
    return c_cipher
        

    
    
        
def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    Alphabet = ["A","B","C","D","E","F","G","H","I","J",'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    output =""
    if letter == " ":
        output = " " 
    elif letter == "_":
        output = "_"
    else:
        letter_val= Alphabet.index(letter)
        shift_val= int(Alphabet.index(letter_shift)+Alphabet.index(letter))
        if shift_val+letter_val > 25:
          shift_val= int(Alphabet.index(letter_shift)+Alphabet.index(letter)) - 26
          shifted_let = Alphabet[shift_val]
          output = shifted_let
        else:
          shift_val= int(Alphabet.index(letter_shift)+Alphabet.index(letter))
          shifted_let = Alphabet[shift_val]
          output = shifted_let
        return (output)

    

def vigenere_cipher(message, key):
 
  Alphabet = ["A","B","C","D","E","F","G","H","I","J",'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  orig=[]
  shift=[]
  shifted=[]
  output=""
   
  for i in message: 
    orig.append(i)
  
  for i in key:
    shift.append(i)
  
   
  for i in range(len(message)):
    if orig[i] == " ": 
      shifted.append(" ")
    elif orig[i] == "_": 
      shifted.append("_")
    else: 
      val = int(Alphabet.index(orig[i]) + Alphabet.index(shift[i]))
      if val > 25:
        val = (val-25)
        shifted.append(Alphabet[val-1])
      else:
        shifted.append(Alphabet[val])
  output= output.join(shifted)
  return (output)





def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.
    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.
    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale
    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".
    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    polished = []
    
    if (len(message) % shift)==0:
        for i in range(len(message)):
            polished += message[(i // shift) + (len(message) // shift) * (i % shift)]
    else:
        while (len(message) % shift) > 0:
            message += "_"             
        for i in range(len(message)):
        
            polished += message[(i // shift) + (len(message) // shift) * (i % shift)]
        
    return ''.join(map(str, polished))





def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    polished = message[1:]
    decode = ""
    i = 1
    until = shift
    
    while len(decode) < len(polished):
        if i > len(polished):
            i = 1
        if until == 1:
            decode = decode + polished[i-1]
            i = i + 1
            until = shift
        else:
            i = i + 1
            until = until - 1
        
    return message[0] + decode
        
