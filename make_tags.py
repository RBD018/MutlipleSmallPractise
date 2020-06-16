def make_tags(tag,world):
    return "'<"+tag+">"+word+"<"+tag+">'"


tag = input("Please Enter a tag: ")
word = input("Please Enter the word: ")
print(make_tags(tag,word))
