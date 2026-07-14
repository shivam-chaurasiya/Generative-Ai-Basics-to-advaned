import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Shivam Babu"
tokens = enc.encode(text)


print("Tokens", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 150937, 313, 418, 21721])
print("Decoded", decoded)