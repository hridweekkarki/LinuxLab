import sys

def encryption(message, shift):
    message = message.upper()
    characters = ""

    for char in message:
      if char.isalpha():
       characters += char

    encoded_text = []

    for char in characters:
        char_ascii = ord(char)
        new_ascii = char_ascii + shift

        if new_ascii > ord("Z"):
          result = (new_ascii - ord("Z")) % 26

          if result == 0:
            result = 26

          new_ascii = result + 64

        encoded_text.append(chr(new_ascii))

    value = ''.join(encoded_text)
    return format_output(value)
