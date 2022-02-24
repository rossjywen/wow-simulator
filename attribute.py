#!/usr/bin/env python3

from collections import OrderedDict

class Attribute():
	def __init__(self, attribute_info):
		self.spell_basic_attr = OrderedDict()
		if 'spell_power' in attribute_info:
			self.spell_basic_attr['spell_power'] = int(attribute_info['spell_power'])
		if 'intellect' in attribute_info:
			self.spell_basic_attr['intellect'] = int(attribute_info['intellect'])
		if 'spirit' in attribute_info:
			self.spell_basic_attr['spirit'] = int(attribute_info['spirit'])
		if 'spell_haste_rating' in attribute_info:
			self.spell_basic_attr['spell_haste'] = attribute_info['spell_haste_rating'] / 32.79	# first time calculation, may be modified by talent.
		if 'spell_critical_rating' in attribute_info:
			self.spell_basic_attr['spell_critical_rating'] = attribute_info['spell_critical_rating']

		self.spell_critical_increase = OrderedDict()
		self.spell_critical_increase['frost'] = 0  
		self.spell_critical_increase['fire'] = 0
		self.spell_critical_increase['arcane'] = 0
		self.spell_critical_increase['holy'] = 0
		self.spell_critical_increase['shadow'] = 0
		self.spell_critical_increase['nature'] = 0

		self.spell_critical_bonus = OrderedDict()
		self.spell_critical_bonus['frost'] = 0.5
		self.spell_critical_bonus['fire'] = 0.5
		self.spell_critical_bonus['arcane'] = 0.5
		self.spell_critical_bonus['holy'] = 0.5
		self.spell_critical_bonus['shadow'] = 0.5
		self.spell_critical_bonus['nature'] = 0.5

		self.spell_amount_increase = OrderedDict()
		self.spell_amount_increase['frost'] = 0
		self.spell_amount_increase['fire'] = 0
		self.spell_amount_increase['arcane'] = 0
		self.spell_amount_increase['holy'] = 0
		self.spell_amount_increase['shadow'] = 0
		self.spell_amount_increase['nature'] = 0

		# below are attribute of defense
		#if 'armor' in attribute_info:
		#	self.armor = attribute_info['armor']
		#if 'resilience' in attribute_info:
		#	self.resilience = attribute_info['resilience']
		self.damage_reduce = {}
		self.damage_reduce['spell'] = 1
		self.damage_reduce['melee'] = 1



	def __str__(self):
		ret_str = ''
		ret_str += '[spell basic attribute]:\n'
		for k, c in self.spell_basic_attr.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[spell critical increase]:\n'
		for k, c in self.spell_critical_increase.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[spell critical bonus]:\n'
		for k, c in self.spell_critical_bonus.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		return ret_str




#class _melee_attr():
#	def __init__(self, melee_damage, melee_power, melee_speed, melee_critical)
#		self.melee_damage = melee_damage
#		self.melee_power = melee_power
#		self.melee_speed = melee_speed
#		self.melee_critical = melee_critical
#
#	def __str__(self):
#		ret_str = '[melee attr]:\n'
#		ret_str += ' melee_damge: ' + str(self.melee_damage) + '\n'
#		ret_str += ' melee_power: ' + str(self.melee_power) + '\n'
#		ret_str += ' melee_speed: ' + str(self.melee_speed) + '\n'
#		ret_str += ' melee_critical: ' + str(self.melee_critical) + '\n'
#		return ret_str

		

if __name__ == '__main__':
	info = OrderedDict()
	info['spell_power']=3999
	info['intellect']=100
	info['spirit']=500
	info['spell_haste_rating']=2000
	info['spell_critical_rating']=500
	p = Attribute(info)
	print(p)
	

