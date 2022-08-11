import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability
from ability import Spell_ability


class DruidTalent():
	def __init__(self):
		pass

	def balance_1_2(self, count):
		'''Starlight Wrath'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Wrath'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Starfire'].modified_panel_cast_time -= 0.1 * count

	def balance_1_3(self, count):
		'''Genesis'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			if ab.periodic == True:
				ab.specific_amount_increase += 0.01 * count

	def balance_2_1(self, count):
		'''Moonglow'''
		pass

	def balance_2_2(self, count):
		'''Nature's Majesty'''
		assert count in (0, 1, 2)
		self.spell_abilities['Wrath'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Starfire'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Starfall'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Nourish'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Healing Touch'].specific_critical_increase += 0.02 * count

	def balance_2_4(self, count):
		'''Improved Moonfire'''
		assert count in (0, 1, 2)
		self.spell_abilities['Moonfire'].specific_amount_increase += 0.05 * count
		self.spell_abilities['Moonfire'].specific_critical_increase += 0.05 * count

	def balance_3_1(self, count):
		'''Brambles'''
		# no need to calculate damage of Thorns and Entangling Root
		pass

	def balance_3_2(self, count):
		'''Nature's Grace'''
		pass

	def balance_3_3(self, count):
		'''Nature's Splendor'''
		assert count in (0, 1)
		# todo more duration on 
		# Moonfire
		# Rejuvenation
		# Regrowth
		# Insect Swarm
		# Lifebloom
		pass

	def balance_3_4(self, count):
		'''Nature's Reach'''
		pass

	def balance_4_2(self, count):
		'''Vengeance'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Starfire'].critical_bonus *= 1 + 0.2 * count
		self.spell_abilities['Starfall'].critical_bonus *= 1 + 0.2 * count
		self.spell_abilities['Moonfire'].critical_bonus *= 1 + 0.2 * count
		self.spell_abilities['Wrath'].critical_bonus *= 1 + 0.2 * count

	def balance_4_3(self, count):
		'''Celestial Focus'''
		# todo inc spell hates, should be multiplication, not addition
		pass

	def balance_5_1(self, count):
		'''Lunar Guidance'''
		pass

	def balance_5_2(self, count):
		'''Insect Swarm'''
		pass

	def balance_5_3(self, count):
		'''Improved Insect Swarm'''
		pass

	def balance_6_1(self, count):
		'''Dreamstate'''
		pass

	def balance_6_2(self, count):
		'''Moonfury'''
		assert count in (0, 1, 2, 3)
		if count <= 2:
			inc = 0.03 * count
		elif count == 3:
			inc = 0.1
		self.spell_abilities['Starfire'].specific_amount_increase += inc
		self.spell_abilities['Moonfire'].specific_amount_increase += inc
		self.spell_abilities['Wrath'].specific_amount_increase += inc

	def balance_6_3(self, count):
		'''Balance of Power'''
		pass

	def balance_7_2(self, count):
		'''Moonkin Form'''
		pass

	def balance_7_3(self, count):
		'''Improved Moonkin Form'''
		# todo spell haste
		pass

	def balance_7_4(self, count):
		'''Improved Faerie Fire'''
		pass

	def balance_8_1(self, count):
		'''Owlkin Frenzy'''
		pass

	def balance_8_3(self, count):
		'''Wrath of Cenarius'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Starfire'].direct_coefficient += 0.04 * count
		self.spell_abilities['Wrath'].direct_coefficient += 0.02 * count

	def balance_9_1(self, count):
		'''Eclipse'''
		pass

	def balance_9_2(self, count):
		'''Typhoon'''
		pass

	def balance_9_3(self, count):
		'''Force of Nature'''
		pass

	def balance_9_4(self, count):
		'''Gale Winds'''
		assert count in (0, 1, 2)
		self.spell_abilities['Hurricane'].specific_amount_increase += 0.15 * count
		self.spell_abilities['Typhoon'].specific_amount_increase += 0.15 * count

	def balance_10_2(self, count):
		'''Earth and Moon'''
		pass

	def balance_11_2(self, count):
		'''Starfall'''
		pass

	def feral_1_2(self, count):
		'''Ferocity'''
		pass

	def feral_1_3(self, count):
		'''Feral Aggression'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_abilities[''].specific_amount_increase += 0.03 * count

	def feral_2_1(self, count):
		'''Feral Instinct'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Swipe'].specific_amount_increase += 0.1 * count

	def feral_2_2(self, count):
		'''Savage Fury'''
		assert count in (0, 1, 2)
		self.physic_abilities['Claw'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Rake'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Mangle (cat)'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Mangle (bear)'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Maul'].specific_amount_increase += 0.1 * count

	def feral_2_3(self, count):
		'''Thick Hide'''
		pass

	def feral_3_1(self, count):
		'''Feral Switfness'''
		pass

	def feral_3_2(self, count):
		'''Survival Instincts'''
		pass

	def feral_3_3(self, count):
		'''Sharpened Claw'''
		# I assume feral druid will always be in form of cat/bear, so I simply add to global critical
		assert count in (0, 1, 2, 3)
		self.physic_basic_attr['melee_critical'] += 0.02 * count
		self.physic_basic_attr['ranged_critical'] += 0.02 * count

	def feral_4_1(self, count):
		'''Shredding Attacks'''
		pass

	def feral_4_2(self, count):
		'''Predatory Strikes'''
		pass

	def feral_4_3(self, count):
		'''Primal Fury'''
		pass

	def feral_4_4(self, count):
		'''Primal Precision'''
		pass

	def feral_5_1(self, count):
		'''Brutal Impact'''
		pass

	def feral_5_3(self, count):
		'''Feral Charge'''
		pass

	def feral_5_4(self, count):
		'''Nurturing Instinct'''
		pass

	def feral_6_1(self, count):
		'''Natural Reaction'''
		pass

	def feral_6_2(self, count):
		'''Heart of Wild'''
		pass

	def feral_6_3(self, count):
		'''Survival of Fittest'''
		pass

	def feral_7_2(self, count):
		'''Leader of the Pact'''
		pass

	def feral_7_3(self, count):
		'''Improved Leader of the Pact'''
		pass

	def feral_7_4(self, count):
		'''Primal Tenacity'''
		pass

	def feral_8_1(self, count):
		'''Protector of the Pact'''
		pass

	def feral_8_3(self, count):
		'''Predatory Instincts'''
		# todo increase critical hit damage
		pass

	def feral_8_4(self, count):
		'''Infected Wounds'''
		pass

	def feral_9_1(self, count):
		'''King of the Jungle'''
		pass

	def feral_9_2(self, count):
		'''Mangle'''
		pass

	def feral_9_3(self, count):
		'''Improved Mangle'''
		pass

	def feral_10_2(self, count):
		'''Rend and Tear'''
		pass

	def feral_10_3(self, count):
		'''Primal Gore'''
		# todo grant the dot cirtical ability
		pass

	def feral_11_2(self, count):
		'''Berserk'''
		pass

	def restoration_1_1(self, count):
		'''Improved Mark of the Wild'''
		pass

	def restoration_1_2(self, count):
		'''Nature's Focus'''
		pass

	def restoration_1_3(self, count):
		'''Furor'''
		pass

	def restoration_2_1(self, count):
		'''Naturalist'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Healing Touch'].modified_panel_cast_time -= 0.1 * count

	def restoration_2_2(self, count):
		'''Subtlety'''
		pass

	def restoration_2_3(self, count):
		'''Natural Shapshifter'''
		pass

	def restoration_3_1(self, count):
		'''Intensity'''
		pass

	def restoration_3_2(self, count):
		'''Omen of Clarity'''
		pass

	def restoration_3_3(self, count):
		'''Master Shapeshifter'''
		# todo this nearly infuence all
		pass

	def restoration_4_2(self, count):
		'''Tranquil Spirit'''
		pass

	def restoration_4_3(self, count):
		'''Improved Rejuvenation'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Rejuvenation'].specific_amount_increase += 0.05 * count

	def restoration_5_1(self, count):
		'''Nature's Swiftness'''
		pass

	def restoration_5_2(self, count):
		'''Gift of Nature'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			if ab.nature == 'heal':
				ab.specific_amount_increase += 0.02 * count

	def restoration_5_4(self, count):
		'''Improved Tranquility'''
		pass

	def restoration_6_1(self, count):
		'''Empowered Touch'''
		assert count in (0, 1, 2)
		self.spell_abilities['Healing Touch'].direct_coefficient += 0.2 * count
		self.spell_abilities['Nourish'].direct_coefficient += 0.1 * count

	def restoration_6_3(self, count):
		'''Nature's Bounty'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Regrowth'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Nourish'].specific_critical_increase += 0.05 * count

	def restoration_7_1(self, count):
		'''Living Spirit'''
		pass

	def restoration_7_2(self, count):
		'''Swiftmend'''
		pass

	def restoration_7_3(self, count):
		'''Nature Perfection'''
		assert count in (0, 1, 2, 3)
		self.spell_basic_attr['spell_critical'] += 0.01 * count

	def restoration_8_2(self, count):
		'''Empowered Rejuvenation'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			if ab.nature == 'heal' and ab.periodic == True:
				ab.periodic_coefficient *= 1 + 0.04 * count

	def restoration_8_3(self, count):
		'''Living Seed'''
		pass

	def restoration_9_1(self, count):
		'''Revitalize'''
		pass

	def restoration_9_2(self, count):
		'''Tree of Life'''
		pass

	def restoration_9_3(self, count):
		'''Improved Tree of Life'''
		pass

	def restoration_10_1(self, count):
		'''Improved Barkskin'''
		pass

	def restoration_10_3(self, count):
		'''Gift of the Earthmother'''
		pass

	def restoration_11_2(self, count):
		'''Wild Growth'''
		pass



class Druid(Attribute, DruidTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.spell_abilities = OrderedDict()
		with open('ability_data/druid_spell_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				self.spell_abilities[item['ability_name']] = Spell_ability(item)

		self.physic_abilities = OrderedDict()
		with open('ability_data/druid_physic_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
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
						res_str = 'balance_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'feral_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'restoration_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Druid, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spell abilities
		for ability in self.spell_abilities.values():
			ability.calculate_amount(self.spell_basic_attr, self.spell_critical_increase, self.spell_amount_increase)
		# calculate amount of physic abilities
		for ability in self.physic_abilities.values():
			ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)


