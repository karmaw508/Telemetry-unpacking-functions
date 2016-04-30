#get_byte = lambda message, byte: message[byte*2:byte*2+2]
#get_bit = lambda byte, bit: (byte & (2**bit)) >> bit


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
    ('GLVBMS_temp_4', int(data, 16))
],

'625': lambda data: [
    ('GLVBMS_current', int(data, 16))
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

#R16 mechanical data 1
'290': lambda data: [
    ('R16[1]_current_speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[1]_speed_setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[1]_torque_setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 mechanical data 2
'294': lambda data: [
    ('R16[2]_current_speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[2]_speed_setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[2]_torque_setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 mechanical data 3
'298': lambda data: [
    ('R16[3]_current_speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[3]_speed_setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[3]_torque_setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 mechanical data 4
'29C': lambda data: [
    ('R16[4]_current_speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[4]_speed_setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[4]_torque_setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 temp data
'291': lambda data: [
    ('R16[1]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[1]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[1]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[1]_motor_temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],
	
#R16 temp data		
'295': lambda data: [		
    ('R16[2]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[2]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[2]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[2]_motor_temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],
	
#R16 temp data		
'299': lambda data: [		
    ('R16[3]_temp_1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[3]_temp_2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[3]_temp_3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[3]_motor_temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
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
    ('R16[1]_torque_current' 		, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[1]_direct_current' 		, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[1]_DC_current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[1]_DC_voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16) / 100)
],

#R16 Electrical data
'296': lambda data: [
    ('R16[2]_torque_current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[2]_direct_current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[2]_DC_current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[2]_DC_voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16) / 100)
],

#R16 Electrical data
'29A': lambda data: [
    ('R16[3]_torque_current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[3]_direct_current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[3]_DC_current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[3]_DC_voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16) / 100)
],

#R16 Electrical data
'29E': lambda data: [
    ('R16[4]_torque_current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[4]_direct_current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[4]_DC_current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[4]_DC_voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16) / 100)
],

#R16 Status data
'293': lambda data: [
	('R16[1]_status_bit_{0}'.format(i) 	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32)
	]+[
    ('R16[1]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32, 64)
],

#R16 Status data
'297': lambda data: [
	('R16[2]_status_bit_{0}'.format(i) 	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32)
    ]+[
    ('R16[2]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32, 64)
],

#R16 Status data
'29B': lambda data: [
	('R16[3]_status_bit_{0}'.format(i) 	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32)
    ]+[
    ('R16[3]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32, 64)
],

#R16 Status data
'29F': lambda data: [
	('R16[4]_status_bit_{0}'.format(i) 	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32)
    ]+[
    ('R16[4]_accumulated_status_{0}'.format(i)	, 1 if 0 != int(endian_invert(data), 32) & (2**i) else 0) for i in range(32, 64)
],

#R16 parameters
'190': lambda data: [
    ('R16[{0}]_parameter_{1}'.format(int(get_byte(data, 0)), int(get_byte(data, 1))) , int(get_byte(data, 2) + get_byte(data, 3), 16))
],
}
