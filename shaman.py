import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability
from ability import Spell_ability


class ShamanTalent():
	def __init__(self):
		pass

	def elemental_1_2(self, count):
		'''Convection'''
		pass

	def elemental_1_3(self, count):
		'''Concussion'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Lightning Bolt'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Chain Lightning'].specific_amount_increase += 0.01 * count
		# 2025/01/04 the database didn't provide the coefficient for Thunderstorm
		#self.spell_abilities['Thunderstorm'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Lava Burst'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Flame Shock (direct)'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Flame Shock (dot)'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Frost Shock'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Earth Shock'].specific_amount_increase += 0.01 * count

	def elemental_2_1(self, count):
		'''Call of Flame'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Lava Burst'].specific_amount_increase += 0.02 * count

	def elemental_2_2(self, count):
		'''Elemental Warding'''
		pass

	def elemental_2_3(self, count):
		'''Elemental Devastation'''
		pass

	def elemental_3_1(self, count):
		'''Reverberation'''
		pass

	def elemental_3_2(self, count):
		'''Elemental Focus'''
		pass

	def elemental_3_3(self, count):
		'''Elemental Fury'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			if ab.school == 'fire' or ab.school == 'frost' or ab.school == 'nature':
				ab.critical_bonus *= 1 + 0.2 * count

	def elemental_4_1(self, count):
		'''Improved Fire Nova'''
		pass

	def elemental_4_4(self, count):
		'''Eye of the Storm'''
		pass

	def elemental_5_1(self, count):
		'''Elemental Reach'''
		pass

	def elemental_5_2(self, count):
		'''Call of Thunder'''
		assert count in (0, 1)
		self.spell_abilities['Lightning Bolt'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Chain Lightning'].specific_critical_increase += 0.05 * count
		#self.spell_abilities['Thunderstorm'].specific_critical_increase += 0.05 * count

	def elemental_5_4(self, count):
		'''Unrelenting Storm'''
		pass

	def elemental_6_1(self, count):
		'''Elemental Precision'''
		pass

	def elemental_6_3(self, count):
		'''Lightning Mastery'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Lightning Bolt'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Chain Lightning'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Lava Burst'].modified_panel_cast_time -= 0.1 * count

	def elemental_7_2(self, count):
		'''Elemental Mastery'''
		pass

	def elemental_7_3(self, count):
		'''Storm, Earth and Fire'''
		# todo periodic part dmg inc
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Flame Shock (direct)'].specific_amount_increase += 0.2 * count
		self.spell_abilities['Flame Shock (dot)'].specific_amount_increase += 0.2 * count

	def elemental_8_1(self, count):
		'''Booming Echoes'''
		# todo direct part dmg inc
		assert count in (0, 1, 2)
		self.spell_abilities['Flame Shock (direct)'].specific_amount_increase += 0.1 * count
		self.spell_abilities['Frost Shock'].specific_amount_increase += 0.1 * count

	def elemental_8_2(self, count):
		'''Elemental Oath'''
		pass

	def elemental_8_3(self, count):
		'''Lightning Overload'''
		pass

	def elemental_9_1(self, count):
		'''Astral Shift'''
		pass

	def elemental_9_2(self, count):
		'''Totem of Wrath'''
		pass
	
	def elemental_9_3(self, count):
		'''Lava Flows'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Lava Burst'].critical_bonus *= 1 + 0.06 * count

	def elemental_10_2(self, count):
		'''Shamanism'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Lightning Bolt'].direct_coefficient += 0.04 * count
		self.spell_abilities['Chain Lightning'].direct_coefficient += 0.04 * count
		self.spell_abilities['Lava Burst'].direct_coefficient += 0.05 * count

	def elemental_11_2(self, count):
		'''Thunderstorm'''
		pass

	def enhancement_1_1(self, count):
		'''Enhancing Totems'''
		pass

	def enhancement_1_2(self, count):
		'''Earth's Grasp'''
		pass

	def enhancement_1_3(self, count):
		'''Ancestral Knowledge'''
		pass

	def enhancement_2_1(self, count):
		'''Guardian Totems'''
		pass

	def enhancement_2_2(self, count):
		'''Thundering Strikes'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			ab.specific_critical_increase += 0.01 * count
		# 2025/01/04 commented out
		#for ab in self.physic_abilities.values():
		#	ab.specific_critical_increase += 0.01 * count

	def enhancement_2_3(self, count):
		'''Improved Ghost Wolf'''
		pass

	def enhancement_2_4(self, count):
		'''Improved Shields'''
		pass

	def enhancement_3_1(self, count):
		'''Elemental Weapons'''
		pass

	def enhancement_3_3(self, count):
		'''Shamanistic Focus'''
		pass

	def enhancement_3_4(self, count):
		'''Anticipation'''
		pass

	def enhancement_4_2(self, count):
		'''Flurry'''
		pass

	def enhancement_4_3(self, count):
		'''Toughness'''
		pass

	def enhancement_5_1(self, count):
		'''Improved Windfury Totem'''
		pass

	def enhancement_5_2(self, count):
		'''Spirit Weapons'''
		pass

	def enhancement_5_3(self, count):
		'''Mental Dexterity'''
		pass

	def enhancement_6_1(self, count):
		'''Unleashed Rage'''
		pass

	def enhancement_6_2(self, count):
		'''Weapon Mastery'''
		# todo inc dmg
		pass

	def enhancement_6_4(self, count):
		'''Frozen Power'''
		pass

	def enhancement_7_1(self, count):
		'''Dual Wield Specialization'''
		pass

	def enhancement_7_2(self, count):
		'''Dual Wield'''
		pass

	def enhancement_7_3(self, count):
		'''Stormstrike'''
		pass

	def enhancement_8_1(self, count):
		'''Static Shock'''
		pass

	def enhancement_8_2(self, count):
		'''Lava Lash'''
		pass

	def enhancement_8_3(self, count):
		'''Improved Stormstrike'''
		pass

	def enhancement_9_1(self, count):
		'''Mental Quickness'''
		pass

	def enhancement_9_2(self, count):
		'''Shamanistic Rage'''
		pass

	def enhancement_9_3(self, count):
		'''Earthen Power'''
		pass

	def enhancement_10_2(self, count):
		'''Maelstrom Weapon'''
		pass

	def enhancement_11_2(self, count):
		'''Feral Spirit'''
		pass

	def restoration_1_2(self, count):
		'''Improved Healing Wave'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Healing Wave'].modified_panel_cast_time -= 0.1 * count

	def restoration_1_3(self, count):
		'''Totemic Focus'''
		pass

	def restoration_2_1(self, count):
		'''Improved Reincarnation'''
		pass

	def restoration_2_2(self, count):
		'''Healing Grace'''
		pass

	def restoration_2_3(self, count):
		'''Tida Focus'''
		pass

	def restoration_3_1(self, count):
		'''Improved Water Shield'''
		pass

	def restoration_3_2(self, count):
		'''Healing Focus'''
		pass

	def restoration_3_3(self, count):
		'''Tidal Force'''
		pass

	def restoration_3_4(self, count):
		'''Ancestral Healing'''
		pass

	def restoration_4_2(self, count):
		'''Restorative Totems'''
		pass

	def restoration_4_3(self, count):
		'''Tidal Mastery'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			if ab.nature == 'heal':
				ab.specific_critical_increase += 0.01 * count
		self.spell_abilities['Lightning Bolt'].specific_critical_increase += 0.01 * count
		self.spell_abilities['Chain Lightning'].specific_critical_increase += 0.01 * count

	def restoration_5_1(self, count):
		'''Healing Way'''
		assert count in (0, 1, 2, 3)
		if count <= 2:
			inc = 0.08 * count
		elif count == 3:
			inc = 0.25
		self.spell_abilities['Healing Wave'].specific_amount_increase += inc

	def restoration_5_2(self, count):
		'''Nature's Swiftness'''
		pass

	def restoration_5_4(self, count):
		'''Focused Mind'''
		pass

	def restoration_6_3(self, count):
		'''Purification'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.spell_abilities.values():
			if ab.nature == 'heal':
				ab.specific_amount_increase += 0.02 * count

	def restoration_7_1(self, count):
		'''Nature's Guardian'''
		pass

	def restoration_7_2(self, count):
		'''Mana Tide Totem'''
		pass

	def restoration_7_3(self, count):
		'''Cleanse Spirit'''
		pass

	def restoration_8_1(self, count):
		'''Blessing of the Eternals'''
		assert count in (0, 1, 2)
		for ab in self.spell_abilities.values():
			ab.specific_critical_increase += 0.02 * count

	def restoration_8_2(self, count):
		'''Improved Chain Heal'''
		assert count in (0, 1, 2)
		self.spell_abilities['Chain Heal'].specific_amount_increase += 0.1 * count

	def restoration_8_3(self, count):
		'''Nature's Blessing'''
		# todo increase heal by ratio of intellect
		pass

	def restoration_9_1(self, count):
		'''Ancestral Awaken'''
		pass

	def restoration_9_2(self, count):
		'''Earth Shield'''
		pass

	def restoration_9_3(self, count):
		'''Improved Earth Shield'''
		assert count in (0, 1, 2)
		self.spell_abilities['Earth Shield'].specific_amount_increase += 0.1 * count

	def restoration_10_2(self, count):
		'''Tidal Waves'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Healing Wave'].direct_coefficient += 0.04 * count
		self.spell_abilities['Lesser Healing Wave'].direct_coefficient += 0.02 * count

	def restoration_11_2(self, count):
		'''Riptide'''
		pass



class Shaman(Attribute, ShamanTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.spell_abilities = OrderedDict()
		with open('ability_data/shaman_spell_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				self.spell_abilities[item['ability_name']] = Spell_ability(item)

		# 2025/01/04
		# commented out this section of code
		# because the database didn't provide coefficients for enhancement shaman abilities
		#self.physic_abilities = OrderedDict()
		#with open('ability_data/shaman_physic_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
		#	content = csv.DictReader(fobj)
		#	for item in content:	# every item is a dict
		#		self.physic_abilities[item['ability_name']] = Physic_ability(item)
		
		# initialize attribute
		Attribute.__init__(self, attr_dict)
	
		# initialize talent
		for depth in range(0, 11):
			for column in range(0, 12):
				if talent_list[depth][column] != None:	
					if column < 4:
						res_str = 'elemental_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'enhancement_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'restoration_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Shaman, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spell abilities
		for ability in self.spell_abilities.values():
			ability.calculate_amount(self.spell_basic_attr, self.spell_critical_increase, self.spell_amount_increase)
		# calculate amount of physic abilities
		#for ability in self.physic_abilities.values():
		#	ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)



