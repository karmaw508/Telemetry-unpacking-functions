#get_byte = lambda message, byte: message[byte*2:byte*2+2]
#get_bit = lambda byte, bit: (byte & (2**bit)) >> bit
#hex_to_int16(2ByteMessage)		Converts little endian message of 2 bytes into a SIGNED int16
#					If you need unsigned. use int(byteMessage, N), but be wary of endianess


{
#ADC_sensor_inputs
'400': lambda data: [
    ('Damper_position_FL' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Damper_rate_FL' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10),
],

'401': lambda data: [
    ('Damper_position_FR' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Damper_rate_FR' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10),
],

'402': lambda data: [
    ('Damper_position_RL' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Damper_rate_RL' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10),
],

'403': lambda data: [
    ('Damper_position_RR' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Damper_rate_RR' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10),
],

'410': lambda data: [
    ('Steering_position_degrees' , int((get_byte(data, 1) + get_byte(data, 0), 16)*360)/4097)
],

'411': lambda data: [
    ('TPS_left' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10)
],

'412': lambda data: [
    ('TPS_right' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10)
],

'413': lambda data: [
    ('KERS' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10)
],

'420': lambda data: [
    ('Temperature_gear_FL' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Temperature_gear_FR' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10)
],

'421': lambda data: [
    ('Temperature_gear_RL' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Temperature_gear_RR' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10)
],

'422': lambda data: [
    ('Temperature_coolant_left' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10)
],

'423': lambda data: [
    ('Temperature_coolant_right' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10)
],

'414': lambda data: [
    ('Brake_pressure_left' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10),
    ('Brake_pressure_right' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10)
],

#GLVBMS
#Mikael Kvalvær
'620': lambda data: [
    ('Voltage_0' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Voltage_1' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
    ('Voltage_2' , int(get_byte(data, 4) + get_byte(data, 5), 16)),
    ('Voltage_3' , int(get_byte(data, 6) + get_byte(data, 7), 16))
],    

'621': lambda data: [
    ('Voltage_4' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Voltage_5' , int(get_byte(data, 2) + get_byte(data, 3), 16))
],   

'623': lambda data: [
    ('Temperature_0' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Temperature_1' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
    ('Temperature_2' , int(get_byte(data, 4) + get_byte(data, 5), 16)),
    ('Temperature_3' , int(get_byte(data, 6) + get_byte(data, 7), 16))
],   

'624': lambda data: [
    ('GLVBMS_temp_4', int(get_byte(data, 0) + get_byte(data, 1), 16))
],

'625': lambda data: [
    ('GLVBMS_current', int(get_byte(data, 1) + get_byte(data, 0), 16))
],

'626': lambda data: [
    ('Min_voltage' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Max_voltage' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
    ('Total_voltage' , int(get_byte(data, 4) + get_byte(data, 5), 16)),
    ('Min_temperature' , int(get_byte(data, 6) + get_byte(data, 7), 16))
],

'627': lambda data: [
    ('Max_temperature' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Balance_settings' , int(get_byte(data, 2) + get_byte(data, 3), 16))
],
#BMS
#Sondre Ninive Andersen
'440': lambda data: [
	('BMS_Max_Cell_Voltage',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Average_Cell_Voltage',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Min_Cell_Voltage',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Max_Voltage_ID',			int(get_byte(data, 6), 8)),
	('BMS_Min_Voltage_ID',			int(get_byte(data, 7), 8))
],

'441': lambda data: [
	('BMS_Max_Cell_Temperature',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Average_Cell_Temperature',	int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Min_Cell_Temperature',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Max_Temperature_ID',		int(get_byte(data, 6), 8)),
	('BMS_Min_Temperature_ID',		int(get_byte(data, 7), 8))
],

'443': lambda data: [
	('BMS_Tractive_System_Voltage',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Tractive_System_Current',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Tractive_System_Power',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_State_of_Charge',			int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'444': lambda data: [
	('BMS_Error_Flags',			int(get_byte(data, 0) + get_byte(data, 1), 16))
],

'500': lambda data: [
	('BMS_Cell_Voltage_0',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_1',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_2',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_3',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'501': lambda data: [
	('BMS_Cell_Voltage_4',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_5',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_6',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_7',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'502': lambda data: [
	('BMS_Cell_Voltage_8',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_9',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_10',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_11',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'503': lambda data: [
	('BMS_Cell_Voltage_12',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_13',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_14',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_15',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'504': lambda data: [
	('BMS_Cell_Voltage_16',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_17',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_18',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_19',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'505': lambda data: [
	('BMS_Cell_Voltage_20',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_21',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_22',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_23',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'506': lambda data: [
	('BMS_Cell_Voltage_24',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_25',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_26',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_27',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'507': lambda data: [
	('BMS_Cell_Voltage_28',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_29',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_30',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_31',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'508': lambda data: [
	('BMS_Cell_Voltage_32',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_33',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_34',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_35',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'509': lambda data: [
	('BMS_Cell_Voltage_36',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_37',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_38',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_39',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'50a': lambda data: [
	('BMS_Cell_Voltage_40',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_41',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_42',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_43',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'50b': lambda data: [
	('BMS_Cell_Voltage_44',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_45',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_46',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_47',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'50c': lambda data: [
	('BMS_Cell_Voltage_48',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_49',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_50',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_51',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'50d': lambda data: [
	('BMS_Cell_Voltage_52',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_53',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_54',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_55',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'50e': lambda data: [
	('BMS_Cell_Voltage_56',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_57',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_58',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_59',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'50f': lambda data: [
	('BMS_Cell_Voltage_60',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_61',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_62',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_63',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'510': lambda data: [
	('BMS_Cell_Voltage_64',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_65',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_66',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_67',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'511': lambda data: [
	('BMS_Cell_Voltage_68',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_69',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_70',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_71',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'512': lambda data: [
	('BMS_Cell_Voltage_72',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_73',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_74',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_75',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'513': lambda data: [
	('BMS_Cell_Voltage_76',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_77',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_78',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_79',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'514': lambda data: [
	('BMS_Cell_Voltage_80',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_81',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_82',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_83',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'515': lambda data: [
	('BMS_Cell_Voltage_84',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_85',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_86',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_87',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'516': lambda data: [
	('BMS_Cell_Voltage_88',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_89',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_90',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_91',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

	'517': lambda data: [
	('BMS_Cell_Voltage_92',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_93',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_94',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_95',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'518': lambda data: [
	('BMS_Cell_Voltage_96',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_97',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_98',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_99',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'519': lambda data: [
	('BMS_Cell_Voltage_100',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_101',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_102',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_103',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'51a': lambda data: [
	('BMS_Cell_Voltage_104',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_105',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_106',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_107',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'51b': lambda data: [
	('BMS_Cell_Voltage_108',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_109',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_110',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_111',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'51c': lambda data: [
	('BMS_Cell_Voltage_112',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_113',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_114',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_115',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'51d': lambda data: [
	('BMS_Cell_Voltage_116',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_117',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_118',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_119',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'51e': lambda data: [
	('BMS_Cell_Voltage_120',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_121',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_122',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_123',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'51f': lambda data: [
	('BMS_Cell_Voltage_124',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_125',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_126',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_127',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'520': lambda data: [
	('BMS_Cell_Voltage_128',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_129',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_130',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_131',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'521': lambda data: [
	('BMS_Cell_Voltage_132',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_133',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_134',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_135',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'522': lambda data: [
	('BMS_Cell_Voltage_136',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_137',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_138',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_139',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

'523': lambda data: [
	('BMS_Cell_Voltage_140',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10000),
	('BMS_Cell_Voltage_141',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10000),
	('BMS_Cell_Voltage_142',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10000),
	('BMS_Cell_Voltage_143',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10000)
],

# BMS TEMPERATURE

'540': lambda data: [
	('BMS_Cell_Temperature_0',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_1',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_2',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_3',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'541': lambda data: [
	('BMS_Cell_Temperature_4',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_5',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_6',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_7',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'542': lambda data: [
	('BMS_Cell_Temperature_8',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_9',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_10',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_11',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'543': lambda data: [
	('BMS_Cell_Temperature_12',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_13',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_14',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_15',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'544': lambda data: [
	('BMS_Cell_Temperature_16',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_17',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_18',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_19',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'545': lambda data: [
	('BMS_Cell_Temperature_20',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_21',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_22',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_23',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'546': lambda data: [
	('BMS_Cell_Temperature_24',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_25',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_26',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_27',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'547': lambda data: [
	('BMS_Cell_Temperature_28',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_29',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_30',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_31',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'548': lambda data: [
	('BMS_Cell_Temperature_32',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_33',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_34',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_35',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'549': lambda data: [
	('BMS_Cell_Temperature_36',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_37',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_38',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_39',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'54a': lambda data: [
	('BMS_Cell_Temperature_40',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_41',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_42',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_43',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'54b': lambda data: [
	('BMS_Cell_Temperature_44',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_45',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_46',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_47',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'54c': lambda data: [
	('BMS_Cell_Temperature_48',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_49',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_50',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_51',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'54d': lambda data: [
	('BMS_Cell_Temperature_52',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_53',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_54',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_55',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'54e': lambda data: [
	('BMS_Cell_Temperature_56',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_57',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_58',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_59',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'54f': lambda data: [
	('BMS_Cell_Temperature_60',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_61',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_62',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_63',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'550': lambda data: [
	('BMS_Cell_Temperature_64',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_65',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_66',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_67',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'551': lambda data: [
	('BMS_Cell_Temperature_68',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_69',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_70',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_71',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'552': lambda data: [
	('BMS_Cell_Temperature_72',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_73',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_74',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_75',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'553': lambda data: [
	('BMS_Cell_Temperature_76',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_77',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_78',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_79',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'554': lambda data: [
	('BMS_Cell_Temperature_80',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_81',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_82',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_83',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'555': lambda data: [
	('BMS_Cell_Temperature_84',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_85',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_86',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_87',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'556': lambda data: [
	('BMS_Cell_Temperature_88',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_89',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_90',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_91',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'557': lambda data: [
	('BMS_Cell_Temperature_92',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_93',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_94',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_95',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'558': lambda data: [
	('BMS_Cell_Temperature_96',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_97',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_98',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_99',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'559': lambda data: [
	('BMS_Cell_Temperature_100',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_101',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_102',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_103',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'55a': lambda data: [
	('BMS_Cell_Temperature_104',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_105',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_106',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_107',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'55b': lambda data: [
	('BMS_Cell_Temperature_108',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_109',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_110',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_111',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'55c': lambda data: [
	('BMS_Cell_Temperature_112',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_113',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_114',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_115',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'55d': lambda data: [
	('BMS_Cell_Temperature_116',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_117',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_118',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_119',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'55e': lambda data: [
	('BMS_Cell_Temperature_120',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_121',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_122',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_123',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'55f': lambda data: [
	('BMS_Cell_Temperature_124',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_125',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_126',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_127',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'560': lambda data: [
	('BMS_Cell_Temperature_128',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_129',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_130',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_131',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'561': lambda data: [
	('BMS_Cell_Temperature_132',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_133',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_134',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_135',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'562': lambda data: [
	('BMS_Cell_Temperature_136',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_137',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_138',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_139',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],

'563': lambda data: [
	('BMS_Cell_Temperature_140',		int(get_byte(data, 0) + get_byte(data, 1), 16) / 10),
	('BMS_Cell_Temperature_141',		int(get_byte(data, 2) + get_byte(data, 3), 16) / 10),
	('BMS_Cell_Temperature_142',		int(get_byte(data, 4) + get_byte(data, 5), 16) / 10),
	('BMS_Cell_Temperature_143',		int(get_byte(data, 6) + get_byte(data, 7), 16) / 10)
],


#Simen
#R16 mechanical data 1
'290': lambda data: [
    ('R16[1]_current_speed' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[1]_speed_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[1]_torque_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100)
],

#R16 mechanical data 2
'294': lambda data: [
    ('R16[2]_current_speed' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[2]_speed_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[2]_torque_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100)
],

#R16 mechanical data 3
'298': lambda data: [
    ('R16[3]_current_speed' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[3]_speed_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[3]_torque_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100)
],

#R16 mechanical data 4
'29C': lambda data: [
    ('R16[4]_current_speed' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[4]_speed_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[4]_torque_setpoint' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100)
],

#R16 temp data
'291': lambda data: [
    ('R16[1]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[1]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[1]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[1]_motor_temp' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],
	
#R16 temp data		
'295': lambda data: [		
    ('R16[2]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[2]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[2]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[2]_motor_temp' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],
	
#R16 temp data		
'299': lambda data: [		
    ('R16[3]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[3]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[3]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[3]_motor_temp' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 temp data
'29D': lambda data: [
    ('R16[4]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[4]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[4]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[4]_motor_temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 Electrical data
'292': lambda data: [
    ('R16[1]_torque_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[1]_direct_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[1]_DC_current' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100),
    ('R16[1]_DC_voltage' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 7), 16) & 1 << 7) else '0000') + get_byte(data, 7) + get_byte(data, 6)).decode('hex'))[0] / 100)
],

#R16 Electrical data
'296': lambda data: [
    ('R16[2]_torque_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[2]_direct_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[2]_DC_current' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100),
    ('R16[2]_DC_voltage' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 7), 16) & 1 << 7) else '0000') + get_byte(data, 7) + get_byte(data, 6)).decode('hex'))[0] / 100)
],

#R16 Electrical data
'29A': lambda data: [
    ('R16[3]_torque_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[3]_direct_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[3]_DC_current' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100),
    ('R16[3]_DC_voltage' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 7), 16) & 1 << 7) else '0000') + get_byte(data, 7) + get_byte(data, 6)).decode('hex'))[0] / 100)
],

#R16 Electrical data
'29E': lambda data: [
    ('R16[4]_torque_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 1), 16) & 1 << 7) else '0000') + get_byte(data, 1) + get_byte(data, 0)).decode('hex'))[0] / 100),
    ('R16[4]_direct_current' 	, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 3), 16) & 1 << 7) else '0000') + get_byte(data, 3) + get_byte(data, 2)).decode('hex'))[0] / 100),
    ('R16[4]_DC_current' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 5), 16) & 1 << 7) else '0000') + get_byte(data, 5) + get_byte(data, 4)).decode('hex'))[0] / 100),
    ('R16[4]_DC_voltage' 		, struct.unpack('>i', (('FFFF' if (int(get_byte(data, 7), 16) & 1 << 7) else '0000') + get_byte(data, 7) + get_byte(data, 6)).decode('hex'))[0] / 100)
],

#R16 Status data
'293': lambda data: [
	('R16[1]_status_bit_{0}'.format(i) 	, 1 if 0 != int(get_byte(data, 3) + get_byte(data, 2) + get_byte(data, 1) + get_byte(data, 0), 16) & (2**i) else 0) for i in range(32)
	]+[
    ('R16[1]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(get_byte(data, 7) + get_byte(data, 6) + get_byte(data, 5) + get_byte(data, 4), 16) & (2**i) else 0) for i in range(32)
],

#R16 Status data
'297': lambda data: [
	('R16[2]_status_bit_{0}'.format(i) 	, 1 if 0 != int(get_byte(data, 3) + get_byte(data, 2) + get_byte(data, 1) + get_byte(data, 0), 16) & (2**i) else 0) for i in range(32)
	]+[
    ('R16[2]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(get_byte(data, 7) + get_byte(data, 6) + get_byte(data, 5) + get_byte(data, 4), 16) & (2**i) else 0) for i in range(32)
],

#R16 Status data
'29B': lambda data: [
	('R16[3]_status_bit_{0}'.format(i) 	, 1 if 0 != int(get_byte(data, 3) + get_byte(data, 2) + get_byte(data, 1) + get_byte(data, 0), 16) & (2**i) else 0) for i in range(32)
	]+[
    ('R16[3]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(get_byte(data, 7) + get_byte(data, 6) + get_byte(data, 5) + get_byte(data, 4), 16) & (2**i) else 0) for i in range(32)
],

#R16 Status data
'29F': lambda data: [
	('R16[4]_status_bit_{0}'.format(i) 	, 1 if 0 != int(get_byte(data, 3) + get_byte(data, 2) + get_byte(data, 1) + get_byte(data, 0), 16) & (2**i) else 0) for i in range(32)
	]+[
    ('R16[4]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(get_byte(data, 7) + get_byte(data, 6) + get_byte(data, 5) + get_byte(data, 4), 16) & (2**i) else 0) for i in range(32)
],

#R16 parameters
'190': lambda data: [
    ('R16[1]_parameter_{0}'.format(int(get_byte(data, 0), 16)), int(get_byte(data, 2) + get_byte(data, 3), 16))
],
#
#ECU Messages
#ECU SLIP RATIOS
'451': lambda data: [
	('SR_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 1000), 
	('SR_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 1000),
	('SR_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 1000),
	('SR_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 1000)
],
#ECU DAMPER ESTIMATED NORMAL FORCES
'453': lambda data: [
	('FZ_DAMPER_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10), 
	('FZ_DAMPER_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10),
	('FZ_DAMPER_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10),
	('FZ_DAMPER_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10)
],
#ECU LOAD TRANSFER AND AERO ESTIMATED NORMAL FORCES
'454': lambda data: [
	('FZ_LOAD_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10), 
	('FZ_LOAD_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10),
	('FZ_LOAD_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10),
	('FZ_LOAD_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10)
],
#ECU CONTROL SYSTEM VALUES
'455': lambda data: [
	('Mz_reference'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10), 
	('Yaw_rate_ref'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100)
],
#ECU GPS LONGITUDE AND LATITUDE
'456': lambda data: [
	('GPS_LONGITUDE'	, int(get_byte(data, 0) + get_byte(data, 1) + get_byte(data, 2) + get_byte(data, 3),32) / 1000000), 
	('GPS_LATITUDE'	 	, int(get_byte(data, 4) + get_byte(data, 5) + get_byte(data, 6) + get_byte(data, 7),32) / 1000000)
],
#ECU YAW RATE, YAW ACCELERATION
'458': lambda data: [
	('Yaw_rate'	 	, hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 1000), 
	('Yaw acc'		, hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100)
],
#ECU ACCELERATIONS, INS Vx and Vy
'459': lambda data: [
	('Ax'	 	, hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100), 
	('Ay'		, hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100),
	('INS_Vx'	, hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 100),
	('INS_Vy'	, hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 100)
],
#ECU GPS FIX AND NUMBER OF TRACKED SATELITES
'45B': lambda data: [
	('GPS_FIX'	 	, int(get_byte(data, 0), 8)), 
	('NR_TR_SAT'	, int(get_byte(data, 1), 8))
],
#ECU, ATTITUDE AND INS STATUS
'45A': lambda data: [
	('STATUS_ATTITUDE'	 	, int(get_byte(data, 0) + get_byte(data,1), 16)), 
	('STATUS_INS'			, int(get_byte(data, 2), 8))
],

#GLVBMS, VOLTAGES
'460': lambda data: [
    ('GLV_vtg0'       , int(get_byte(data,1) + get_byte(data,0),16)  / 10000.0), 
    ('GLV_vtg1'       , int(get_byte(data,3) + get_byte(data,2),16)  / 10000.0),
    ('GLV_vtg2'       , int(get_byte(data,5) + get_byte(data,4),16)  / 10000.0),
    ('GLV_vtg3'       , int(get_byte(data,7) + get_byte(data,6),16)  / 10000.0)
],
'461': lambda data: [
    ('GLV_vtg4'       , int(get_byte(data,1) + get_byte(data,0),16)  / 10000.0), 
    ('GLV_vtg5'       , int(get_byte(data,3) + get_byte(data,2),16)  / 10000.0),
],

'462': lambda data: [
    ('GLV_tmp0'       , int(get_byte(data,1) + get_byte(data,0),16)  / 100.0), 
    ('GLV_vmp1'       , int(get_byte(data,3) + get_byte(data,2),16)  / 100.0),
    ('GLV_tmp2'       , int(get_byte(data,5) + get_byte(data,4),16)  / 100.0),
    ('GLV_tmp3'       , int(get_byte(data,7) + get_byte(data,6),16)  / 100.0),
],
'463': lambda data: [
    ('GLV_tmp4'       , int(get_byte(data,1) + get_byte(data,0),16)  / 100.0), 
],


'465': lambda data: [
    ('GLV_minVtg'       , int(get_byte(data,1) + get_byte(data,0),16)  / 10000.0), 
    ('GLV_maxVtg'       , int(get_byte(data,3) + get_byte(data,2),16)  / 10000.0),
    ('GLV_totVtg'       , int( get_byte(data,7) + get_byte(data,6) + get_byte(data,5) + get_byte(data,4), 16) / 10000.0 ),
],


'466': lambda data: [
    ('GLV_minTemp'       , int(get_byte(data,1) + get_byte(data,0),16)  / 100.0),
    ('GLV_maxTemp'       , int(get_byte(data,3) + get_byte(data,2),16)  / 100.0),
    ('GLV_current'       , int(get_byte(data,7) + get_byte(data,6),16)  / 1000.0),
],






}

