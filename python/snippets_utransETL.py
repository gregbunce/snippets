# python snippits for use in the utran ETL project

# check if valid POSTTYPE
postTypeDomain = GetCodedDomainValue(row.S_TYPE, dictOfValidPostTypes)
if postTypeDomain != "":
    row.POSTTYPE = postTypeDomain
elif postTypeDomain == "" and len(row.S_TYPE) > 1:  
    # add the post type they gave to the notes field so we can evaluate it
    row.UTRANS_NOTES = row.UTRANS_NOTES + "POSTTYPE: " + row.S_TYPE + "; "
    # add the bad domain value to the text file log
    AddBadValueToTextFile(countyNumber, "POSTTYPE", str(row.S_TYPE))


# check if valid CLASS
classDomain = GetCodedDomainValue(row.CLASS, dictOfValidRoadClass)
if classDomain != "":
    row.DOT_FCLASS = classDomain
elif classDomain == "" and (row.CLASS is not None or row.CLASS != ""):
    # add the CLASS they gave to the notes field so we can evaluate it
    row.UTRANS_NOTES = row.UTRANS_NOTES + "DOT_FCLASS: " + row.CLASS + "; "
    # add the bad domain value to the text file log
    AddBadValueToTextFile(countyNumber, "DOT_FCLASS", str(row.CLASS))
