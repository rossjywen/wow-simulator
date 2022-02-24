#!/usr/bin/env python3

import json
import sys
from collections import OrderedDict

class Spell():
	def __init__(self, spell_info):
		assert isinstance(spell_info, dict)
		# below are based on static data from excel file
		self.spell_name = spell_info['spell_name']
		self.spell_attribute_tags = spell_info['spell_attribute_tags']
		self.panel_cast_time = float(spell_info['panel_cast_time'])	# used to calculate coefficient, won't be modified
		self.direct_property = spell_info['direct_property']
		self.periodic_property = spell_info['periodic_property']
		self.school = spell_info['school']
		self.database_coefficient = spell_info['database_coefficient']

		self.direct_min = None
		self.direct_max = None	# when it is channel, this field possess tick count.
		self._parse_direct_property()

		self.periodic_total = None
		self.periodic_duration = None
		self.periodic_tick_count = None
		self._parse_periodic_property()

		self.nature = ''
		self.direct = False
		self.channel = False
		self.periodic = False
		self.aoe = False
		self.effect = False
		self.fixed = False
		self._parse_spell_attribute()

		self.direct_coefficient = None
		self.periodic_coefficient = None
		self._calculate_coefficient()

		# below are based talent modification
		self.modified_panel_cast_time = self.panel_cast_time	# used to calculate _actual_cast_time 
		self.specific_amount_increase = 0
		self.specific_critical_increase= 0
		self.specific_critical_bonus_increase = 0

		# below are based on calculation
		self._actual_cast_time = None
		self._final_increase = None
		self._final_critical = None
		self._final_critical_bonus = None
		self._amount_noncritical_direct_min = None
		self._amount_noncritical_direct_max = None		# if direct it is max, if channel it is per-tick.
		self._amount_critical_direct_min = None
		self._amount_critical_direct_max = None			# if direct it is max, if channel it is per-tick.
		self._amount_average_direct_min = None
		self._amount_average_direct_max = None			# if direct it is max, if channel it is per-tick.
		self._amount_ps_direct_min = None
		self._amount_ps_direct_max = None				# if direct it is max, if channel it is per-tick.
		self._amount_noncritical_total_periodic = None
		self._amount_noncritical_tick_periodic = None
		self._amount_critical_total_periodic = None
		self._amount_critical_tick_periodic = None
		
	

	def calculate_amount(self, attr_basic, attr_critical_increase, attr_critical_bonus, attr_increase):
		self._calculate_actual_cast_time(attr_basic)
		self._calculate_final(attr_basic, attr_critical_increase, attr_critical_bonus, attr_increase)

		if self.direct == True:				# need to calculate direct part
			self._amount_noncritical_direct_min = (self.direct_min + attr_basic['spell_power'] * self.direct_coefficient) * (1 + self._final_increase)
			self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self._final_critical_bonus)
			self._amount_average_direct_min = self._amount_noncritical_direct_min * (1 - self._final_critical) + self._amount_critical_direct_min * self._final_critical
			self._amount_ps_direct_min = self._amount_noncritical_direct_min / self._actual_cast_time
			if self.channel == False:		# direct spell
				self._amount_noncritical_direct_max = (self.direct_max + attr_basic['spell_power'] * self.direct_coefficient) * (1 + self._final_increase)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self._final_critical_bonus)
				self._amount_average_direct_max = self._amount_noncritical_direct_max * (1 - self._final_critical) + self._amount_critical_direct_max * self._final_critical
				self._amount_ps_direct_max = self._amount_noncritical_direct_max / self._actual_cast_time
			else:							# channel spell
				self._amount_noncritical_direct_max = self._amount_noncritical_direct_min / self.direct_max
				self._amount_critical_direct_max = self._amount_critical_direct_min / self.direct_max
				self._amount_average_direct_max = self._amount_average_direct_min / self.direct_max
				self._amount_ps_direct_max = self._amount_ps_direct_min / self.direct_max
		if self.periodic == True:			# need to calculate periodic part
			self._amount_noncritical_total_periodic = (self.periodic_total + attr_basic['spell_power'] * self.periodic_coefficient) * (1 + self._final_increase)
			self._amount_noncritical_tick_periodic = self._amount_noncritical_total_periodic / self.periodic_tick_count
			self._amount_critical_total_periodic = self._amount_noncritical_total_periodic * self._final_critical_bonus
			self._amount_critical_tick_periodic = self._amount_critical_total_periodic / self.periodic_tick_count

	
	def _calculate_final(self, attr_basic, attr_critical_increase, attr_critical_bonus, attr_increase):
		self._final_increase = attr_increase[self.school] + self.specific_amount_increase
		self._final_critical = (attr_basic['intellect'] / 166.6667 + attr_basic['spell_critical_rating'] / 45.91 + attr_critical_increase[self.school]) / 100 + self.specific_critical_increase
		self._final_critical_bonus = attr_critical_bonus[self.school] + self.specific_critical_bonus_increase
		# todo class constant


	def _calculate_actual_cast_time(self, attr_basic):
		if self.panel_cast_time == 0:
			self._actual_cast_time = 1.5 / (1 + attr_basic['spell_haste'])	# equal to GCD
		else:
			self._actual_cast_time = self.modified_panel_cast_time / (1 + attr_basic['spell_haste'])


	def _parse_direct_property(self):
		if self.direct_property == None:
			pass
		else:
			tmp = self.direct_property.split('-')
			self.direct_min = int(tmp[0])
			self.direct_max = int(tmp[1])

	def _parse_periodic_property(self):
		if self.periodic_property == None:
			pass
		else:
			tmp = self.periodic_property.split('-')
			self.periodic_total = int(tmp[0])
			self.periodic_duration = int(tmp[1])
			self.periodic_tick_count = int(tmp[2])
	
	def _parse_spell_attribute(self):
		attrs = self.spell_attribute_tags.split('-')
		for att_item in attrs:
			#print(att_item)
			# dmg heal absorb direct channel dot hot hybrid aoe effect fixed
			if att_item == 'dmg':
				self.nature = 'dmg'
			elif att_item == 'heal':
				self.nature = 'heal'
			elif att_item == 'absorb':
				self.nature = 'absorb'
			elif att_item == 'direct':
				self.direct = True
			elif att_item == 'channel':
				self.direct = True
				self.channel = True
			elif att_item == 'dot':
				self.periodic = True
			elif att_item == 'hot':
				self.periodic = True
			elif att_item == 'hybrid':
				self.direct = True
				self.periodic = True
			elif att_item == 'aoe':
				self.aoe = True
			elif att_item == 'effect':
				self.effect = True
			elif att_item == 'fixed':
				self.fixed = True
			else:
				assert True, 'unknown tag'

	def _calculate_coefficient(self):
		if self.fixed == True:
			if self.nature == 'absorb':
				self.direct_coefficient = float(self.database_coefficient)
			else:
				if self.direct == True and self.periodic == True:
					tmp = self.database_coefficient.split('-')
					self.direct_coefficient = float(tmp[0])
					self.periodic_coefficient = float(tmp[1])
				else:
					if self.direct == True:
						self.direct_coefficient = float(self.database_coefficient)
					if self.periodic == True:
						self.periodic_coefficient = float(self.database_coefficient)
		else:
			if self.direct == True and self.periodic == False:		# direct
				if self.panel_cast_time < 1.5:
					self.direct_coefficient = 1.5 / 3.5
				elif self.panel_cast_time > 7 and self.channel == False:
					self.direct_coefficient = 7 / 3.5
				else:
					self.direct_coefficient = self.panel_cast_time / 3.5
				if self.nature == 'heal':
					self.direct_coefficient *= 1.88
				if self.aoe == True:
					self.direct_coefficient *= 0.5
				if self.effect == True:
					self.direct_coefficient *= 0.95
			elif self.direct == False and self.periodic == True:	# periodic
				self.periodic_coefficient = self.periodic_duration / 15
				if self.nature == 'heal':
					self.periodic_coefficient *= 1.88
			elif self.direct == True and self.periodic == True:		# hybrid
				c_periodic = self.periodic_duration / 15
				if self.panel_cast_time < 1.5:
					c_direct = 1.5 / 3.5
				else:
					c_direct = self.panel_cast_time / 3.5
				self.periodic_coefficient = c_periodic * c_periodic / (c_periodic + c_direct)
				self.direct_coefficient = c_direct * c_direct / (c_periodic + c_direct)
			
	def __str__(self):
		ret_str = '[{0}({1})]: \n'.format(self.spell_name, self.spell_attribute_tags)
		ret_str += ' actual cast time: {}\n'.format(self._actual_cast_time)
		ret_str += ' specific amount increase: {}\n'.format(self.specific_amount_increase)
		ret_str += ' final amount increase: {}\n'.format(self._final_increase)
		ret_str += ' specific critical increase: {}\n'.format(self.specific_critical_increase)
		ret_str += ' final critical increase: {}\n'.format(self._final_critical)
		if self.direct_coefficient:
			ret_str += ' direct coefficient: {}\n'.format(self.direct_coefficient)
		if self.periodic_coefficient:
			ret_str += ' periodic coefficient: {}\n'.format(self.periodic_coefficient)
		ret_str += ' database coefficient: {}\n'.format(self.database_coefficient)


		if self.direct == True:
			ret_str += ' [direct amount]:\n'
			if self.channel == False:
				ret_str += '  non critical min: {}\n'.format(self._amount_noncritical_direct_min)
				ret_str += '  non critical max: {}\n'.format(self._amount_noncritical_direct_max)
				ret_str += '  critical min: {}\n'.format(self._amount_critical_direct_min)
				ret_str += '  critical max: {}\n'.format(self._amount_critical_direct_max)
				ret_str += '  average min: {}\n'.format(self._amount_average_direct_min)
				ret_str += '  average max: {}\n'.format(self._amount_average_direct_max)
				ret_str += '  per-second min: {}\n'.format(self._amount_ps_direct_min)
				ret_str += '  per-second max: {}\n'.format(self._amount_ps_direct_max)
			else:
				ret_str += '  non critical: {}\n'.format(self._amount_noncritical_direct_min)
				ret_str += '  non critical per-tick: {}\n'.format(self._amount_noncritical_direct_max)
				ret_str += '  critical: {}\n'.format(self._amount_critical_direct_min)
				ret_str += '  critical per-tick: {}\n'.format(self._amount_critical_direct_max)
				ret_str += '  average: {}\n'.format(self._amount_average_direct_min)
				ret_str += '  average per-tick: {}\n'.format(self._amount_average_direct_max)
				ret_str += '  per-second: {}\n'.format(self._amount_ps_direct_min)
				ret_str += '  per-second per-tick: {}\n'.format(self._amount_ps_direct_max)

		if self.periodic == True:
			ret_str += ' [periodic amount]:\n'
			ret_str += '  non critical total: {}\n'.format(self._amount_noncritical_total_periodic)
			ret_str += '  non critical per-tick: {}\n'.format(self._amount_noncritical_tick_periodic)

		return ret_str





if __name__ == '__main__':
	with open(sys.argv[1]) as fobj:
		json_content = fobj.read()
		content = json.loads(json_content)

	for item in content:
		spl = Spell(item)
		print(spl)



