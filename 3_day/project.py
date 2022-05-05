#Welcome to Hacker Island!

print('''
	       ___   ____
	     /' --;^/ ,-_\     \ | /
	     / / --o\ o-\ \\   --(_)--
	    /-/-/|o|-|\-\\|\\   / | \
	     '` ` |-|   `` '
	          |-|
	          |-|O
	         |-(\,__
	        ...|-|\--,\_....
	    ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,  ______   ---------   _____     ------
''')
print("Welcome to Hacker Island.")
print("Your mission is to find the bug.") 
step_1 = input("You have just been thrown out of a boat onto a deserted island beach. Night is approaching fast. You see a dense forest in front of you. Do you walk towards the setting sun or walk into the forest? 'sun' or 'forest'?\n").lower()
if step_1 == "sun":
	print("Your clothes are getting dry and you are warm.\n")
	step_2 = input("The sun is almost gone. You are warm but now hungry and thirsty. You see some coconuts on the ground. Right at that moment, seagulls dive at fish in the clear blue water.  You think for a moment if you want to fish or gather coconuts. Type 'fish' or 'coconuts'?\n").lower()
	if step_2 == "coconuts":
			print("You find 3 coconuts.  You break them open on a rock. They are full of delicious water and you eat all the flesh. It will do for tonight! You begin to get sleepy.\n")
			step_3 = input("You are fighting sleep but are afraid of exposure.  You have to figure shelter.  You see a bunch of boulders that could be good for tonight. Then you remember seeing a bunch of palm leaves. Type 'boulders' or 'leaves'?\n").lower()
			if step_3 == "leaves":
				print("You dig a hole in the sand and use the leaves to cover yourself up and hide. It will do for tonight!\n")
				step_4 = input("It is a new day. You see something reflect off a seagulls. You are both hungry and curious.  You don't see anymore coconuts but think you see some crabs in the water.  Do you pick up a rock and kill the seagull or try to gather the crustaceans? Type 'rock', 'catch','walk'\n").lower()
				if step_4 == "rock":
					print("You don't know how but you hit the seagull with the first throw! Upon inspection, you see a listening device used to spy on you. Congratulations, you found the bug!  The hackers are impressed and offer you a job.")
				elif step_4 == "walk":
					print("You keep walking but you are tired, hungry and thirsty.  You aren't paying attention and walk off a cliff.  GAME OVER.")
				else:
					print("You start into the water to catch the crabs.  However, sharks with lasers attack you.  You are shredded to pieces and the sharks devour. GAME OVER.")
			else: 
				print("You fall asleep in between the boulders.  You didn't realize the tide was low and drown.  GAME OVER.")
	else: 
			print("You try to fish but only waste all your energy and have no food or water.  Your clothes are now wet again.  You pass out for exhaustion and dehydration and are eaten by seagulls.  GAME OVER. ")
else:
		print("The hackers spotted you on their surveillance camera.  They deploy of nanobots who kill your operating systems. GAME OVER.")