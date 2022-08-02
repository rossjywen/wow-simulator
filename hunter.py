import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability


class HunterTalent():
	def __init__(self):
		pass

	def beast_mastery_1_2(self, count):
		'''Improved Aspect of the Hawk'''
		pass

	def beast_mastery_1_3(self, count):
		'''Endurance Training'''
		pass

	def beast_mastery_2_1(self, count):
		'''Focused Fire'''
		assert count in (0, 1, 2)
		self.physic_amount_increase['melee'] += 0.01 * count
		self.physic_amount_increase['ranged'] += 0.01 * count

	def beast_mastery_2_2(self, count):
		'''Improved Aspect of the Monkey'''
		pass

	def beast_mastery_2_3(self, count):
		'''Thick Hide'''
		pass

	def beast_mastery_2_4(self, count):
		'''Improved Revive Pet'''
		pass

	def beast_mastery_3_1(self, count):
		'''Pahtfinding'''
		pass

	def beast_mastery_3_2(self, count):
		'''Aspect Mastery'''
		pass

	def beast_mastery_3_3(self, count):
		'''Unleashed Fury'''
		pass

	def beast_mastery_4_2(self, count):
		'''Improved Mend Pet'''
		pass

	def beast_mastery_4_3(self, count):
		'''Ferocity'''
		pass

	def beast_mastery_5_1(self, count):
		'''Spirit Bond'''
		pass

	def beast_mastery_5_2(self, count):
		'''Intimidation'''
		pass

	def beast_mastery_5_4(self, count):
		'''Bestial Discipline'''
		pass

	def beast_mastery_6_1(self, count):
		'''Animal Handler'''
		pass

	def beast_mastery_6_3(self, count):
		'''Frenzy'''
		pass

	def beast_mastery_7_1(self, count):
		'''Ferocious Inspiration'''
		assert count in (0, 1, 2, 3)
		for sp_key in self.physic_abilities.keys():	# because hunter only have Physic_ability
			self.physic_abilities[sp_key].specific_amount_increase += 0.01 * count
		self.physic_abilities['Arcane Shot'].specific_amount_increase += 0.03 * count
		self.physic_abilities['Steady Shot'].specific_amount_increase += 0.03 * count

	def beast_mastery_7_2(self, count):
		'''Bestial Wrath'''
		pass

	def beast_mastery_7_3(self, count):
		'''Catlike Reflexes'''
		pass

	def beast_mastery_8_1(self, count):
		'''Invigoration'''
		pass

	def beast_mastery_8_3(self, count):
		'''Serpent's Swiftness'''
		# todo what is 'ranged attack speed'?
		pass

	def beast_mastery_9_1(self, count):
		'''Longevity'''
		pass

	def beast_mastery_9_2(self, count):
		'''The Beast Within'''
		pass

	def beast_mastery_9_3(self, count):
		'''Cobra Strikes'''
		pass

	def beast_mastery_10_2(self, count):
		'''Kindred Spirits'''
		pass

	def beast_mastery_11_2(self, count):
		'''Beast Mastery'''
		pass

	def marksmanship_1_1(self, count):
		'''Improved Concussive Shot'''
		pass

	def marksmanship_1_2(self, count):
		'''Focused Aim'''
		pass

	def marksmanship_1_3(self, count):
		'''Lethal Shot'''
		pass

	def marksmanship_2_1(self, count):
		'''Careful Aim'''
		pass

	def marksmanship_2_2(self, count):
		'''Improved Hunter's Mask'''
		pass

	def marksmanship_2_3(self, count):
		'''Mortal Shots'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.physic_abilities.values():
			if ab.physic_type == 'ranged':
				ab.critical_bonus *= 1 + 0.06 * count

	def marksmanship_3_1(self, count):
		'''Go for the Throat'''
		pass

	def marksmanship_3_2(self, count):
		'''Improved Arcane Shot'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Arcane Shot'].specific_amount_increase += 0.05 * count

	def marksmanship_3_3(self, count):
		'''Aimed Shot'''
		pass

	def marksmanship_3_4(self, count):
		'''Rapid Killing'''
		pass

	def marksmanship_4_2(self, count):
		'''Improved Stings'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Serpent Sting'].specific_amount_increase += 0.1 * count

	def marksmanship_4_3(self, count):
		'''Efficiency'''
		pass

	def marksmanship_5_1(self, count):
		'''Concussive Barage'''
		pass

	def marksmanship_5_2(self, count):
		'''Readiness'''
		pass

	def marksmanship_5_3(self, count):
		'''Barrage'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Multi Shot'].specific_amount_increase += 0.04 * count
		self.physic_abilities['Aimed Shot'].specific_amount_increase += 0.04 * count
		self.physic_abilities['Volley'].specific_amount_increase += 0.04 * count

	def marksmanship_6_1(self, count):
		'''Combat Experience'''
		pass

	def marksmanship_6_4(self, count):
		'''Ranged Weapon Specialization'''
		assert count in (0, 1, 2, 3)
		inc = 0
		if count == 0:
			inc = 0
		elif count == 1:
			inc = 0.01
		elif count == 2:
			inc = 0.03
		elif count == 3:
			inc = 0.05

		for sp_key, sp_val in self.physic_abilities.items():
			if sp_val.physic_type == 'ranged':
				self.physic_abilities[sp_key].specific_amount_increase += inc 

	def marksmanship_7_1(self, count):
		'''Piercing Shots'''
		pass

	def marksmanship_7_2(self, count):
		'''Trueshot Aura'''
		pass

	def marksmanship_7_3(self, count):
		'''Improved Barrage'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Multi Shot'].specific_critical_increase += 0.04 * count
		self.physic_abilities['Aimed Shot'].specific_critical_increase += 0.04 * count

	def marksmanship_8_2(self, count):
		'''Master Marksman'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_basic_attr['melee_critical'] += 0.01 * count
		self.physic_basic_attr['ranged_critical'] += 0.01 * count

	def marksmanship_8_3(self, count):
		'''Rapid Recuperation'''
		pass

	def marksmanship_9_1(self, count):
		'''Wild Quiver'''
		pass

	def marksmanship_9_2(self, count):
		'''Silencing Shot'''
		pass

	def marksmanship_9_3(self, count):
		'''Improved Steady Shot'''
		pass

	def marksmanship_10_2(self, count):
		'''Marked for Death'''
		self.physic_abilities['Aimed Shot'].critical_bonus *= 1 + (0.02 * count)
		self.physic_abilities['Arcane Shot'].critical_bonus *= 1 + (0.02 * count)
		self.physic_abilities['Steady Shot'].critical_bonus *= 1 + (0.02 * count)
		self.physic_abilities['Kill Shot'].critical_bonus *= 1 + (0.02 * count)
		self.physic_abilities['Chimera Shot'].critical_bonus *= 1 + (0.02 * count)

	def marksmanship_11_2(self, count):
		'''Chimera Shot'''
		pass

	def survival_1_1(self, count):
		'''Improved Tracking'''
		pass

	def survival_1_2(self, count):
		'''Hawk Eye'''
		pass

	def survival_1_3(self, count):
		'''Savage Strikes'''
		# I did not include Raptor Strike, Mongoose, Counterattack to test
		pass

	def survival_2_1(self, count):
		'''Surefooted'''
		pass

	def survival_2_2(self, count):
		'''Entrapment'''
		pass

	def survival_2_3(self, count):
		'''Trap Mastery'''
		pass

	def survival_2_4(self, count):
		'''Survival Instinct'''
		assert count in (0, 1, 2)
		self.physic_abilities['Arcane Shot'].specific_critical_increase += 0.02 * count
		self.physic_abilities['Steady Shot'].specific_critical_increase += 0.02 * count
		self.physic_abilities['Explosive Shot'].specific_critical_increase += 0.02 * count

	def survival_3_1(self, count):
		'''Survivalist'''
		pass

	def survival_3_2(self, count):
		'''Scatter Shot'''
		pass

	def survival_3_3(self, count):
		'''Deflection'''
		pass

	def survival_3_4(self, count):
		'''Survival Tactics'''
		pass

	def survival_4_2(self, count):
		'''T.N.T'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Explosive Shot'].specific_amount_increase += 0.02 * count
		#self.physic_abilities['Explosive Trap'].specific_amount_increase += 0.02 * count
		self.physic_abilities['Black Arrow'].specific_amount_increase += 0.02 * count
		#self.physic_abilities['Immolation Trap'].specific_amount_increase += 0.02 * count

	def survival_4_4(self, count):
		'''Lock and Load'''
		pass

	def survival_5_1(self, count):
		'''Hunter vs. Wild'''
		pass

	def survival_5_2(self, count):
		'''Killer Instinct'''
		assert count in (0, 1, 2, 3)
		self.physic_basic_attr['melee_critical'] += 0.01 * count
		self.physic_basic_attr['ranged_critical'] += 0.01 * count

	def survival_5_3(self, count):
		'''Countattack'''
		pass

	def survival_6_1(self, count):
		'''Lightning Reflexes'''
		pass

	def survival_6_3(self, count):
		'''Resourcefulness'''
		pass

	def survival_7_1(self, count):
		'''Expose Weakness'''
		pass

	def survival_7_2(self, count):
		'''Wyvern Sting'''
		pass

	def survival_7_3(self, count):
		'''Thrill of the Hunt'''
		pass

	def survival_8_1(self, count):
		'''Master Tactician'''
		pass

	def survival_8_2(self, count):
		'''Noxious Stings'''
		pass

	def survival_9_1(self, count):
		'''Point of No Escape'''
		pass

	def survival_9_2(self, count):
		'''Black Arrow'''
		pass

	def survival_9_4(self, count):
		'''Sniper Training'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Kill Shot'].specific_critical_increase += 0.05 * count

	def survival_10_3(self, count):
		'''Hunting Party'''
		pass

	def survival_11_2(self, count):
		'''Explosive Shot'''
		pass


class Hunter(Attribute, HunterTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.physic_abilities = OrderedDict()
		with open('ability_data/hunter_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
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
						res_str = 'beast_mastery_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'marksmanship_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'survival_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Hunter, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spells
		for ability in self.physic_abilities.values():
			ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)
	


