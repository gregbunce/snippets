## To validate fields with Domain values use the appropriate functions, such as....                
ValidateAssign_POSTTYPE(row, row.S_TYPE, countyNumber)
ValidateAssign_DOT_FCLASS(row, row.S_AGFUNC, countyNumber) 
ValidateAssign_DOT_SRFTYP(row, row.S_SURF, countyNumber)


## To parse out full address and check for validated and parsed values, call the function this way...
if row.ALIAS1 is not None or row.ALIAS1 != "":
    is_valid_parse, pre_dir, street_name, post_type, post_dir = ParseFullAddress(row.ALIAS1)

    if is_valid_parse == True:
        # it WAS a valid parse
        if street_name.isdigit():
            # the street name is numeric
            row.AN_NAME = street_name
            row.AN_POSTDIR = post_dir
        else:
            # the streetname is alpha
            row.A1_PREDIR = pre_dir
            row.A1_NAME = street_name
            row.A1_POSTTYPE = post_type
            row.A1_POSTDIR = post_dir
    else:
        # it was NOT a valid parse
        row.A1_NAME = row.ALIAS1
