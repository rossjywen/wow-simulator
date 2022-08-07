import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Spell_ability


class PriestTalent():
	def __init__(self):
		pass

	def discipline_1_2(self, count):
		'''Unbreakalbe Will'''
		pass

	def discipline_1_3(self, count):
		'''Twin Disciplines'''
		# todo influence DOT?
		pass

	def discipline_2_1(self, count):
		'''Silent Resolve'''
		pass

	def discipline_2_2(self, count):
		'''Improved Inner Fire'''
		pass

	def discipline_2_3(self, count):
		'''Improved Power Word: Fortitude'''
		pass

	def discipline_2_4(self, count):
		'''Martydom'''
		pass

	def discipline_3_1(self, count):
		'''Meditation'''
		pass

	def discipline_3_2(self, count):
		'''Inner Forcus'''
		pass

	def discipline_3_3(self, count):
		'''Improved Power Word: Shield'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Power Word: Shield'].specific_amount_increase += 0.05 * count

	def discipline_4_1(self, count):
		'''Absolution'''
		pass

	def discipline_4_2(self, count):
		'''Mental Agility'''
		pass

	def discipline_4_4(self, count):
		'''Improved Mana Burn'''
		# Mana Burn real effect cann't be calculated so I ignore this ability
		pass

	def discipline_5_1(self, count):
		'''Reflective Shield'''
		pass

	def discipline_5_2(self, count):
		'''Mental Strength'''
		pass

	def discipline_5_3(self, count):
		'''Soul Warding'''
		pass

	def discipline_6_1(self, count):
		'''Focus Power'''
		assert count in (0, 1, 2)
		# todo need fix all-dmg need add 'absorb'
		self.spell_amount_increase['all_dmg'] += 0.02 * count
		self.spell_amount_increase['all_heal'] += 0.02 * count

	def discipline_6_3(self, count):
		'''Enlightenment'''
		# todo it is not addition on 'spell_haste'
		assert count in (0, 1, 2, 3)
		self.spell_basic_attr['spell_haste'] += 0.02 * count

	def discipline_7_1(self, count):
		'''Focused Will'''
		assert count in (0, 1, 2, 3)
		self.spell_basic_attr['spell_critical'] += 0.01 * count

	def discipline_7_2(self, count):
		'''Power Infusion'''
		pass

	def discipline_7_3(self, count):
		'''Improved Flash Heal'''
		pass	# cannt simulate these effects based on the status of target

	def discipline_8_1(self, count):
		'''Renewed Hope'''
		pass	# cannt simulate these effects based on the status of target

	def discipline_8_2(self, count):
		'''Rapture'''
		pass

	def discipline_8_3(self, count):
		'''Aspiration'''
		pass

	def discipline_9_1(self, count):
		'''Devine Aegis'''
		pass

	def discipline_9_2(self, count):
		'''Pain Suppression'''
		pass

	def discipline_9_3(self, count):
		'''Grace'''
		pass

	def discipline_10_2(self, count):
		'''Borrowed Time'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Power Word: Shield'].direct_coefficient += 0.08 * count

	def discipline_11_2(self, count):
		'''Penance'''
		pass

	def holy_1_1(self, count):
		'''Healing Focus'''
		pass

	def holy_1_2(self, count):
		'''Improved Renew'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Renew'].specific_amount_increase += 0.05 * count
	
	def holy_1_3(self, count):
		'''Holy Specialization'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_critical_increase['holy'] += 0.01 * count
	
	def holy_2_2(self, count):
		'''Spell Warding'''
		pass
	
	def holy_2_3(self, count):
		'''Devine Fury'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Smite'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Holy Fire'].modified_panel_cast_time -= 0.1 * count
		self.spell_abilities['Greater Heal'].modified_panel_cast_time -= 0.1 * count

	def holy_3_1(self, count):
		'''Desperate Prayer'''
		pass

	def holy_3_2(self, count):
		'''Blessed Recovery'''
		pass
	
	def holy_3_4(self, count):
		'''Inspiration'''
		pass
	
	def holy_4_1(self, count):
		'''Holy Reach'''
		pass
	
	def holy_4_2(self, count):
		'''Improved Healing'''
		pass

	def holy_4_3(self, count):
		'''Searing Light'''
		assert count in (0, 1, 2)
		self.spell_abilities['Smite'].specific_amount_increase += 0.05 * count
		self.spell_abilities['Holy Fire'].specific_amount_increase += 0.05 * count
		self.spell_abilities['Holy Nova (dmg)'].specific_amount_increase += 0.05 * count
		self.spell_abilities['Penance (dmg)'].specific_amount_increase += 0.05 * count

	def holy_5_1(self, count):
		'''Healing Prayers'''
		pass
	
	def holy_5_2(self, count):
		'''Spirit of Redemption'''
		pass
	
	def holy_5_3(self, count):
		'''Spiritual Guidance'''
		pass
	
	def holy_6_1(self, count):
		'''Surge of Light'''
		pass

	def holy_6_3(self, count):
		'''Spiritual Healing'''
		assert count in (0, 1, 2, 3, 4, 5)
		for spell in self.spell_abilities.values():
			if spell.nature == 'heal':
				spell.specific_amount_increase += 0.05 * count

	def holy_7_1(self, count):
		'''Holy Concentration'''
		pass
	
	def holy_7_2(self, count):
		'''Lightwell'''
		pass
	
	def holy_7_3(self, count):
		'''Blessed Resilience'''
		assert count in (0, 1, 2, 3)
		for spell in self.spell_abilities.values():
			if spell.nature == 'heal':
				spell.specific_amount_increase += 0.01 * count
	
	def holy_8_1(self, count):
		'''Body and Soul'''
		pass

	def holy_8_2(self, count):
		'''Empowered Healing'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Flash Heal'].direct_coefficient += 0.04 * count
		self.spell_abilities['Binding Heal'].direct_coefficient += 0.04 * count
		self.spell_abilities['Greater Heal'].direct_coefficient += 0.08 * count

	def holy_8_3(self, count):
		'''Serendipity'''
		pass
	
	def holy_9_1(self, count):
		'''Empowered Renew'''	# change Renew from a 'heal-hot' to 'heal-hybrid'
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Renew'].periodic_coefficient += 0.05 * count
		
		self.spell_abilities['Renew'].direct = True
		self.spell_abilities['Renew'].direct_min = 0.05 * count * self.spell_abilities['Renew'].periodic_total
		self.spell_abilities['Renew'].direct_max = self.spell_abilities['Renew'].direct_min
		self.spell_abilities['Renew'].direct_coefficient = (1.5 / 3.5 * 1.88) + 0.05 * count
	
	def holy_9_2(self, count):
		'''Circle of Healing'''
		pass
	
	def holy_9_3(self, count):
		'''Test of Faith'''	# cannt simulate these effects based on the status of target
		pass

	def holy_10_2(self, count):
		'''Divine Providence'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Circle of Healing'].specific_amount_increase += 0.02 * count
		self.spell_abilities['Binding Heal'].specific_amount_increase += 0.02 * count
		self.spell_abilities['Holy Nova (heal)'].specific_amount_increase += 0.02 * count
		self.spell_abilities['Prayer of Healing'].specific_amount_increase += 0.02 * count
		self.spell_abilities['Prayer of Mending'].specific_amount_increase += 0.02 * count

	def holy_11_2(self, count):
		'''Guardian Spirit'''
		pass
	
	def shadow_1_1(self, count):
		'''Spirit Tap'''
		pass

	def shadow_1_2(self, count):
		'''Improved Spirit Tap'''
		pass

	def shadow_1_3(self, count):
		'''Darkness'''
		assert count in (0, 1, 2, 3, 4, 5)
		for sp in self.spell_abilities.values():
			if sp.school == 'shadow':
				sp.specific_amount_increase += 0.02 * count

	def shadow_2_1(self, count):
		'''Shadow Affinity'''
		pass

	def shadow_2_2(self, count):
		'''Improved Shadow Word: Pain'''
		assert count in (0, 1, 2)
		self.spell_abilities['Shadow Word: Pain'].specific_amount_increase += 0.03 * count

	def shadow_2_3(self, count):
		'''Shadow Focus'''
		pass

	def shadow_3_1(self, count):
		'''Improved Psychic Scream'''
		pass

	def shadow_3_2(self, count):
		'''Improved Mind Blast'''
		pass

	def shadow_3_3(self, count):
		'''Mind Flay'''
		pass

	def shadow_4_2(self, count):
		'''Veiled Shadows'''
		pass

	def shadow_4_3(self, count):
		'''Shadow Reach'''
		pass

	def shadow_4_4(self, count):
		'''Shadow Weaving'''
		pass

	def shadow_5_1(self, count):
		'''Silence'''
		pass

	def shadow_5_2(self, count):
		'''Vampiric Embrace'''
		pass

	def shadow_5_3(self, count):
		'''Improved Vampiric Embrace'''
		pass

	def shadow_5_4(self, count):
		'''Focused Mind'''
		pass

	def shadow_6_1(self, count):
		'''Mind Melt'''
		self.spell_abilities['Mind Blast'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Mind Flay'].specific_critical_increase += 0.02 * count
		self.spell_abilities['Mind Sear'].specific_critical_increase += 0.02 * count
		
		self.spell_abilities['Devouring Plague'].specific_critical_increase += 0.03 * count
		self.spell_abilities['Vampiric Touch'].specific_critical_increase += 0.03 * count
		self.spell_abilities['Shadow Word: Pain'].specific_critical_increase += 0.03 * count

	def shadow_6_3(self, count):
		'''Improved Devouring Plague'''	# change Devouring Plague from a 'dmg-dot' to 'dmg-hybrid'
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Devouring Plague'].specific_amount_increase += 0.05 * count
		
		self.spell_abilities['Devouring Plague'].direct = True
		self.spell_abilities['Devouring Plague'].direct_min = 0.1 * count * self.spell_abilities['Devouring Plague'].periodic_total
		self.spell_abilities['Devouring Plague'].direct_max = self.spell_abilities['Devouring Plague'].direct_min
		self.spell_abilities['Devouring Plague'].direct_coefficient = 1.5 / 3.5

	def shadow_7_2(self, count):
		'''Shadowform'''
		assert count in (0, 1)
		if count == 1:
			self.spell_amount_increase['shadow'] += 0.15	# assume all shadow damage done in Shadowform

			self.spell_abilities['Shadow Word: Pain'].critical_bonus = 1
			self.spell_abilities['Shadow Word: Pain'].periodic_can_critical = True

			self.spell_abilities['Devouring Plague'].critical_bonus = 1
			self.spell_abilities['Devouring Plague'].periodic_can_critical = True 
			self.spell_abilities['Devouring Plague'].periodic_can_haste = True 

			self.spell_abilities['Vampiric Touch'].critical_bonus = 1
			self.spell_abilities['Vampiric Touch'].periodic_can_critical = True
			self.spell_abilities['Vampiric Touch'].periodic_can_haste = True

	def shadow_7_3(self, count):
		'''Shadow Power'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.spell_abilities['Mind Blast'].critical_bonus *= 1 + 0.2 * count
		self.spell_abilities['Mind Flay'].critical_bonus *= 1 + 0.2 * count
		self.spell_abilities['Shadow Word: Death'].critical_bonus *= 1 + 0.2 * count

	def shadow_8_1(self, count):
		'''Improved Shadowform'''
		pass

	def shadow_8_3(self, count):
		'''Misery'''
		assert count in (0, 1, 2, 3)
		self.spell_abilities['Mind Blast'].direct_coefficient += 0.05 * count
		self.spell_abilities['Mind Flay'].direct_coefficient += 0.05 * count
		self.spell_abilities['Mind Sear'].direct_coefficient += 0.05 * count

	def shadow_9_1(self, count):
		'''Psychic Horror'''
		pass

	def shadow_9_2(self, count):
		'''Vampiric Touch'''
		pass

	def shadow_9_3(self, count):
		'''Pain and Suffering'''
		pass

	def shadow_10_3(self, count):
		'''Twisted Faith'''	# cannt simulate these effects based on the status of target
		pass

	def shadow_11_2(self, count):
		'''Dispersion'''
		pass


class Priest(Attribute, PriestTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.spell_abilities = OrderedDict()
		with open('ability_data/priest_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				self.spell_abilities[item['ability_name']] = Spell_ability(item)
		
		# initialize attribute
		Attribute.__init__(self, attr_dict)

		# initialize talent
		for depth in range(0, 11):
			for column in range(0, 12):
				if talent_list[depth][column] != None:	
					if column < 4:
						res_str = 'discipline_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'holy_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'shadow_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(Priest, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spells
		for spell in self.spell_abilities.values():
			spell.calculate_amount(self.spell_basic_attr, self.spell_critical_increase, self.spell_amount_increase)



