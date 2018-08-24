# Chapter 01: Exploring your data

## 1. Loading and viewing your data
In this chapter, you're going to look at a subset of the Department of Buildings Job Application Filings dataset from the NYC Open Data portal. This dataset consists of job applications filed on January 22, 2017.

Your first task is to load this dataset into a DataFrame and then inspect it using the .head() and .tail() methods. However, you'll find out very quickly that the printed results don't allow you to see everything you need, since there are too many columns. Therefore, you need to look at the data in another way.

The .shape and .columns attributes let you see the shape of the DataFrame and obtain a list of its columns. From here, you can see which columns are relevant to the questions you'd like to ask of the data. To this end, a new DataFrame, df_subset, consisting only of these relevant columns, has been pre-loaded. This is the DataFrame you'll work with in the rest of the chapter.

Get acquainted with the dataset now by exploring it with pandas! This initial exploratory analysis is a crucial first step of data cleaning.

### Instructions:
* Import pandas as pd.
* Read 'dob_job_application_filings_subset.csv' into a DataFrame called df.
* Print the head and tail of df.
* Print the shape of df and its columns. Note: .shape and .columns are attributes, not methods, so you don't need to follow these with parentheses ().
* Hit 'Submit Answer' to view the results! Notice the suspicious number of 0 values. Perhaps these represent missing data.

#### Script:
```
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())

```
#### Output:
```
<script.py> output:
           Job #  Doc #        Borough       House #  \
    0  121577873      2      MANHATTAN  386            
    1  520129502      1  STATEN ISLAND  107            
    2  121601560      1      MANHATTAN  63             
    3  121601203      1      MANHATTAN  48             
    4  121601338      1      MANHATTAN  45             
    
                            Street Name  Block  Lot    Bin # Job Type Job Status  \
    0  PARK AVENUE SOUTH                   857   38  1016890       A2          D   
    1  KNOX PLACE                          342    1  5161350       A3          A   
    2  WEST 131 STREET                    1729    9  1053831       A2          Q   
    3  WEST 25TH STREET                    826   69  1015610       A2          D   
    4  WEST 29 STREET                      831    7  1015754       A3          D   
    
                ...                         Owner's Last Name  \
    0           ...            MIGLIORE                         
    1           ...            BLUMENBERG                       
    2           ...            MARKOWITZ                        
    3           ...            CASALE                           
    4           ...            LEE                              
    
                  Owner's Business Name Owner's House Number  \
    0  MACKLOWE MANAGEMENT                      126            
    1  NA                                       107            
    2  635 RIVERSIDE DRIVE NY LLC               619            
    3  48 W 25 ST LLC C/O BERNSTEIN             150            
    4  HYUNG-HYANG REALTY CORP                  614            
    
               Owner'sHouse Street Name            City  State    Zip  \
    0  EAST 56TH STREET                  NEW YORK           NY  10222   
    1  KNOX PLACE                        STATEN ISLAND      NY  10314   
    2  WEST 54TH STREET                  NEW YORK           NY  10016   
    3  WEST 30TH STREET                  NEW YORK           NY  10001   
    4  8 AVENUE                          NEW YORK           NY  10001   
    
      Owner'sPhone #                                    Job Description  \
    0     2125545837  GENERAL MECHANICAL & PLUMBING MODIFICATIONS AS...   
    1     3477398892  BUILDERS PAVEMENT PLAN 143 LF.                ...   
    2     2127652555  GENERAL CONSTRUCTION TO INCLUDE NEW PARTITIONS...   
    3     2125941414  STRUCTURAL CHANGES ON THE 5TH FLOOR (MOONDOG E...   
    4     2019881222  FILING HEREWITH FACADE REPAIR PLANS. WORK SCOP...   
    
                   DOBRunDate  
    0  04/26/2013 12:00:00 AM  
    1  04/26/2013 12:00:00 AM  
    2  04/26/2013 12:00:00 AM  
    3  04/26/2013 12:00:00 AM  
    4  04/26/2013 12:00:00 AM  
    
    [5 rows x 82 columns]
               Job #  Doc #        Borough       House #  \
    12841  520143988      1  STATEN ISLAND  8              
    12842  121613833      1      MANHATTAN  724            
    12843  121681260      1      MANHATTAN  350            
    12844  320771704      1       BROOKLYN  499            
    12845  520143951      1  STATEN ISLAND  1755           
    
                                Street Name  Block  Lot    Bin # Job Type  \
    12841  NOEL STREET                        5382   20  5069722       A2   
    12842  10 AVENUE                          1059    4  1082503       A2   
    12843  MANHATTAN AVE.                     1848   31  1055849       A2   
    12844  UNION STREET                        431   43  3007185       A2   
    12845  RICHMOND ROAD                       887   28  5022931       A2   
    
          Job Status           ...                         Owner's Last Name  \
    12841          D           ...            MALITO                           
    12842          D           ...            CROMAN                           
    12843          A           ...            ARYEH                            
    12844          D           ...            WIGGINS                          
    12845          D           ...            CAMBRIA                          
    
                      Owner's Business Name Owner's House Number  \
    12841  GENO MALITO                              8              
    12842  722-724 10TH AVENUE HOLDING LLC          632            
    12843  DG UWS LLC                               619            
    12844  N/A                                      77             
    12845  RONALD CAMBRIA                           1755           
    
                   Owner'sHouse Street Name            City  State    Zip  \
    12841  NOEL STREET                       STATEN ISLAND      NY  10312   
    12842  BROADWAY                          NEW YORK           NY  10012   
    12843  WEST 54TH STREET                  NEW YORK           NY  10019   
    12844  PROSPECT PLACE                    BROOKLYN           NY  11217   
    12845  RICHMOND ROAD                     STATEN ISLAND      NY  10304   
    
          Owner'sPhone #                                    Job Description  \
    12841     9174685659  HORIZONTAL ENLARGEMENT OF ATTACHED ONE CAR GAR...   
    12842     2122289300  RENOVATION OF EXISTING APARTMENT #3B ON THIRD ...   
    12843     2127652555  REPLACE BURNER IN EXSTG BOILER WITH NEW GAS BU...   
    12844     9178487799  INSTALL NEW SPRINKLER SYSTEM THROUGHOUT THE BU...   
    12845     7184482740  INTERIOR PARTITIONS AND MINOR PLUMBING WORK TO...   
    
                       DOBRunDate  
    12841  06/13/2013 12:00:00 AM  
    12842  06/13/2013 12:00:00 AM  
    12843  06/13/2013 12:00:00 AM  
    12844  06/13/2013 12:00:00 AM  
    12845  06/13/2013 12:00:00 AM  
    
    [5 rows x 82 columns]
    (12846, 82)
    Index(['Job #', 'Doc #', 'Borough', 'House #', 'Street Name', 'Block', 'Lot',
           'Bin #', 'Job Type', 'Job Status', 'Job Status Descrp',
           'Latest Action Date', 'Building Type', 'Community - Board', 'Cluster',
           'Landmarked', 'Adult Estab', 'Loft Board', 'City Owned', 'Little e',
           'PC Filed', 'eFiling Filed', 'Plumbing', 'Mechanical', 'Boiler',
           'Fuel Burning', 'Fuel Storage', 'Standpipe', 'Sprinkler', 'Fire Alarm',
           'Equipment', 'Fire Suppression', 'Curb Cut', 'Other',
           'Other Description', 'Applicant's First Name', 'Applicant's Last Name',
           'Applicant Professional Title', 'Applicant License #',
           'Professional Cert', 'Pre- Filing Date', 'Paid', 'Fully Paid',
           'Assigned', 'Approved', 'Fully Permitted', 'Initial Cost',
           'Total Est. Fee', 'Fee Status', 'Existing Zoning Sqft',
           'Proposed Zoning Sqft', 'Horizontal Enlrgmt', 'Vertical Enlrgmt',
           'Enlargement SQ Footage', 'Street Frontage', 'ExistingNo. of Stories',
           'Proposed No. of Stories', 'Existing Height', 'Proposed Height',
           'Existing Dwelling Units', 'Proposed Dwelling Units',
           'Existing Occupancy', 'Proposed Occupancy', 'Site Fill', 'Zoning Dist1',
           'Zoning Dist2', 'Zoning Dist3', 'Special District 1',
           'Special District 2', 'Owner Type', 'Non-Profit', 'Owner's First Name',
           'Owner's Last Name', 'Owner's Business Name', 'Owner's House Number',
           'Owner'sHouse Street Name', 'City ', 'State', 'Zip', 'Owner'sPhone #',
           'Job Description', 'DOBRunDate'],
          dtype='object')
           Job #  Doc #        Borough Initial Cost Total Est. Fee  \
    0  121577873      2      MANHATTAN    $75000.00        $986.00   
    1  520129502      1  STATEN ISLAND        $0.00       $1144.00   
    2  121601560      1      MANHATTAN    $30000.00        $522.50   
    3  121601203      1      MANHATTAN     $1500.00        $225.00   
    4  121601338      1      MANHATTAN    $19500.00        $389.50   
    
       Existing Zoning Sqft  Proposed Zoning Sqft  Enlargement SQ Footage  \
    0                     0                     0                       0   
    1                     0                     0                       0   
    2                     0                     0                       0   
    3                     0                     0                       0   
    4                     0                     0                       0   
    
       Street Frontage  ExistingNo. of Stories  Proposed No. of Stories  \
    0                0                       0                        0   
    1              143                       0                        0   
    2                0                       5                        5   
    3                0                      12                       12   
    4                0                       6                        6   
    
       Existing Height  Proposed Height  
    0                0                0  
    1                0                0  
    2               54               54  
    3              120              120  
    4               64               64  
               Job #  Doc #        Borough Initial Cost Total Est. Fee  \
    12841  520143988      1  STATEN ISLAND    $30700.00        $448.62   
    12842  121613833      1      MANHATTAN    $62000.00        $852.10   
    12843  121681260      1      MANHATTAN   $166000.00       $1923.30   
    12844  320771704      1       BROOKLYN    $65000.00        $883.00   
    12845  520143951      1  STATEN ISLAND     $9500.00        $316.50   
    
           Existing Zoning Sqft  Proposed Zoning Sqft  Enlargement SQ Footage  \
    12841                  1490                  1782                     206   
    12842                     0                     0                       0   
    12843                     0                     0                       0   
    12844                     0                     0                       0   
    12845                     0                     0                       0   
    
           Street Frontage  ExistingNo. of Stories  Proposed No. of Stories  \
    12841                0                       1                        1   
    12842                0                       5                        5   
    12843                0                       6                        6   
    12844                0                       1                        1   
    12845                0                       1                        1   
    
           Existing Height  Proposed Height  
    12841               10               10  
    12842               55               55  
    12843               64               64  
    12844               18               18  
    12845               18               18
```

##### Comment:
Great work! In addition to the suspicious number of 0 values, which may represent missing data, notice that the columns that contain monetary values - 'Initial Cost' and 'Total Est. Fee' - have a dollar sign in the beginning. These columns may be coded as strings instead of numeric values. You will check this in the next exercise.
