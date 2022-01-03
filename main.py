
import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

d1 = []
d2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
   
    for i in csv_reader:
        d1.append(i)
       
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
   
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)  
    csvwriter.writerows(p_d)
   
df = pd.read_csv('total_stars.csv')
df.tail(8)



# import pandas as pd 
# import csv

# from pandas.io.pytables import PossibleDataLossError

# df =pd.read_csv("data130.csv")


#deleting unwanted coloumns
# del df["hyperlink"]
# del df["temp_planet_date"]
# del df["temp_planet_mass"]
# del df["pl_letter"]
# del df["pl_name"]
# del df["pl_controvflag"]
# del df["pl_pnum"]
# del df["pl_orbper"]
# del df["pl_orbpererr1"]
# del df["pl_orbpererr2"]
# del df["pl_orbperlim"]
# del df["pl_orbsmax"]
# del df["pl_orbsmaxerr1"]
# del df["pl_orbsmaxerr2"]
# del df["pl_orbsmaxlim"]
# del df["pl_orbeccen"]
# del df["pl_orbeccenerr1"]
# del df["pl_orbeccenerr2"]
# del df["pl_orbeccenlim"]
# del df["pl_orbinclerr1"]
# del df["pl_orbinclerr2"]
# del df["pl_orbincllim"]
# del df["pl_bmassj"]
# del df["pl_bmassjerr1"]
# del df["pl_bmassjerr2"]
# del df["pl_bmassjlim"]
# del df["pl_bmassprov"]
# del df["pl_radj"]
# del df["pl_radjerr1"]
# del df["pl_radjerr2"]
# del df["pl_radjlim"]
# del df["pl_denserr1"]
# del df["pl_denserr2"]
# del df["pl_denslim"]
# del df["pl_ttvflag"]
# del df["pl_kepflag"]
# del df["pl_k2flag"]
# del df["pl_nnotes"]
# del df["ra"]
# del df["dec"]
# del df["st_dist"]
# del df["st_disterr1"]
# del df["st_disterr2"]
# del df["st_distlim"]
# del df["gaia_dist"]
# del df["gaia_disterr1"]
# del df["gaia_disterr2"]
# del df["gaia_distlim"]
# del df["st_optmag"]
# del df["st_optmagerr"]
# del df["st_optmaglim"]
# del df["st_optband"]
# del df["gaia_gmag"]
# del df["gaia_gmagerr"]
# del df["gaia_gmaglim"]
# del df["st_tefferr1"]
# del df["st_tefferr2"]
# del df["st_tefflim"]
# del df["st_masserr1"]
# del df["st_masserr2"]
# del df["st_masslim"]
# del df["st_raderr1"]
# del df["st_raderr2"]
# del df["st_radlim"]
# del df["rowupdate"]
# del df["pl_facility"]


# #renaming complex names
# df = df.rename({
#     'pl_hostname':"solar_system_name",
#     'pl_discmethod':"planet_discovery_method",
#     'pl_orbincl':"planet_orbital_inclination",
#     'pl_dens':"pl_density",
#      'ra_str':"right_ascension",
#      'dec_str':"declination",
#      "st_teff":"host_temperature",
#      'st_mass':"host_mass",
#      'st_rad':"host_radius"
# },axis='columns')

# df.to_csv('main.csv') #changing into new csv