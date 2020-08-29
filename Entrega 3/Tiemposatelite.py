import datetime as dt 

 # <List_of_OSVs count="9361">


      # <X unit="m">299061.452952</X>
      # <Y unit="m">2504739.190677</Y>
      # <Z unit="m">-6617606.990132</Z>
      # <VX unit="m/s">2395.743301</VX>
      # <VY unit="m/s">-6748.728991</VY>
      # <VZ unit="m/s">-2447.219878</VZ>
      # <TAI>TAI=2020-07-25T23:00:19.000000</TAI>
      # <UTC>UTC=2020-07-25T22:59:42.000000</UTC>
      # <UT1>UT1=2020-07-25T22:59:41.787032</UT1>
      # <Absolute_Orbit>+33617</Absolute_Orbit>
x_i = 299061.452952     #metros 
y_i = 2504739.190677    #metros 
z_i = -6617606.990132   #metros 
vx_i = 2395.743301 # m/s 
vy_i=  -6748.728991 # m/s
vz_i=  -2447.219878 # m/s





      # <TAI>TAI=2020-07-27T01:00:19.000000</TAI>
      # <UTC>UTC=2020-07-27T00:59:42.000000</UTC>
      # <UT1>UT1=2020-07-27T00:59:41.787584</UT1>
      # <Absolute_Orbit>+33633</Absolute_Orbit>
      # <X unit="m">1758481.857868</X>
      # <Y unit="m">6851700.745053</Y>
      # <Z unit="m">205527.869685</Z>
      # <VX unit="m/s">1589.991471</VX>
      # <VY unit="m/s">-175.785352</VY>
      # <VZ unit="m/s">-7426.986520</VZ>
      # <Quality>NOMINAL</Quality>

x_f  =   1758481.857868
y_f  =   6851700.745053
z_f  =   205527.869685
vx_f =   1589.991471
vz_f =   -175.785352
vz_f =   -7426.986520





utc_EOF_format =        "%Y-%m-%dT%H:%M:%S.%f"
# t1 = dt.datetime.strptime("2020-07-25T22:59:42.000000",utc_EOF_format)
# t2 = dt.datetime.strptime("2020-07-27T00:59:42.000000",utc_EOF_format)
t1 = dt.datetime.strptime("2018-08-14T22:59:42.000000",utc_EOF_format)
t2 = dt.datetime.strptime("2018-08-16T00:59:42.000000",utc_EOF_format)

intervalo = t2 -t1 
intervalor_en_segundos = intervalo.total_seconds()

print (intervalo)
print (intervalor_en_segundos)





