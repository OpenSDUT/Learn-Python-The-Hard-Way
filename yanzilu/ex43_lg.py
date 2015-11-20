#-*- coding:utf-8 -*-
#Basic Object-Oriented Analysis and Design

from sys import exit
from random import randint

class Scene(object):#基类
	def enter(self):
		print "This scene is not yet configured.Subclass it and implement enter()."
		exit(1)


#引擎
class Engine(object):
	#传入进来的scene_map是一个MAP类的对象
	def __init__(self,scene_map):
		self.scene_map = scene_map
	def play(self):
		#调用MAP类中的opening_scene()方法和next_scene()方法
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene("finished")
		
		while current_scene != last_scene:
			#调用当下场景的enter方法,获取用户输入的内容,然后根据内容返回下一步操作的场景
			next_scene_name = current_scene.enter()
			#将获取到的场景所在的类,为下一次的循环做准备
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		#确定打印最后一个场景
		current_scene.enter()

#死亡场景
class Death(Scene):
	
	quips = [
		"You died. You kinda suck at this.",
		"You mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)


#初始设置,中央走廊
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew.You are last surviving member and you last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge,and blow the ship up after getting into an"
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out,red scaly,dark grimy teeth,and evil clown costume"
		print "flowing around his hate filled body.He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")

		#根据用户不同的输入进入不同的场景
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim.  Your laser hits his costume but misses him entirely.  This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead.  Then he eats you."
			return 'death'

		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'

		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

#其他场景,激光武器库
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container.  There's a keypad lock on the box"
		print "and you need the code to get the bomb out.  If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb.  The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
        
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'

#其他场景,主控舱
class TheBridge(Scene):
	def enter(self):
		print "You burst onto the Bridge with the netron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship.  Each of them has an even uglier"
		print "clown costume than the last.  They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'

		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"



#其他场景,救生
class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes.  It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print "but you don't have time to look.  There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
        
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below.  As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time.  You won!"

			return 'finished'

#结束场景
class Finished(Scene):
	def enter(self):
		print "You won!Good job."
		return 'finished'



#地图选择
class Map(object):
	
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
    }

	def __init__(self,start_scene):
		self.start_scene = start_scene

	def next_scene(self,scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
