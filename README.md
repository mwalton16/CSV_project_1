# matplotlib_csv
Advanced Python - Matplotlib - using CSV files

this project is to teach students how to use CSV files in python
this project also teaches students how to visualize the data using matplotlib

# Open Files
The Sitka and Death Valley files are opened in the reader format. The CSV library is then used to transcribe the data to csv_sitka and csv_dv

# Create Index Dictionaries and Lists
I create two dictionaries, one for each file. The purpose of the dictionary is to assign each column title to an index value so that the column number can be referenced in the for loop. Each column header is a key and the index number is the value.

# Data Collection
Because we are pulling the highs and lows for each location, the corresponding values for 'TMAX' and 'TMIN' in their respective dictionaries are chosen for the plot data columns.

For each file, a try function is written. The try function attempts to return the high and low for each file for each observation and then append it to the previously created lists. Only the Sitka for loop appends the date to a list because it would be redundant otherwise.

### Plot Creation
Two subplots are created: one for each location. The highs and lows for each location are pulled, with the highs being drawn in red and the lows being drawn in blue. Each plot gets a title and a supertitle is written at the end.