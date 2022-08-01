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
		parse, remaining = getopt.getopt(args[1:],'hc:t:a:',['help', 'class=', 'talent=', 'attribute='])
		#print(parse)
		if len(remaining) > 0:
			print('unknown parameter: ' + str(remaining))
		for opt, arg in parse:
			if opt in ('-h', '--help'):
				print_usage()
				sys.exit(0)
			elif opt in ('-c', '--class'):
				if arg in ('mage', 'warlock', 'priest', 'hunter'):
					p_class = arg
				else:
					print('the class not supported yet or in wrong format')
					print('currently supported class 1.mage 2.priest 3.warlock 4.hunter')
					print_usage()
					sys.exit(1)
			elif opt in ('-t', '--talent'):
				p_talent = arg
			elif opt in ('-a', '--attribute'):
				p_attribute = arg
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

		charactor = Mage(attribute, talent_list)

		for s in charactor.spell_abilities.values():
			print(s)
	
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

		charactor = Priest(attribute, talent_list)

		for s in charactor.spell_abilities.values():
			print(s)
	
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

		charactor = Warlock(attribute, talent_list)

		for s in charactor.spell_abilities.values():
			print(s)
	
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
	
		charactor = Hunter(attribute, talent_list)

		for s in charactor.physic_abilities.values():
			print(s)

	else:
		pass



