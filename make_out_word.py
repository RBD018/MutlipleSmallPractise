def make_out_word(out,word):
    ln =int(len(out)/2)
    return out[:ln]+word+out[ln:]


out = input('Enter the output patter: ')
word = input('Enter the word you want to put in between the out: ')
print(make_out_word(out,word))

