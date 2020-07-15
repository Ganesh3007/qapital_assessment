import requests as r
import json

try:

    res=r.get('https://reqres.in/api/users?page=2')

    if res.status_code==200:


        data=json.loads(res.content)

        count=0
        for i in range(0,len(data)):
            if data['data'][i]['id']==12 and data['data'][i]['first_name']=='Rachel' :
                a=True
            
            
            
            if data['data'][i]['id']:
                count+=1
                
            

            if data['data'][i]['id']==8 and data['data'][i]['first_name']=='Lindsay' :
                b=True
                
        if a==True:
            print('id 12 is assigned to Rachel')
        else:
            print('id 12 is not assigned to Rachel')

        if b==True:
            print('id 8 is assigned to Lindsay')
        else:
            print('id 8 is not assigned to Lindsay')

        if count==12:
            print('total number of users is 12')
        else:
            print('total number of users is not 12')
    else:
        print('error while requesting the api')





    res2=r.get('https://reqres.in/api/users/2')
    
    if res2.status_code==200:


        data=json.loads(res2.content)
       
        
        for i in range(0,len(data)):
            if data['data']['id']==2 :
                b=True
            if data['ad']['company']=="StatusCode Weekly":
                a=True
        
        if a==True and b==True:
            print( 'company name “StatusCode Weekly” is associated with employee id 2.')
        else:
            print('company name “StatusCode Weekly” is not associated with employee id 2.')

        
    else:
        print('error while requesting the api')
    
    res1=r.get('https://reqres.in/api/users/23')
    
    if res1.status_code==404:
        print('HTTPS Status code is 404 for user id 23')
    else:
        print('HTTPS Status code is not 404 for user id 23')

except Exception as e:
    print(str(e)+'sds')





   
    


