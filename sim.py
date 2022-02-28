#!/usr/bin/env python3

import sys
import getopt
import json
from mage import Mage
from collections import OrderedDict


def print_usage():
	print('[usage]:')
	print('  --class= + specify class (necessary)')
	print('  --talent= + json file containing the specific talent of class (necessary)')
	print('  --attribute= + json file containing the attribute without influence of talent (necessary)')


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
				if arg in ('mage', 'warlock', 'priest'):
					p_class = arg
				else:
					print('the class not supported yet or in wrong format')
					print('currently supported class 1.mage')
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
			with open(p_attribute) as fobj:
				jsc = fobj.read()
				attribute_list = json.loads(jsc)
		except FileNotFoundError:
			print('attribute json file not found.')
			sys.exit(1)

		info = attribute_list[0]
		charactor = Mage(info, talent_list)
		for s in charactor.spells.values():
			print(s)
	#elif p_class == ... 	# for other classes
		# do something
	else:
		pass



