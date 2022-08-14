#!/usr/bin/env python3

import csv
import sys
from collections import OrderedDict

class Spell_ability():
	def __init__(self, ability_info):
		assert isinstance(ability_info, dict)

		# below are based on static data from csv file
		self.spell_name = ability_info['ability_name']
		self.spell_attribute_tags = ability_info['ability_attribute_tags']
		self.panel_cast_time = float(ability_info['panel_cast_time'])	# used to calculate coefficient, won't be modified
		self.direct_property = ability_info['direct_property']
		self.periodic_property = ability_info['periodic_property']
		self.school = ability_info['school']
		self.database_coefficient = ability_info['database_coefficient']

		self.direct_min = None
		self.direct_max = None	# when it is channel, this field possess tick count.
		self._parse_direct_property()

		self.periodic_total = 0
		self.periodic_duration = 0
		self.periodic_tick_count = 0
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

		self.periodic_can_critical = False
		self.periodic_can_haste = False

		# below are based talent modification
		self.modified_panel_cast_time = self.panel_cast_time	# used to calculate _actual_cast_time 
		self.specific_amount_increase = 0
		self.specific_critical_increase = 0
		self.critical_bonus = 0.5

		# below are based on calculation
		self._actual_cast_time = 0
		self._final_increase = 0
		self._final_critical = 0
		self._amount_noncritical_direct_min = 0
		self._amount_noncritical_direct_max = 0		# if direct it is max, if channel it is per-tick.
		self._amount_critical_direct_min = 0
		self._amount_critical_direct_max = 0			# if direct it is max, if channel it is per-tick.
		self._amount_average_direct_min = 0
		self._amount_average_direct_max = 0			# if direct it is max, if channel it is per-tick.
		self._amount_ps_direct_min = 0
		self._amount_ps_direct_max = 0				# if direct it is max, if channel it is per-tick.
		self._amount_noncritical_total_periodic = 0
		self._amount_noncritical_tick_periodic = 0
		self._amount_critical_total_periodic = 0
		self._amount_critical_tick_periodic = 0
		self._periodic_duration = 0
		self._periodic_duration_tick = 0
		
	

	def calculate_amount(self, attr_basic, attr_critical_increase, attr_increase):
		self._calculate_actual_cast_time(attr_basic)
		self._calculate_final(attr_basic, attr_critical_increase, attr_increase)

		if self.direct == True:				# need to calculate direct part
			self._amount_noncritical_direct_min = (self.direct_min + attr_basic['spell_power'] * self.direct_coefficient) * self._final_increase
			self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
			self._amount_average_direct_min = self._amount_noncritical_direct_min * (1 - self._final_critical) + self._amount_critical_direct_min * self._final_critical
			self._amount_ps_direct_min = self._amount_noncritical_direct_min / self._actual_cast_time
			if self.channel == False:		# direct spell
				self._amount_noncritical_direct_max = (self.direct_max + attr_basic['spell_power'] * self.direct_coefficient) * self._final_increase
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
				self._amount_average_direct_max = self._amount_noncritical_direct_max * (1 - self._final_critical) + self._amount_critical_direct_max * self._final_critical
				self._amount_ps_direct_max = self._amount_noncritical_direct_max / self._actual_cast_time
			else:							# channel spell
				self._amount_noncritical_direct_max = self._amount_noncritical_direct_min / self.direct_max
				self._amount_critical_direct_max = self._amount_critical_direct_min / self.direct_max
				self._amount_average_direct_max = self._amount_average_direct_min / self.direct_max
				self._amount_ps_direct_max = self._amount_ps_direct_min / self.direct_max
		if self.periodic == True:			# need to calculate periodic part
			self._amount_noncritical_total_periodic = (self.periodic_total + attr_basic['spell_power'] * self.periodic_coefficient) * self._final_increase
			self._amount_noncritical_tick_periodic = self._amount_noncritical_total_periodic / self.periodic_tick_count
			self._amount_critical_total_periodic = self._amount_noncritical_total_periodic * (1 + self.critical_bonus)
			self._amount_critical_tick_periodic = self._amount_critical_total_periodic / self.periodic_tick_count

	
	def _calculate_final(self, attr_basic, attr_critical_increase, attr_increase):
		if self.nature == 'dmg':
			self._final_increase = (1 + self.specific_amount_increase) * (1 + attr_increase[self.school]) * (1 + attr_increase['all_dmg'])
		elif self.nature == 'heal':
			self._final_increase = (1 + self.specific_amount_increase) * (1 + attr_increase[self.school]) * (1 + attr_increase['all_heal'])
		elif self.nature == 'absorb':
			self._final_increase = 1 + self.specific_amount_increase
			self.critical_bonus = 0
	
		self._final_critical = attr_basic['spell_critical'] + attr_critical_increase[self.school] + self.specific_critical_increase


	def _calculate_actual_cast_time(self, attr_basic):
		if self.panel_cast_time == 0:
			self._actual_cast_time = 1.5 / (1 + attr_basic['spell_haste'])	# equal to GCD
		else:
			self._actual_cast_time = self.modified_panel_cast_time / (1 + attr_basic['spell_haste'])
	
		if self.periodic == True:
			if self.periodic_can_haste == True:
				self._periodic_duration = self.periodic_duration / (1 + attr_basic['spell_haste'])
			else:
				self._periodic_duration = self.periodic_duration
			self._periodic_duration_tick = self._periodic_duration / self.periodic_tick_count


	def _parse_direct_property(self):
		if self.direct_property == '':
			pass
		else:
			tmp = self.direct_property.split('-')
			self.direct_min = int(tmp[0])
			self.direct_max = int(tmp[1])

	def _parse_periodic_property(self):
		if self.periodic_property == '':
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
			# dmg heal absorb direct channel dot hot hybrid aoe effect fixed
			if self.nature == 'absorb':
				self.direct_coefficient = float(self.database_coefficient)
			elif self.direct == True and self.periodic == True:
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
				else:	# including (channel & > 7) or (non-channel & < 7)
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
		ret_str += ' actual cast time: {:.2f}\n'.format(self._actual_cast_time)
		ret_str += ' specific amount increase: {:.2f}\n'.format(self.specific_amount_increase)
		ret_str += ' final amount increase: {:.2f}\n'.format(self._final_increase)
		ret_str += ' specific critical increase: {:.2f}\n'.format(self.specific_critical_increase)
		ret_str += ' final critical increase: {:.4f}\n'.format(self._final_critical)
		ret_str += ' critical bonus: {:.2f}\n'.format(self.critical_bonus)
		if self.direct_coefficient:
			ret_str += ' direct coefficient: {:.4f}\n'.format(self.direct_coefficient)
		if self.periodic_coefficient:
			ret_str += ' periodic coefficient: {:.4f}\n'.format(self.periodic_coefficient)
		ret_str += ' database coefficient: {}\n'.format(self.database_coefficient)


		if self.direct == True:
			ret_str += ' [direct amount]:\n'
			if self.channel == False:
				ret_str += '  non critical min: {:.0f}\n'.format(self._amount_noncritical_direct_min)
				ret_str += '  non critical max: {:.0f}\n'.format(self._amount_noncritical_direct_max)
				ret_str += '  critical min: {:.0f}\n'.format(self._amount_critical_direct_min)
				ret_str += '  critical max: {:.0f}\n'.format(self._amount_critical_direct_max)
				ret_str += '  average min: {:.0f}\n'.format(self._amount_average_direct_min)
				ret_str += '  average max: {:.0f}\n'.format(self._amount_average_direct_max)
				ret_str += '  per-second min: {:.0f}\n'.format(self._amount_ps_direct_min)
				ret_str += '  per-second max: {:.0f}\n'.format(self._amount_ps_direct_max)
			else:
				ret_str += '  non critical: {:.0f}\n'.format(self._amount_noncritical_direct_min)
				ret_str += '  non critical per-tick: {:.0f}\n'.format(self._amount_noncritical_direct_max)
				ret_str += '  critical: {:.0f}\n'.format(self._amount_critical_direct_min)
				ret_str += '  critical per-tick: {:.0f}\n'.format(self._amount_critical_direct_max)
				ret_str += '  average: {}\n'.format(self._amount_average_direct_min)
				ret_str += '  average per-tick: {:.0f}\n'.format(self._amount_average_direct_max)
				ret_str += '  per-second: {}\n'.format(self._amount_ps_direct_min)
				ret_str += '  per-second per-tick: {:.0f}\n'.format(self._amount_ps_direct_max)

		if self.periodic == True:
			if self.periodic_can_critical == True:
				ret_str += ' [periodic amount (can critical hit)]:\n'
			else:
				ret_str += ' [periodic amount]:\n'
			ret_str += '  non critical total: {:.0f}\n'.format(self._amount_noncritical_total_periodic)
			ret_str += '  duration total: {:.2f}\n'.format(self._periodic_duration)
			ret_str += '  non critical per-tick: {:.0f}\n'.format(self._amount_noncritical_tick_periodic)
			if self.periodic_can_critical == True:
				ret_str += '  critical per-tick: {:.0f}\n'.format(self._amount_critical_tick_periodic)
			ret_str += '  duration per-tick: {:.2f}\n'.format(self._periodic_duration_tick)

		return ret_str



class Physic_ability():
	def __init__(self, ability_info):
		# below are based on static data from csv file
		self.physic_name = ability_info['ability_name']
		self.physic_type = ability_info['ability_type']
		self.physic_attribute_tags = ability_info['ability_attribute_tags']
		self.weapon_property = ability_info['weapon_property']
		self.attackpower_property = ability_info['attackpower_property']
		self.school = ability_info['school']
		self.nature = 'dmg'	# 'heal' in tags will override this

		# below are based on parsing
		self.ap = False
		self.ap_direct = False
		self.ap_dot = False
		
		self.wp = False
		self.wp_nonnorm = False
		self.wp_norm = False
		self.wp_base = False
		
		self._parse_attribute_tags()
		
		self.wp_hand = None
		self.wp_coefficient = None
		self.wp_const_min = None
		self.wp_const_max = None
		self.ap_coefficient = None
		self.ap_const_min = None
		self.ap_const_max = None
		self.periodic_const = None
		self.periodic_duration = 0
		self.periodic_tick_count = 0
		
		self._parse_property()
		
		# below are based on talent modification
		self.specific_amount_increase = 0
		self.specific_critical_increase = 0
		if self.wp == True or self.ap_direct == True:	# according to wow-wiki
			self.critical_bonus = 1 					# 100% bonus physical damage that occurs as a result of an attack made with melee or ranged weapons
		else:
			self.critical_bonus = 0.5
		
		# below are based on calculation
		self._final_increase = 0
		self._final_critical = 0

		self._amount_noncritical_direct_min = 0
		self._amount_noncritical_direct_max = 0
		self._amount_critical_direct_min = 0
		self._amount_critical_direct_max = 0
		#self._amount_average_direct_min = 0	# todo average
		#self._amount_average_direct_max = 0
		self._periodic_total = 0	# no physic-dot can be critical hit
		self._periodic_tick = 0
		self._periodic_tick_time = 0

	

	def _parse_attribute_tags(self):
		attrs = self.physic_attribute_tags.split('-')
		for attr in attrs:
			if attr == 'wp':
				self.wp = True
			elif attr == 'ap':
				self.ap = True
			elif attr == 'direct':
				self.ap_direct = True
			elif attr == 'dot':
				self.ap_dot = True
			elif attr == 'nonnorm':
				self.wp_nonnorm = True
			elif attr == 'norm':
				self.wp_norm = True
			elif attr == 'base':
				self.wp_base = True
			elif attr == 'heal':
				self.nature = 'heal'
		

	def _parse_property(self):
		if self.wp == True:
			tmp = self.weapon_property.split('-')
			self.wp_hand = tmp[0]
			self.wp_coefficient = float(tmp[1])
			self.wp_const_min = int(tmp[2])
			self.wp_const_max = int(tmp[3])

		if self.ap == True:
			if self.ap_direct == True:
				tmp = self.attackpower_property.split('-')
				self.ap_coefficient = float(tmp[0])
				self.ap_const_min = int(tmp[1])
				self.ap_const_max = int(tmp[2])
			elif self.ap_dot == True:
				tmp = self.attackpower_property.split('-')
				self.ap_coefficient = float(tmp[0])
				self.periodic_const = int(tmp[1])
				self.periodic_duration = int(tmp[2])
				self.periodic_tick_count = int(tmp[3])
	

	def _calculate_final(self, attr_basic, attr_amount_increase):
		if self.wp == True or self.ap_direct == True:
			self._final_increase = (1 + self.specific_amount_increase) * (1 + attr_amount_increase[self.school]) * (1 + attr_amount_increase[self.physic_type])
		else:
			self._final_increase = (1 + self.specific_amount_increase) * (1 + attr_amount_increase[self.school])
		
		if self.physic_type == 'melee':
			self._final_critical = attr_basic['melee_critical'] + self.specific_critical_increase
		elif self.physic_type == 'ranged':
			self._final_critical = attr_basic['ranged_critical'] + self.specific_critical_increase
		
	
	def calculate_amount(self, attr_basic, attr_amount_increase, main_melee_weapon, off_melee_weapon, ranged_weapon):
		self._calculate_final(attr_basic, attr_amount_increase)
		if self.physic_type == 'melee':
			# weapon part
			if self.wp_nonnorm == True:
				if self.wp_hand == 'main':
					self._amount_noncritical_direct_min = (main_melee_weapon['non_norm_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
					self._amount_noncritical_direct_max = (main_melee_weapon['non_norm_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				elif self.wp_hand == 'off':
					self._amount_noncritical_direct_min = (off_melee_weapon['non_norm_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
					self._amount_noncritical_direct_max = (off_melee_weapon['non_norm_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			elif self.wp_norm == True:
				if self.wp_hand == 'main':
					self._amount_noncritical_direct_min = (main_melee_weapon['norm_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
					self._amount_noncritical_direct_max = (main_melee_weapon['norm_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				elif self.wp_hand == 'off':
					self._amount_noncritical_direct_min = (off_melee_weapon['norm_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
					self._amount_noncritical_direct_max = (off_melee_weapon['norm_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			elif self.wp_base == True:
				if self.wp_hand == 'main':
					self._amount_noncritical_direct_min = (main_melee_weapon['base_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
					self._amount_noncritical_direct_max = (main_melee_weapon['base_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				elif self.wp_hand == 'off':
					self._amount_noncritical_direct_min = (off_melee_weapon['base_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
					self._amount_noncritical_direct_max = (off_melee_weapon['base_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			# attackpower part
			if self.ap_direct == True:
				self._amount_noncritical_direct_min += (attr_basic['melee_attack_power'] * self.ap_coefficient + self.ap_const_min) * self._final_increase
				self._amount_noncritical_direct_max += (attr_basic['melee_attack_power'] * self.ap_coefficient + self.ap_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			elif self.ap_dot == True:
				self._periodic_total = (attr_basic['melee_attack_power'] * self.ap_coefficient + self.periodic_const) * self._final_increase
				self._periodic_tick = self._periodic_total / self.periodic_tick_count
				self._periodic_tick_time = self.periodic_duration / self.periodic_tick_count
		elif self.physic_type == 'ranged':	# ranged weapon is unique, not like melee weapon.
			# weapon part
			if self.wp_nonnorm == True:
				self._amount_noncritical_direct_min = (ranged_weapon['non_norm_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
				self._amount_noncritical_direct_max = (ranged_weapon['non_norm_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			elif self.wp_norm == True:
				self._amount_noncritical_direct_min = (ranged_weapon['norm_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
				self._amount_noncritical_direct_max = (ranged_weapon['norm_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			elif self.wp_base == True:
				self._amount_noncritical_direct_min = (ranged_weapon['base_dmg_min'] * self.wp_coefficient + self.wp_const_min) * self._final_increase
				self._amount_noncritical_direct_max = (ranged_weapon['base_dmg_max'] * self.wp_coefficient + self.wp_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			# attackpower part
			if self.ap_direct == True:
				self._amount_noncritical_direct_min +=  (attr_basic['ranged_attack_power'] * self.ap_coefficient + self.ap_const_min) * self._final_increase
				self._amount_noncritical_direct_max +=  (attr_basic['ranged_attack_power'] * self.ap_coefficient + self.ap_const_max) * self._final_increase
				self._amount_critical_direct_min = self._amount_noncritical_direct_min * (1 + self.critical_bonus)
				self._amount_critical_direct_max = self._amount_noncritical_direct_max * (1 + self.critical_bonus)
			elif self.ap_dot == True:
				self._periodic_total = (attr_basic['ranged_attack_power'] * self.ap_coefficient + self.periodic_const) * self._final_increase
				self._periodic_tick = self._periodic_total / self.periodic_tick_count
				self._periodic_tick_time = self.periodic_duration / self.periodic_tick_count


	def __str__(self):
		ret_str = '[{0} ({1})]: \n'.format(self.physic_name, self.physic_attribute_tags)
		ret_str += ' specific amount increase: {:.2f}\n'.format(self.specific_amount_increase)
		ret_str += ' final amount increase: {:.6f}\n'.format(self._final_increase)
		ret_str += ' specific critical increase: {:.2f}\n'.format(self.specific_critical_increase)
		ret_str += ' final critical increase: {:.2f}\n'.format(self._final_critical)
		ret_str += ' critical bonus: {:.2f}\n'.format(self.critical_bonus)
		
		if self.wp == True:
			ret_str += ' [weapon amount]:\n'
			ret_str += '  non critical min: {:.0f}\n'.format(self._amount_noncritical_direct_min)
			ret_str += '  non critical max: {:.0f}\n'.format(self._amount_noncritical_direct_max)
			ret_str += '  critical min: {:.0f}\n'.format(self._amount_critical_direct_min)
			ret_str += '  critical max: {:.0f}\n'.format(self._amount_critical_direct_max)
		
		if self.ap == True:
			ret_str += ' [attack amount]:\n'
			if self.ap_direct == True:
				ret_str += '  non critical min: {:.0f}\n'.format(self._amount_noncritical_direct_min)
				ret_str += '  non critical max: {:.0f}\n'.format(self._amount_noncritical_direct_max)
				ret_str += '  critical min: {:.0f}\n'.format(self._amount_critical_direct_min)
				ret_str += '  critical max: {:.0f}\n'.format(self._amount_critical_direct_max)
			elif self.ap_dot == True:
				ret_str += '  total dmg: {:.0f}\n'.format(self._periodic_total)
				ret_str += '  per-tick dmg: {:.0f}\n'.format(self._periodic_tick)
				ret_str += '  per-tick-time: {:.0f}\n'.format(self._periodic_tick_time)
		return ret_str
		

if __name__ == '__main__':
	with open(sys.argv[1], encoding="utf-8-sig", mode='r') as fobj:
		content = csv.DictReader(fobj)
		for item in content:
			#spl = Spell_ability(item)
			#print('[{0}({1})]: \n'.format(spl.spell_name, spl.spell_attribute_tags))
			phy = Physic_ability(item)
			print(phy)
			#print('[{0}({1})]: \n'.format(phy.physic_name, phy.physic_attribute_tags))



