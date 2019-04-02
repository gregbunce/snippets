## using nested cursors and cursor field names with da cursors
# get list of field names
roads_fieldnames = [f.name for f in arcpy.ListFields(roads)]
network_roads_fieldnames = [f.name for f in arcpy.ListFields(network_roads)]
# set up nested search and insert cursors
with arcpy.da.SearchCursor(roads, '*') as search_cursor, arcpy.da.InsertCursor(network_roads, network_roads_fieldnames) as insert_cursor:
        for row in search_cursor:
            # field value from field name
            name = str(search_cursor[roads_fieldnames.index('NAME')])
            pre_dir = str(search_cursor[roads_fieldnames.index('PREDIR')])
            
            # create list of row values to insert
            insert_row_values = [name, pre_dir]
            # insert the new row with the list of values
            for insert_row in insert_row_values:
                insert_cursor.insertRow(insert_row) 
            
            
            
            



            
