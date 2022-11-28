#github link : https://github.com/kimsangy/DSCI510-Final-Project
#readme link : https://github.com/kimsangy/DSCI510-Final-Project/blob/main/README.md
#requirment.txt link : https://github.com/kimsangy/DSCI510-Final-Project/blob/main/requirements.txt
import requests
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.5f}'.format
pd.set_option('mode.chained_assignment',  None)


def pearson_correlation(a: list, b: list) -> float:
    return np.corrcoef(a,b)[0, 1]

'''
def calculate_correlation(data):
    data['2020_GDP'] = data['2020_GDP'].replace(np.nan,0)  #Countries without GDP per capita data in the WorldBank dataset were excluded.

    list1 = []  # for number of participating 
    list2 = []  # for 2020_GDP

    for i in range(len(data)):       #Put list each data
        if data['2020_GDP'][i] != 0:            #Countries without GDP per capita data in the WorldBank dataset were excluded.
                    if data['2020_GDP'][i] != 'nan':
                        list1.append(float(data['NUM'][i]))                
                        list2.append(float(data['2020_GDP'][i]))

#    print(list1)
#    print(list2)
    print(pearson_correlation(list1, list2))

'''


def get_dataset1_analysis(filename1):    #Dataset1 : Participating_Countries/2020,2021 GDP per capita 
    csv = pd.read_csv(filename1)




 #   csv.fillna(0)
    list1_group1_gdp = []   #list for 5 group average gdp
    list2_group2_gdp = []
    list3_group3_gdp = []
    list4_group4_gdp = []
    list5_group5_gdp = []

    list1_group1 = []       #list for 5 group team_code
    list2_group2 = []
    list3_group3 = []
    list4_group4 = []
    list5_group5 = []

    list1_group1_num = []       #list for 5 group number of participation
    list2_group2_num = []
    list3_group3_num = []
    list4_group4_num = []
    list5_group5_num = []


    
    for i in range(len(csv)):       #Put list each data
        if csv['2020_GDP'][i] != 0:
            if csv['NUM'][i] <=1:
                list1_group1_gdp.append(csv['2020_GDP'][i])                
                list1_group1.append(csv['TEAM_CODE'][i])
                list1_group1_num.append(csv['NUM'][i])
            elif csv['NUM'][i] > 1 and csv['NUM'][i] <= 5:
                list2_group2_gdp.append(csv['2020_GDP'][i])
                list2_group2.append(csv['TEAM_CODE'][i])   
                list2_group2_num.append(csv['NUM'][i])                           
            elif csv['NUM'][i] > 5 and csv['NUM'][i] <= 10:
                list3_group3_gdp.append(csv['2020_GDP'][i]) 
                list3_group3.append(csv['TEAM_CODE'][i])  
                list3_group3_num.append(csv['NUM'][i])                             
            elif csv['NUM'][i] > 10 and csv['NUM'][i] <= 15:
                list4_group4_gdp.append(csv['2020_GDP'][i]) 
                list4_group4.append(csv['TEAM_CODE'][i])     
                list4_group4_num.append(csv['NUM'][i])                 
            elif csv['NUM'][i] > 15:
                list5_group5_gdp.append(csv['2020_GDP'][i])   
                list5_group5.append(csv['TEAM_CODE'][i])    
                list5_group5_num.append(csv['NUM'][i])



    print('Analysis1---------------------------------------------------','\n')  
    #Step1. Group the number of World Cup participations into Group1: 1 time, Group2: 2-5 times, Group3: 6-10 times, Group4: 11-15 times, Group5: 16 times or more.
    print("Step1. Group the number of World Cup participations into Groups")
    print('Group1(1 time) :', list1_group1, '\n')       #print list for 5 group team_code
    print('Group2(2~5 times) :', list2_group2, '\n')
    print('Group3(6~10 times) :', list3_group3, '\n')
    print('Group4(11~15 times) :', list4_group4, '\n')   
    print('Group5(over 16 times) :', list5_group5, '\n')   
           
    newlist1 = [x for x in list1_group1_gdp if pd.isnull(x) == False] #Countries without GDP per capita data in the WorldBank dataset were excluded.
    newlist2= [x for x in list2_group2_gdp if pd.isnull(x) == False]
    newlist3= [x for x in list3_group3_gdp if pd.isnull(x) == False]
    newlist4= [x for x in list4_group4_gdp if pd.isnull(x) == False]
    newlist5= [x for x in list5_group5_gdp if pd.isnull(x) == False]

    average_GDP_group1 = sum(newlist1)/len(newlist1)        # Group1: Number of participations: 1
    average_GDP_group2 = sum(newlist2)/len(newlist2)        # Group2: Number of participations 2~5
    average_GDP_group3 = sum(newlist3)/len(newlist3)        # Group3: Number of participations 6~10
    average_GDP_group4 = sum(newlist4)/len(newlist4)        # Group4: Number of participations 11~15
    average_GDP_group5 = sum(newlist5)/len(newlist5)        # Group4: Number of participations over 16


    Num_of_paticipations = ['1', '2-5', '6-10', '11-15','over 16']
    average_GDP = [average_GDP_group1,average_GDP_group2,average_GDP_group3,average_GDP_group4,average_GDP_group5]


 #   print(Num_of_paticipations)
 #   print(average_GDP)
#    print(average_GDP)

    #Step2. Calculate the average of 2020 GDP per capita for each group

    print('------','\n')  
    print("Step2. Calculate the average of 2020 GDP per capita for each group")

    print('Group1(1 time) :', average_GDP[0], '\n')         #print list for 5 group average gdp
    print('Group2(2~5 times) :', average_GDP[1], '\n')
    print('Group3(6~10 times) :', average_GDP[2], '\n')
    print('Group4(11~15 times) :', average_GDP[3], '\n')   
    print('Group5(over 16 times) :', average_GDP[4], '\n')   
    print('------','\n')      



    print("Step3. Visualization",'\n')


    plt.title("Correlation between the number of World Cup participations and GDP")
    plt.xlabel("Number of_paticipations")    
    plt.ylabel("Average GDP per capita (USD)")
    plt.bar(Num_of_paticipations, average_GDP)
    plt.savefig('figure1.pdf', dpi=300)
 #   plt.show()

    print('------','\n')      
    print("Step4. Calculate pearson_correlation between the number of World Cup participations and 2020 GDP per capita for each group",'\n')
    
    average_NUM_group1 = sum(list1_group1_num)/len(list1_group1_num)        # Average number of participations in Group1 
    average_NUM_group2 = sum(list2_group2_num)/len(list2_group2_num)        # Average number of participations in Group2 
    average_NUM_group3 = sum(list3_group3_num)/len(list3_group3_num)        # Average number of participations in Group3 
    average_NUM_group4 = sum(list4_group4_num)/len(list4_group4_num)        # Average number of participations in Group4 
    average_NUM_group5 = sum(list5_group5_num)/len(list5_group5_num)        # Average number of participations in Group5 

    average_NUM_GROUPS = [average_NUM_group1,average_NUM_group2,average_NUM_group3,average_NUM_group4, average_NUM_group5]



    print('Average number of participations in Groups : ',average_NUM_GROUPS)
    print('Average GDP per capita in Groups : ', average_GDP)
    print('Pearson correlation is : ', pearson_correlation(average_NUM_GROUPS, average_GDP))




    print('---------------------------------------------------','\n')  

def get_dataset2_analysis(filename1):    #Dataset2 : Host_Countries/ GDP per capita of before and after year  
    csv = pd.read_csv(filename1)

    csv['YEAR(TEAM_CODE)'] = 0    

    for i in range(len(csv)):
        csv['YEAR(TEAM_CODE)'][i] = str(csv['HOST_YEAR'][i]) +  "(" + str(csv['TEAM_CODE'][i]) + ")"

 #   print(csv)
    csv.plot(x = 'YEAR(TEAM_CODE)', y =['BEFORE_YEAR_GDP', 'AFTER_YEAR_GDP'], kind="bar", rot =0, figsize = (20,10))


    plt.title("Correlation between World Cup host and GDP per capita")
    plt.xlabel("Host year(Nation)")    
    plt.ylabel("GDP per capita (USD)")
    plt.xticks(rotation=90)
    plt.savefig('figure2.pdf', dpi=300)



def get_addtional_analysis(filename2, filename3):
    df = gdp_data_from_file(filename3) #Get gdp data
    df2 = gdp_dataset2_from_file(filename2) # Get dataset2

 #   print(df2)

    list1_1962 = []   #list for 5 group average gdp
    list2_1966 = []
    list3_1970 = []
    list4_1974 = []
    list5_1978 = []
    list6_1982 = []
    list7_1986 = []
    list8_1990 = []
    list9_1994 = []
    list10_1998 = []
    list11_2002 = []
    list12_2006 = []
    list13_2010 = []
    list14_2014 = []
    list15_2018 = []


    for i in range(len(df)):       #Put list each data
        if df['1962'][i] != 0:
            list1_1962.append(df['1962'][i])                
            newlist1 = [x for x in list1_1962 if pd.isnull(x) == False]
        if df['1966'][i] != 0:
            list2_1966.append(df['1966'][i])                
            newlist2 = [x for x in list2_1966 if pd.isnull(x) == False]
        if df['1970'][i] != 0:
            list3_1970.append(df['1970'][i])                
            newlist3 = [x for x in list3_1970 if pd.isnull(x) == False]
        if df['1974'][i] != 0:
            list4_1974.append(df['1974'][i])                
            newlist4 = [x for x in list4_1974 if pd.isnull(x) == False]
        if df['1978'][i] != 0:
            list5_1978.append(df['1978'][i])                
            newlist5 = [x for x in list5_1978 if pd.isnull(x) == False]
        if df['1982'][i] != 0:
            list6_1982.append(df['1982'][i])                
            newlist6 = [x for x in list6_1982 if pd.isnull(x) == False]
        if df['1986'][i] != 0:
            list7_1986.append(df['1986'][i])                
            newlist7 = [x for x in list7_1986 if pd.isnull(x) == False]
        if df['1990'][i] != 0:
            list8_1990.append(df['1990'][i])                
            newlist8 = [x for x in list8_1990 if pd.isnull(x) == False]
        if df['1994'][i] != 0:
            list9_1994.append(df['1994'][i])                
            newlist9 = [x for x in list9_1994 if pd.isnull(x) == False]
        if df['1998'][i] != 0:
            list10_1998.append(df['1998'][i])                
            newlist10 = [x for x in list10_1998 if pd.isnull(x) == False]
        if df['2002'][i] != 0:
            list11_2002.append(df['2002'][i])                
            newlist11 = [x for x in list11_2002 if pd.isnull(x) == False]
        if df['2006'][i] != 0:
            list12_2006.append(df['2006'][i])                
            newlist12 = [x for x in list12_2006 if pd.isnull(x) == False]
        if df['2010'][i] != 0:
            list13_2010.append(df['2010'][i])                
            newlist13 = [x for x in list13_2010 if pd.isnull(x) == False]
        if df['2014'][i] != 0:
            list14_2014.append(df['2014'][i])                
            newlist14 = [x for x in list14_2014 if pd.isnull(x) == False]
        if df['2018'][i] != 0:
            list15_2018.append(df['2018'][i])                
            newlist15 = [x for x in list15_2018 if pd.isnull(x) == False]



    average_GDP_1962 = sum(newlist1)/len(newlist1)        
    average_GDP_1966 = sum(newlist2)/len(newlist2)        
    average_GDP_1970 = sum(newlist3)/len(newlist3)        
    average_GDP_1974 = sum(newlist4)/len(newlist4)        
    average_GDP_1978 = sum(newlist5)/len(newlist5)        
    average_GDP_1982 = sum(newlist6)/len(newlist6)        
    average_GDP_1986 = sum(newlist7)/len(newlist7)        
    average_GDP_1990 = sum(newlist8)/len(newlist8)        
    average_GDP_1994 = sum(newlist9)/len(newlist9)        
    average_GDP_1998 = sum(newlist10)/len(newlist10)        
    average_GDP_2002 = sum(newlist11)/len(newlist11)     
    average_GDP_2006 = sum(newlist12)/len(newlist12)     
    average_GDP_2010 = sum(newlist13)/len(newlist13)         
    average_GDP_2014 = sum(newlist14)/len(newlist14)         
    average_GDP_2018 = sum(newlist15)/len(newlist15)         


    #Additional Analysis. Comparison of World Average GDP and Host Country GDP
    print("Additional Analysis. Comparison of World Average GDP and Host Country GDP")

    print(df2['HOST_YEAR'][6], 'Average GDP is', average_GDP_1962, ',', df2['TEAM_CODE'][6], 'GDP is', df2['HOST_YEAR_GDP'][6] ) 
    print(df2['HOST_YEAR'][7], 'Average GDP is', average_GDP_1966, ',', df2['TEAM_CODE'][7], 'GDP is', df2['HOST_YEAR_GDP'][7] ) 
    print(df2['HOST_YEAR'][8], 'Average GDP is', average_GDP_1970, ',', df2['TEAM_CODE'][8], 'GDP is', df2['HOST_YEAR_GDP'][8] ) 
    print(df2['HOST_YEAR'][9], 'Average GDP is', average_GDP_1974, ',', df2['TEAM_CODE'][9], 'GDP is', df2['HOST_YEAR_GDP'][9] ) 
    print(df2['HOST_YEAR'][10], 'Average GDP is', average_GDP_1978, ',', df2['TEAM_CODE'][10], 'GDP is', df2['HOST_YEAR_GDP'][10] ) 
    print(df2['HOST_YEAR'][11], 'Average GDP is', average_GDP_1982, ',', df2['TEAM_CODE'][11], 'GDP is', df2['HOST_YEAR_GDP'][11] ) 
    print(df2['HOST_YEAR'][12], 'Average GDP is', average_GDP_1986, ',', df2['TEAM_CODE'][12], 'GDP is', df2['HOST_YEAR_GDP'][12] ) 
    print(df2['HOST_YEAR'][13], 'Average GDP is', average_GDP_1990, ',', df2['TEAM_CODE'][13], 'GDP is', df2['HOST_YEAR_GDP'][13] ) 
    print(df2['HOST_YEAR'][14], 'Average GDP is', average_GDP_1994, ',', df2['TEAM_CODE'][14], 'GDP is', df2['HOST_YEAR_GDP'][14] ) 
    print(df2['HOST_YEAR'][15], 'Average GDP is', average_GDP_1998, ',', df2['TEAM_CODE'][15], 'GDP is', df2['HOST_YEAR_GDP'][15] ) 
    print(df2['HOST_YEAR'][16], 'Average GDP is', average_GDP_2002, ',', df2['TEAM_CODE'][16], 'GDP is', df2['HOST_YEAR_GDP'][16] )
    print(df2['HOST_YEAR'][17], 'Average GDP is', average_GDP_2002, ',', df2['TEAM_CODE'][17], 'GDP is', df2['HOST_YEAR_GDP'][17] )     
    print(df2['HOST_YEAR'][18], 'Average GDP is', average_GDP_2006, ',', df2['TEAM_CODE'][18], 'GDP is', df2['HOST_YEAR_GDP'][18] ) 
    print(df2['HOST_YEAR'][19], 'Average GDP is', average_GDP_2010, ',', df2['TEAM_CODE'][19], 'GDP is', df2['HOST_YEAR_GDP'][19] ) 
    print(df2['HOST_YEAR'][20], 'Average GDP is', average_GDP_2014, ',', df2['TEAM_CODE'][20], 'GDP is', df2['HOST_YEAR_GDP'][20] ) 
    print(df2['HOST_YEAR'][21], 'Average GDP is', average_GDP_2018, ',', df2['TEAM_CODE'][21], 'GDP is', df2['HOST_YEAR_GDP'][21] ) 



def gdp_data_from_file(filename):
    csv = pd.read_csv(filename, skiprows=4)
 #   print(csv)
    return(csv)

def gdp_dataset2_from_file(filename):
    csv = pd.read_csv(filename)
 #   print(csv)
    return(csv)



if __name__ == '__main__':

    filename1 = "output_data/dataset1_Participating_Countries_GDP.csv"                            
    filename2 = "output_data/dataset2_Hosting_Countries_GDP.csv"                           
    filename3 = "source_data/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_4701206.csv"  # GDP per capita from world bank 
                                                                            # https://data.worldbank.org/indicator/NY.GDP.PCAP.CD                                                                           

    get_dataset1_analysis(filename1)        #Analysis1
    get_dataset2_analysis(filename2)        #Analysis2
    get_addtional_analysis(filename2, filename3)        #Additioanl Analysis


