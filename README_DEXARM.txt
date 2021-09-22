dexarmPort1 = 'COM3'
dexarmPort2 = 'COM4'

# joystick map
exec_action1 --------- Num 1 ---Lance le cycle complet
go_home -------------- Num 2 ---Impératif après chaque démarrage du logiciel
move_to -------------- Num 3 ---Utile seulement pour développeur
move_to_work_height--- Num 4 ---Pour descendre les deux plotteurs à leur plan de travail
disconnect ----------- Num 5 ---En cas de neccesité afin de déconnecter les ports série
release_picker ------- Num 7 ---Pour éteindre la pumpe si nécessaire
set_work_origin ------ Num 8 ---Pour définir les plans de travail des deux plotteurs
exec_action2 --------- Num 9 ---Work in progress

down_dexarm1 --------- Down ----Faire descendre dexarm/stylo (incrémentation de 3)
up_dexarm1 ----------- Up ------Faire monter dexarm/stylo (incrémentation de 3)
down_dexarm2 --------- Left ----Faire descendre dexarm/ventouse (incrémentation de 3)
up_dexarm2 ----------- Right ---Faire monter dexarm/stylo (incrémentation de 3)