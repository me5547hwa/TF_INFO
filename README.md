
    mjdb_14000_data_cleaned.csv is cleaned on Fri Dec 11 18:54:20 2020.

    The data was downloaded from meijao database, including 14000 samples(patients).
    
    The following variants(columns) has been selected and cleaned.

    All null values were kept null.|n
    For numeric data, values out of selected range were set to -999.

    For categorical data, values out of selected categories were labeled as Z.

    
    "pid" representing "patient id" was kept.

    "yr" representing "year" was kept.

    "age" representing "patient age" was treated as numeric data, 0 < age <= 100.

    "gender" representing "patient gender" was treated as categorical data, (1): male, (2): female.

    "g_hei" representing "patient height" was treated as numeric data, 0 < g_hei <= 200.

    "g_wei" representing "patient weight" was treated as numeric data, 0 < g_wei <= 150.

    "g_wei" representing "patient bmi" was treated as numeric data, 0 < g_bmi <= 150.

    "g_wei" representing "right hand systolic blood pressure" was treated as numeric data, 60 < g_ssr <= 300.

    
    "drinkornot_96" representing "How often do you drink?" was treated as categorical data, (1): never or almost never, (2): has quit alcohol now, (3)sometimes, (4) often, (5) everyday.

    "drinkornot_97", "drinkornot_98", "drinkornot_17" all representing "How often do you drink weekly?" were treated as categorical data, (1): never or less than 1, (2): has quit alcohol now, (3)once or twice, (4) 3-4 times, (5) everyday.

    The 4 mentioned above were combined to one category "drinkornot" since most of them have similar standard.

    
    "psick09" representing "Have you been diagnosed with high blood pressure" was treated as categorical data, (0): no, (1): yes.

    "psick10" representing "Have you been diagnosed with diabetes?" was treated as categorical data, (0): no, (1): yes.

    "psick11" representing "Have you been diagnosed with stroke?" was treated as categorical data, (0): no, (1): yes.

    
    "mdrug07" representing "Have you been taking hyperlipidemia drugs" was treated as categorical data, (0): no, (1): yes.

    This column is selected to indicate whether the patient is diagnosed with hyperlipidemia, since the exact question  only exists in the 2017 version.

    