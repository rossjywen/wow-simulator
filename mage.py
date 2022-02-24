#!/usr/bin/env python3

import json
from collections import OrderedDict
from attribute import Attribute
from spell import Spell



class MageTalent():
	def __init__(self):
		pass

	#def get_spells(self):
	#	'''virtual function'''
	#	raise NotImplementedError('call to abstract method '

	#def get_attribute(self):
	#	'''virtual function'''
	#	raise NotImplementedError('call to abstract method '

	def frost_1_1(self, count):
		'''Frostbite'''
		assert count in (0,1,2,3)
		pass
	
	def frost_1_2(self, count):
		'''Improved Frostbolt'''
		assert count in (0,1,2,3,4,5)
		self.spells['Frostbolt'].modified_panel_cast_time -= count * 0.1

	def frost_1_3(self, count):
		'''Ice Floes'''
		pass

	def frost_2_1(self, count):
		'''Ice Shards'''
		assert count in (0,1,2,3)
		if count <= 2:
			self.spell_critical_bonus['frost'] *=  1 + count * 0.33
		elif count == 3:
			self.spell_critical_bonus['frost'] *= 2
		else:
			assert False

	def frost_2_2(self, count):
		'''Frost Warding'''
		pass

	def frost_2_3(self, count):
		'''Precision'''
		# todo check whether this talent will be displayed in the panel
		pass
	
	def frost_2_4(self, count):
		'''Permafrost'''
		pass

	def frost_3_1(self, count):
		'''Piercing Ice'''
		assert count in (0,1,2,3)
		self.spell_amount_increase['frost'] += count * 0.02

	def frost_3_2(self, count):
		'''Icy Veins'''
		pass

	def frost_3_3(self, count):
		'''Improved Blizzard'''
		pass

	def frost_4_1(self, count):
		'''Arctic Reach'''
		pass

	def frost_4_2(self, count):
		'''Frost Channeling'''
		pass

	def frost_4_3(self, count):
		# todo add state
		'''Shatter'''
		pass

	def frost_5_1(self, count):
		'''Cold Snap'''
		pass

	def frost_5_2(self, count):
		'''Improved Cone of Cold'''
		assert count in (0,1,2,3)
		self.spells['Cone of Cold'].specific_amount_increase += count * 0.15

	def frost_5_3(self, count):
		'''Frozen Core'''
		assert count in (0,1,2,3)
		self.damage_reduce['spell'] -= count * 0.02
		self.damage_reduce['melee'] -= count * 0.02

	def frost_6_1(self, count):
		'''Cold as Ice'''
		pass

	def frost_6_2(self, count):
		'''Winters Chill'''
		pass

	def frost_7_1(self, count):
		'''Shattered Barrier'''
		pass

	def frost_7_2(self, count):
		'''Ice Barrier'''
		pass

	def frost_7_3(self, count):
		'''Arctic Winds'''
		assert count in (0,1,2,3,4,5)
		self.spell_amount_increase['frost']+= count * 0.01

	def frost_8_1(self, count):
		'''Empowered Frostbolt'''
		assert count in (0,1,2)
		self.spells['Frostbolt'].direct_coefficient += count * 0.1
		self.spells['Frostbolt'].modified_panel_cast_time -= count * 0.1
		
	def frost_8_2(self, count):
		'''Fingers of Frost'''
		pass

	def frost_9_1(self, count):
		'''Brain Freeze'''
		pass

	def frost_9_2(self, count):
		'''Summon Water Elenmental'''
		pass

	def frost_9_3(self, count):
		'''Enduring Winter'''
		pass

	def frost_10_1(self, count):
		'''Chilled to the Bone'''
		assert count in (0,1,2,3,4,5)
		self.spells['Frostbolt'].specific_amount_increase += count * 0.02
		self.spells['Frostfire Bolt'].specific_amount_increase += count * 0.02
		self.spells['Ice Lance'].specific_amount_increase += count * 0.02

	def frost_11_1(self, count):
		'''Deep Freeze'''
		pass

	def fire_1_1(self, count):
		'''Improved Fire Blast'''
		pass

	def fire_1_2(self, count):
		'''Incineration'''
		assert count in (0,1,2,3)
		self.spells['Fire Blast'].specific_critical_increase += count * 0.02
		self.spells['Scorch'].specific_critical_increase += count * 0.02
		self.spells['Arcane Blast'].specific_critical_increase += count * 0.02
		self.spells['Cone of Cold'].specific_critical_increase += count * 0.02

	def fire_1_3(self, count):
		'''Improved Fireball'''
		assert count in (0,1,2,3,4,5)
		self.spells['Fire Ball'].modified_cast_time -= count * 0.1

	def fire_2_1(self, count):
		'''Ignite'''
		pass

	def fire_2_2(self, count):
		'''Burning Determination'''
		pass

	def fire_2_3(self, count):
		'''World In Flames'''
		assert count in (0,1,2,3)
		self.spells['Flamestrike'].specific_critical_increase += count * 0.02
		self.spells['Pyroblast'].specific_critical_increase += count * 0.02
		self.spells['Blast Wave'].specific_critical_increase += count * 0.02
		self.spells['Dragons Breath'].specific_critical_increase += count * 0.02
		self.spells['Blizzard'].specific_critical_increase += count * 0.02
		self.spells['Arcane Explosion'].specific_critical_increase += count * 0.02

	def fire_3_1(self, count):
		'''Flame Throwing'''
		pass

	def fire_3_2(self, count):
		'''Impact'''
		pass

	def fire_3_3(self, count):
		'''Pyroblast'''
		pass

	def fire_3_4(self, count):
		'''Burning Soul'''
		pass

	def fire_4_1(self, count):
		'''Improved Scorch'''
		assert count in (0,1,2,3)
		self.spells['Scorch'].specific_critical_increase += count * 0.01
		self.spells['Fireball'].specific_critical_increase += count * 0.01
		self.spells['Frostfire Bolt'].specific_critical_increase += count * 0.01

	def fire_4_2(self, count):
		'''Molten Shields'''
		pass

	def fire_4_3(self, count):
		'''Master of Elements'''
		pass

	def fire_5_1(self, count):
		'''Playing with Fire'''
		assert count in (0,1,2,3)
		for k in self.spell_amount_increase.keys():
			self.spell_amount_increase[k] += count * 0.01
		self.damage_reduce['spell'] += count * 0.01
		self.damage_reduce['melee'] += count * 0.01

	def fire_5_2(self, count):
		'''Critical Mass'''
		assert count in (0,1,2,3)
		self.spell_critical_increase['fire'] += count * 0.02

	def fire_5_3(self, count):
		'''Blast Wave'''
		pass

	def fire_6_1(self, count):
		'''Blazing Speed'''
		pass

	def fire_6_2(self, count):
		'''Fire Power'''
		assert count in (0,1,2,3,4,5)
		self.spell_amount_increase['fire'] += count * 0.02

	def fire_7_1(self, count):
		'''Pyromaniac'''
		assert count in (0,1,2,3)
		for k in self.spell_critical_increase.keys():
			self.spell_critical_increase[k] += 0.01

	def fire_7_2(self, count):
		'''Combustion'''
		pass

	def fire_7_3(self, count):
		'''Molten Fury'''
		pass

	def fire_8_1(self, count):
		'''Fiery Payback'''
		pass

	def fire_8_2(self, count):
		'''Empowered Fire'''
		assert count in (0,1,2,3)
		self.spells['Fireball'].direct_coefficient += count * 0.05
		self.spells['Frostfire Bolt'].direct_coefficient += count * 0.05
		self.spells['Pyroblast'].direct_coefficient += count * 0.05

	def fire_9_1(self, count):
		'''Firestarter'''
		pass

	def fire_9_2(self, count):
		'''Dragons's Breath'''
		pass

	def fire_9_3(self, count):
		'''Hot Streak'''
		pass

	def fire_10_1(self, count):
		'''Burnout'''
		assert count in (0,1,2,3,4,5)
		for k in self.spell_criitcal_bonus.keys():
			self.spell_critical_bouns *= 1 + count * 0.1

	def fire_11_1(self, count):
		'''Living Bomb'''
		pass
	
	def arcane_1_1(self, count):
		'''Arcane Subtlety'''
		pass

	def arcane_1_2(self, count):
		'''Arcane Focus'''
		pass

	def arcane_1_3(self, count):
		'''Arcane Stability'''
		pass

	def arcane_2_1(self, count):
		'''Arcane Fortitude'''
		# todo intellect will change armor, and talent will change intellect
		#self.armor += 
		pass

	def arcane_2_2(self, count):
		'''Magic Absorption'''
		pass

	def arcane_2_3(self, count):
		'''Arcane Concentration'''
		pass

	def arcane_3_1(self, count):
		'''Magic Attunement'''
		pass

	def arcane_3_2(self, count):
		'''Spell Impact'''
		assert count in (0,1,2,3)
		self.spells['Arcane Explosion'].specific_amount_increase += count * 0.02
		self.spells['Arcane Blast'].specific_amount_increase += count * 0.02
		self.spells['Blast Wave'].specific_amount_increase += count * 0.02
		self.spells['Fire Blast'].specific_amount_increase += count * 0.02
		self.spells['Scorch'].specific_amount_increase += count * 0.02
		self.spells['Fireball'].specific_amount_increase += count * 0.02
		self.spells['Ice Lance'].specific_amount_increase += count * 0.02
		self.spells['Cone of Cold'].specific_amount_increase += count * 0.02

	def arcane_3_3(self, count):
		'''Student of the Mind'''
		assert count in (0,1,2,3)
		self.spell_basic_attr['spirit'] *= 1 + count * 0.04

	def arcane_3_4(self, count):
		'''Focus Magic'''
		pass

	def arcane_4_1(self, count):
		'''Arcane Shielding'''
		pass

	def arcane_4_2(self, count):
		'''Improved Counterspell'''
		pass

	def arcane_4_3(self, count):
		'''Arcane Meditation'''
		pass

	def arcane_4_4(self, count):
		'''Torment the Weak'''
		pass

	def arcane_5_1(self, count):
		'''Improved Blink'''
		pass

	def arcane_5_2(self, count):
		'''Presence of Mind'''
		pass

	def arcane_5_3(self, count):
		'''Arcane Mind'''
		assert count in (0,1,2,3,4,5)
		self.spell_basic_attr['intellect'] *= 1 + count * 0.03

	def arcane_6_1(self, count):
		'''Prismatic Cloak'''
		assert count in (0,1,2,3)
		self.damage_reduce['spell'] -= count * 0.02
		self.damage_reduce['melee'] -= count * 0.02

	def arcane_6_2(self, count):
		'''Arcane Instability'''
		assert count in (0,1,2,3)
		for k in self.spell_amount_increase.keys():
			self.spell_amount_increase[k] += count * 0.01
		for k in self.spell_critical_increase.keys():
			self.spell_critical_increase[k] += count * 0.01

	def arcane_6_3(self, count):
		'''Arcane Potency'''
		pass

	def arcane_7_1(self, count):
		'''Arcane Empowerment'''
		assert count in (0,1,2,3)
		self.spells['Arcane Missile'].direct_coefficient += count * 0.15
		self.spells['Arcane Blast'].specific_amount_increase += count * 0.03

	def arcane_7_2(self, count):
		'''Arcane Power'''
		pass

	def arcane_7_3(self, count):
		'''Incanter Absorption'''
		pass

	def arcane_8_1(self, count):
		'''Arcane Flows'''
		pass

	def arcane_8_2(self, count):
		'''Mind Mastery'''
		assert count in (0,1,2,3,4,5)
		self.spell_basic_attr['spell power'] += count * 0.03 * self.spell_basic_attr['intellect']

	def arcane_9_1(self, count):
		'''Slow'''
		pass

	def arcane_9_2(self, count):
		'''Missile Barrage'''
		pass

	def arcane_10_1(self, count):
		'''Netherwind Presence'''
		assert count in (0,1,2,3)
		self.spell_basic_attr['spell haste'] += count * 0.02

	def arcane_10_2(self, count):
		'''Spell Power'''
		assert count in (0,1,2)
		for k in self.spell_critical_bonus.keys():
			self.spell_critical_bonus[k] *= 1 + count * 0.25

	def arcane_11_1(self, count):
		'''Arcane Barrage'''
		pass




	
class MageGlyph():
	def __init__(self):
		pass


class Mage(Attribute, MageTalent, MageGlyph):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.spells = OrderedDict()
		with open('data/mage_spells.json') as fobj:
			jsc = fobj.read()
			content = json.loads(jsc)
		for item in content:
			self.spells[item['spell_name']] = Spell(item)
		
		# initialize attribute
		Attribute.__init__(self, attr_dict)

		# initialize talent
		for depth in range(0, 11):
			for column in range(0, 12):
				if talent_list[depth][column] != None:	
					if column < 4:
						res_str = 'arcane_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'fire_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'frost_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Mage, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spells
		for spell in self.spells.values():
			spell.calculate_amount(self.spell_basic_attr, self.spell_critical_increase, self.spell_critical_bonus, self.spell_amount_increase)



if __name__ == '__main__':
	mage = Mage()
	fun = getattr(Mage, 'arcane_11_1')
	print(type(fun))
	fun(mage, 3)



