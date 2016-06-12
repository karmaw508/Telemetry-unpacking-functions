#get_byte = lambda message, byte: message[byte*2:byte*2+2]
#get_bit = lambda byte, bit: (byte & (2**bit)) >> bit
#hex_to_int16(2ByteMessage)		Converts message of 2 bytes into a SIGNED int16. Takes little endian, so no need to swap bytes
#hex_to_uint16(2ByteMessage)	
#hex_to_int32(4ByteMessage)	
#hex_to_uint32(4ByteMessage)	

{
#ADC_sensor_inputs
'400': lambda data: [
    ('Damper_position_FL' , hex_to_uint16(get_byte(data, 0) + get_byte(data, 1))/10.0),
    ('Damper_rate_FL' , hex_to_int16(get_byte(data, 2) + get_byte(data, 3) )/10.0),
],

'401': lambda data: [
    ('Damper_position_FR' , hex_to_uint16(get_byte(data, 0) + get_byte(data, 1))/10.0),
    ('Damper_rate_FR' , hex_to_int16(get_byte(data, 2) + get_byte(data, 3) )/10.0),
],

'402': lambda data: [
    ('Damper_position_RL' , hex_to_uint16(get_byte(data, 0) + get_byte(data, 1))/10.0),
    ('Damper_rate_RL' , hex_to_int16(get_byte(data, 2) + get_byte(data, 3) )/10.0),
],

'403': lambda data: [
    ('Damper_position_RR' , hex_to_uint16(get_byte(data, 0) + get_byte(data, 1))/10.0),
    ('Damper_rate_RR' , hex_to_int16(get_byte(data, 2) + get_byte(data, 3))/10.0),
],

'410': lambda data: [
    ('Steering_position_degrees' , hex_to_int16(get_byte(data, 0) + get_byte(data, 1) )*360.0/4097.0)
],

'411': lambda data: [
    ('TPS_left' , hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) / 10.0)
],

'412': lambda data: [
    ('TPS_right' , hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) / 10.0)
],

'413': lambda data: [
    ('KERS' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10)
],

'420': lambda data: [
    ('Temperature_gear_FL' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10.0),
    ('Temperature_gear_FR' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10.0)
],

'421': lambda data: [
    ('Temperature_gear_RL' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10.0),
    ('Temperature_gear_RR' , int(get_byte(data, 3) + get_byte(data, 2), 16)/10.0)
],

'422': lambda data: [
    ('Temperature_coolant_left' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10.0)
],

'423': lambda data: [
    ('Temperature_coolant_right' , int(get_byte(data, 1) + get_byte(data, 0), 16)/10.0)
],

'414': lambda data: [
    ('Brake_pressure_left' , int(get_byte(data, 0), 16)  / 10.0),
    ('Brake_pressure_right' , int(get_byte(data, 1), 16) /10.0)
],
#BSPD - Trigger ( data uint8_t == 0 means that BSPD has trigged ).
'480': lambda data: [
    ('BSPD_trigger' , int(get_byte(data, 0), 8))
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
	('BMS_Max_Cell_Voltage',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Average_Cell_Voltage',	hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Min_Cell_Voltage',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Max_Voltage_ID',			int(get_byte(data, 6),16)),
	('BMS_Min_Voltage_ID',			int(get_byte(data, 7),16))
],

'441': lambda data: [
	('BMS_Max_Cell_Temperature',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Average_Cell_Temperature',	hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Min_Cell_Temperature',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Max_Temperature_ID',		int(get_byte(data, 6),16)),
	('BMS_Min_Temperature_ID',		int(get_byte(data, 7),16)),
],

'442': lambda data: [
	('BMS_Tractive_System_Voltage',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Tractive_System_Current',		hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Tractive_System_Power',		hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_State_of_Charge',			hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'443': lambda data: [
	('BMS_Error_Flags',			hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)))
],

'500': lambda data: [
	('BMS_Cell_Voltage_0',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_1',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_2',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_3',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'501': lambda data: [
	('BMS_Cell_Voltage_4',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_5',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_6',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_7',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'502': lambda data: [
	('BMS_Cell_Voltage_8',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_9',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_10',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_11',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'503': lambda data: [
	('BMS_Cell_Voltage_12',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_13',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_14',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_15',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'504': lambda data: [
	('BMS_Cell_Voltage_16',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_17',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_18',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_19',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'505': lambda data: [
	('BMS_Cell_Voltage_20',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_21',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_22',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_23',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'506': lambda data: [
	('BMS_Cell_Voltage_24',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_25',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_26',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_27',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'507': lambda data: [
	('BMS_Cell_Voltage_28',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_29',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_30',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_31',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'508': lambda data: [
	('BMS_Cell_Voltage_32',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_33',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_34',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_35',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'509': lambda data: [
	('BMS_Cell_Voltage_36',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_37',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_38',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_39',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'50A': lambda data: [
	('BMS_Cell_Voltage_40',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_41',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_42',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_43',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'50B': lambda data: [
	('BMS_Cell_Voltage_44',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_45',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_46',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_47',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'50C': lambda data: [
	('BMS_Cell_Voltage_48',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_49',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_50',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_51',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'50D': lambda data: [
	('BMS_Cell_Voltage_52',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_53',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_54',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_55',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'50E': lambda data: [
	('BMS_Cell_Voltage_56',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_57',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_58',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_59',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'50F': lambda data: [
	('BMS_Cell_Voltage_60',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_61',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_62',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_63',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'510': lambda data: [
	('BMS_Cell_Voltage_64',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_65',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_66',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_67',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'511': lambda data: [
	('BMS_Cell_Voltage_68',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_69',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_70',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_71',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'512': lambda data: [
	('BMS_Cell_Voltage_72',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_73',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_74',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_75',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'513': lambda data: [
	('BMS_Cell_Voltage_76',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_77',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_78',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_79',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'514': lambda data: [
	('BMS_Cell_Voltage_80',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_81',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_82',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_83',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'515': lambda data: [
	('BMS_Cell_Voltage_84',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_85',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_86',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_87',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'516': lambda data: [
	('BMS_Cell_Voltage_88',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_89',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_90',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_91',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

	'517': lambda data: [
	('BMS_Cell_Voltage_92',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_93',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_94',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_95',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'518': lambda data: [
	('BMS_Cell_Voltage_96',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_97',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_98',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_99',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'519': lambda data: [
	('BMS_Cell_Voltage_100',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_101',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_102',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_103',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'51A': lambda data: [
	('BMS_Cell_Voltage_104',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_105',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_106',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_107',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'51B': lambda data: [
	('BMS_Cell_Voltage_108',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_109',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_110',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_111',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'51C': lambda data: [
	('BMS_Cell_Voltage_112',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_113',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_114',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_115',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'51D': lambda data: [
	('BMS_Cell_Voltage_116',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_117',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_118',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_119',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'51E': lambda data: [
	('BMS_Cell_Voltage_120',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_121',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_122',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_123',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'51F': lambda data: [
	('BMS_Cell_Voltage_124',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_125',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_126',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_127',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'520': lambda data: [
	('BMS_Cell_Voltage_128',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_129',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_130',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_131',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'521': lambda data: [
	('BMS_Cell_Voltage_132',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_133',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_134',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_135',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'522': lambda data: [
	('BMS_Cell_Voltage_136',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_137',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_138',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_139',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'523': lambda data: [
	('BMS_Cell_Voltage_140',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.0001),
	('BMS_Cell_Voltage_141',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.0001),
	('BMS_Cell_Voltage_142',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.0001),
	('BMS_Cell_Voltage_143',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.0001)
],

'540': lambda data: [
	('BMS_Cell_Temperature_0',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_1',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_2',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_3',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'541': lambda data: [
	('BMS_Cell_Temperature_4',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_5',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_6',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_7',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'542': lambda data: [
	('BMS_Cell_Temperature_8',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_9',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_10',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_11',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'543': lambda data: [
	('BMS_Cell_Temperature_12',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_13',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_14',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_15',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'544': lambda data: [
	('BMS_Cell_Temperature_16',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_17',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_18',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_19',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'545': lambda data: [
	('BMS_Cell_Temperature_20',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_21',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_22',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_23',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'546': lambda data: [
	('BMS_Cell_Temperature_24',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_25',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_26',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_27',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'547': lambda data: [
	('BMS_Cell_Temperature_28',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_29',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_30',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_31',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'548': lambda data: [
	('BMS_Cell_Temperature_32',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_33',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_34',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_35',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'549': lambda data: [
	('BMS_Cell_Temperature_36',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_37',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_38',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_39',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'54A': lambda data: [
	('BMS_Cell_Temperature_40',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_41',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_42',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_43',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'54B': lambda data: [
	('BMS_Cell_Temperature_44',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_45',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_46',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_47',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'54C': lambda data: [
	('BMS_Cell_Temperature_48',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_49',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_50',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_51',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'54D': lambda data: [
	('BMS_Cell_Temperature_52',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_53',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_54',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_55',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'54E': lambda data: [
	('BMS_Cell_Temperature_56',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_57',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_58',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_59',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'54F': lambda data: [
	('BMS_Cell_Temperature_60',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_61',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_62',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_63',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'550': lambda data: [
	('BMS_Cell_Temperature_64',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_65',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_66',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_67',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'551': lambda data: [
	('BMS_Cell_Temperature_68',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_69',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_70',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_71',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'552': lambda data: [
	('BMS_Cell_Temperature_72',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_73',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_74',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_75',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'553': lambda data: [
	('BMS_Cell_Temperature_76',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_77',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_78',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_79',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'554': lambda data: [
	('BMS_Cell_Temperature_80',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_81',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_82',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_83',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'555': lambda data: [
	('BMS_Cell_Temperature_84',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_85',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_86',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_87',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'556': lambda data: [
	('BMS_Cell_Temperature_88',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_89',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_90',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_91',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'557': lambda data: [
	('BMS_Cell_Temperature_92',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_93',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_94',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_95',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'558': lambda data: [
	('BMS_Cell_Temperature_96',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_97',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_98',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_99',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'559': lambda data: [
	('BMS_Cell_Temperature_100',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_101',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_102',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_103',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'55A': lambda data: [
	('BMS_Cell_Temperature_104',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_105',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_106',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_107',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'55B': lambda data: [
	('BMS_Cell_Temperature_108',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_109',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_110',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_111',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'55C': lambda data: [
	('BMS_Cell_Temperature_112',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_113',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_114',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_115',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'55D': lambda data: [
	('BMS_Cell_Temperature_116',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_117',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_118',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_119',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'55E': lambda data: [
	('BMS_Cell_Temperature_120',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_121',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_122',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_123',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'55F': lambda data: [
	('BMS_Cell_Temperature_124',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_125',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_126',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_127',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'560': lambda data: [
	('BMS_Cell_Temperature_128',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_129',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_130',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_131',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'561': lambda data: [
	('BMS_Cell_Temperature_132',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_133',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_134',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_135',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'562': lambda data: [
	('BMS_Cell_Temperature_136',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_137',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_138',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_139',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

'563': lambda data: [
	('BMS_Cell_Temperature_140',		hex_to_uint16(get_byte(data, 0) + get_byte(data, 1)) * 0.1),
	('BMS_Cell_Temperature_141',		hex_to_uint16(get_byte(data, 2) + get_byte(data, 3)) * 0.1),
	('BMS_Cell_Temperature_142',		hex_to_uint16(get_byte(data, 4) + get_byte(data, 5)) * 0.1),
	('BMS_Cell_Temperature_143',		hex_to_uint16(get_byte(data, 6) + get_byte(data, 7)) * 0.1)
],

#Simen
#TODO bruk hex_to_in16
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

#TODO Skal det være int32??
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

#SF II
'3D0': lambda data: [
	('OPTICAL_VX'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100.0), 
	('OPTICAL_VY'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100.0),
	('OPTICAL_SA'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 100.0)
],


#ECU Messages
#ECU SLIP RATIOS
'451': lambda data: [
	('SR_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 1000.0), 
	('SR_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 1000.0),
	('SR_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 1000.0),
	('SR_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 1000.0)
],
#ECU FX/FZ = normalized traction force
'452': lambda data: [
	('FX_DIV_FZ_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10.0), 
	('FX_DIV_FZ_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10.0),
	('FX_DIV_FZ_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10.0),
	('FX_DIV_FZ_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10.0)
],
#ECU DAMPER ESTIMATED NORMAL FORCES
'453': lambda data: [
	('FZ_DAMPER_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10.0), 
	('FZ_DAMPER_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10.0),
	('FZ_DAMPER_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10.0),
	('FZ_DAMPER_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10.0)
],
#ECU LOAD TRANSFER AND AERO ESTIMATED NORMAL FORCES
'454': lambda data: [
	('FZ_LOAD_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10.0), 
	('FZ_LOAD_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10.0),
	('FZ_LOAD_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10.0),
	('FZ_LOAD_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10.0)
],
#ECU FX_ESTIMATED
'45C': lambda data: [
	('Fx_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10.0), 
	('Fx_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10.0),
	('Fx_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10.0),
	('Fx_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10.0)
],
#ECU RPM DERIVATIVE
'45D': lambda data: [
	('RPM_DER_FL'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) ), 
	('RPM_DER_FR'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) ),
	('RPM_DER_RL'	 , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) ),
	('RPM_DER_RR'	 , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) )
],


#ECU CONTROL SYSTEM VALUES
'455': lambda data: [
	('Mz_reference'	 , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100.0), 
	('Yaw_rate_ref'	 , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100.0)
],
#ECU GPS LONGITUDE AND LATITUDE
'456': lambda data: [
	('GPS_LONGITUDE'	, int(get_byte(data, 0) + get_byte(data, 1) + get_byte(data, 2) + get_byte(data, 3),16) / 1000000.0), 
	('GPS_LATITUDE'	 	, int(get_byte(data, 4) + get_byte(data, 5) + get_byte(data, 6) + get_byte(data, 7),16) / 1000000.0)
],
#ECU YAW RATE, YAW ACCELERATION
'458': lambda data: [
	('Yaw_rate'	 	, hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 1000.0), 
	('Yaw acc'		, hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100.0)
],
#ECU ACCELERATIONS, INS Vx and Vy
'459': lambda data: [
	('Ax'	 	, hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100.0), 
	('Ay'		, hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100.0),
	('INS_Vx'	, hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 100.0),
	('INS_Vy'	, hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 100.0)
],
#ECU GPS FIX AND NUMBER OF TRACKED SATELITES
'45B': lambda data: [
	('GPS_FIX'	 	, int(get_byte(data, 0), 16)), 
	('NR_TR_SAT'	, int(get_byte(data, 1), 16))
],
#ECU, ATTITUDE AND INS STATUS
'45A': lambda data: [
	('STATUS_ATTITUDE'	 	, hex_to_uint16(get_byte(data, 0) + get_byte(data, 1))),
	('STATUS_INS'			, int(get_byte(data, 2),16))
],
#ECU, FILTERED STEERING WHEEL ANGLE, AND SPEED
'45F': lambda data: [
	('ECU_STW_Angle'	 	, hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) * 0.0573),
	('ECU_STW_Speed'		, hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) * 0.573)
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
    ('GLV_vtg5'       , int(get_byte(data,3) + get_byte(data,2),16)  / 10000.0)
],

'462': lambda data: [
    ('GLV_tmp0'       , int(get_byte(data,1) + get_byte(data,0),16)  / 100.0), 
    ('GLV_vmp1'       , int(get_byte(data,3) + get_byte(data,2),16)  / 100.0),
    ('GLV_tmp2'       , int(get_byte(data,5) + get_byte(data,4),16)  / 100.0),
    ('GLV_tmp3'       , int(get_byte(data,7) + get_byte(data,6),16)  / 100.0)
],
'463': lambda data: [
    ('GLV_tmp4'       , int(get_byte(data,1) + get_byte(data,0),16)  / 100.0)
],

'465': lambda data: [
    ('GLV_minVtg'       , int(get_byte(data,1) + get_byte(data,0),16)  / 10000.0), 
    ('GLV_maxVtg'       , int(get_byte(data,3) + get_byte(data,2),16)  / 10000.0),
    ('GLV_totVtg'       , int( get_byte(data,7) + get_byte(data,6) + get_byte(data,5) + get_byte(data,4), 16) / 10000.0 )
],

'466': lambda data: [
    ('GLV_minTemp'       , int(get_byte(data,1) + get_byte(data,0),16)  / 100.0),
    ('GLV_maxTemp'       , int(get_byte(data,3) + get_byte(data,2),16)  / 100.0),
    ('GLV_current'       , int(get_byte(data,7) + get_byte(data,6),16)  / 1000.0)
],

#AMK INVERTERS

#AMK SETPOINTS FROM ECU
'185': lambda data: [
	('AMK_FL_control',			hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_FL_RPM_setpoint',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_FL_torque_pos',		hex_to_int16(get_byte(data,4)+get_byte(data,5)) / 100.0	),
	('AMK_FL_torque_neg',		hex_to_int16(get_byte(data,6)+get_byte(data,7)) / 100.0	)
],

'186': lambda data: [
	('AMK_FR_control',			hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_FR_RPM_setpoint',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_FR_torque_pos',		hex_to_int16(get_byte(data,4)+get_byte(data,5)) / 100.0	),
	('AMK_FR_torque_neg',		hex_to_int16(get_byte(data,6)+get_byte(data,7)) / 100.0	)
],

'189': lambda data: [
	('AMK_RL_control',			hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_RL_RPM_setpoint',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_RL_torque_pos',		hex_to_int16(get_byte(data,4)+get_byte(data,5)) / 100.0	),
	('AMK_RL_torque_neg',		hex_to_int16(get_byte(data,6)+get_byte(data,7)) / 100.0	)
],

'18A': lambda data: [
	('AMK_RR_control',			hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_RR_RPM_setpoint',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_RR_torque_pos',		hex_to_int16(get_byte(data,4)+get_byte(data,5)) / 100.0	),
	('AMK_RR_torque_neg',		hex_to_int16(get_byte(data,6)+get_byte(data,7)) / 100.0	)
],
#AMK Actual Values 1
'284': lambda data: [
	('AMK_FL_STATUS',					hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_FL_Actual_velocity',			hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_FL_Torque_current',			hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0067),
	('AMK_FL_Magnetizing_current',		hex_to_int16(get_byte(data,6)+get_byte(data,7))	* 0.0067),
	('AMK_FL_Motor_torque',				hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0025)
],
#AMK Actual Values 2
'286': lambda data: [
	('AMK_FL_Temp_Motor',		hex_to_int16(get_byte(data,0)+get_byte(data,1)) / 10.0	),
	('AMK_FL_Temp_Inverter',	hex_to_int16(get_byte(data,2)+get_byte(data,3)) / 10.0	),		
	('AMK_FL_Error_info',	    hex_to_uint16(get_byte(data,4)+get_byte(data,5))		),
	('AMK_FL_Temp_IGBT',		hex_to_int16(get_byte(data,6)+get_byte(data,7)) / 10.0	)
],

#AMK Actual Values 1
'285': lambda data: [
	('AMK_FR_STATUS',				hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_FR_Actual_velocity',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_FR_Torque_current',			hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0067),
	('AMK_FR_Magnetizing_current',		hex_to_int16(get_byte(data,6)+get_byte(data,7))	* 0.0067),
	('AMK_FR_Motor_torque',				hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0025)
],
#AMK Actual Values 2
'287': lambda data: [
	('AMK_FR_Temp_Motor',		hex_to_int16(get_byte(data,0)+get_byte(data,1))/10.0	),
	('AMK_FR_Temp_Inverter',	hex_to_int16(get_byte(data,2)+get_byte(data,3))/10.0	),		
	('AMK_FR_Error_info',		hex_to_uint16(get_byte(data,4)+get_byte(data,5))		),
	('AMK_FR_Temp_IGBT',		hex_to_int16(get_byte(data,6)+get_byte(data,7))/10.0	)
],

#AMK Actual Values 1
'288': lambda data: [
	('AMK_RL_STATUS',				hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_RL_Actual_velocity',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_RL_Torque_current',			hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0067),
	('AMK_RL_Magnetizing_current',		hex_to_int16(get_byte(data,6)+get_byte(data,7))	* 0.0067),
	('AMK_RL_Motor_torque',				hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0025)
],
#AMK Actual Values 2
'28A': lambda data: [
	('AMK_RL_Temp_Motor',		hex_to_int16(get_byte(data,0)+get_byte(data,1))/10.0	),
	('AMK_RL_Temp_Inverter',		hex_to_int16(get_byte(data,2)+get_byte(data,3))/10.0	),		
	('AMK_RL_Error_info',		hex_to_uint16(get_byte(data,4)+get_byte(data,5))		),
	('AMK_RL_Temp_IGBT',		hex_to_int16(get_byte(data,6)+get_byte(data,7))/10.0	)
],

#AMK Actual Values 1
'289': lambda data: [
	('AMK_RR_STATUS',				hex_to_uint16(get_byte(data,0)+get_byte(data,1))	),
	('AMK_RR_Actual_velocity',		hex_to_int16(get_byte(data,2)+get_byte(data,3))	),
	('AMK_RR_Torque_current',			hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0067),
	('AMK_RR_Magnetizing_current',		hex_to_int16(get_byte(data,6)+get_byte(data,7))	* 0.0067),
	('AMK_RR_Motor_torque',				hex_to_int16(get_byte(data,4)+get_byte(data,5)) * 0.0025)
],
#AMK Actual Values 2
'28B': lambda data: [
	('AMK_RR_Temp_Motor',		hex_to_int16(get_byte(data,0)+get_byte(data,1))/10.0	),
	('AMK_RR_Temp_Inverter',		hex_to_int16(get_byte(data,2)+get_byte(data,3))/10.0	),		
	('AMK_RR_Error_info',		hex_to_uint16(get_byte(data,4)+get_byte(data,5))		),
	('AMK_RR_Temp_IGBT',		hex_to_int16(get_byte(data,6)+get_byte(data,7))/10.0	)
],


#FAN CONTROL STATUS
'4B0': lambda data: [
	('Battery_fans_dutycycle',	int(get_byte(data,0),16) ),
	('Radiator_fans_dutycycle',	int(get_byte(data,1),16) ),
	('Pump_state',			int(get_byte(data,2),16) ),
	('Fan_ctrl_mode',		int(get_byte(data,3),16) ),
	('12V_state',			int(get_byte(data,4),16) )
],


}

