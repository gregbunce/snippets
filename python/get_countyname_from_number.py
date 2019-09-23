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
