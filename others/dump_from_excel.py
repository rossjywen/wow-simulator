#!/usr/bin/env python3

import xlwings
import sys
import getopt
import json
from collections import OrderedDict

def dump_from_excel():
	excel_obj = xlwings.Book(input_file)
	sht = excel_obj.sheets[input_page]
	info = sht.range(start_cell + ':' + end_cell).value

	if output_type == 'list':
		json_data = json.dumps(info, indent=4)
	elif output_type == 'dict':
		header = info[0]
		content = info[1:]
		entry_len = len(info[0])
		parse_list = []

		for item in content:
			parse_info = OrderedDict()
			for index in range(0, entry_len):
				parse_info[header[index]] = item[index]
			parse_list.append(parse_info)

		json_data = json.dumps(parse_list, indent=4)
	else:
		pass
		
	
	if output_file == '':
		print(json_data)
	else:
		with open(output_file, 'w') as fobj:
			fobj.truncate(0)
			fobj.write(json_data)

		#with open(output_file, 'r+')as fobj:
		#	fc = fobj.read()
		#	jc = json.loads(fc)
		#	print(jc)


def print_usage():
	print('[usage]:')
	print(' -h/--help: print this info')
	print(' -i/--input= + excel file name to specify input (necessary)')
	print(' -p/--page= + excel sheet name or index (necessary)')
	print(' -o/--output= + file name specify output (optional)')
	print(' -s/--start= + start excel cell e.g a1/b5/c2... (necessary)')
	print(' -e/--end= + end excel cell e.g a2/c10/g100... (necessary)')
	print(' -t/--type= + list/dict to specify format of output data')


input_file=''
output_file=''
input_page=''
start_cell=''
end_cell=''
output_type=''

def args_parse(argv):
	global input_file
	global input_page
	global output_file
	global start_cell
	global end_cell
	global output_type


	parse, remainings = getopt.getopt(argv, 'hi:p:s:e:o:t:', ['help', 'input=', 'page=', 'start=', 'end=', 'output=', 'type='])
	#print(parse)
	for opt, arg in parse:
		if opt in ['-h', '--help']:
			print_usage()
			sys.exit(0)
		elif opt in ['-i', '--input']:
			input_file = arg
		elif opt in ['-p', '--page']:
			input_page = arg
		elif opt in ['-o', '--output']:
			output_file = arg
		elif opt in ['-s', '--start']:
			start_cell = arg
		elif opt in ['-e', '--end']:
			end_cell = arg
		elif opt in ['-t', '--type']:
			output_type = arg
		else:
			pass

	if input_file == '':
		print('lack of input file name')
		print_usage()
		sys.exit(1)
	if input_page == '':
		print('lack of sheet name')
		print_usage()
		sys.exit(1)
	if start_cell == '':
		print('lack of start cell name')
		print_usage()
		sys.exit(1)
	if end_cell == '':
		print('lack of end cell name')
		print_usage()
		sys.exit(1)
	if output_type not in ('list', 'dict'):
		print('lack of output type or wrong type')
		print_usage()
		sys.exit(1)

	if remainings:
		print('following arguements are ignored')
		for item in remainings:
			print(item)


if __name__ == '__main__':
	args_parse(sys.argv[1:])
	
	dump_from_excel()


