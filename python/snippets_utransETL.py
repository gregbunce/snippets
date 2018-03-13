# python snippits for use in the utran ETL project


#### BEGIN >> CHECK FOR VALID DOMAIN VALUES ####
# POSTTYPE #
postTypeDomain = GetCodedDomainValue(row.S_TYPE, dictOfValidPostTypes)
if postTypeDomain != "":
    row.POSTTYPE = postTypeDomain
elif postTypeDomain == "" and len(row.S_TYPE) > 1:  
    # add the post type they gave to the notes field so we can evaluate it
    row.UTRANS_NOTES = row.UTRANS_NOTES + "POSTTYPE: " + row.S_TYPE + "; "
    # add the bad domain value to the text file log
    AddBadValueToTextFile(countyNumber, "POSTTYPE", str(row.S_TYPE))

# CLASS #
classDomain = GetCodedDomainValue(row.CLASS, dictOfValidRoadClass)
if classDomain != "":
    row.DOT_FCLASS = classDomain
elif classDomain == "" and row.CLASS is not None:
    if not row.CLASS.isspace():
        # add the CLASS they gave to the notes field so we can evaluate it
        row.UTRANS_NOTES = row.UTRANS_NOTES + "DOT_FCLASS: " + row.CLASS + "; "
        # add the bad domain value to the text file log
        AddBadValueToTextFile(countyNumber, "DOT_FCLASS", str(row.CLASS))

#### CHECK FOR VALID DOMAIN VALUES << END ####        
        
        
        
#### BEGIN >>> VALIDATE AND PARSE STREETNAME VALUES ####
## AN_NAME #
# parses out '645 N' into the appropriate fields
an_Name = row.CountyFieldName

if an_Name.isdigit():
    # row.AN_NAME = an_Name
    print an_Name
else:
    # check if any of the values are numeric (maybe they added the postdir in the field)
    if any(char.isdigit() for char in an_Name):
   		# parse the streetname
        an_Name_split = an_Name.split(" ")
        # see if there's more than one word
        if len(an_Name_split) > 1:
            # check if first word is numeric
            if an_Name_split[0].isdigit():
                # this is a valid AN_NAME
                row.AN_NAME = anName_split[0]
                print an_Name_split[0]
                # check if second word is a valid AN_POSTDIR
                an_POSTDIR = an_Name_split[1].upper()
                if an_POSTDIR in ("N","S","E","W"):
                    row.AN_POSTDIR = an_POSTDIR
                    print an_POSTDIR
                    
#### VALIDATE AND PARSE STREETNAME VALUES << END ####                    
