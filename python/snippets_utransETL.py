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
        
        
        
#### BEGIN >>> CALL VALIDATE FUNCTIONS ####
## AN_NAME #
if row.ACS_NAME != "":
    # call the validation function
    an_Name, an_PostDir = Validate_AN_NAME(row.ACS_NAME)
    # AN_NAME
    row.AN_NAME = an_Name            

    # AN_POSTDIR
    if an_PostDir != "":
        row.AN_POSTDIR = an_PostDir
    else:
        row.AN_POSTDIR = row.ACS_SUF
                    
#### CALL VALIDATE FUNCTIONS << END ####                    
