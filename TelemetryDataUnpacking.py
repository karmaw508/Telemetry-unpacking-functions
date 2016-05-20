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

'421': lambda data: [
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
    ('GLV_vtg0'       , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10000), 
    ('GLV_vtg1'       , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10000),
    ('GLV_vtg2'       , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 10000),
    ('GLV_vtg3'       , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 10000)
],
'461': lambda data: [
    ('GLV_vtg4'       , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10000), 
    ('GLV_vtg5'       , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10000),
],

'462': lambda data: [
    ('GLV_tmp0'       , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100), 
    ('GLV_vmp1'       , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100),
    ('GLV_tmp2'       , hex_to_int16(get_byte(data, 4) + get_byte(data, 5)) / 100),
    ('GLV_tmp3'       , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 100)
],
'463': lambda data: [
    ('GLV_tmp4'       , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100), 
],


'465': lambda data: [
    ('GLV_minVtg'       , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 10000), 
    ('GLV_maxVtg'       , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 10000),
    ('GLV_totVtg'       , hex_to_int16(get_byte(data, 4) + get_byte(data, 5) + get_byte(data,6) + get_byte(data,7)) / 10000),
],


'466': lambda data: [
    ('GLV_minTemp'       , hex_to_int16(get_byte(data, 0) + get_byte(data, 1)) / 100), 
    ('GLV_maxTemp'       , hex_to_int16(get_byte(data, 2) + get_byte(data, 3)) / 100),
    ('GLV_current'       , hex_to_int16(get_byte(data, 6) + get_byte(data, 7)) / 1000)
],






}

