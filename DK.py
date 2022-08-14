import csv
from collections import OrderedDict
from attribute import Attribute
from ability import Physic_ability

class DKTalent():
	def __init__():
		pass
	
	def blood_1_1(self, count):
		'''Butchery'''
		pass

	def blood_1_2(self, count):
		'''Subversion'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Blood Strike'].specific_critical_increase += 0.03 * count
		self.physic_abilities['Scourge Strike'].specific_critical_increase += 0.03 * count
		self.physic_abilities['Heart Strike'].specific_critical_increase += 0.03 * count
		self.physic_abilities['Obliterate'].specific_critical_increase += 0.03 * count

	def blood_1_3(self, count):
		'''Blade Barrier'''
		pass

	def blood_2_1(self, count):
		'''Bladed Armor'''
		pass

	def blood_2_2(self, count):
		'''Scent of Blood'''
		pass

	def blood_2_3(self, count):
		'''Two-Handed Weapon Specialization'''
		# todo detect abilities with two-hand weapon
		pass

	def blood_3_1(self, count):
		'''Rune Tap'''
		pass

	def blood_3_2(self, count):
		'''Dark Conviction'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_basic_attr['melee_critical'] += 0.01 * count

	def blood_3_3(self, count):
		'''Death Rune Mastery'''
		pass

	def blood_4_1(self, count):
		'''Improved Rune Tap'''
		pass

	def blood_4_3(self, count):
		'''Spell Deflection'''
		pass

	def blood_4_4(self, count):
		'''Vendetta'''
		pass

	def blood_5_1(self, count):
		'''Bloody Strikes'''
		self.physic_abilities['Blood Strike'].specific_amount_increase += 0.05 * count
		self.physic_abilities['Heart Strike'].specific_amount_increase += 0.15 * count
		self.physic_abilities['Blood Boil'].specific_amount_increase += 0.1 * count

	def blood_5_3(self, count):
		'''Veteran of the Third War'''
		pass

	def blood_5_4(self, count):
		'''Mark of Blood'''
		pass

	def blood_6_2(self, count):
		'''Bloody Vengeance'''
		pass

	def blood_6_3(self, count):
		'''Abomination's Might'''
		pass

	def blood_7_1(self, count):
		'''Bloodworms'''
		pass

	def blood_7_2(self, count):
		'''Hysteria'''
		pass

	def blood_7_3(self, count):
		'''Improved Blood Presence'''
		pass

	def blood_8_1(self, count):
		'''Improved Death Strike'''
		assert count in (0, 1, 2)
		self.physic_abilities['Death Strike'].specific_amount_increase += 0.15 * count
		self.physic_abilities['Death Strike'].specific_critical_increase += 0.03 * count

	def blood_8_2(self, count):
		'''Sudden Doom'''
		pass

	def blood_8_3(self, count):
		'''Vampiric Blood'''
		pass

	def blood_9_1(self, count):
		'''Will of the Necropolis'''
		pass

	def blood_9_2(self, count):
		'''Heart Strike'''
		pass

	def blood_9_3(self, count):
		'''Might of Mograine'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Blood Boil'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Blood Strike'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Death Strike'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Heart Strike'].critical_bonus *= 1 + 0.15 * count

	def blood_10_2(self, count):
		'''Blood Gorged'''
		pass

	def blood_11_2(self, count):
		'''Dancing Rune Weapon'''
		pass

	def frost_1_1(self, count):
		'''Improved Icy Touch'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Icy Touch'].specific_amount_increase += 0.05 * count

	def frost_1_2(self, count):
		'''Runic Power Mastery'''
		pass

	def frost_1_3(self, count):
		'''Toughness'''
		pass

	def frost_2_2(self, count):
		'''Icy Reach'''
		pass

	def frost_2_3(self, count):
		'''Black Ice'''
		assert count in (0, 1, 2, 3, 4, 5)
		self.physic_amount_increase['frost'] += 0.02 * count
		self.physic_amount_increase['shadow'] += 0.02 * count

	def frost_2_4(self, count):
		'''Nerves of Cold Steel'''
		# todo I'm not sure this should modify the off-weapon data or modify the ability data, I will fix this 
		#for sp_k, sp_v in self.physic_abilities.items():
		#	if sp_v.wp_hand == 'off' or
		pass

	def frost_3_1(self, count):
		'''Icy Talons'''
		pass

	def frost_3_2(self, count):
		'''Lickborne'''
		pass

	def frost_3_3(self, count):
		''''''
		# todo what is 'melee special ability'?
		pass

	def frost_4_2(self, count):
		'''Killing Machine'''
		pass

	def frost_4_3(self, count):
		'''Chill of the Grave'''
		pass

	def frost_4_4(self, count):
		'''Endless Winter'''
		pass

	def frost_5_2(self, count):
		'''Frigid Dreadplate'''
		pass

	def frost_5_3(self, count):
		'''Glacier Rot'''
		pass

	def frost_5_4(self, count):
		'''Deathchill'''
		pass

	def frost_6_1(self, count):
		'''Improved Icy Talons'''
		# todo melee haste
		pass

	def frost_6_2(self, count):
		'''Merciless Combat'''
		pass

	def frost_6_3(self, count):
		'''Rime'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Icy Touch'].specific_critical_increase += 0.05 * count
		self.physic_abilities['Obliterate'].specific_critical_increase += 0.05 * count

	def frost_7_1(self, count):
		'''Chilblains'''
		pass

	def frost_7_2(self, count):
		'''Hungering Cold'''
		pass

	def frost_7_3(self, count):
		'''Improved Frost Presence'''
		pass

	def frost_8_1(self, count):
		'''Thread of Thassarian'''
		# todo off-hand weapon enable
		pass

	def frost_8_2(self, count):
		'''Blood of the North'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Blood Strike'].specific_amount_increase += 0.03 * count
		self.physic_abilities['Frost Strike'].specific_amount_increase += 0.03 * count

	def frost_8_3(self, count):
		'''Unbreakable Armor'''
		pass

	def frost_9_1(self, count):
		'''Acclimation'''
		pass

	def frost_9_2(self, count):
		'''Frost Strike'''
		pass

	def frost_9_3(self, count):
		'''Guile of Gorefiend'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Blood Strike'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Frost Strike'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Howling Blast'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Obliterate'].critical_bonus *= 1 + 0.15 * count

	def frost_10_2(self, count):
		'''Tundra Stalker'''
		pass

	def frost_11_2(self, count):
		'''Howling Blast'''
		pass

	def unholy_1_1(self, count):
		'''Vicious Strike'''
		assert count in (0, 1, 2)
		self.physic_abilities['Plague Strike'].specific_critical_increase += 0.03 * count
		self.physic_abilities['Scourge Strike'].specific_critical_increase += 0.03 * count

		self.physic_abilities['Plague Strike'].critical_bonus *= 1 + 0.15 * count
		self.physic_abilities['Scourge Strike'].critical_bonus *= 1 + 0.15 * count

	def unholy_1_2(self, count):
		'''Virulence'''
		pass

	def unholy_1_3(self, count):
		'''Anticipation'''
		pass

	def unholy_2_1(self, count):
		'''Epidemic'''
		# todo increase amount of disease
		pass

	def unholy_2_2(self, count):
		'''Morbidity'''
		assert count in (0, 1, 2, 3)
		self.physic_abilities['Death Coil (dmg)'].specific_amount_increase += 0.05 * count
		self.physic_abilities['Death Coil (heal)'].specific_amount_increase += 0.05 * count

	def unholy_2_3(self, count):
		'''Unholy Command'''
		pass

	def unholy_2_4(self, count):
		'''Ravenous Dead'''
		# todo pet
		pass

	def unholy_3_1(self, count):
		'''Outbreak'''
		assert count in (0, 1, 2, 3)
		if count == 0:
			pass
		elif count == 1:
			self.physic_abilities['Plague Strike'].specific_amount_increase += 0.1
			self.physic_abilities['Scourge Strike'].specific_amount_increase += 0.07
		elif count == 2:
			self.physic_abilities['Plague Strike'].specific_amount_increase += 0.2
			self.physic_abilities['Scourge Strike'].specific_amount_increase += 0.13
		elif count == 3:
			self.physic_abilities['Plague Strike'].specific_amount_increase += 0.3
			self.physic_abilities['Scourge Strike'].specific_amount_increase += 0.2

	def unholy_3_2(self, count):
		'''Necrosis'''
		# todo auto attack
		pass

	def unholy_3_3(self, count):
		'''Corpse Explosion'''
		pass

	def unholy_4_2(self, count):
		'''On a Pale Horse'''
		pass

	def unholy_4_3(self, count):
		'''Blood-Caked Blade'''
		pass

	def unholy_4_4(self, count):
		'''Night of Dead'''
		pass

	def unholy_5_1(self, count):
		'''Unholy Blight'''
		pass

	def unholy_5_2(self, count):
		'''Impurity'''
		assert count in (0, 1, 2, 3, 4, 5)
		for ab in self.physic_abilities.values():
			if ab.ap == True:
				ab.ap_coefficient *= 1 + 0.04 * count

	def unholy_5_3(self, count):
		'''Dirge'''
		pass

	def unholy_6_1(self, count):
		'''Desecration'''
		pass

	def unholy_6_2(self, count):
		'''Magic Suppression'''
		# todo anti-magic shell absorb
		pass

	def unholy_6_3(self, count):
		'''Reaping'''
		pass

	def unholy_6_4(self, count):
		'''Master of Ghouls'''
		pass

	def unholy_7_1(self, count):
		'''Desolation'''
		pass

	def unholy_7_2(self, count):
		'''Anti-Magic Zone'''
		pass

	def unholy_7_3(self, count):
		'''Improved Unholy Presence'''
		pass

	def unholy_7_4(self, count):
		'''Ghoul Frenzy'''
		pass

	def unholy_8_2(self, count):
		'''Crypt Fever'''
		pass

	def unholy_8_3(self, count):
		'''Bone Shield'''
		pass

	def unholy_9_1(self, count):
		'''Wandering Plague'''
		pass

	def unholy_9_2(self, count):
		'''Ebon Plaguebringer'''
		pass

	def unholy_9_3(self, count):
		'''Scourge Strike'''
		pass

	def unholy_10_2(self, count):
		'''Rage of Rivendare'''
		pass

	def unholy_11_2(self, count):
		'''Summon Gargoyle'''
		pass


class DK(Attribute, DKTalent):
	def __init__(self, attr_dict, talent_list):
		# initialize all spells
		self.physic_abilities = OrderedDict()
		with open('ability_data/DK_abilities.csv', encoding="utf-8-sig", mode='r') as fobj:
			content = csv.DictReader(fobj)
			for item in content:	# every item is a dict
				self.physic_abilities[item['ability_name']] = Physic_ability(item)
				self.physic_abilities[item['ability_name']].critical_bonus = 1	# DK positibe ability [Runic Focus]
		
		# initialize attribute
		Attribute.__init__(self, attr_dict)
	
		# initialize talent
		for depth in range(0, 11):
			for column in range(0, 12):
				if talent_list[depth][column] != None:	
					if column < 4:
						res_str = 'blood_{y}_{x}'.format(y=depth+1, x=column+1)
					elif column < 8:
						res_str = 'frost_{y}_{x}'.format(y=depth+1, x=column-4+1)
					else:
						res_str = 'unholy_{y}_{x}'.format(y=depth+1, x=column-4-4+1)
					#print(res_str)
					fun = getattr(DK, res_str)
					fun(self, talent_list[depth][column])
				else:
					continue
		
		# calculate amount of spells
		for ability in self.physic_abilities.values():
			ability.calculate_amount(self.physic_basic_attr, self.physic_amount_increase, self.main_melee_weapon, self.off_melee_weapon, self.ranged_weapon)





