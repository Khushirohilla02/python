import cowsay
cowsay.cow("hello everyone")

import pyjokes
print(pyjokes.get_joke())

import cowsay
import pyjokes
cowsay.cow(pyjokes.get_joke())