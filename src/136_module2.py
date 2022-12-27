# Run command: pip install morse3

from morse3 import Morse as m

text1 = "I love you"
morse1 = m(text1).stringToMorse()  # ..   .-.. --- ...- .   -.-- --- ..-
print(morse1)

normal1 = m(morse1)  # candy
print(normal1.morseToString())
