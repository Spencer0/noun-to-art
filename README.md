# Overview
Noun-to-art (NTA)'s goal is to take in a noun from the user and create art.

# Usage
- Print output: python asciify.py <Phrase>
- Save output: python asciify.py <Phrase> > res.txt

If the phrase has multiple matches, it will return a disambiguation list. Otherwise it will print ascii art to the console.


### Examples
python asciify.py Longbow

```

;:::::::::::::;;;:::::::::::::::::::::::;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::;::::::;::;;:::::::::::::::::::::::::;;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::;
:::;::::::;;;;;:::::::::::::::::::::::::;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;
:::;;:::::::::;;::::::::::::::::::::::::;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::;;;::::::;;;;;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::;;;;:::::;;;;;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::;;:;;::::;;;;;;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
;;::::::::::;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;**+;::::::::::::::::::::::::::
::;;;;::::::::;::::::::::::::::::::::::::::::::::::::::::;;::::::::::+S?**;:::::::::::::::::::::::::
:;;::::::::;;;:::::::::::::::::::::::::::::::::::::::::::;;;::::::::::**%?+;::::::::::::::::::::::::
:::::::::::::;::::::::::::::::::::::::::::::::::::::::::::;;::::::::::+*;??+;:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;::::::::;*+::+%++;:::::::::::::::::::::
:::::;::::::::::::::::::::::::::::::::::::::::::::::::::::::;::::::::+*::::+?++;::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::+*+;:::::::;*;:::::+*++;:::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::;***+;::::::;*;::::::;*++:::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::+;:;;*??;;:::::*+::::::::+*++::::::::::::::::::
:;:::::::::::::::::::::::::::::::::::::::::::::::::::++;:;++*?+;:::+*::::::::::*++*:::::::::::::::::
:;;::::::::;:::::::::::::::::::::::::::::::::::::::::;+++;+;:??*;::*;::::::::::;*++;::::::::::::::::
::;;:::::::;;;;:::::::::::::::::::::;;:::::::::::::::;??+++;::?**;+*::::::::::::+*+*::::::::::::::::
::::;;;;::;;;:::::::::::::;;;;:::::;;;*+;::;;;;::::::;+?+**;::;?+**;:::::::::::::*+++:::::::::::::::
::::;:;;::;;;:::::::::::;;:::::;*%%S%+*%??%%SS%?*;:::+;+**+::::+**?::::::::::::::;*+*;::::::::::::::
::::::::::;;;:::::::::;;::::::*%S%S%SS%%?%#%#S%%S%+::++;?*+:::::+??:::::::::::::::**+*::::::::::::::
*+;:::::::;;;::::::;::::::::;*##SS%S%%S?%*SS?*++*S?::+;;%??:::::*?+*::::::::::::::;*++;:::::::::::::
##S??+;:::;;;:::;;;;;+*?*;::*%S#SS%%??%%S???;;+;+%S+:++:%??::::;*?+*+::::::::::::::+*++:::::::::::::
SSSS##S%+;:;;:;;;;*?%%%%%%*:+%?%S%***++?%%+?;?%%S%S*:*+:%?*;:::+*;+++:::::::::::::::*+++::::::::::::
SSSSS####S*;::;;+%%%%%%%%%?%?%?%%+;;;+*?SS+%S?%%%SS+:*+:%??;::;?;:*++:::::::::::::::+*+*::::::::::::
SSSSSS#S###S%+:;%%%%S%???**S#?%*?;*?;?#SSS+%S?#SSSS%+**?S%??+;**::+*;;:::::::::::::::?+*;:::::::::::
SSSSSSSSS#####?+%%%S%???++;*#?S*?*%#???%%S**%S%?%%??%?????*?%%?+:::*++:::::::::::::::*++*:::::::::::
SS%SSSSSS##S###?%%%S*?*;;;+%#%%%*?%%S*%?SS?+#S%??***%???%%%%%?%%;::+*+;::::::::::::::;*+*;::::::::::
SSSS#%%%SSSS####S%SS?%++**+%%%?%******%?%S%+S%??*+;;%%SS*%???*?S*::;?+;:::::::::::::::*++;::::::::::
SSS%%%%SSS%S####S%%%%%;?%#??%%?%**;++**%%?%+S??%+;+*%%%SS%*+?**?%;::?*+:::::::::::::::*+++::::::::::
SSSSSS%S%SS%SSSS#%%%%S+??%?+%%S%*%**++*S%*?+??S*;%SSS%%%%?;*?++*%+::+?+:::::::::::::::;*++::::::::::
SSSSSSSSSS%??SSSS%%%%S??*****%#S*?%%%?%?%%%+?%S*?%??%%%%%*+?*;;+%*::+?+;:::::::::::::::?+*;:::::::::
SSSSSSSSS%%??%S%SS%%?#S*+*+*?%%S*****?*%%%S*??%*?*+%S%%%%+*?+;??%*:::?+;:::::::::::::::?*+;:::::::::
SSS%SSSSSS?%%%SSSS%S?%#%+?*+*%??*?****?S%S%**%??*+;?%S%?***%?+%S%;:::?*;:::::::::::::::***+:::::::::
SSSS%SSSSS%SSS%SSS%%S%%S??%?*?SS??%%%SS%%%???%*??*+%SSS**?*?S+?S+::::**+;::::::::::::::+?++:::::::::
SSSSSSSSSS%%SSS%SS%%%%%%SSSSS?SS?*#S%%%%%?%?????%%%%SS%?*??*?*?%+:::,+?+;:;*+?*;:::::::;?++:::::::::
SSSSSSS%SS%%S%%%%S%%%%%%%%%%%?S#?*S%?%%%%?%%%%???%%%%%%S?*;+**??+::;;*%*+*??+?S+:::::::;?++:::::::::
SSSSSSSSSS%%SS%%S%SS%%%%%?%%S?S#%*S%%%%%%%%%%%%%%?%%???***?%%?*??**?%??*+??%**+:::::::::?++:::::::::
SSSSSSSSSS%SSSS%SS%S%%%%%%%%%?%%?+SS%%%?%%%?%%%%?%*+;;;*%?%%%%%%%***+*S???;;;:::::::::::?**;;**;::::
SSSS#SSSS%##S%%%S%%%S%%%%%%%%?%??+S#SSSS%%%%%%%%?S??+;+*??*%%%%%%****%???%%?*****?***++*???%S?%?+:::
SSS###SSSSSSS%%SSS%%%S%%%%%%%?%%?+%%SS##??%?+%%%??%%%%%?%?????S??*+:+?+*??*++*******???%%?%%%?%?;:::
SSSSSSSSS%SSS%SSS%%%SSS%%%%%??%%?+%?*??%?%%?**??%???%%S%S??SSS?*%?%?S%*;*?;:::::::::::+%??%?+;+:::::
SSSSSSSS%%%%%%SS%**?*%%%%%?*?*?%%+%S???+%S?**??%%%%%%%%%S%***??%%?%%S#%*?*;:::::::::::*+?S??+:::::::
SSSSS##SSSSS%SSS?+****%%**%%?*???+S#SS?*%#?*??%%%%%%%%%%??%%?%%%%%%%%%%S??::::::::::::*;%?*?+:::::::
SSS#S%???%?SSSSS?**?%??#++*%?**?%+S@#S?*%#%?%%%%%%%%%%%%?+%%%%%%%%%%%%???%*+;:;+;::::+*+%%?%;:;:::::
S#S%*++++++?SS%S%*?%S??S*+%??*??%*%###??SSS%%%?%%%%%%%%%%**%%%%%%%%%%%%???????SS%??????*%**+;:::::::
S#?+++*?++;+*S%%%*%%#S?S*+%?%**?%*%?%%%%%S%%%??%%%%%??%%%%+?%%?*+**%%%%%?????%#SSS%??*?%?*?:::::::::
#%*+*%%S%%?++%S%S?%S##%S?*%%%?*?%+?S?%%#%SS%%%%%%%%????%%%?+?+:::::;+*%%%%%%?%#SSS%????S*+*:::::::::
#?+*%SSSSSS?*%S%S?%SS##S???%?%??%+?%%%%#SS%%%%%%%%%???%%%?%*+::::::::;?*?+***?%#S?*+;;;%+*+:::::::::
S*+?S%%%SSSS%%%S#%%SSS#??%??%?%??+%%%%%%%%%%%%%%%%????%%???+++:::::::;*+*::::;;;;:::::;?+*;:::::::::
S**S%%SSS%%S???SS%%#S#%?S%???%#S???#S?S%*%SSS%%%%%????%%??;:;+;::::::;*++;;;::::::::::**+*::::::::::
S++%S%%SSS%???*%#%%S#%?S#S%????S%?**%S##%?SS%%SS%%%%?%%?%*:::**::::::+**+;;;;:::::::::*+*+::::::::::
#*+?%%%SSSS*;?S%#%%S%*%##S%????%*+++*S#%%%%S%%SSS%%%%%%%%;:::;?+:::::***;;::;;:::::::;?+*:::::::::::
#?*+%S%%SS?++%S%#S%%*?SS#S%????S?+;+%S%%?%%%%%%S%%%%%%%%%;;;;:+?;:::;*++:;:::::::::::***+:::::::::::
SS*++%%%?*++*S%%S#%*?S%S#S%%???%%*?S#%?%??%%%%%%%%%%%?%%%+;;:;;**;::;*++:;::::::::::;?**;:::::::::::
SSS?*++++++*SS%S%#%%SS%S#S%%%?%%S%*SS????*%%%%??%S%%??%%%*;::::;?+::***;;:::::::::::+?+*::::::::::::
SS#S%?+*+*%SS%%S%%#SS?%S#S%%%*%%%?*S%%???*?%?%??**%%SS%+?*;:::::+?+:**+;;:::::::::::*?**::::::::::::
SSSSSS%S%SSSS%%%%%%S%%?%#SSS%?%%S?*S%%??%*?%?%%?%?*?%%*:+*;;;::::*?+*++:;;:::::::::;?*?;;;::::::::::
S%#SSSSSSSSSSSS%%%%S%%%%%%SS%?%SS*+%%%%%%??%%%%%??%**%?:+?;;;;:::;???++;;;:::::::::+*++;;;::::::::::
#S#SSSSSSSS%S%S%%%%%S%%%%?%#S?%SS*+%S%%%%%?%%%%?%?%%%**++*;;;;;:::+%?*;;;;;::::::::?**::;;::::::::::
##SSSSSSSS%S#%S%%%%SS%%%S#%?S?%##**%%%%%?%?%%%%%%%%%%%?**?+;;:::::+%%+;;;;;:::::::+?++:::;::::::::::
#S##SSSSSSS%SSS%%%%%S%%%S%%%%?SSS?*%S%%%%%%?%%%%%??%%%?%%??*;::::;**?*;:;;;:::::::?**;:::;;;::::::::
#SS###SSSS%SSS%S%%S%%%%%SS%???%%%?*%%%%%%%%?%%%%%%%?*?***%?**::::+**+*+;;;:::::::+%++::::;;;;:::::::
#S##SS#SSS%SSSS%%%%%%%%SSS%??????*?%%%%%%%%%?%%%%?%%%*;::?S%*;::+***;;*+:::::::::%**::::::::::;:::::
SS###%SSSSSSSSS%SS%%S%%S%S%??%?SS??%%%%%?%%%*?%%%%%%%+:::**;:::;***;;:+?;:::::::*%*+::::::::::::::;;
SSS###SSSSSSSSS%SSSS%%%S%S%%*?%SS?%%%S%%?%%%?*%%%%%%%+:;;**;:::***;:::;+*;::::::%**::;::::::::::::::
SSSS##SSSSSSSSSSS#SS%%%S%SS%??%SS*%%SS%%??%%%*?%%%%?%?;;;+*;::***+:::::;**:::::*?*;::;;:::::::::::::
SSSSSSSSSS##SS%SS%S%%%%%%S%???%SS*S%SS%%?%%?%%*%%%%%%%+;;+?+:+**?:::;:::;*+:::+%*+::::::::::::::::::
SSSSSSSSSSSSSSSS%%%%%%S%SS%???%SS?S%%S%%%%%%?%??%%%%%%?;;;*+*?**::::;;:::+?+:;%*+:::::::::::::::::::
SSS###SSSSSSSSSS%%%%%%S%SS???%SSS?S%%S%%%%??%%%*?%%%%%%;:;*??**::;;:::::::*%*??+;:::::::::::::::::::
SSS##SSSSSSSSSSSSSS%%%%%S%??%%SSS%S%%S%%?????%%%*%%%%%%*:;??*+::::;;;:::::;?%?*;::::::::::::::::::::
SSSSSSS#SSSSSSSS##SSSS%%S??%?%SSS%%%%S%%??????%%%*%%%%%%;+*?;::::::;;::::::*%?+:::::::::::::::::::::
SSSSSSSSSSSSSSSS##%SSS%%S????%%SS%%%%%%%%?????%%%???%%%%*;;;::::::::;::::;*?*+::::::::::::::::::::::
SSSSSSSSSSSSSSSSSSSSSS%S%????%%SS%%%%%%?%%????%%%%?*%?%%%;;::::::::::;:::;**;:::::::::::::::::::::::
SSSSSSS###SSSSSSSSSSSS%S%%???%%SS%%?%%%?%??%%?%%%%%%%?%%%*;;::::::::::::;;::::::::::::::::::::::::::
#SSSSSSSSS#SSSSSSSSSS%%%%%???%%SS????%%%??????%%%%S%%%*?%S;;;:::::;:::::::::::::::::::::::::::::::::
SS##SSSSSSSSSSS#SSSSS%%SS????%??%%%%??%??*?????%%%S%%%??*%+;;;::::::::::::::::::::::::::::::::::::::
#S#SSSSSSSSSSS##SSSS%?%%?%%%%%%%%*?%?????????%%%%%%%?%%%?S+;;;::::::::::::::::::::;;::::::::::::::::
###SSSSSSSSSSS#SSS#%%%#S#S%S#%SSS*#%??*??%??%%%%%%%%?%%%SS+;;;;:::::::::::::::::::::;:::::::::::::::
###SSSSSSSSSSS#SSS#SS##S#%S#S%SSS?#S%*****????????%S%??%SS+:;;;;;;;;;:::::::::::::::::::::::::::::::
####SSSSSSSSS##SSSSSS#S#S?###%S#%?%%%;?*+*%S???????%%?%?%S*::;;;;;:;;:::::::::::::::::::::::::::::::
####SSSSSSSSS#SSSSSSS#S#%%##S%%S%?%%+*?*+?S%%%*?S%?%?%???S%:::::;:;;;:::::::::::::::::::::::::::::::
#####SSS#SSSS#SSSSSS###S%S#SS%S#%%%?:?***%S%S??S%?%%?S%??%%;::::::::::::::::::::::;:::::::::::::::::
###SSSSSSSSS#SSSSSSS##%%%#SSS%S#%%S+;?*+?SSS%?S*+?%??%?%?%S+:::::::::;;:::::::::::::::::::::::::::::
###SSSSSS%SSSS#SSSSS#SS%#SSSS%S#%S?:;?**?%S%?%%:+??*?*+%%?S*:::::::::;::::::::::::;:::::;:::::::::::
SSSSSSSSSSSSSSSSSSS##%SS#SSSSSS#%S;:;?*?%%S%?S*:;%?*?*:*S?%%::::::::::::;;::::::::;::;:;;:::::::::::
SSSSSSSSSSS%%SS#%SS##SS#SSSSSSS#%?::;?*%*%S?S%::;%%*%*:;%S?S;:::::::::::;;;::::::::::;;;;:::::::::::
SSSSSSSSSSS%SSS%SSS#SSS#S%%SSSS#%;::;?*?+S?%S;:::?%*?+::;S?S*:::::::::::::;;:::::::;;;;;;:::::::::::
SSSSSSS#S%SSSSSSSS##S%S%%%S%SSSS?:::+???*%?#*::::*%*?+:::?%%S::::::::::::::;;::::::;;;;;;:::::::::::
SSSSSS%SS%%SSSSSSS##SS#S%SS%SSS%*:::???*%?SS:::::+%*?;:::;%?S*:::::::::::;:;;;;;:::;;;;;;::::::::;:;
SSSSS%%%%S%%%%%%S#%#%#S%%%SSSS%%*::;?*%?%%#+:::::;%*?;::::*%?%:::::;:::::::::;;::::::::::::::::::;:;
SSSSS%%%SSSS%%SS#S%%%SS%%%S##SSS#*:*??%S?S?::::::;%+?;::::+S?S*;:::;;::::::::;;::::::::::::::::::::;
SSSSSSS%S%SS####SSSS%%%%%SS###SSS#%S??S%%#+::::::;%*?%?+;;:%S%S%?;:;;::::;::;;:::::::::::::::::::::;
SSS%SSS%SS%S####S####SS%SS##S#S#SS#SSSS?S%:::::::+#SS##SS?*%SSS#SS*+;+%+:;;;;;:::::::::::::::::::::;
SSSSSSSSS%*%#SS###SSSSSSSSS##S%%#S%SSSS?%%*;:::::?@@@@@###SSS##@####SS@?:::::;;;::::::::::::::::::;;
;;;++;;+;;:?###%+*???%%SS%%S%?;+SSSSS##SS%S%+;;++?#S*+*%SSSS#S?%%S###S%+:;:;;;;;;::::::::::::::::;;;
:::::;;:::;S###+::::::;;;;;+;;;S#%%@?S###SSSSS%%S;::::;;;;;;+;::::;*+;::::;;;;;;;:::::::::::::::;;;;
::::::;;::;S##?:::::::::::::::;SS%S?:;++++*?SSSS?;;::;;;:::::;;:::::::::::::;;;;;:::::::::::::;;::;;
::::::::;::;+;:::;:::::::::::::%S%S+::::::::;+;::;;;;;:::::::;:::::::::::::::;::;;:::::::::::;;;;:;;
:::::::::::::::;:::::::::::::::?SSS;::::::::::::::::::::::::::::::::::::::::;;:;;;::::::::::::::;::;
:::;;::;:;:::::::::::::::::::::%##*::::::::::::::::::::::::::::::::::::::::::;:;;;::;;::;:::::::;;;;
:;::;;;;;;;::::::::::::::;:::::?S*:::::::::::::::::::::::::::;::::::::::::::::::;;::;;:;::::::;;;:;;
:;:::;;;:::::::::::::::::;:::::;;::::::::::::::::::::::;:::::::::::::::::::::::;;;;;:;;;;;::::;;;;;;
;;:::;;;:::::::::::::::::::::::;;::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;::::;;;;;
;;::;;:::::::::::::::::::::::::;;;:::::::::::::::::::::::::::::::::::::::::::::::;:::;;;;;:::::::;;;
:;;;;;:::::::::::::::::::::::::;:::::::::::::::::::::::::::::::::::::::::::::::::;:::;;;;;;:::;;;;;;
```
