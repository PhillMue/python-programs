#!/usr/bin/python3

class AnimalActions:
	def quack(self): return self.strings['quack']
	def feathers(self): return self.strings['feathers']
	def bark(self): return self.strings['bark']
	def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaack!",
        feathers = "The duck has gray and white feathers.",
        bark = "The dark cannot bark.",
        fur = "The dark has no fur." 
    )	