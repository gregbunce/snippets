## To validate fields with Domain values use the appropriate functions, such as....                
# ValidateAndAssign_FieldValue(row, utrans_field_name, county_field_value, county_number, dict_of_valid_values)
ValidateAndAssign_FieldValue(row, "POSTTYPE", row.STREETTYPE, countyNumber, dictOfValidPostTypes)
ValidateAndAssign_FieldValue(row, "ONEWAY", row.ONEWAY_, countyNumber, dictOfValidOneWay)
ValidateAndAssign_FieldValue(row, "DOT_SRFTYP", row.SURFTYPE, countyNumber, dictOfValidSurfaceType)
ValidateAndAssign_FieldValue(row, "STATUS", row.STATUS_, countyNumber, dictOfValidStatus)

## To parse out full address and check for validated and parsed values, call the function this way...
# ParseAndAssign_FullAddress(row, field_name_to_parse, bool_primary=False, bool_alias1=False, bool_alias2=False)
ParseAndAssign_FullAddress(row, "ALIAS1", False, True, False)
