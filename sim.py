#!/usr/bin/env python3

import sys
import getopt
import json
import csv
from collections import OrderedDict

from mage import Mage
from priest import Priest
from warlock import Warlock
from hunter import Hunter
from DK import DK
from paladin import Paladin
from rogue import Rogue
from warrior import Warrior
from shaman import Shaman


def print_usage():
	print('[usage]:')
	print('  --class= + specify class (necessary)')
	print('  --talent= + json file containing the specific talent of class (necessary)')
	print('  --attribute= + csv file containing the attribute without influence of talent (necessary)')


p_class=''
p_talent=''
p_attribute=''

def parse_arg(args):
	global p_class
	global p_talent
	global p_attribute
	#print(args)
	if len(args) == 1:
		print('lack of parameters')
		print_usage()
		sys.exit(1)
	else:
		try:
			parse, remaining = getopt.getopt(args[1:],'hc:t:a:',['help', 'class=', 'talent=', 'attribute='])
			#print(parse)
			if len(remaining) > 0:
				print('unknown parameter: ' + str(remaining))
			for opt, arg in parse:
				if opt in ('-h', '--help'):
					print_usage()
					sys.exit(1)
				elif opt in ('-c', '--class'):
					if arg in ('mage', 'warlock', 'priest', 'rogue', 'hunter', 'paladin', 'DK', 'warrior', 'shaman'):
						p_class = arg
					else:
						print('the class not supported yet or in wrong format')
						print('currently supported class 1.mage 2.warlock 3.priest 4. 5.rogue 6.hunter 7.shaman 8.paladin 9.DK 10.warrior')
						print_usage()
						sys.exit(1)
				elif opt in ('-t', '--talent'):
					p_talent = arg
				elif opt in ('-a', '--attribute'):
					p_attribute = arg
		except getopt.GetoptError:
			print('found error in parameters analysis')
			print_usage()
			sys.exit(1)
	if p_class == '' or p_talent == '' or p_attribute == '':
		print('necessary parameter is needed, see usage.')
		print_usage()
		sys.exit(1)


if __name__ == '__main__':
	parse_arg(sys.argv)
	#print(p_class)
	#print(p_talent)
	#print(p_attribute)
	
	if p_class == 'mage':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding="utf-8-sig", mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)

		character = Mage(attribute, talent_list)
	
	elif p_class == 'priest':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not fount.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding="utf-8-sig", mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)

		character = Priest(attribute, talent_list)
	
	elif p_class == 'warlock':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding="utf-8-sig", mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)

		character = Warlock(attribute, talent_list)
			
	elif p_class == 'hunter':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding='utf-8-sig', mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)
	
		character = Hunter(attribute, talent_list)
	
	elif p_class == 'DK':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding='utf-8-sig', mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)
	
		character = DK(attribute, talent_list)
	
	elif p_class == 'paladin':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding='utf-8-sig', mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)
	
		character = Paladin(attribute, talent_list)
	
	elif p_class == 'rogue':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding='utf-8-sig', mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)
	
		character = Rogue(attribute, talent_list)
	
	elif p_class == 'warrior':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding='utf-8-sig', mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)
	
		character = Warrior(attribute, talent_list)
	
	elif p_class == 'shaman':
		try:
			with open(p_talent) as fobj:
				jsc = fobj.read()
				talent_list = json.loads(jsc)
		except FileNotFoundError:
			print('talent json file not found.')
			sys.exit(1)

		try:
			with open(p_attribute, encoding='utf-8-sig', mode='r') as fobj:
				content = csv.DictReader(fobj)
				for attribute in content:
					print(attribute)
					print('')
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)
	
		character = Shaman(attribute, talent_list)
	else:
		pass
	

	print(character)

	if hasattr(character, 'spell_abilities'):
		spell_csv = list()
		for s in character.spell_abilities.values():
			#print(s)
			item = dict()
			item['name'] = s.spell_name
			item['cast time'] = '{:.2f}'.format(s._actual_cast_time)
			item['amount increase'] = '{:.6f}'.format(s._final_increase)
			item['critical'] = '{:.4f}'.format(s._final_critical)
			item['critical bonus'] = s.critical_bonus
			# --- direct ---
			item['[D] non-crit'] = '{:.0f} - {:.0f}'.format(s._amount_noncritical_direct_min, s._amount_noncritical_direct_max)
			item['[D] crit'] = '{:.0f} - {:.0f}'.format(s._amount_critical_direct_min, s._amount_critical_direct_max)
			#item['[D] average'] = '{:.0f} - {:.0f}'.format(s._amount_average_direct_min, s._amount_average_direct_max)
			# --- periodic ---
			item['[P] duration/count/tick'] = '{:.2f} / {:.0f} / {:.2f}'.format(s._periodic_duration, s.periodic_tick_count, s._periodic_duration_tick)
			if s.periodic_can_critical == True:
				item['[P] total-tick-tick(crit)'] = '{:.0f} / {:.0f} / {:.0f}'.format(s._amount_noncritical_total_periodic, s._amount_noncritical_tick_periodic, s._amount_critical_tick_periodic)
			else:
				item['[P] total-tick-tick(crit)'] = '{:.0f} / {:.0f} / {:.0f}'.format(s._amount_noncritical_total_periodic, s._amount_noncritical_tick_periodic, s._amount_noncritical_tick_periodic)
			spell_csv.append(item)

		with open('{}_spell_log.csv'.format(p_class), 'w', encoding='utf-8', newline='') as f:
			writer = csv.DictWriter(f, spell_csv[0].keys())
			writer.writeheader()
			writer.writerows(spell_csv)

	if hasattr(character, 'physic_abilities'):
		physic_csv = list()
		for s in character.physic_abilities.values():
			#print(s)
			item = dict()
			item['name'] = s.physic_name
			item['amount increase'] = '{:.6f}'.format(s._final_increase)
			item['critical'] = '{:.4f}'.format(s._final_critical)
			item['critical bonus'] = '{:.2f}'.format(s.critical_bonus)
			item['[D] non-crit'] = '{:.0f} - {:.0f}'.format(s._amount_noncritical_direct_min, s._amount_noncritical_direct_max)
			item['[D] crit'] = '{:.0f} - {:.0f}'.format(s._amount_critical_direct_min, s._amount_critical_direct_max)
			item['[P] duration/count/tick'] = '{:.0f} / {:.0f} / {:.0f}'.format(s.periodic_duration, s.periodic_tick_count, s._periodic_tick_time)
			item['[P] total-tick'] = '{:.0f} - {:.0f}'.format(s._periodic_total, s._periodic_tick)
			#item[''] = '{:.2f}'.format(s.)
			#item[''] = '{:.2f}'.format(s.)
			physic_csv.append(item)

		with open('{}_physic_log.csv'.format(p_class), 'w', encoding='utf-8', newline='') as f:
			writer = csv.DictWriter(f, physic_csv[0].keys())
			writer.writeheader()
			writer.writerows(physic_csv)


