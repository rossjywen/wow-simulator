import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability



class WarriorTalent():
	def __init__(self):
		pass

	def arms_1_1(self, count):
		'''Improved Heroic Strike'''
		pass

	def arms_1_2(self, count):
		'''Deflection'''
		pass

	def arms_1_3(self, count):
		'''Improved Rend'''
		assert count in (0, 1, 2)
		self.physic_abilities['Rend'].specific_amount_increase += 0.1 * count

	def arms_2_1(self, count):
		'''Improved Charge'''
		pass

	def arms_2_2(self, count):
		'''Iron Will'''
		pass

	def arms_2_3(self, count):
		'''Tactical Mastery'''
		pass

	def arms_3_1(self, count):
		'''Improved Overpower'''
		assert count in (0, 1, 2)
		self.physic_abilities['Overpower'].specific_critical_increase += 0.25 * count

	def arms_3_2(self, count):
		'''Anger Management'''
		pass

	def arms_3_3(self, count):
		'''Impale'''
		assert count in (0, 1, 2)
		for ab in self.physic_abilities.values():
			ab.critical_bonus *= 1 + 0.1 * count

	def arms_3_4(self, count):
		'''Deep Wounds'''
		pass

	def arms_4_2(self, count):
		'''Two Handed Specialization'''
		# todo test influence on what abilities
		pass

	def arms_4_3(self, count):
		'''Taste for Blood'''
		pass

	def arms_5_1(self, count):
		'''Poleaxe Specialization'''
		self.physic_basic_attr['melee_critical'] += 0.01 * count
		#self.physic_basic_attr['ranged_critical'] += 0.01 * count
		# increase critical hit damage I just modify critical_bonus
		# todo will check influence what ability

	def arms_5_2(self, count):
		'''Sweeping Strikes'''
		pass

	def arms_5_3(self, count):
		'''Mace Specialization'''
		# equivalent to add ArP, but currently I did not record ArP
		pass

	def arms_5_4(self, count):
		'''Sword Specialization'''
		pass

	def arms_6_1(self, count):
		'''Weapon Mastery'''
		pass

	def arms_6_3(self, count):
		'''Improved Hamstring'''
		pass

	def arms_6_4(self, count):
		'''Trauma'''
		pass

	def arms_7_1(self, count):
		'''Second Wind'''
		pass

	def arms_7_2(self, count):
		'''Mortal Strike'''
		pass

	def arms_7_3(self, count):
		'''Strength of Arm'''
		pass

	def arms_7_4(self, count):
		'''Improved Slam'''
		pass

	def arms_8_1(self, count):
		'''Juggernaut'''
		pass

	def arms_8_2(self, count):
		'''Improved Mortal Strike'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Mortal Strike'].specific_amount_increase += 0.03 * count

	def arms_8_3(self, count):
		'''Unrelenting Assaut'''
		assert count in (0, 1, 2)
		self.physic_abilities['Overpower'].specific_amount_increase += 0.1 * count
		self.physic_abilities['Revenge'].specific_amount_increase += 0.1 * count

	def arms_9_1(self, count):
		'''Sudden Death'''
		pass

	def arms_9_2(self, count):
		'''Endless Rage'''
		pass

	def arms_9_3(self, count):
		'''Blood Frenzy'''
		pass

	def arms_10_2(self, count):
		'''Wrecking Crew'''
		pass

	def arms_11_2(self, count):
		'''Bladestorm'''
		pass

	def fury_1_1(self, count):
		'''Armed to Teeth'''
		pass

	def fury_1_2(self, count):
		'''Booming Voice'''
		pass

	def fury_1_3(self, count):
		'''Cruelty'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_basic_attr['melee_critical'] += 0.01 * count

	def fury_2_2(self, count):
		'''Improved Demoralizing Shout'''
		pass

	def fury_2_3(self, count):
		'''Unbridled Wrath'''
		pass

	def fury_3_1(self, count):
		'''Improved Cleave'''
		# todo
		pass

	def fury_3_2(self, count):
		'''Piercing Howl'''
		pass

	def fury_3_3(self, count):
		'''Blood Craze'''
		pass

	def fury_3_4(self, count):
		'''Commanding Presence'''
		pass

	def fury_4_1(self, count):
		'''Dual Wield Specialization'''
		# todo offhand weapon
		pass

	def fury_4_2(self, count):
		'''Improved Execute'''
		pass

	def fury_4_3(self, count):
		'''Enrage'''
		pass

	def fury_5_1(self, count):
		'''Precision'''
		pass

	def fury_5_2(self, count):
		'''Death Wish'''
		pass

	def fury_5_3(self, count):
		'''Improved Intercept'''
		pass

	def fury_6_1(self, count):
		'''Improved Berserker Rage'''
		pass

	def fury_6_3(self, count):
		'''Flurry'''
		pass

	def fury_7_1(self, count):
		'''Intensify Rage'''
		pass

	def fury_7_2(self, count):
		'''Bloodthirst'''
		pass

	def fury_7_4(self, count):
		'''Improved Whirlwind'''
		assert count in (0, 1, 2)
		self.physic_abilities['Whirlwind'].specific_amount_increase += 0.1 * count

	def fury_8_1(self, count):
		'''Furious Attacks'''
		pass

	def fury_8_4(self, count):
		'''Improved Berserker Stance'''
		pass

	def fury_9_1(self, count):
		'''Heroic Fury'''
		pass

	def fury_9_2(self, count):
		'''Rampage'''
		pass

	def fury_9_3(self, count):
		'''Bloodsurge'''
		pass

	def fury_10_2(self, count):
		'''Unending Fury'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_abilities['Slam'].specific_amount_increase += 0.2 * count
		self.physic_abilities['Bloodthirst'].specific_amount_increase += 0.2 * count
		self.physic_abilities['Whirlwind'].specific_amount_increase += 0.2 * count

	def fury_11_2(self, count):
		'''Titan's Grip'''
		# todo all reduce 10%
		pass

	def protection_1_1(self, count):
		'''Improved Bloodrage'''
		pass

	def protection_1_2(self, count):
		'''Shield Specialization'''
		pass

	def protection_1_3(self, count):
		'''Improved Thunder Clap'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Thunder Clap'].specific_amount_increase += 0.1 * count

	def protection_2_2(self, count):
		'''Incite'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Heroic Strike'].specific_critical_increase += 0.05 * count
		self.physic_abilities['Thunder Clap'].specific_critical_increase += 0.05 * count
		self.physic_abilities['Cleave'].specific_critical_increase += 0.05 * count

	def protection_2_3(self, count):
		'''Anticipation'''
		pass

	def protection_3_1(self, count):
		'''Last Stand'''
		pass

	def protection_3_2(self, count):
		'''Improved Revenge'''
		assert count in (0, 1, 2)
		self.physic_abilities['Revenge'].specific_amount_increase += 0.3 * count

	def protection_3_3(self, count):
		'''Shield Mastery'''
		pass

	def protection_3_4(self, count):
		'''Toughness'''
		pass

	def protection_4_1(self, count):
		'''Improved Spell Reflection'''
		pass

	def protection_4_2(self, count):
		'''Improved Disarm'''
		pass

	def protection_4_3(self, count):
		'''Puncture'''
		pass

	def protection_5_1(self, count):
		'''Improved Disciplines'''
		pass

	def protection_5_2(self, count):
		'''Concussion Blow'''
		pass

	def protection_5_3(self, count):
		'''Gag Order'''
		assert count in (0, 1, 2)
		self.physic_abilities['Shield Slam'].specific_amount_increase += 0.05 * count

	def protection_6_3(self, count):
		'''One-Handed Weapon Specialization'''
		assert count in (0, 1, 2, 3, 4, 5)
		# I assume warrior with this talent active must be equiping a one-handed weapon
		self.physic_amount_increase['melee'] += 0.02 * count
		self.physic_amount_increase['ranged'] += 0.02 * count

	def protection_7_1(self, count):
		'''Improved Defensive Stance'''
		pass

	def protection_7_2(self, count):
		'''Vigilance'''
		pass

	def protection_7_3(self, count):
		'''Focused Rage'''
		pass

	def protection_8_2(self, count):
		'''Vitality'''
		pass

	def protection_8_3(self, count):
		'''Safeguard'''
		pass

	def protection_9_1(self, count):
		'''Warbringer'''
		pass

	def protection_9_2(self, count):
		'''Devastate'''
		pass

	def protection_9_3(self, count):
		'''Critical Block'''
		pass

	def protection_10_2(self, count):
		'''Sword and Board'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Devastate'].specific_critical_increase += 0.05 * count

	def protection_10_3(self, count):
		'''Damge Shield'''
		pass

	def protection_11_2(self, count):
		'''Shockwave'''
		pass



class Warrior(Attribute, WarriorTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all abilities
		self.physic_abilities = OrderedDict()
		with open('ability_data/warrior_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
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
						res_str = 'arms_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'fury_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'protection_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Warrior, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of physic abilities
		for ability in self.physic_abilities.values():
			ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)


