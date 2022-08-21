import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability



class RogueTalent():
	def __init__(self):
		pass

	def assassination_1_1(self, count):
		'''Improved Eviscerate'''
		assert count in (0, 1, 2, 3)
		if count == 0:
			inc = 0
		elif count == 1 or count == 2:
			inc = 0.07 * count
		elif count == 3:
			inc = 0.2
		self.physic_abilities['Eviscerate (min)'].specific_amount_increase += inc
		self.physic_abilities['Eviscerate (max)'].specific_amount_increase += inc

	def assassination_1_2(self, count):
		'''Remorseless Attacks'''
		pass

	def assassination_1_3(self, count):
		'''Malice'''
		# this talent modify panel info so don't need to implement
		pass

	def assassination_2_1(self, count):
		'''Ruthlessness'''
		pass

	def assassination_2_2(self, count):
		'''Blood Spatter'''
		assert count in (0, 1, 2)
		self.physic_abilities['Garrote'].specific_amount_increase += 0.15 * count
		self.physic_abilities['Rupture'].specific_amount_increase += 0.15 * count

	def assassination_2_4(self, count):
		'''Puncturing Wounds'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Backstab'].specific_critical_increase += 0.1 * count
		self.physic_abilities['Mutilate (main)'].specific_critical_increase += 0.05 * count
		self.physic_abilities['Mutilate (off)'].specific_critical_increase += 0.05 * count

	def assassination_3_1(self, count):
		'''Vigor'''
		pass

	def assassination_3_2(self, count):
		'''Improved Expose Armor'''
		pass

	def assassination_3_3(self, count):
		'''Lethality'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_abilities['Backstab'].critical_bonus *= 1 + 0.06 * count
		self.physic_abilities['Hemorrhage'].critical_bonus *= 1 + 0.06 * count
		self.physic_abilities['Mutilate (main)'].critical_bonus *= 1 + 0.06 * count
		self.physic_abilities['Mutilate (off)'].critical_bonus *= 1 + 0.06 * count
		self.physic_abilities['Sinister Strike'].critical_bonus *= 1 + 0.06 * count
		self.physic_abilities['Gouge'].critical_bonus *= 1 + 0.06 * count

	def assassination_4_2(self, count):
		'''Vile Poisons'''
		# also increase poison damage
		assert count in (0, 1, 2, 3)
		if count <= 2:
			inc = 0.07 * count
		elif count == 3:
			inc = 0.2
		self.physic_abilities['Envenom'].specific_amount_increase += inc

	def assassination_4_3(self, count):
		'''Improved Poisons'''
		pass

	def assassination_5_1(self, count):
		'''Fleet Footed'''
		pass

	def assassination_5_2(self, count):
		'''Cold Blood'''
		pass

	def assassination_5_3(self, count):
		'''Improved Kidney Shot'''
		pass

	def assassination_5_4(self, count):
		'''Quick Recovery'''
		pass

	def assassination_6_2(self, count):
		'''Seal Fate'''
		pass

	def assassination_6_3(self, count):
		'''Murder'''
		assert count in (0, 1, 2)
		self.physic_amount_increase['all_dmg'] += 0.02 * count

	def assassination_7_1(self, count):
		'''Deadly Brew'''
		pass

	def assassination_7_2(self, count):
		'''Overkill'''
		pass

	def assassination_7_3(self, count):
		'''Deadened Nerves'''
		pass

	def assassination_8_1(self, count):
		'''Focused Attacks'''
		pass

	def assassination_8_3(self, count):
		'''Find Weakness'''
		assert count in (0, 1, 2, 3)
		for ab in self.physic_abilities.values():
			ab.specific_amount_increase += 0.02 * count

	def assassination_9_1(self, count):
		'''Master Poisoner'''
		pass

	def assassination_9_2(self, count):
		'''Mutilate'''
		pass

	def assassination_9_3(self, count):
		'''Ture the Tables'''
		pass

	def assassination_10_2(self, count):
		'''Cut to the Chase'''
		pass

	def assassination_11_2(self, count):
		'''Hunger for Blood'''
		pass

	def combat_1_1(self, count):
		'''Improved Gouge'''
		pass

	def combat_1_2(self, count):
		'''Improved Sinister Strike'''
		pass

	def combat_1_3(self, count):
		'''Dual Wield Specialization'''
		# I suppose the 'base_dmg' of weapon does not need to be modified
		assert count in (0, 1, 2, 3, 4, 5)
		self.off_melee_weapon['non_norm_dmg_min'] *= 1 + 0.1 * count
		self.off_melee_weapon['non_norm_dmg_max'] *= 1 + 0.1 * count
		self.off_melee_weapon['norm_dmg_min'] *= 1 + 0.1 * count
		self.off_melee_weapon['norm_dmg_max'] *= 1 + 0.1 * count
	def combat_2_1(self, count):
		'''Improved Slice and Dice'''
		pass

	def combat_2_2(self, count):
		'''Deflection'''
		pass

	def combat_2_4(self, count):
		'''Precision'''
		pass

	def combat_3_1(self, count):
		'''Endurance'''
		pass

	def combat_3_2(self, count):
		'''Riposte'''
		pass

	def combat_3_3(self, count):
		'''Close Quarters Combat'''
		pass

	def combat_4_1(self, count):
		'''Improved Kick'''
		pass

	def combat_4_2(self, count):
		'''Improved Sprint'''
		pass

	def combat_4_3(self, count):
		'''Lightning Reflex'''
		# todo melee haste
		pass

	def combat_4_4(self, count):
		'''Aggression'''
		assert count in (0, 1, 2, 3, 4)
		self.physic_abilities['Sinister Strike'].specific_amount_increase += 0.03 * count
		self.physic_abilities['Backstab'].specific_amount_increase += 0.03 * count
		self.physic_abilities['Eviscerate (min)'].specific_amount_increase += 0.03 * count
		self.physic_abilities['Eviscerate (max)'].specific_amount_increase += 0.03 * count

	def combat_5_1(self, count):
		'''Mace Specialization'''
		pass

	def combat_5_2(self, count):
		'''Blade Flurry'''
		pass

	def combat_5_3(self, count):
		'''Hack and Slash'''
		pass

	def combat_6_2(self, count):
		'''Weapon Expertise'''
		pass

	def combat_6_3(self, count):
		'''Blade Twisting'''
		assert count in (0, 1, 2)
		self.physic_abilities['Sinister Strike'].specific_amount_increase += 0.05 * count
		self.physic_abilities['Backstab'].specific_amount_increase += 0.05 * count

	def combat_7_1(self, count):
		'''Vitality'''
		pass

	def combat_7_2(self, count):
		'''Adrenaline Rush'''
		pass

	def combat_7_3(self, count):
		'''Nerves of Steel'''
		pass

	def combat_8_1(self, count):
		'''Throwing Specialization'''
		pass

	def combat_8_3(self, count):
		'''Combat Potency'''
		pass

	def combat_9_1(self, count):
		'''Unfair Advantage'''
		pass

	def combat_9_2(self, count):
		'''Surprise Attacks'''
		assert count in (0, 1)
		self.physic_abilities['Sinister Strike'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Backstab'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Shive'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Hemorrhage'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Gouge'].specific_amount_increase += 0.1 * count

	def combat_9_3(self, count):
		'''Savage Combat'''
		pass

	def combat_10_2(self, count):
		'''Prey the Weak'''
		pass

	def combat_11_2(self, count):
		'''Killing Spree'''
		pass

	def subtlety_1_1(self, count):
		'''Relentless Strikes'''
		pass

	def subtlety_1_2(self, count):
		'''Master of Deception'''
		pass

	def subtlety_1_3(self, count):
		'''Opportunity'''
		assert count in (0, 1, 2)
		self.physic_abilities['Backstab'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Mutilate (main)'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Mutilate (off)'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Garrote'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Ambush'].specific_amount_increase += 0.1 * count

	def subtlety_2_1(self, count):
		'''Sleight of Hand'''
		pass

	def subtlety_2_2(self, count):
		'''Dirty Tricks'''
		pass

	def subtlety_2_3(self, count):
		'''Camouflage'''
		pass

	def subtlety_3_1(self, count):
		'''Elusiveness'''
		pass

	def subtlety_3_2(self, count):
		'''Ghostly Strike'''
		pass

	def subtlety_3_3(self, count):
		'''Serrated Blades'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Rupture'].specific_amount_increase += 0.1 * count

	def subtlety_4_1(self, count):
		'''Setup'''
		pass

	def subtlety_4_2(self, count):
		'''Initiative'''
		pass

	def subtlety_4_3(self, count):
		'''Improved Amubush'''
		assert count in (0, 1, 2)
		self.physic_abilities['Ambush'].specific_critical_increase += 0.25 * count

	def subtlety_5_1(self, count):
		'''Heightened Senses'''
		pass

	def subtlety_5_2(self, count):
		'''Preparation'''
		pass

	def subtlety_5_3(self, count):
		'''Dirty Deeds'''
		pass

	def subtlety_5_4(self, count):
		'''Hemorrhage'''
		pass

	def subtlety_6_1(self, count):
		'''Master of Subtlety'''
		pass

	def subtlety_6_3(self, count):
		'''Deadiness'''
		pass

	def subtlety_7_1(self, count):
		'''Enveloping Shadows'''
		pass

	def subtlety_7_2(self, count):
		'''Premeditation'''
		pass

	def subtlety_7_3(self, count):
		'''Cheat Death'''
		pass

	def subtlety_8_2(self, count):
		'''Sinister Calling'''
		# due to test, 'damage bonus' is wp_coefficient
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_abilities['Backstab'].wp_coefficient += 0.03 * count
		self.physic_abilities['Hemorrhage'].wp_coefficient += 0.03 * count

	def subtlety_8_3(self, count):
		'''Waylay'''
		pass

	def subtlety_9_1(self, count):
		'''Honor Among Thieves'''
		pass

	def subtlety_9_2(self, count):
		'''Shadowstep'''
		pass

	def subtlety_9_3(self, count):
		'''Filthy Tricks'''
		pass

	def subtlety_10_2(self, count):
		'''Slaughter from the Shadows'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_amount_increase['all_dmg'] += 0.01 * count

	def subtlety_11_2(self, count):
		'''Shadowdance'''
		pass



class Rogue(Attribute, RogueTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all abilities
		self.physic_abilities = OrderedDict()
		with open('ability_data/rogue_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				self.physic_abilities[item['ability_name']] = Physic_ability(item)
		
		# initialize attribute
		Attribute.__init__(self, attr_dict)
	
		# initialize talent
		for depth in range(0, 11):
			for column in range(0, 12):
				if talent_list[depth][column] != None:	
					if column < 4:
						res_str = 'assassination_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'combat_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'subtlety_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Rogue, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of physic abilities
		for ability in self.physic_abilities.values():
			ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)


