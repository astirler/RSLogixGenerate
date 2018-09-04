# RSLogixGenerate
Generate RSLogix5000 code and tags from an excel spreadsheet

1. Create the spreadsheet. Each row below row 1 (header data) represents the replacement value for the corresponding strategy. For each       strategy you have, create a sheet. If you have a strategy that is called Motor, rename that tab to match the name exactly. For the       strategy description use RoutineDescript in the column name and the strategy routine description in RSLogix5000. For the strategy         renaming in the generation, create a column with the same name as the tab e.g. Motor and put the replacement name for the strategy in     the column below.

    Each replacement that is done checks for the ":"  to be located in the cell. When found it creates a description, so if                   MotorStarter_01 replacement was PC_2443:Tank 456 outlet pump. The description would be Tank 456 outlet pump. The only REQUIRED           replacement is the strategy name which in this example is MotorControl. There can be as many columns as needed. Any column with an       empty cell leaves the tag that it represents unchanged.


2. Create the code samples in RSLogix5000. For example if you have a strategy that is used for motor control export that routine. If you 
    have a strategy for a two position valve export that routine. You can do 1 or more.
    
3. Once the strategies are duplicated and exported to the same file as the folder containing the strategies to a folder called Output.
    each strategy will need to be imported into the project. As the imports are done the tags are created and the routines are imported 
    into the program that it was generated in. These can easliy be moved from there to any other program that you wish.
