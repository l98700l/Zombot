import math
import random



#                   #
#   Player Class    #
#                   #
class Player:
    def __init__(self):
        self.name = "John"
        self.level = 1
        self.exp = 0
        self.health = 100
        self.maxHealth = 100
        self.accuracy = 1.0
		
        #Armor and Weapons
        self.weaponEquip = None
        self.armorHead = None
        self.armorChest = None
        self.armorLegs = None
        self.armorFeet = None

        #Inventory Stuff
        self.credits = 100
        self.weaponList = list()
        self.armorList = list()
        self.itemList = list()
        self.medKits = 1

#	def addExp(self, xp):
#        self.exp += xp
#        while self.woodcuttingExp >= self.woodcuttingExpNeeded:
#            print("Woodcutting level up!")
#            self.exp -= self.expNeeded
#            self.expNeeded += round(self.expNeeded*(2/3))
#            self.level += 1
#
#	def printStats(self):
#		clrScreen()
#		print("-----Stats-----")
#		print("Name = " + str(self.name))
#		print("Health = " + str(self.health))
#		print("Max Health = " + str(self.maxHealth))
#		print("Accuracy = " + str(self.accuracy))
#
#	def addWeapon(self, wpn):
#		if self.weaponEquip == None or self.weaponEquip.durability <= 0:
#			if self.level >= wpn.level:
#				self.weaponEquip = wpn
#				print(self.weaponEquip.name + " has been equipped.")
#		self.weaponList.append(wpn)
#
#	def addArmor(self, arm):
#		if self.combatLvl >= arm.level:
#			if arm.type == "Helmet" and self.armorHelm == None or self.armorHelm.durability <= 0:
#				self.armorHelm = arm
#				print(self.armorHelm.name + " has been equipped.")
#			elif arm.type == "Chestplate" and self.armorChestplate == None or self.armorChestplate.durability <= 0:
#				self.armorChestplate = arm
#				print(self.armorChestplate.name + " has been equipped.")
#			elif arm.type == "Gauntlets" and self.armorGauntlets == None or self.armorGauntlets.durability <= 0:
#				self.armorGauntlets = arm
#				print(self.armorGauntlets.name + " has been equipped.")
#			elif arm.type == "Leggings" and self.armorLeggings == None or self.armorLeggings.durability <= 0:
#				self.armorLeggings = arm
#				print(self.armorLeggings.name + " has been equipped.")
#			elif arm.type == "Boots" and self.armorBoots == None or self.armorBoots.durability <= 0:
#				self.armorBoots = arm
#				print(self.armorBoots.name + " has been equipped.")
#
#		self.armorList.append(arm)
#
#	def equipWeapon(self, wpn):
#		if wpn > self.weaponList.__len__() or wpn < 1:
#			print("Not a correct value.")
#		else:
#			if self.level >= self.weaponList[wpn-1].level:
#				self.weaponEquip = self.weaponList[wpn-1]
#				print(self.weaponEquip.name + " has been equipped.")
#			else:
#				print("Level is too low. Need: " + str(self.weaponList[wpn-1].level) + ".")
#
#	def unequipWeapon(self):
#		if self.weaponEquip != None:
#			print(self.weaponEquip.name + " has been unequipped.")
#			self.weaponEquip = None
#		else:
#			print("No weapon is equipped.")
#
#	def dropWeapon(self, wpn):
#		if wpn > self.weaponList.__len__() or wpn < 1:
#			print("Not a correct value.")
#		else:
#			if self.weaponList[wpn-1] == self.weaponEquip:
#				self.weaponEquip = None
#			print(self.weaponList[wpn-1].name + " has been dropped.")
#			del self.weaponList[wpn-1]
#
#	def equipArmor(self, arm):
#		if arm > self.armorList.__len__() or arm < 1:
#			print("Not a correct value.")
#		else:
#			if self.level >= self.armorList[arm-1].level:
#				if self.armorList[arm-1].type == "Helmet":
#					self.armorHelm = self.armorList[arm-1]
#					print(self.armorList[arm-1].name + " has been equipped.")
#				if self.armorList[arm-1].type == "Chestplate":
#					self.armorChestplate = self.armorList[arm-1]
#					print(self.armorList[arm-1].name + " has been equipped.")
#				if self.armorList[arm-1].type == "Gauntlets":
#					self.armorGauntlets = self.armorList[arm-1]
#					print(self.armorList[arm-1].name + " has been equipped.")
#				if self.armorList[arm-1].type == "Leggings":
#					self.armorLeggings = self.armorList[arm-1]
#					print(self.armorList[arm-1].name + " has been equipped.")
#				if self.armorList[arm-1].type == "Boots":
#					self.armorBoots = self.armorList[arm-1]
#					print(self.armorList[arm-1].name + " has been equipped.")
#			else:
#				print("Combat level is too low. Need: " + str(self.armorList[arm-1].level) + ".")
#
#	def unequipArmor(self, arm):
#		if arm > self.armorList.__len__() or arm < 1:
#			print("Not a correct value.")
#		else:
#			if self.armorList[arm-1].type == "Helmet":
#				self.armorHelm = None
#			if self.armorList[arm-1].type == "Chestplate":
#				self.armorChestplate = None
#			if self.armorList[arm-1].type == "Gauntlets":
#				self.armorGauntlets = None
#			if self.armorList[arm-1].type == "Leggings":
#				self.armorLeggings = None
#			if self.armorList[arm-1].type == "Boots":
#				self.armorBoots = None
#
#	def dropArmor(self, arm):
#		if arm > self.armorList.__len__() or arm < 1:
#			print("Not a correct value.")
#		else:
#			if self.armorList[arm-1].type == "Helmet" and self.armorList[arm-1] == self.armorHelm:
#				self.armorHelm = None
#			elif self.armorList[arm-1].type == "Chestplate" and self.armorList[arm-1] == self.a#rmorChestplate:
#				self.armorChestplate = None
#			elif self.armorList[arm-1].type == "Gauntlets" and self.armorList[arm-1] == self.a#rmorGauntlets:
#				self.armorGauntlets = None
#			elif self.armorList[arm-1].type == "Leggings" and self.armorList[arm-1] == self.armorLeggings:
#				self.armorLeggings = None
#			elif self.armorList[arm-1].type == "Boots" and self.armorList[arm-1] == self.armorBoots:
#				self.armorBoots = None
#			print(self.armorList[arm-1].name + " has been dropped.")
#			del self.armorList[arm-1]
#
#                   #
#   Weapon Class    #
#                   #
class Weapon:
    def __init__(self, nme="Wooden Sword", typ="Melee", dmg=1, spd=10, dur=50, cst=10, lvl=1, tier=1):
        self.name=nme
        self.type=typ
        self.damage=dmg
        self.speed=spd
        self.durability=dur
        self.cost=cst
        self.description=None
        self.level=lvl
        self.tier=tier
        self.maxDurability = self.durability

        if self.type == "Ranged":
            self.range = 40

    def printStats(self):
        print("Name: " + self.name)
        print("Type: " + self.type)
        print("Damage: " + str(self.damage))
        print("Durability: " + str(self.durability))
        print("Cost: " + str(self.cost))
        print("Description: " + str(self.description))
        print("Combat Level Requirement: " + str(self.level))