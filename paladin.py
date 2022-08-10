import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability
from ability import Spell_ability



class PaladinTalent():
	def __init__(self):
		pass


	def holy_1_2(self, count):
		'''Spiritual Focus'''
		pass

	def holy_1_3(self, count):
		'''Seal of the Pure'''
		# todo seal dmg inc
		pass
	
	def holy_2_1(self, count):
		'''Healing Light'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Holy Light'].specific_amount_increase += 0.04 * count
		self.spell_abilities['Flash of Light'].specific_amount_increase += 0.04 * count
		self.spell_abilities['Holy Shock (heal)'].specific_amount_increase += 0.04 * count
		self.spell_abilities['Holy Shock (dmg)'].specific_amount_increase += 0.04 * count
	
	def holy_2_2(self, count):
		'''Divine Intellect'''
		pass
	
	def holy_2_3(self, count):
		'''Unyielding Faith'''
		pass

	def holy_3_1(self, count):
		'''Aura Mastery'''
		pass

	def holy_3_2(self, count):
		'''Illumination'''
		pass
	
	def holy_3_3(self, count):
		'''Improved Lay on Hands'''
		pass
	
	def holy_4_1(self, count):
		'''Improved Concentration Aura'''
		pass
	
	def holy_4_3(self, count):
		'''Improved Blessing of Wisdom'''
		pass

	def holy_4_4(self, count):
		'''Blessed Hands'''
		pass

	def holy_5_1(self, count):
		'''Pure of Heart'''
		pass
	
	def holy_5_2(self, count):
		'''Divine Favor'''
		pass
	
	def holy_5_3(self, count):
		'''Sanctified Light'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Holy Light'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Holy Shock (heal)'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Holy Shock (dmg)'].specific_critical_increase += 0.02 * count

	
	def holy_6_1(self, count):
		'''Purifying Power'''
		pass

	def holy_6_3(self, count):
		'''Holy Power'''
		self.spell_critical_increase['holy'] += 0.01 * count

	def holy_7_1(self, count):
		'''Light's Grace'''
		pass
	
	def holy_7_2(self, count):
		'''Holy Shock'''
		pass
	
	def holy_7_3(self, count):
		'''Blessed Life'''
		pass
	
	def holy_8_1(self, count):
		'''Sacred Cleansing'''
		pass

	def holy_8_3(self, count):
		'''Holy Guidance'''
		pass

	def holy_9_1(self, count):
		'''Divine Illumination'''
		pass
	
	def holy_9_3(self, count):
		'''Judgement of the Pure'''
		# todo dmg by seal?
		pass
	
	def holy_10_2(self, count):
		'''Infusion of Light'''
		pass
	
	def holy_10_3(self, count):
		'''Enlightened Judgements'''
		pass

	def holy_11_2(self, count):
		'''Beacon of Light'''
		pass

	def protection_1_2(self, count):
		'''Divinity'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_amount_increase['all_heal'] += 0.01 * count

	def protection_1_3(self, count):
		'''Divine Strength'''
		pass
	
	def protection_2_1(self, count):
		'''Stoicism'''
		pass
	
	def protection_2_2(self, count):
		'''Guardian's Favor'''
		pass
	
	def protection_2_3(self, count):
		'''Anticipation'''
		pass

	def protection_3_1(self, count):
		'''Divine Sacrifice'''
		pass

	def protection_3_2(self, count):
		'''Improved Righteous Fury'''
		pass
	
	def protection_3_3(self, count):
		'''Toughness'''
		pass
	
	def protection_4_1(self, count):
		'''Divine Guardian'''
		pass
	
	def protection_4_2(self, count):
		'''Improved Hammer of Justice'''
		pass

	def protection_4_3(self, count):
		'''Improved Devotion Aura'''
		pass

	def protection_5_2(self, count):
		'''Blessing of Sanctuary'''
		pass
	
	def protection_5_3(self, count):
		'''Reckoning'''
		pass
	
	def protection_6_1(self, count):
		'''Sacred Duty'''
		pass
	
	def protection_6_3(self, count):
		'''One-Handed Weapon Specialization'''
		assert count in (0, 1, 2, 3)
		# I assume paladin with this talent active must do dmg with one-hand weapon
		self.spell_amount_increase['all_dmg'] += 0.04 * count
		self.physic_amount_increase['melee'] += 0.04 * count
		self.physic_amount_increase['ranged'] += 0.04 * count

	def protection_7_1(self, count):
		'''Spiritual Attunement'''
		pass

	def protection_7_2(self, count):
		'''Holy Shield'''
		pass
	
	def protection_7_3(self, count):
		'''Ardent Defender'''
		pass
	
	def protection_8_1(self, count):
		'''Redoubt'''
		pass
	
	def protection_8_3(self, count):
		'''Combat Expertise'''
		assert count in (0, 1, 2 ,3)
		self.spell_basic_attr['spell_critical'] += 0.02 * count
		self.physic_basic_attr['melee_critical'] += 0.02 * count
		self.physic_basic_attr['ranged_critical'] += 0.02 * count

	def protection_9_1(self, count):
		'''Touched by the Light'''
		# todo check if it is right
		assert count in (0, 1, 2, 3)
		for sp in self.spell_abilities.values():
			if sp.nature == 'heal':
				sp.critical_bonus += 1.5 * 0.2 * count

	def protection_9_2(self, count):
		'''Avenger's Shield'''
		pass
	
	def protection_9_3(self, count):
		'''Guarded by the Light'''
		pass
	
	def protection_10_2(self, count):
		'''Shield of the Templar'''
		pass
	
	def protection_10_3(self, count):
		'''Judgements of the Just'''
		pass

	def protection_11_2(self, count):
		'''Hammer of the Righteous'''
		pass

	def retribution_1_2(self, count):
		'''Deflection'''
		pass

	def retribution_1_3(self, count):
		'''Benediction'''
		pass
	
	def retribution_2_1(self, count):
		'''Improved Judgement'''
		pass
	
	def retribution_2_2(self, count):
		'''Heart of the Crusader'''
		pass
	
	def retribution_2_3(self, count):
		'''Improved Blessing of Might'''
		pass

	def retribution_3_1(self, count):
		'''Vindication'''
		pass

	def retribution_3_2(self, count):
		'''Conviction'''
		# todo increase critical of all spell and attack
		#self.
		pass
	
	def retribution_3_3(self, count):
		'''Seal of Command'''
		pass
	
	def retribution_3_4(self, count):
		'''Pursuit of Justice'''
		pass
	
	def retribution_4_1(self, count):
		'''Eye for an Eye'''
		pass

	def retribution_4_3(self, count):
		'''Sanctity of Battle'''
		assert count in (0, 1, 2, 3)
		# todo increase critical of all spell and attack
		self.physic_abilities['Exorcism'].specific_amount_increase += 0.05 * count
		self.physic_abilities['Crusader Strike'].specific_amount_increase += 0.05 * count
	
	def retribution_4_4(self, count):
		'''Crusade'''
		# addition 1% per-count to Humanoid/Undead/Elementals
		assert count in (0, 1, 2, 3)
		self.spell_amount_increase['all_dmg'] += 0.01 * count
		self.physic_amount_increase['melee'] += 0.01 * count
		self.physic_amount_increase['ranged'] += 0.01 * count
	
	def retribution_5_1(self, count):
		'''Two-Handed Weapon Specialization'''
		# todo apply to what kind of ability?
		pass
	
	def retribution_5_3(self, count):
		'''Sanctified Retribution'''
		pass

	def retribution_6_2(self, count):
		'''Vengeance'''
		pass

	def retribution_6_3(self, count):
		'''Divine Purpose'''
		pass
	
	def retribution_7_1(self, count):
		'''The Art of War'''
		assert count in (0, 1, 2)
		self.physic_abilities['Judgement'].specific_amount_increase += 0.05 * count
		self.physic_abilities['Crusader Strike'].specific_amount_increase += 0.05 * count
		self.physic_abilities['Divine Storm'].specific_amount_increase += 0.05 * count
	
	def retribution_7_2(self, count):
		'''Repentance'''
		pass
	
	def retribution_7_3(self, count):
		'''Judgements of the Wise'''
		pass

	def retribution_8_2(self, count):
		'''Fanaticism'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Judgement'].specific_critical_increase += 0.06 * count
	
	def retribution_8_3(self, count):
		'''Sanctified Wrath'''
		assert count in (0, 1, 2)
		self.physic_abilities['Hammer of Wrath'].specific_critical_increase += 0.25 * count
	
	def retribution_9_1(self, count):
		'''Swift Retribution'''
		pass
	
	def retribution_9_2(self, count):
		'''Crusader Strike'''
		pass

	def retribution_9_3(self, count):
		'''Sheath of Light'''
		pass

	def retribution_10_2(self, count):
		'''Righteous Vengeance'''
		pass

	def retribution_11_2(self, count):
		'''Divine Storm'''
		pass
	


class Paladin(Attribute, PaladinTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.spell_abilities = OrderedDict()
		with open('ability_data/paladin_spell_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				self.spell_abilities[item['ability_name']] = Spell_ability(item)

		self.physic_abilities = OrderedDict()
		with open('ability_data/paladin_physic_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
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
						res_str = 'holy_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'protection_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'retribution_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Paladin, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spell abilities
		for ability in self.spell_abilities.values():
			ability.calculate_amount(self.spell_basic_attr, self.spell_critical_increase, self.spell_amount_increase)
		# calculate amount of physic abilities
		for ability in self.physic_abilities.values():
			ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)



