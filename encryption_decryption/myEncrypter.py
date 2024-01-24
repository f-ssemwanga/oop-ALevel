from string import ascii_letters, punctuation
class Encypter:
  '''This has methods to encrypt and decrypt a given phrase
      uses ceaser cipher
  '''
  def __init__(self):
    '''constructor method'''
    self.out =[]
    self.cryptOut = []

    self.alphabet = list((ascii_letters+punctuation))
    self.key = 84690572193695274820765054327894631502

  def encrypt(self, phrase):
    '''Encrypts and returns an encrypted phrase'''
    for  eachLetter in phrase:
      if eachLetter in self.alphabet:
        index = self.alphabet.index(eachLetter)
        crypting = (index + self.key) % len(self.alphabet)
        new = self.alphabet[crypting]
        self.out.append(new)
      else:
        self.out.append(eachLetter)
    return "".join(self.out)

testInst = Encypter()
print(testInst.encrypt("You Muppet"))