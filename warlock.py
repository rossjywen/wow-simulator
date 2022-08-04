import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Spell_ability


class WarlockTalent():
	def __init__(self):
		pass
	
	def affliction_1_1(self, count):
		'''Improved Curse of Agony'''
		assert count in (0, 1, 2)
		self.spell_abilities['Curse of Agony'].specific_amount_increase += 0.05 * count
	
	def affliction_1_2(self, count):
		'''Suppression'''
		pass
	
	def affliction_1_3(self, count):
		'''Improved Corruption'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Corruption'].specific_amount_increase += 0.02 * count
		#self.spell_abilities['Seed of Corruption'].specific_critical_increase += 0.01 * count

	def affliction_2_1(self, count):
		'''Improved Curse of Weakness'''
		pass

	def affliction_2_2(self, count):
		'''Improved Drain Soul'''
		pass
	
	def affliction_2_3(self, count):
		'''Improved Life Tap'''
		pass
	
	def affliction_2_4(self, count):
		'''Soul Siphon'''
		pass
	
	def affliction_3_1(self, count):
		'''Improved Fear'''
		pass
	
	def affliction_3_2(self, count):
		'''Fel Concentration'''
		pass
	
	def affliction_3_3(self, count):
		'''Amplify Curse'''
		pass
	
	def affliction_4_1(self, count):
		'''Grim Reach'''
		pass
	
	def affliction_4_2(self, count):
		'''Nightfall'''
		pass
	
	def affliction_4_4(self, count):
		'''Empowered Corruption'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Corruption'].periodic_coefficient += 0.12 * count
		
	def affliction_5_1(self, count):
		'''Shadow Embrace'''
		pass
	
	def affliction_5_2(self, count):
		'''Siphon Life'''
		assert count in (0, 1)
		self.spell_abilities['Corruption'].specific_amount_increase += 0.05 * count
		#self.spell_abilities['Seed of Corruption'].specific_amount_increase += 0.05 * count
		self.spell_abilities['Unstable Affliction'].specific_amount_increase += 0.05 * count
		self.spell_abilities['Unstable Affliction (dispel)'].specific_amount_increase += 0.05 * count

	def affliction_5_3(self, count):
		'''Curse of Exhaustion'''
		pass
	
	def affliction_6_1(self, count):
		'''Improved Felhunter'''
		# pet ability increase
		pass
	
	def affliction_6_2(self, count):
		'''Shadow Mastery'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_amount_increase['shadow'] += 0.03 * count

	def affliction_7_1(self, count):
		'''Eradiction'''
		pass
	
	def affliction_7_2(self, count):
		'''Contagion'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Curse of Agony'].specific_amount_increase += 0.01 * count
		self.spell_abilities['Corruption'].specific_amount_increase += 0.01 * count
		#self.spell_abilities['Seed of Corruption'].specific_amount_increase += 0.01 * count

	def affliction_7_3(self, count):
		'''Dark Pact'''
		pass
	
	def affliction_8_1(self, count):
		'''Improved Howl of Terror'''
		pass
	
	def affliction_8_3(self, count):
		'''Malediction'''
		assert count in (0, 1, 2, 3)
		for k in self.spell_amount_increase.keys():
			self.spell_amount_increase[k] += 0.01 * count
		self.spell_abilities['Corruption'].specific_critical_increase += 0.03 * count
		self.spell_abilities['Unstable Affliction'].specific_critical_increase += 0.03 * count
		self.spell_abilities['Unstable Affliction (dispel)'].specific_critical_increase += 0.03 * count

	def affliction_9_1(self, count):
		'''Death's Embrace'''
		pass
	
	def affliction_9_2(self, count):
		'''Unstable Affliction'''
		# below code actually implement >>Glyph of Quick Decay<< because all affliction warlock use this glyph
		# I assume this talent-point to beidentified as >>affliction warlock<< so I choose this position to implement this
		self.spell_abilities['Corruption'].periodic_can_haste = True
	
	def affliction_9_3(self, count):
		'''Pandemic'''
		assert count in (0, 1)
		# todo make dot critical-able and bonus is 100% same as Shadowform
		self.spell_abilities['Corruption'].critical_bonus = 1
		self.spell_abilities['Corruption'].periodic_can_critical = True

		self.spell_abilities['Unstable Affliction'].critical_bonus = 1
		self.spell_abilities['Unstable Affliction (dispel)'].critical_bonus = 1
		self.spell_abilities['Unstable Affliction'].periodic_can_critical = True

		self.spell_abilities['Haunt'].critical_bonus *= 1 + count
	
	def affliction_10_2(self, count):
		'''Everlasting Affliction'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Corruption'].periodic_coefficient += 0.06 * count
		self.spell_abilities['Unstable Affliction'].periodic_coefficient += 0.05 * count
		self.spell_abilities['Unstable Affliction (dispel)'].direct_coefficient += 0.05 * count
	
	def affliction_11_2(self, count):
		'''Haunt'''
		pass

	def demonology_1_1(self, count):
		'''Improved Healthstone'''
		pass

	def demonology_1_2(self, count):
		'''Improved Imp'''
		# pet ability
		pass

	def demonology_1_3(self, count):
		'''Demonic Embrace'''
		pass

	def demonology_1_4(self, count):
		'''Fel Synergy'''
		pass

	def demonology_2_1(self, count):
		'''Improved Fel Funnel'''
		pass

	def demonology_2_2(self, count):
		'''Demonic Brutality'''
		# pet ability
		pass

	def demonology_2_3(self, count):
		'''Fel Vitality'''
		pass

	def demonology_3_1(self, count):
		'''Improved Succubus'''
		pass

	def demonology_3_2(self, count):
		'''Soul Link'''
		pass

	def demonology_3_3(self, count):
		'''Fel Domination'''
		pass

	def demonology_3_4(self, count):
		'''Demonic Aegis'''
		pass

	def demonology_4_2(self, count):
		'''Unholy Power'''
		# pet ability
		pass

	def demonology_4_3(self, count):
		'''Master Summoner'''
		pass

	def demonology_5_1(self, count):
		'''Mana Feed'''
		pass

	def demonology_5_3(self, count):
		'''Master Conjurer'''
		pass

	def demonology_6_2(self, count):
		'''Master Demonologist'''
		pass

	def demonology_6_3(self, count):
		'''Molten Core'''
		# todo 'increase duration of Immolate 3s..'
		pass

	def demonology_7_1(self, count):
		'''Demonic Resilience'''
		pass

	def demonology_7_2(self, count):
		'''Demonic Empowerment'''
		pass

	def demonology_7_3(self, count):
		'''Demonic Knowledge'''
		# todo check if increase spell power in panel
		pass

	def demonology_8_2(self, count):
		'''Demonic Tactics'''
		# todo check if increase critical will be displayed in panel
		# pet ability
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_basic_attr['spell_critical'] += 0.02 * count

	def demonology_8_3(self, count):
		'''Decimation'''
		pass

	def demonology_9_1(self, count):
		'''Improved Demonic Tactics'''
		pass

	def demonology_9_2(self, count):
		'''Summon Felguard'''
		pass

	def demonology_9_3(self, count):
		'''Nemesis'''
		pass

	def demonology_10_2(self, count):
		'''Demonic Pact'''
		pass

	def demonology_11_2(self, count):
		'''Metamorphosis'''
		pass

	def destruction_1_2(self, count):
		'''Improved Shadow Bolt'''
		assert count in (0, 1 ,2 ,3, 4, 5)
		self.spell_abilities['Shadow Bolt'].specific_amount_increase += 0.02 * count

	def destruction_1_3(self, count):
		'''Bane'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Shadow Bolt'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Chaos Bolt'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Immolate'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Soul Fire'].modified_panel_cast_time -= 0.4 * count

	def destruction_2_1(self, count):
		'''Aftermath'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Immolate'].specific_amount_increase += 0.03 * count
		# todo in fact, this talent increase the dot-portion of Immolate, I will fix this later.

	def destruction_2_2(self, count):
		'''Molten Skin'''
		pass

	def destruction_2_3(self, count):
		'''Cataclysm'''
		pass

	def destruction_3_1(self, count):
		'''Demonic Power'''
		# Imp's spell
		pass

	def destruction_3_2(self, count):
		'''Shadowburn'''
		pass

	def destruction_3_3(self, count):
		'''Ruin'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Chaos Bolt'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Conflagrate'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Immolate'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Incinerate'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Rain of Fire'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Searing Pain'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Shadow Bolt'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Shadowburn'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Shadowflame'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Shadowfury'].critical_bonus *= 1 + (0.2 * count)
		self.spell_abilities['Soul Fire'].critical_bonus *= 1 + (0.2 * count)

	def destruction_4_1(self, count):
		'''Intensity'''
		pass

	def destruction_4_2(self, count):
		'''Destructive Reach'''
		pass

	def destruction_4_4(self, count):
		'''Improved Searing Pain'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Searing Pain'].specific_critical_increase += 0.04 * count

	def destruction_5_1(self, count):
		'''Blachlash'''
		assert count in (0, 1, 2, 3)
		self.spell_basic_attr['spell_critical'] += 0.01 * count

	def destruction_5_2(self, count):
		'''Improved Immolate'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Immolate'].specific_amount_increase += 0.1 * count

	def destruction_5_3(self, count):
		'''Devastation'''
		assert count in (0, 1)
		self.spell_abilities['Chaos Bolt'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Conflagrate'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Immolate'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Incinerate'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Rain of Fire'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Searing Pain'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Shadow Bolt'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Shadowburn'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Shadowflame'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Shadowfury'].specific_critical_increase += 0.05 * count
		self.spell_abilities['Soul Fire'].specific_critical_increase += 0.05 * count

	def destruction_6_1(self, count):
		'''Nether Protection'''
		pass

	def destruction_6_3(self, count):
		'''Emberstorm'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_amount_increase['fire'] += 0.03 * count
		self.spell_abilities['Incinerate'].modified_panel_cast_time -= 0.05 * count

	def destruction_7_2(self, count):
		'''Conflagrate'''
		pass

	def destruction_7_3(self, count):
		'''Soul Leech'''
		pass

	def destruction_7_4(self, count):
		'''Pyroclasm'''
		pass

	def destruction_8_2(self, count):
		'''Shadow and Flame'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Shadow Bolt'].direct_coefficient *= 1 + 0.04 * count
		self.spell_abilities['Shadowburn'].direct_coefficient *= 1 + 0.04 * count
		self.spell_abilities['Chaos Bolt'].direct_coefficient *= 1 + 0.04 * count
		self.spell_abilities['Incinerate'].direct_coefficient *= 1 + 0.04 * count

	def destruction_8_3(self, count):
		'''Improved Soul Leech'''
		pass

	def destruction_9_1(self, count):
		'''Backdraft'''
		pass

	def destruction_9_2(self, count):
		'''Shadowfury'''
		pass

	def destruction_9_3(self, count):
		'''Empowered Imp'''
		pass

	def destruction_10_2(self, count):
		'''Fire and Brimstone'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Conflagrate'].specific_critical_increase += 0.05 * count

	def destruction_11_2(self, count):
		'''Chaos Bolt'''
		pass


class Warlock(Attribute, WarlockTalent):
	def __init__(self, attr_dict, talent_list):
		self.spell_abilities = OrderedDict()
		with open('ability_data/warlock_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				if item['ability_type'] == 'magic':
					self.spell_abilities[item['ability_name']] = Spell_ability(item)
				elif item['ability_type'] == 'melee':
					pass	# todo melee_ability
				elif item['ability_type'] == 'range':
					pass	# todo range_ability
		
		# initialize attribute
		Attribute.__init__(self, attr_dict)

		# initialize talent
		for depth in range(0, 11):
			for column in range(0, 12):
				if talent_list[depth][column] != None:	
					if column < 4:
						res_str = 'affliction_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'demonology_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'destruction_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Warlock, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spells
		for spell in self.spell_abilities.values():
			spell.calculate_amount(self.spell_basic_attr, self.spell_critical_increase, self.spell_amount_increase)
	


