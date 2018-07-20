## To validate fields with Domain values use the appropriate functions, such as....                
# ValidateAndAssign_FieldValue(row, utrans_field_name, county_field_value, county_number, dict_of_valid_values)
ValidateAndAssign_FieldValue(row, "POSTTYPE", row.STREETTYPE, countyNumber, dictOfValidPostTypes)
ValidateAndAssign_FieldValue(row, "ONEWAY", row.ONEWAY_, countyNumber, dictOfValidOneWay)
ValidateAndAssign_FieldValue(row, "DOT_SRFTYP", row.SURFTYPE, countyNumber, dictOfValidSurfaceType)
ValidateAndAssign_FieldValue(row, "STATUS", row.STATUS_, countyNumber, dictOfValidStatus)
ValidateAndAssign_FieldValue(row, "DOT_CLASS", row.CLASS, countyNumber, dictOfValidRoadClass)

## To parse out full address and check for validated and parsed values, call the function this way...
# ParseAndAssign_FullAdds(row, field_name_to_parse, bool_primary=False, bool_alias1=False, bool_alias2=False)
ParseAndAssign_FullAddress(row, "ALIAS1", False, True, False)

## other helper functions
HasFieldValue(field_value):
  """ example: (row.STATUS) """
    
VertLevel_TranslateOldDomainToNewDomain(row, old_vert_domain_value, county_number):
  """ example: (row, row.VERTLEVEL, countyNumber) """
  
HasValidDirection(field_value):
  """ example: (row.STATUS) """
  
## parse-out and validate no-space, numeric address (100N to 100 N)
numeric_name = ""
alias_postdir = ""
if HasFieldValue(row.ACS_ALIAS):
    numeric_name, alias_postdir = TryToParse100N(row.ACS_ALIAS)
if numeric_name != "" and alias_postdir != "":
    # the exapmle value of 100N was parsed
    row.AN_NAME = numeric_name
    if HasValidDirection(alias_postdir):
        row.AN_POSTDIR = alias_postdir
else:
    if row.ACS_ALIAS.isdigit():
        row.AN_NAME = row.ACS_ALIAS
        
## Delete row
if row.S_SURF in (400, 410, 420, 430, 440):
    rows.deleteRow(row)
    del row

