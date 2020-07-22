import requests
def corona_func(countr):
    string='https://api.covid19api.com/total/country/'+countr #countr is country here

    r = requests.get(string)


    a = r.text[-380:]
    b = a[a.find('{'):]


    confirmed  = int(b[b.find('firmed":')+8:b.find(',"Deaths"')])
    deaths = int(b[b.find('eaths":')+7:b.find(',"Recover')])
    recovered = int(b[b.find('covered":')+9:b.find(',"Active')])
    active = int(b[b.find('ctive":')+7:b.find(',"Date')])
    
    corona_statement = 'In case of '+countr+' Total confirmed cases are '+str(confirmed)+'. Total deaths are '+str(deaths)+'. Total recovered patients till now are '+str(recovered)+'. Active cases in '+countr+' currently are '+str(active)+'.'
    
    return corona_statement




