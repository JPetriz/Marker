# Verificador de cordones y marcado de piezas

Este programa es una version en python de uno que ya existe en JAVA, el cual trabaja en un dispositivo de analisis de cordones de soldadura.

En resumen el programa detecta el ultimo ciclo de soldadura producido y analiza los resultados de los cordones en la base de datos del equipo (firebird), va formando los registros de las piezas procesadas , ya que para generar una pieza final
se necesitan varios ciclos de soldadura y los componentes pasan por diferentes pasos, al final, cuando se tienen todos los datos de una pieza final el programa analiza si es una pieza OK o no, si la pieza es una pieza OK el programa debera
de generar un codigo que sera mandado a un equipo de marcado por micropercusion mediante un puerto serial ( en este caso se usa un adaptador USB-SERIAL)

el programa esta incompleto, quedaron incompletos el programa character_procesor, el GUI, y el programa serial_port, watcher , y sus respectivos test; el motivo por cual quedo incompleto fue por falta de tiempo tiempo para el desarollo y mi falta de 
experiencia en python , aunque es un proyecto que planeo contemplar a mas tardar en enero (dependiendo mi carga de trabajo)


