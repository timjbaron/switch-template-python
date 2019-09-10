# Branch template configuration script

# Import switch_template file
t = open(r"switch_template.txt", "r")
tempstr = t.read()
t.close()

# Ask user for site information
print('What is the hostname of the device?')
hostname = input()

print('What is the branch IP number? Example: type 28 for 10.28.10.1')
ipxx = input()

print('What City is the branch in? Example: Paris')
city = input()

print('What State or Country is the branch in? Example: France')
state = input()

print('How many switches will the branch have?')
switch_number = int(input())

switch_dict = {}
for i in range(switch_number):
    switchnumber = i
    print("What is the serial number of switch ",i,"?")
    switch_dict.update( {switchnumber: input()})

# If more than two switches, create additional lines of configuration for port and virtual chassis
add_sw_ports = ""
add_sw_vr_chass = ""

for k, v in switch_dict.items():
    if k > 1:
        k = str(k)
        add_sw_ports += ("set interfaces interface-range access_ports member-range ge-"+k+"/0/1 to ge-"+k+"/0/47\n")
        add_sw_vr_chass += ("set virtual-chassis member "+k+" serial-number "+v+" role line-card\n")

# Concatenate city and state together
city_state = city + '-' + state

# Create dictionary that references variables in switch_template and above newly created variables 
device_values = {
    '[hostname]': hostname,
    '[xx]': ipxx,
    '[name]': city,
    '[location]': city_state,
    '[serial_1]': switch_dict[0],
    '[serial_2]': switch_dict[1],
    '/*additional_swch_ports*/': add_sw_ports, 
    '/*additional_swch_vr_chas*/': add_sw_vr_chass,
    }

# Replace the variables in switch_template with newly created variables and print
for key,val in device_values.items():
    tempstr = tempstr.replace(key,val)

print(tempstr)

    
