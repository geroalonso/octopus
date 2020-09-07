from num_to_cur import num_to_cur #my own module 
from property_objects import *
from date import dif_dates

#defining variables
print('''List of Corporation Names: biscayne, doral_cuerpo_1, doral_cuerpo_2,
	plantation, sample, oaktree, hiawassee, portrichey''')
prop = input('Please Enter Property name: ')
corporation = prop.corporation
buildingaddress = prop.address
unit = input('Please Enter Unit: ')
unitsize = input('Please Enter Unit Size: ')
corpaddress = '12955 Biscayne Boulevard, Suite 406B, North Miami, FL 33181'


tenant = input('Please Enter Tenant Name: ')
tenantaddress = input('Please Enter Tenant Address:')
tenantpersonalguarantor = input('Please Enter Personal Guarantor: ')
guarantorssn = input('Please Enter Personal Guarantor SSN: ')


commencementdate = input('Please Enter Commencement Date d/m/yyyy: ')
com_day, com_month, com_year  = commencementdate.split('/')
expirationdate = input('Please Enter Commencement Date d/m/yyyy: ')
exp_day, exp_month, exp_year  = expirationdate.split('/')
leaseterm = dif_dates(int(com_day), int(com_month), int(com_year), int(exp_day), int(exp_month), int(exp_year))


rentcommencementdate = input('Please Enter Rent Commencement Date d/m/yyyy: ')
baserent = input('Please Enter Base Rent: ')
securitydepositnumbers = float(input('Please Enter Security Deposit without $: '))
securitydepositwords = num_to_cur(security_deposit_numbers)
use = input('Please Enter Use: ')
noticeemail = input('Please Enter Notice Email: ')
landlordwork = input('Please Enter Landlord Work: ')
liabilityinsurance = str(r'One Million Dollars ($1,000,000.00)')
propertyinsurance = str(r'One Million Dollars ($1,000,000.00)')
county = prop.county
cam = prop.cam

exhibit = input('Please Enter Exhibit Name (none): ')
if exhibit != 'none': 
	#create figure on site

brokername = input('Please Enter Broker Name (none): ')
if broker_name != 'none':
	comsplit = input('Please Enter Commission Split (none): ')
	#create clause 

opt_to_renew = input('Is there an Option to Renew? (y/n)')
if opt_to_renew == 'y':
	#create clause


gross_rent = input('Is the lease gross? (y/n): ')
if add_rent == 'n':
	#add clause of additional rent

exclusivity = input('Is use exclusive? (y/n):')
if exclusivity == 'y':
	#add clause of exclusivity 











