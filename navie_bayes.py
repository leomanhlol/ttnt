#import thu vien
import pandas as pd

#doc du lieu
df = pd.read_csv('data_rain.csv')
temp_list = df['Temp']
wind_list = df['Wind']
moisture_list = df['Moisture']
rain_list = df['Rain']

#xet phan lop (t,w,m)
#Buoc 1, xet C1 = yes, tinh P(Yes) va P(x|c1)
#tinh P(Yes)
p_yes = len(df[df['Rain']=='Yes'])/len(df)
#tinh P(No)
p_no = len(df[df['Rain']=='No'])/len(df)

#tinh cac P(x|c1)
def p_x_c_yes(t,w,m):
    res=[]
    k=1
    res.append(len(df[df['Temp']==t])/len(df[df['Rain']=='Yes']))
    res.append(len(df[df['Wind']==w])/len(df[df['Rain']=='Yes']))
    res.append(len(df[df['Moisture']==m])/len(df[df['Rain']=='Yes']))
    for i in res:
        k=k*i
    return k 

def p_x_c_no(t,w,m):
    res=[]
    k=1
    res.append(len(df[df['Temp']==t])/len(df[df['Rain']=='No']))
    res.append(len(df[df['Wind']==w])/len(df[df['Rain']=='No']))
    res.append(len(df[df['Moisture']==m])/len(df[df['Rain']=='No']))
    for i in res:
        k=k*i
    return k

#tinh P(c1)* tich cac P(xi|c1) va P(c2)* tich cac P(xi|c2), dua ra gia tri lon hon va ket luan
def decision(t,w,m):
    res= max(p_x_c_yes(t,w,m)*p_yes,p_x_c_no(t,w,m)*p_no)
    if res == p_x_c_yes(t,w,m)*p_yes:
        print("Du doan se co mua")
    else:
        print("Du doan se khong mua")

#ket qua du doan voi cac phan lop
print('BAI TOAN DU BAO THOI TIET SU DUNG NAVIE BAYES')
print('--------------------')
print("Kha nang co mua khi troi nong, gio to, do am cao: ",p_x_c_yes('Hot','Strong','High')*p_yes)
print("Kha nang co mua khi troi nong, gio to, do am cao: ",p_x_c_no('Hot','Strong','High')*p_no)
decision('Hot','Strong','High')
print('--------------------')
print("Kha nang co mua khi troi lanh, gio to, do am cao: ",p_x_c_yes('Cold','Strong','High')*p_yes)
print("Kha nang co mua khi troi lanh, gio to, do am cao: ",p_x_c_no('Cold','Strong','High')*p_no)
decision('Cold','Strong','High')
print('--------------------')
print("Kha nang co mua khi troi mat, khong gio, do am thap: ",p_x_c_yes('Cool','No','Low')*p_yes)
print("Kha nang co mua khi troi mat, khong gio, do am thap: ",p_x_c_no('Cool','No','Low')*p_no)
decision('Cool','No','Low')

print('--------------------')
print("Nhap nhiet do: ")
t=input()
print("Nhap suc gio: ")
w=input()
print("Nhap do am: ")
m=input()

def prediction(t,w,m):
    return decision(t,w,m)

prediction(t,w,m)



