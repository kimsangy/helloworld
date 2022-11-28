
#github link : https://github.com/kimsangy/DSCI510-Final-Project
#readme link : https://github.com/kimsangy/DSCI510-Final-Project/blob/main/README.md
#requirment.txt link : https://github.com/kimsangy/DSCI510-Final-Project/blob/main/requirements.txt
import requests
import re
import pandas as pd

pd.options.display.float_format = '{:.5f}'.format
pd.set_option('mode.chained_assignment',  None)

def world_cup_host_countries_from_file(filename): #host_Countries
    csv = pd.read_csv(filename)
 #  print(csv)
    temp_dic = {}

    for i in range(len(csv)):
        temp_string = csv['tournament_name'][i].split()

        temp_dic[csv['key_id'][i] ] = [csv['team_code'][i], temp_string[0]]

    df = pd.DataFrame.from_dict(temp_dic, orient = 'index', columns = ['TEAM_CODE', 'HOST_YEAR'])

    df['BEFORE_YEAR_GDP'] = 0
    df['HOST_YEAR_GDP'] = 0    
    df['AFTER_YEAR_GDP'] = 0

 #   print(df)
    df.replace(to_replace= 'ENG', value ='GBR', inplace=True)

    return df

def world_cup_qulified_teams_data_from_file(filename): #Participating_Countries
    csv = pd.read_csv(filename)
    temp_dic = {}

#    print(len(csv))

    for i in range(len(csv)):
 #       print(csv['team_code'][i])
 
        if csv['team_code'][i] not in temp_dic:
            temp_dic[csv['team_code'][i]] = 1
        else :
            temp_dic[csv['team_code'][i]] = temp_dic[csv['team_code'][i]] + 1


    df = pd.DataFrame()
    df['TEAM_CODE'] = temp_dic.keys()
    df['NUM'] = temp_dic.values()
 #   print(df)
    df['2020_GDP'] = 0
    df['2021_GDP'] = 0
    df.replace(to_replace= 'ENG', value ='GBR', inplace=True)

    
    return df
    
    


def gdp_data_from_file(filename):
    csv = pd.read_csv(filename, skiprows=4)
 #   print(csv)
    return(csv)



def make_new_dataset1_qualified_teams_gdp(filename2,filename3):
    df1 = world_cup_qulified_teams_data_from_file(filename2)
 
 
    df2 = gdp_data_from_file(filename3)

    for i in range(len(df2)):
        for j in range(len(df1)):
            if df2['Country Code'][i] == df1['TEAM_CODE'][j]:
                df1['2020_GDP'][j] = df2['2020'][i]                
                df1['2021_GDP'][j] = df2['2021'][i]
#    print(df1)

    df1.to_csv("./output_data/dataset1_Participating_Countries_GDP.csv")


def make_new_dataset2_host_teams_gdp(filename1,filename3):
    df1 = world_cup_host_countries_from_file(filename1)
    df2 = gdp_data_from_file(filename3)

    for i in range(len(df2)):
          for j in range(1,len(df1)+1):      
            if df2['Country Code'][i] == df1['TEAM_CODE'][j]:
                if(int(df1['HOST_YEAR'][j]) >= 1960):
                    before_year = int(df1['HOST_YEAR'][j])-1
                    host_year = int(df1['HOST_YEAR'][j])
                    after_year = int(df1['HOST_YEAR'][j])+1                   
                    df1['BEFORE_YEAR_GDP'][j] = df2[str(before_year)][i]
                    df1['HOST_YEAR_GDP'][j] = df2[str(host_year)][i]                               
                    df1['AFTER_YEAR_GDP'][j] = df2[str(after_year)][i]

 #   print(df1)
    df1.to_csv("./output_data/dataset2_Hosting_Countries_GDP.csv")




if __name__ == '__main__':

    filename1 = "source_data/host_countries.csv"                            # 1. World_Cup_Data from kaggle
    filename2 = "source_data/qualified_teams.csv"                           # https://www.kaggle.com/datasets/joshfjelstul/world-cup-database
    filename3 = "source_data/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_4701206.csv"  # 2. GDP per capita from world bank 
                                                                            # https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
    make_new_dataset1_qualified_teams_gdp(filename2,filename3)
    make_new_dataset2_host_teams_gdp(filename1,filename3)


    