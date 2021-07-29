import arcpy

#: Pass in county number and get county name.
def get_countyname(county_number):
    county_name = ''

    if county_number == 49039:
        county_name = 'SANPETE'
    if county_number == 49021:
        county_name = 'IRON'
    if county_number == 49025:
        county_name = 'KANE'
    if county_number == 49057:
        county_name = 'WEBER'
    if county_number == 49037:
        county_name = 'SAN_JUAN'
    if county_number == 49017:
        county_name = 'GARFIELD'
    if county_number == 49033:
        county_name = 'RICH'
    if county_number == 49043:
        county_name = 'SUMMIT'
    if county_number == 49045:
        county_name = 'TOOELE'
    if county_number == 49001:
        county_name = 'BEAVER'
    if county_number == 49003:
        county_name = 'BOX_ELDER'
    if county_number == 49005:
        county_name = 'CACHE'
    if county_number == 49047:
        county_name = 'UINTAH'
    if county_number == 49019:
        county_name = 'GRAND'
    if county_number == 49053:
        county_name = 'WASHINGTON'
    if county_number == 49027:
        county_name = 'MILLARD'
    if county_number == 49051:
        county_name = 'WASATCH'
    if county_number == 49023:
        county_name = 'JUAB'
    if county_number == 49049:
        county_name = 'UTAH'
    if county_number == 49013:
        county_name = 'DUCHESNE'
    if county_number == 49009:
        county_name = 'DAGGETT'
    if county_number == 49031:
        county_name = 'PIUTE'
    if county_number == 49011:
        county_name = 'DAVIS'
    if county_number == 49029:
        county_name = 'MORGAN'
    if county_number == 49055:
        county_name = 'WAYNE'
    if county_number == 49015:
        county_name = 'EMERY'
    if county_number == 49041:
        county_name = 'SEVIER'
    if county_number == 49007:
        county_name = 'CARBON'
    if county_number == 49035:
        county_name = 'SALT_LAKE'

    if county_name == '':
        return "NotFound"
    else:
        return county_name


#: Pass in county name and get county number.
def get_countyid(county_name):
    county_number = ''

    if county_name == 'SANPETE':
        county_number = 49039
    if county_name == 'IRON':
        county_number = 49021
    if county_name == 'KANE':
        county_number = 49025
    if county_name == 'WEBER':
        county_number = 49057
    if county_name == 'SAN_JUAN':
        county_number = 49037
    if county_name == 'GARFIELD':
        county_number = 49017
    if county_name == 'RICH':
        county_number = 49033
    if county_name == 'SUMMIT':
        county_number = 49043
    if county_name == 'TOOELE':
        county_number = 49045
    if county_name == 'BEAVER':
        county_number = 49001
    if county_name == 'BOX_ELDER':
        county_number = 49003
    if county_name == 'CACHE':
        county_number = 49005
    if county_name == 'UINTAH':
        county_number = 49047
    if county_name == 'GRAND':
        county_number = 49019
    if county_name == 'WASHINGTON':
        county_number = 49053
    if county_name == 'MILLARD':
        county_number = 49027
    if county_name == 'WASATCH':
        county_number = 49051
    if county_name == 'JUAB':
        county_number = 49023
    if county_name == 'UTAH':
        county_number = 49049
    if county_name == 'DUCHESNE':
        county_number = 49013
    if county_name == 'DAGGETT':
        county_number = 49009
    if county_name == 'PIUTE':
        county_number = 49031
    if county_name == 'DAVIS':
        county_number = 49011
    if county_name == 'MORGAN':
        county_number = 49029
    if county_name == 'WAYNE':
        county_number = 49055
    if county_name == 'EMERY':
        county_number = 49015
    if county_name == 'SEVIER':
        county_number = 49041
    if county_name == 'CARBON':
        county_number = 49007
    if county_name == 'SALT_LAKE':
        county_number = 49035

    if county_number == '':
        return "NotFound"
    else:
        return county_number
