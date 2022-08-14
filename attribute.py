#!/usr/bin/env python3

from collections import OrderedDict

class Attribute():
	def __init__(self, attribute_info):
		# -------------------- spell part start --------------------
		self.spell_basic_attr = OrderedDict()

		if 'spell_power' in attribute_info:
			self.spell_basic_attr['spell_power'] = int(attribute_info['spell_power'])
		else:
			print("spell power does not exist")

		if 'spell_haste' in attribute_info:
			self.spell_basic_attr['spell_haste'] = float(attribute_info['spell_haste'])
			assert self.spell_basic_attr['spell_haste'] < 1, "haste > 1"
		else:
			print("spell haste does not exist")

		if 'spell_critical' in attribute_info:
			self.spell_basic_attr['spell_critical'] = float(attribute_info['spell_critical'])
			assert self.spell_basic_attr['spell_critical'] < 1, "critical > 1"
		else:
			print("spell critical does not exist")

		
		self.spell_critical_increase = OrderedDict()
		self.spell_critical_increase['absorb'] = 0  
		self.spell_critical_increase['frost'] = 0  
		self.spell_critical_increase['fire'] = 0
		self.spell_critical_increase['arcane'] = 0
		self.spell_critical_increase['holy'] = 0
		self.spell_critical_increase['shadow'] = 0
		self.spell_critical_increase['nature'] = 0

		self.spell_amount_increase = OrderedDict()
		self.spell_amount_increase['all_dmg'] = 0
		self.spell_amount_increase['all_heal'] = 0
		self.spell_amount_increase['absorb'] = 0
		self.spell_amount_increase['frost'] = 0
		self.spell_amount_increase['fire'] = 0
		self.spell_amount_increase['arcane'] = 0
		self.spell_amount_increase['holy'] = 0
		self.spell_amount_increase['shadow'] = 0
		self.spell_amount_increase['nature'] = 0
		# -------------------- spell part end --------------------


		# -------------------- physic part start --------------------
		self.physic_basic_attr = OrderedDict()
		
		if 'melee_attack_power' in attribute_info:
			self.physic_basic_attr['melee_attack_power'] = int(attribute_info['melee_attack_power'])
		else:
			print('melee AP does not exist')

		if 'melee_critical' in attribute_info:
			self.physic_basic_attr['melee_critical'] = float(attribute_info['melee_critical'])
		else:
			print('melee critical does not exist')

		# no class use melee haste in PVP so I currently ignore haste

		if 'ranged_attack_power' in attribute_info:
			self.physic_basic_attr['ranged_attack_power'] = int(attribute_info['ranged_attack_power'])
		else:
			print('ranged AP does not exist')

		if 'ranged_critical' in attribute_info:
			self.physic_basic_attr['ranged_critical'] = float(attribute_info['ranged_critical'])
		else:
			print('ranged critical does not exist')

		self.physic_amount_increase = OrderedDict()
		self.physic_amount_increase['all_dmg'] = 0

		self.physic_amount_increase['melee'] = 0	# for melee weapon
		self.physic_amount_increase['ranged'] = 0	# for ranged weapon

		self.physic_amount_increase['physical'] = 0
		
		self.physic_amount_increase['absorb'] = 0

		self.physic_amount_increase['frost'] = 0
		self.physic_amount_increase['fire'] = 0
		self.physic_amount_increase['arcane'] = 0
		self.physic_amount_increase['holy'] = 0
		self.physic_amount_increase['shadow'] = 0
		self.physic_amount_increase['nature'] = 0

		
		self.main_melee_weapon = OrderedDict()
		if 'main_melee_weapon' in attribute_info and attribute_info['main_melee_weapon'] != None:
			tmp = attribute_info['main_melee_weapon'].split('-')
			self.main_melee_weapon['type'] = tmp[0]
			self.main_melee_weapon['speed'] = float(tmp[1])
			self.main_melee_weapon['base_dmg_min'] = int(tmp[2])
			self.main_melee_weapon['base_dmg_max'] = int(tmp[3])
			self._calculate_main_hand_weapon()

		self.off_melee_weapon = OrderedDict()
		if 'off_melee_weapon' in attribute_info and attribute_info['off_melee_weapon'] != None:
			tmp = attribute_info['off_melee_weapon'].split('-')
			self.off_melee_weapon['type'] = tmp[0]
			self.off_melee_weapon['speed'] = float(tmp[1])
			self.off_melee_weapon['base_dmg_min'] = int(tmp[2])
			self.off_melee_weapon['base_dmg_max'] = int(tmp[3])
			self._calculate_off_hand_weapon()
		
		self.ranged_weapon = OrderedDict()
		if 'ranged_weapon' in attribute_info and attribute_info['ranged_weapon'] != None:
			tmp = attribute_info['ranged_weapon'].split('-')
			self.ranged_weapon['type'] = tmp[0]
			self.ranged_weapon['speed'] = float(tmp[1])
			self.ranged_weapon['base_dmg_min'] = int(tmp[2])
			self.ranged_weapon['base_dmg_max'] = int(tmp[3])
			if 'ammo_dps' in attribute_info:
				self.ammo_dps = float(attribute_info['ammo_dps'])
			else:
				self.ammo_dps = 0
				print('ammo dps does not exist')
			self._calculate_ranged_weapon()
		# -------------------- physic part end --------------------

	def _calculate_main_hand_weapon(self):
		assert self.main_melee_weapon['type'] in ('dager', 'one_hand', 'two_hand')
		# non_norm_weapon_dmg = base_weapon_dmg + (weapon_speed * AP/14)
		self.main_melee_weapon['non_norm_dmg_min'] = self.main_melee_weapon['base_dmg_min'] + (self.main_melee_weapon['speed'] * self.physic_basic_attr['melee_attack_power'] / 14)
		self.main_melee_weapon['non_norm_dmg_max'] = self.main_melee_weapon['base_dmg_max'] + (self.main_melee_weapon['speed'] * self.physic_basic_attr['melee_attack_power'] / 14)
		# norm_weapon_dmg = base_weapon_dmg + (norm_weapon_speed * AP/14)
		if self.main_melee_weapon['type'] == 'dager':
			norm_speed = 1.7
		elif self.main_melee_weapon['type'] == 'one_hand':
			norm_speed = 2.4
		elif self.main_melee_weapon['type'] == 'two_hand':
			norm_speed = 3.3
		self.main_melee_weapon['norm_dmg_min'] = self.main_melee_weapon['base_dmg_min'] + (norm_speed * self.physic_basic_attr['melee_attack_power'] / 14)
		self.main_melee_weapon['norm_dmg_max'] = self.main_melee_weapon['base_dmg_max'] + (norm_speed * self.physic_basic_attr['melee_attack_power'] / 14)

	def _calculate_off_hand_weapon(self):
		assert self.off_melee_weapon['type'] in ('dager', 'one_hand', 'two_hand')
		# non_norm_weapon_dmg = base_weapon_dmg + (weapon_speed * AP/14)
		self.off_melee_weapon['non_norm_dmg_min'] = self.off_melee_weapon['base_dmg_min'] + (self.off_melee_weapon['speed'] * self.physic_basic_attr['melee_attack_power'] / 14)
		self.off_melee_weapon['non_norm_dmg_max'] = self.off_melee_weapon['base_dmg_max'] + (self.off_melee_weapon['speed'] * self.physic_basic_attr['melee_attack_power'] / 14)
		# norm_weapon_dmg = base_weapon_dmg + (norm_weapon_speed * AP/14)
		if off_melee_weapon['type'] == 'dager':
			norm_speed = 1.7
		elif off_melee_weapon['type'] == 'one_hand':
			norm_speed = 2.4
		elif off_melee_weapon['type'] == 'two_head':
			norm_speed = 3.3
		self.off_melee_weapon['norm_dmg_min'] = self.off_melee_weapon['base_dmg_min'] + (norm_speed * self.physic_basic_attr['melee_attack_power'] / 14)
		self.off_melee_weapon['norm_dmg_max'] = self.off_melee_weapon['base_dmg_max'] + (norm_speed * self.physic_basic_attr['melee_attack_power'] / 14)



	def _calculate_ranged_weapon(self):
		# non_norm_weapon_dmg = base_weapon_dmg + (weapon_speed * (ammo_dps + AP/14))
		self.ranged_weapon['non_norm_dmg_min'] = self.ranged_weapon['base_dmg_min'] + (self.ranged_weapon['speed'] * (self.physic_basic_attr['ranged_attack_power'] / 14 + self.ammo_dps))
		self.ranged_weapon['non_norm_dmg_max'] = self.ranged_weapon['base_dmg_max'] + (self.ranged_weapon['speed'] * (self.physic_basic_attr['ranged_attack_power'] / 14 + self.ammo_dps))
		# norm_weapon_dmg = base_weapon_dmg + (norm_weapon_speed * (ammo_dps + AP/14))
		self.ranged_weapon['norm_dmg_min'] = self.ranged_weapon['base_dmg_min'] + (2.8 * (self.physic_basic_attr['ranged_attack_power'] / 14 + self.ammo_dps))
		self.ranged_weapon['norm_dmg_max'] = self.ranged_weapon['base_dmg_max'] + (2.8 * (self.physic_basic_attr['ranged_attack_power'] / 14 + self.ammo_dps))

	def __str__(self):
		ret_str = ''
		# ---------- spell part ----------
		ret_str += '[spell basic attribute]:\n'
		for k, c in self.spell_basic_attr.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[spell amount increase]:\n'
		for k, c in self.spell_amount_increase.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[spell critical increase]:\n'
		for k, c in self.spell_critical_increase.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'

		# ---------- physic part ----------
		ret_str += '[physic basic attribute]:\n'
		for k, c in self.physic_basic_attr.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[main hand weapon attribute]:\n'
		for k, c in self.main_melee_weapon.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[off hand weapon attribute]:\n'
		for k, c in self.off_melee_weapon.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[ranged weapon attribute]:\n'
		for k, c in self.ranged_weapon.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'
		ret_str += '[physic amount increase]:\n'
		for k, c in self.physic_amount_increase.items():
			ret_str += '|-{0}:{1}\n'.format(k, c)
		ret_str += '\n'

		return ret_str




if __name__ == '__main__':
	info = OrderedDict()
	info['spell_critical']= 0.7

	info['ranged_attack_power']= 4934
	info['ranged_weapon'] = 'ranged-3.0-783-1071'
	info['ammo_dps'] = 91.5

	info['melee_attack_power']= 604
	info['main_melee_weapon'] = 'two_hand-2.4-33-51'
	p = Attribute(info)
	print(p)
	

