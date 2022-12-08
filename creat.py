
import pandas as pd

col=["Last Name:","First Name:","sex:","family income(€):","moyen:","Age:"]

e1=["Ababou","Laid","M",440,11.00,22]
e2=["Abdeli","kadiro","M",None,10.33,19]
e3=["Boud","khawla","W",None,10.49,19]
e4=["Abidi","ines","W",870,14,18]
e5=["Abidi","kada","M",870,12,18]
e6=["Mokh","Adel","M",300,13,19]
e7=["Benyaser","Moh","M",700,10,20]
e8=["Benyah","Hadjer","W",500,9,19]
e9=["Abr","Rania","W",900,9.9,19]
e10=["Seba","ilies","M",None,11,20]
e11=["Bou","Hocy","M",420,10,20]


#creat csv file
data=pd.DataFrame([e1,e2,e3,e4,e5,e6,e7,e8,
e10,e11],columns=col)


data.to_csv("Dat2.csv")
