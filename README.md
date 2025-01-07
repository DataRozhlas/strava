Časosběrné sledování segmentů na Stravě. Půjde z něj například zjistit, kdy se šlape na Praděd a kdy se běhá po Stromovce.

Nad rámec dat ze Stravy se do ```segments.parquet``` počítá vzdálenost vzdušnou čarou mezi startem a cílem – užitečné pro odfiltrování oválů a velodromů, na kterých může pár lidí nadělat velké denní výkyvy v effortech.

## Poslední aktualizace

2025-01-06

## Sledované segmenty

" shape: (261, 7)
| name           | activity_type  | country  | city           | distance | total_elevati | effort_count |
| ---            | ---            | ---      | ---            | ---      | on_gain       | ---          |
| str            | str            | str      | str            | f64      | ---           | i64          |
|                |                |          |                |          | f64           |              |
|----------------|----------------|----------|----------------|----------|---------------|--------------|
| Richmond ITT1  | Ride           | United   | London         | 589.3    | 7.2           | 4625706      |
|                |                | Kingdom  |                |          |               |              |
| Box Hill 2.2k  | Ride           | United   | Mole Valley    | 2296.62  | 119.1         | 1415731      |
|                |                | Kingdom  | District,      |          |               |              |
|                |                |          | Surrey, ...    |          |               |              |
| Die Eine Runde | Ride           | Czech    | Brno           | 380.0    | 0.0           | 1089698      |
|                |                | Republic |                |          |               |              |
| Overtake the   | Run            | United   | London         | 591.8    | 2.2           | 663738       |
| Boris Bikes    |                | Kingdom  |                |          |               |              |
| Třebešín-dráha | Ride           | Czech    | Prague         | 347.2    | 0.0           | 402245       |
| K              |                | Republic |                |          |               |              |
| Alpe d'Huez    | Ride           | France   | Le Bourg       | 12024.9  | 1047.3        | 336372       |
|                |                |          | D'Oisans       |          |               |              |
| Sa Calobra -   | Ride           | Spain    | Escorca        | 9416.77  | 659.8         | 323412       |
| Coll dels Reis |                |          |                |          |               |              |
| Opičí Časovka, | Ride           | Czech    | Prague         | 1390.1   | 6.0           | 323005       |
| Podolská       |                | Republic |                |          |               |              |
| vodárn...      |                |          |                |          |               |              |
| Prostějov kolo | Ride           | Czech    | Prostějov      | 311.1    | 0.0           | 251263       |
| dráha P        |                | Republic |                |          |               |              |
| Koppenberg     | Ride           | Belgium  | Oudenaarde     | 556.595  | 63.1          | 245118       |
| Mont Ventoux   | Ride           | France   | Bédoin         | 20741.8  | 1569.4        | 242103       |
| (par Bedoin)   |                |          |                |          |               |              |
| Stelvio -      | Ride           | Italy    | null           | 2982.1   | 5.4           | 235601       |
| Bormio Turn    |                |          |                |          |               |              |
| Downhill       |                |          |                |          |               |              |
| Zweite hup u   | Ride           | Czechia  | Praha-Troja    | 314.1    | 6.6           | 234006       |
| ZOO            |                |          |                |          |               |              |
| Zbraslav -     | Ride           | Czechia  | Zbraslav       | 2359.0   | 5.7           | 216976       |
| Komořany       |                |          |                |          |               |              |
| Stadion Na     | Run            | Czechia  | Prague         | 420.9    | 0.0           | 215619       |
| Děkance        |                |          |                |          |               |              |
| Lužánky        | Run            | Czechia  | Brno-střed     | 268.9    | 3.8           | 180145       |
| rovinka        |                |          |                |          |               |              |
| Šlechtovka -   | Run            | Czechia  | Praha 7        | 225.4    | 0.0           | 156359       |
| finální        |                |          |                |          |               |              |
| rovinka        |                |          |                |          |               |              |
| time trial at  | Ride           | Czech    | Brno           | 1438.1   | 20.6          | 141864       |
| Svratka        |                | Republic |                |          |               |              |
| Passo Stelvio  | Ride           | Italy    | null           | 23600.3  | 1840.3        | 139224       |
| Od posledního  | Ride           | Czechia  | Bílovice nad   | 827.8    | 6.2           | 124484       |
| tunelu do      |                |          | Svitavou       |          |               |              |
| Bílovi...      |                |          |                |          |               |              |
| VUT horní      | Run            | Czechia  | Brno           | 405.2    | 0.0           | 109048       |
| dráha 400m     |                |          |                |          |               |              |
| Col du         | Ride           | France   | Luz Saint      | 18827.5  | 1397.7        | 99930        |
| Tourmalet (par |                |          | Sauveur        |          |               |              |
| Luz-St-S...    |                |          |                |          |               |              |
| Vítkov up      | Run            | Czechia  | Prague         | 118.2    | 6.0           | 86621        |
| sprint         |                |          |                |          |               |              |
| Pražačka 320   | Run            | Czechia  | Prague         | 343.3    | 0.0           | 75242        |
| Viveros-Paseo  | Run            | Spain    | Valencia       | 1722.9   | 18.0          | 73160        |
| alameda        |                |          |                |          |               |              |
| TJ Sokol okruh | Run            | Czech    | Prague         | 418.8    | 5.7           | 72849        |
|                |                | Republic |                |          |               |              |
| Kolo na        | Run            | Czechia  | Třebíč         | 475.6    | 6.2           | 69590        |
| stadionu v     |                |          |                |          |               |              |
| Třebíči        |                |          |                |          |               |              |
| Srbsko -       | Ride           | Czechia  | Srbsko         | 5736.1   | 13.5          | 61460        |
| Hlásná Třebáň  |                |          |                |          |               |              |
| Stezka do      | Ride           | Czech    | Zlin           | 1368.28  | 23.1348       | 60475        |
| Zlina          |                | Republic |                |          |               |              |
| Rokytka od     | Ride           | Czechia  | Praha 14       | 1823.0   | 4.0           | 59010        |
| myčky          |                |          |                |          |               |              |
| Dráha Plzeň    | Ride           | Czechia  | Pilsen         | 361.9    | 0.0           | 54673        |
| okruh P        |                |          |                |          |               |              |
| Sptint pod     | Ride           | Czechia  | Olomučany      | 778.8    | 0.0           | 53348        |
| Býčí skálou    |                |          |                |          |               |              |
| 400 m -        | Run            | Czechia  | Olomouc        | 400.0    | 2.9           | 52422        |
| atletický      |                |          |                |          |               |              |
| okruh -        |                |          |                |          |               |              |
| Loko...        |                |          |                |          |               |              |
| Hvězda flat    | Run            | Czech    | Praha 6        | 1001.15  | 11.426        | 49909        |
|                |                | Republic |                |          |               |              |
| tenis 1K       | Run            | Czech    | Brno           | 1002.8   | 0.0           | 49020        |
|                |                | Republic |                |          |               |              |
| Tyršák         | Run            | Czechia  | Šumperk        | 426.5    | 3.1           | 46670        |
| čtyřstofka     |                |          |                |          |               |              |
| Llanberis path | Hike           | United   | Caernarfon     | 2417.5   | 0.0           | 45005        |
| bottom section |                | Kingdom  |                |          |               |              |
| ...            |                |          |                |          |               |              |
| Od dubu ke     | Run            | Czech    | Prague         | 385.7    | 2.9           | 44623        |
| Gizele         |                | Republic |                |          |               |              |
| Revnicak Eve   | Ride           | Czechia  | Řevnice        | 5562.4   | 287.8         | 43493        |
| Risova         | Ride           | Czech    | Brno           | 2612.4   | 138.5         | 41396        |
| studanka - od  |                | Republic |                |          |               |              |
| zavory         |                |          |                |          |               |              |
| Most Legií     | Run            | Czechia  | Praha 1        | 328.1    | 2.08          | 40264        |
| (směr Kampa)   |                |          |                |          |               |              |
| Jiráskovo      | Ride           | Czechia  | České          | 1113.6   | 9.7           | 39669        |
| nábřeží k      |                |          | Budějovice     |          |               |              |
| Husovce        |                |          |                |          |               |              |
| Junglepark     | Run            | Czech    | Brno           | 367.37   | 25.6568       | 38084        |
|                |                | Republic |                |          |               |              |
| 400m-Jičín     | Run            | Czechia  | Jičín          | 401.7    | 3.2           | 38024        |
| Karlův most    | Run            | Czech    | Prague         | 289.0    | 2.8           | 37490        |
| ONLY           |                | Republic |                |          |               |              |
| Stodůlecký -   | Run            | Czechia  | Praha 13       | 542.0    | 0.0           | 36838        |
| Nepomucký      |                |          |                |          |               |              |
| rybník         |                |          |                |          |               |              |
| Smetanovy      | Run            | Czechia  | Olomouc        | 639.7    | 3.65364       | 35542        |
| reverse        |                |          |                |          |               |              |
| Ještěd Finale  | Ride           | Czechia  | Světlá pod     | 763.9    | 69.2          | 35105        |
| konec před     |                |          | Ještědem       |          |               |              |
| kostk...       |                |          |                |          |               |              |
| 400m           | Run            | Czechia  | Pardubice V    | 414.7    | 0.0           | 33533        |
| Lužánky -      | Run            | Czech    | Brno           | 411.9    | 0.0           | 32808        |
| Plochá dráha   |                | Republic |                |          |               |              |
| Sedýlko -      | Ride           | Czech    | Loučná Nad     | 1210.1   | 69.9          | 31977        |
| Praděd climb   |                | Republic | Desnou         |          |               |              |
| Sprintík křižo | Ride           | Czech    | Blansko        | 3075.3   | 222.0         | 30470        |
| vatka/skalní   |                | Republic |                |          |               |              |
| mlý...         |                |          |                |          |               |              |
| Szpic Jested   | Ride           | Czechia  | Liberec        | 2926.9   | 236.7         | 30366        |
| last 3 km ( od |                |          |                |          |               |              |
| r...           |                |          |                |          |               |              |
| Muglinovská→Hr | Ride           | Czechia  | Ostrava        | 2847.9   | 46.4          | 30174        |
| adní lávka (po |                |          |                |          |               |              |
| p...           |                |          |                |          |               |              |
| svadov—valtiro | Ride           | Czechia  | Ústí nad Labem | 2883.8   | 7.0           | 27238        |
| v              |                |          | -Neštěmice     |          |               |              |
| Lysá hora - 5  | Ride           | Czech    | Staré Hamry    | 4951.0   | 485.4         | 26025        |
| km             |                | Republic |                |          |               |              |
| Údolí Svatý    | Ride           | Czech    | Beroun         | 5730.4   | 38.8          | 24900        |
| Jan            |                | Republic |                |          |               |              |
| S&Ch20         | Ride           | Czechia  | Ostrovačice    | 5136.6   | 78.0          | 24520        |
| Masarykův      |                |          |                |          |               |              |
| okruh          |                |          |                |          |               |              |
| Maslovice -    | Ride           | Czech    | Máslovice      | 5287.0   | 33.8          | 24501        |
| Kralupy        |                | Republic |                |          |               |              |
| Klinovec Top   | Ride           | Czechia  | Jáchymov       | 940.2    | 58.0          | 24427        |
| Stezka nábřeží | Run            | Czechia  | Zlín           | 588.5    | 5.4           | 23788        |
| Stadion        | Run            | Czechia  | Čelákovice     | 403.4    | 5.6           | 23530        |
| Čelákovice     |                |          |                |          |               |              |
| 400m (II.)     |                |          |                |          |               |              |
| Adamaov climb  | Ride           | Czechia  | Adamov         | 3599.6   | 278.9         | 22707        |
| Juliska 400 m  | Run            | Czechia  | Prague         | 410.1    | 10.8          | 22164        |
| Papezov -      | Ride           | Czechia  | Krásná         | 7714.6   | 13.2          | 21245        |
| Prazmo         |                |          |                |          |               |              |
| Výstup na      | Ride           | Czechia  | null           | 1190.2   | 65.2          | 20481        |
| Klínovec       |                |          |                |          |               |              |
| Cyklostezka    | Ride           | Czechia  | Hřensko        | 1001.9   | 27.9          | 20268        |
| sprint směr    |                |          |                |          |               |              |
| Děčín          |                |          |                |          |               |              |
| Malchor - Lysá | Hike           | Czech    | Krásná         | 727.9    | 120.2         | 20111        |
| Hora           |                | Republic |                |          |               |              |
| Total brikule  | Ride           | Czechia  | Staré Město    | 572.0    | 0.0           | 19132        |
| 🚀             |                |          |                |          |               |              |
| Cyklostezka    | Ride           | Czechia  | Náchod         | 3593.0   | 11.5          | 18864        |
| Náchod ->      |                |          |                |          |               |              |
| Velké Po...    |                |          |                |          |               |              |
| 400 m (track   | Run            | Czechia  | Benešov        | 406.8    | 0.0           | 18817        |
| num. 2)        |                |          |                |          |               |              |
| Podle Radbuzy  | Ride           | Czech    | Pilsen         | 2315.0   | 15.8          | 18400        |
|                |                | Republic |                |          |               |              |
| Trinec-Tesin   | Ride           | Czechia  | Třinec         | 4677.3   | 9.4           | 17820        |
| MH - Klaster   | Ride           | Czechia  | Klášter        | 1458.9   | 4.8           | 17589        |
|                |                |          | Hradiště nad   |          |               |              |
|                |                |          | Jizerou        |          |               |              |
| Benedikt -     | Run            | Czechia  | Most           | 1995.5   | 35.7          | 16628        |
| Parkoviště     |                |          |                |          |               |              |
| stezka         | Run            | Czech    | České          | 1000.0   | 6.4           | 16043        |
|                |                | Republic | Budějovice     |          |               |              |
| Židlochovice   | Ride           | Czechia  | Židlochovice   | 12812.5  | 20.4          | 15945        |
| -> Olympia     |                |          |                |          |               |              |
| Do sedla       | Ride           | Czech    | Loučná pod     | 2782.7   | 177.4         | 15827        |
| Klínovce po    |                | Republic | Klínovcem      |          |               |              |
| silnici        |                |          |                |          |               |              |
| Ovál ZŠ        | Run            | Czechia  | Hradec Králové | 269.6    | 0.0           | 15633        |
| Štefánikova    |                |          |                |          |               |              |
| Tuhnice        | Ride           | Czech    | Karlovy Vary   | 2383.8   | 0.0           | 15542        |
| most-Drahovice |                | Republic |                |          |               |              |
| most,st...     |                |          |                |          |               |              |
| Mutěnka - z    | Ride           | Czechia  | Kyjov          | 3713.4   | 0.0           | 15204        |
| Kyjova po      |                |          |                |          |               |              |
| odbočku ...    |                |          |                |          |               |              |
| Kynšperský     | Ride           | Czechia  | Kynšperk nad   | 634.2    | 0.0           | 15182        |
| ATAK           |                |          | Ohří           |          |               |              |
| Šárka Valley   | Run            | Czechia  | Praha 6        | 976.5    | 0.0           | 15181        |
| (short)        |                |          |                |          |               |              |
| Decin - Bad    | Ride           | Czechia  | Děčín          | 18518.5  | 28.0          | 15069        |
| Schandau       |                |          |                |          |               |              |
| Abzweig R...   |                |          |                |          |               |              |
| Track          | Run            | Czechia  | Domažlice      | 397.4    | 5.6           | 14708        |
| Domažlice      |                |          |                |          |               |              |
| 400m -         | Run            | Czechia  | Jihlava        | 394.1    | 0.0           | 14591        |
| Sportovní      |                |          |                |          |               |              |
| areál Na       |                |          |                |          |               |              |
| Stou...        |                |          |                |          |               |              |
| Štvanická      | Run            | Czechia  | Prague         | 277.5    | 6.2           | 14503        |
| lávka (do      |                |          |                |          |               |              |
| Karlína)       |                |          |                |          |               |              |
| Zlaťák konec - | Ride           | Czechia  | Vítkovice      | 507.3    | 42.1          | 14461        |
| smrt           |                |          |                |          |               |              |
| Transformator  | Hike           | Czechia  | Ostravice      | 1537.0   | 158.4         | 14098        |
| k Butorance (u |                |          |                |          |               |              |
| s...           |                |          |                |          |               |              |
| Hradní lávka   | Run            | Czechia  | Ostrava        | 996.4    | 22.7          | 14042        |
| => Sýkorův     |                |          |                |          |               |              |
| most           |                |          |                |          |               |              |
| k přehradě hop | Ride           | Czech    | Krásná Lípa    | 315.9    | 21.4          | 13871        |
|                |                | Republic |                |          |               |              |
| TJ Znojmo Lap  | Run            | Czechia  | Znojmo         | 404.6    | 5.1           | 13647        |
| Park 1         | Run            | Czech    | Ostrava        | 718.9    | 0.0           | 13600        |
|                |                | Republic |                |          |               |              |
| mezi mosty     | Run            | Czechia  | Pardubice      | 957.4    | 6.2           | 12916        |
| Chrudim climb  | Ride           | Czech    | Chrudim        | 866.4    | 16.6          | 12612        |
|                |                | Republic |                |          |               |              |
| Špindlerovka - | Ride           | Czechia  | Špindlerův     | 4162.3   | 232.3         | 12583        |
| část II. (od   |                |          | Mlýn           |          |               |              |
| Če...          |                |          |                |          |               |              |
| Hostyn-od.zast | Ride           | Czech    | Bystřice Pod   | 5103.32  | 340.8         | 12560        |
| avky.po.znacku |                | Republic | Hostýnem       |          |               |              |
| .P             |                |          |                |          |               |              |
| Sedmička,      | Ride           | Czechia  | Přední Výtoň   | 4110.2   | 19.9          | 12542        |
| Lipno {        |                |          |                |          |               |              |
| Černý důl      | Ride           | Czechia  | Černý Důl      | 3571.2   | 180.6         | 12541        |
| konec          |                |          |                |          |               |              |
| Hoffmanky      |                |          |                |          |               |              |
| Solan last km  | Ride           | Czechia  | Hutisko-Solane | 1105.9   | 77.4567       | 12358        |
|                |                |          | c              |          |               |              |
| Eurovie -      | Ride           | Czechia  | Pardubice II   | 1364.7   | 2.0           | 12048        |
| nadjezd Rosice |                |          |                |          |               |              |
| Obří hřeben -  | Hike           | Poland   | Karpacz        | 453.9    | 81.8          | 11209        |
| stoupák        |                |          |                |          |               |              |
| Nová           | Ride           | Czechia  | Jihlava        | 2526.5   | 22.2          | 11048        |
| cyklostezka do |                |          |                |          |               |              |
| Bosche  2      |                |          |                |          |               |              |
| od hráze až na | Run            | Czech    | Liberec        | 949.6    | 40.1          | 10846        |
| konec přehrady |                | Republic |                |          |               |              |
| ...            |                |          |                |          |               |              |
| Cyklostezka    | Ride           | Czechia  | Dobříš         | 558.5    | 11.0          | 10768        |
| Stará          |                |          |                |          |               |              |
| huť-Dobříš     |                |          |                |          |               |              |
| most - Loket   | Ride           | Czechia  | Staré Sedlo    | 2515.6   | 2.2           | 10610        |
| Bunč climb     | Ride           | Czech    | Kostelany      | 1876.0   | 0.0           | 10555        |
|                |                | Republic |                |          |               |              |
| Okolo Bobrůvky | Ride           | Czechia  | Nové Město na  | 918.5    | 0.0           | 10461        |
| Tři Studně -   |                |          | Moravě         |          |               |              |
| Ko...          |                |          |                |          |               |              |
| Daskabát flat  | Ride           | Czech    | Velký Újezd    | 1868.0   | 4.4           | 10016        |
|                |                | Republic |                |          |               |              |
| Kolem stadionu | Run            | Czechia  | Hradec Kralove | 449.9    | 0.0           | 9726         |
| Krkonošská     | Ride           | Czechia  | Vrchlabí       | 833.5    | 0.0           | 9571         |
| Kleť k         | Ride           | Czech    | Kájov          | 2495.8   | 186.0         | 9563         |
| vysílači -     |                | Republic |                |          |               |              |
| finále         |                |          |                |          |               |              |
| Velodrom 1kolo | Ride           | Czechia  | Louny          | 492.1    | 8.9           | 9533         |
| Lednice -      | Ride           | Czechia  | Lednice        | 3609.1   | 15.5          | 9504         |
| Bulhary        |                |          |                |          |               |              |
| Rovinka        | Ride           | Czechia  | Malý Beranov   | 948.2    | 6.4           | 9373         |
| Beranov        |                |          |                |          |               |              |
| Lysa hora -    | Run            | Czech    | Ostravice      | 298.4    | 63.6          | 9361         |
| jizni          |                | Republic |                |          |               |              |
| sjezdovka      |                |          |                |          |               |              |
| Szlak          | Hike           | Poland   | Karpacz        | 2131.5   | 344.6         | 9130         |
| czerwony,      |                |          |                |          |               |              |
| Schronisko     |                |          |                |          |               |              |
| Nad...         |                |          |                |          |               |              |
| plný kule z    | Ride           | Czechia  | Kolín          | 648.1    | 0.0           | 8614         |
| kolína         |                |          |                |          |               |              |
| Kaufland -     | Ride           | Czechia  | Jičín          | 1923.7   | 10.2          | 8543         |
| Popendorf      |                |          |                |          |               |              |
| Plácky-soutok  | Ride           | Czechia  | Hradec Králové | 3226.9   | 13.6          | 8324         |
| Panelovka-Tich | Run            | Czechia  | Mostkovice     | 802.8    | 0.0           | 8242         |
| á 800m         |                |          |                |          |               |              |
| Lípy (směrem   | Run            | Czechia  | Jičín          | 1714.8   | 7.6           | 8066         |
| do Jičína)     |                |          |                |          |               |              |
| 611 - Mstetice | Ride           | Czech    | Jirny          | 1681.0   | 0.0           | 7891         |
|                |                | Republic |                |          |               |              |
| Šantovka -     | Ride           | Czechia  | Olomouc        | 1139.4   | 3.0           | 7871         |
| Kojeňák        |                |          |                |          |               |              |
| Ku řopíku      | Run            | Czechia  | Děčín          | 794.7    | 4.4           | 7752         |
| Třebíč -       | Ride           | Czech    | Stařeč         | 881.7    | 18.6          | 7745         |
| Stařeč po      |                | Republic |                |          |               |              |
| cyklostezce... |                |          |                |          |               |              |
| Máchovo        | Ride           | Czechia  | Doksy          | 4746.0   | 27.6          | 7606         |
| kritérium -    |                |          |                |          |               |              |
| přes bory ...  |                |          |                |          |               |              |
| Od Sanusu ke   | Run            | Czech    | Hradec Králové | 575.0    | 8.2           | 7505         |
| gymplu         |                | Republic |                |          |               |              |
| Vlevo dole     | Ride           | Czechia  | Most           | 4725.9   | 11.9054       | 7502         |
| jezero Most    |                |          |                |          |               |              |
| Od letňáku ke  | Run            | Czechia  | Jihlava        | 460.0    | 2.02579       | 7468         |
| starému vchodu |                |          |                |          |               |              |
| Z...           |                |          |                |          |               |              |
| Výrovka -      | Ride           | Czech    | Pec pod        | 1420.0   | 160.0         | 7446         |
| Modré Sedlo    |                | Republic | Sněžkou        |          |               |              |
| 2012 Pikes     | Ride           | United   | Woodland Park  | 19471.3  | 1440.4        | 7331         |
| Peak Hill      |                | States   |                |          |               |              |
| Climb          |                |          |                |          |               |              |
| JestedSkyrace  | Run            | Czech    | Liberec        | 1005.5   | 159.0         | 7297         |
| - last uphill  |                | Republic |                |          |               |              |
| - ...          |                |          |                |          |               |              |
| Od křižovatky  | Ride           | Czechia  | Strání         | 2393.7   | 129.0         | 7241         |
| do Strání po   |                |          |                |          |               |              |
| vys...         |                |          |                |          |               |              |
| LS - Park      | Run            | Czechia  | Bruntál        | 381.4    | 2.2           | 7240         |
| Boost          |                |          |                |          |               |              |
| Bečva -        | Ride           | Czechia  | Prostřední     | 9570.7   | 525.4         | 6990         |
| Pustevny       |                |          | Bečva          |          |               |              |
| Uphill         |                |          |                |          |               |              |
| #ULhalf -      | Run            | Czechia  | Ústí nad       | 1435.9   | 9.8           | 6927         |
| Strekovske     |                |          | Labem-Střekov  |          |               |              |
| Nabrezi        |                |          |                |          |               |              |
| Šobes - sjezd  | Ride           | Czech    | Podmolí        | 1422.0   | 2.2           | 6886         |
|                |                | Republic |                |          |               |              |
| Javorový od    | Hike           | Czechia  | Třinec         | 1265.3   | 393.2         | 6878         |
| stanice        |                |          |                |          |               |              |
| lanovky        |                |          |                |          |               |              |
| Klobouky       | Ride           | Czechia  | Valašské       | 1089.8   | 17.6          | 6800         |
| Viadukt        |                |          | Klobouky       |          |               |              |
| Dom Śląski Up  | Hike           | Czechia  | Pec pod        | 2549.5   | 435.7         | 6770         |
| Hill           |                |          | Sněžkou        |          |               |              |
| Javorník       | Run            | Czech    | Trojanovice    | 1059.98  | 116.111       | 6355         |
| finish od      |                | Republic |                |          |               |              |
| Pinduly        |                |          |                |          |               |              |
| Tatran         | Run            | Czech    | Třemošná       | 421.5    | 7.4           | 6324         |
| Třemošná       |                | Republic |                |          |               |              |
| Podél dálnice  | Ride           | Czechia  | Nepřevázka     | 11403.1  | 44.9728       | 6232         |
| Sprint Páteček | Ride           | Czechia  | Sušice         | 1792.3   | 6.8           | 6200         |
| - Santos       |                |          |                |          |               |              |
| Tři prameny -  | Hike           | Czechia  | Hřensko        | 1941.0   | 175.2         | 6175         |
| Pravčická      |                |          |                |          |               |              |
| brána          |                |          |                |          |               |              |
| do Srní        | Ride           | Czechia  | Srní           | 753.4    | 43.1          | 6096         |
| Interval       | Run            | Czech    | Olomouc        | 848.8    | 0.0           | 5909         |
|                |                | Republic |                |          |               |              |
| Hoštejn-Zábřeh | Ride           | null     | null           | 7688.6   | 0.0           | 5898         |
| Benešovský     | Ride           | Czechia  | Benešov u      | 1087.6   | 13.2          | 5788         |
| brdek          |                |          | Semil          |          |               |              |
| Kuželna -      | Run            | Czechia  | Vsetín         | 814.3    | 3.43077       | 5676         |
| Splav 800m     |                |          |                |          |               |              |
| Kvilda Bučina  | Ride           | Czech    | Kvilda         | 5645.6   | 139.2         | 5605         |
|                |                | Republic |                |          |               |              |
| Starý Kolín -  | Ride           | Czechia  | Starý Kolín    | 2289.7   | 10.0          | 5541         |
| Svatá Kateřina |                |          |                |          |               |              |
| Nové Lesy-Dvůr | Ride           | null     | null           | 3238.1   | 0.0           | 5332         |
| Králové        |                |          |                |          |               |              |
| Kerhartice-Cho | Ride           | Czech    | Ústí nad       | 15217.4  | 41.2          | 5216         |
| ceň            |                | Republic | Orlicí         |          |               |              |
| Stojka na      | Ride           | Czechia  | Železná Ruda   | 382.6    | 39.3          | 5008         |
| Pancíř         |                |          |                |          |               |              |
| Ciclo Via BNL  | Run            | Czechia  | Brandýs nad    | 1025.6   | 0.0           | 4982         |
| -> K           |                |          | Labem-Stará    |          |               |              |
|                |                |          | Bolesl...      |          |               |              |
| Bludička-Opavi | Run            | Czechia  | Opava          | 578.4    | 2.4           | 4901         |
| ce             |                |          |                |          |               |              |
| Final climb ke | Ride           | Czech    | Deštné v       | 667.2    | 54.5          | 4899         |
| srubu na       |                | Republic | Orlických      |          |               |              |
| Deštno...      |                |          | horách         |          |               |              |
| Od lávky k     | Run            | Czechia  | Rakovník       | 302.1    | 0.0           | 4879         |
| lávce          |                |          |                |          |               |              |
| Sjezd Blatno-B | Ride           | Czechia  | Blatno         | 3672.7   | 2.2           | 4810         |
| řezenec        |                |          |                |          |               |              |
| Luby end       | Run            | Czech    | Klatovy        | 517.7    | 0.0           | 4694         |
|                |                | Republic |                |          |               |              |
| Vojenský ovál  | Run            | Czechia  | Hradec Králové | 410.8    | 0.0           | 4509         |
| 400M           |                |          |                |          |               |              |
| 400 metrů, 44  | Run            | Czechia  | Brno-Královo   | 427.7    | 4.1           | 4461         |
| 120 diváků     |                |          | Pole           |          |               |              |
| Luční bouda -  | Hike           | Czechia  | Pec pod        | 3347.1   | 231.8         | 4451         |
| Sněžka         |                |          | Sněžkou        |          |               |              |
| Pustevny -     | Hike           | Czechia  | Trojanovice    | 3632.9   | 166.0         | 4411         |
| Radhošť        |                |          |                |          |               |              |
| stupani k      | Ride           | Czech    | Javorník       | 1865.9   | 32.2          | 4403         |
| vetr. mlynu    |                | Republic |                |          |               |              |
| Kuzelov        |                |          |                |          |               |              |
| hurá na Říp    | Ride           | null     | null           | 617.5    | 0.0           | 4245         |
| Červená voda - | Ride           | Czech    | Červená Voda   | 6543.5   | 261.2         | 4104         |
| Suchý vrch     |                | Republic |                |          |               |              |
| Dlouhá míle    | Run            | Czechia  | Sušice         | 1515.0   | 4.0           | 4033         |
| Pod Homoli     | Ride           | Czech    | Liberk         | 1547.8   | 89.7          | 3982         |
| Climb          |                | Republic |                |          |               |              |
| Šup do parku   | Run            | Czechia  | Plzeň 1        | 424.9    | 0.0           | 3939         |
| Tuhnická lávka | Run            | Czechia  | Karlovy Vary   | 1058.3   | 6.8           | 3931         |
| -Chebský most  |                |          |                |          |               |              |
| Nábřeží        | Run            | Czechia  | Kadaň          | 1319.6   | 21.4          | 3882         |
| Dářská         | Ride           | Czechia  | Radostín       | 3293.8   | 16.0          | 3864         |
| rašeliniště    |                |          |                |          |               |              |
| panelka k      | Ride           | Czech    | Pec            | 530.6    | 60.4          | 3862         |
| bráně ˇerchova |                | Republic |                |          |               |              |
| Kozí hřbety -  | Hike           | Czechia  | Špindlerův     | 1993.7   | 16.8          | 3837         |
| Luční bouda    |                |          | Mlýn           |          |               |              |
| Hradiště -     | Run            | Czechia  | Uherské        | 437.7    | 0.0           | 3792         |
| čtyřstovka     |                |          | Hradiště       |          |               |              |
| Pisek podel    | Run            | null     | null           | 708.4    | 7.6           | 3740         |
| reky I         |                |          |                |          |               |              |
| Opavice od     | Run            | Czechia  | Krnov          | 672.8    | 0.0           | 3673         |
| zatáčky        |                |          |                |          |               |              |
| U Jordánu do   | Run            | Czechia  | Tábor          | 984.6    | 20.3          | 3607         |
| kopce          |                |          |                |          |               |              |
| Ruda ->        | Ride           | Czech    | Železná Ruda   | 3222.9   | 144.0         | 3598         |
| Gerlovka       |                | Republic |                |          |               |              |
| Pec - Sněžka   | Hike           | Czech    | Pec pod        | 6374.3   | 870.3         | 3521         |
| (přes Obřák)   |                | Republic | Sněžkou        |          |               |              |
| Kopeček - od   | Run            | Czech    | Samotišky      | 776.1    | 109.8         | 3360         |
| kruháče k      |                | Republic |                |          |               |              |
| bazilic...     |                |          |                |          |               |              |
| Debř-Michalovi | Run            | Czechia  | Hrdlořezy      | 1122.2   | 12.0          | 3179         |
| ce ☠           |                |          |                |          |               |              |
| Kopec pod      | Ride           | Czech    | Kutna Hora     | 838.6    | 41.6          | 3032         |
| Barborou       |                | Republic |                |          |               |              |
| segment z      | Ride           | Czechia  | Tábor          | 819.3    | 43.0          | 2996         |
| Tábora         |                |          |                |          |               |              |
| Gránické údolí | Run            | Czechia  | Znojmo         | 1026.2   | 0.0           | 2730         |
| - Central Part |                |          |                |          |               |              |
| ...            |                |          |                |          |               |              |
| Segment        | Run            | Czech    | Ctiněves       | 565.1    | 131.4         | 2682         |
|                |                | Republic |                |          |               |              |
| Richtrovy      | Hike           | Czechia  | Pec pod        | 1350.1   | 194.4         | 2681         |
| boudy -        |                |          | Sněžkou        |          |               |              |
| Výrovka        |                |          |                |          |               |              |
| Kleť           | Hike           | Czechia  | Holubov        | 1899.1   | 362.1         | 2653         |
| Železniční     | Run            | Czechia  | Ostrava        | 2136.6   | 34.5          | 2612         |
| most => Jez    |                |          |                |          |               |              |
| Vítkovi...     |                |          |                |          |               |              |
| Le Grande      | Ride           | Czech    | Spálov         | 1790.4   | 23.3          | 2557         |
| Classico       |                | Republic |                |          |               |              |
| Snezka po      | Run            | null     | null           | 743.4    | 173.0         | 2502         |
| schodech       |                |          |                |          |               |              |
| Rovinka od     | Run            | Czechia  | Klatovy        | 732.4    | 0.0           | 2437         |
| kruháče k      |                |          |                |          |               |              |
| bazénu         |                |          |                |          |               |              |
| Jesenice-Blatn | Ride           | Czechia  | Jesenice       | 3956.5   | 2.4           | 2353         |
| o DH           |                |          |                |          |               |              |
| Špindlerův     | Hike           | Czechia  | Špindlerův     | 385.2    | 78.2          | 2303         |
| Mlýn - Školní  |                |          | Mlýn           |          |               |              |
| Giro di Tyrš   | Run            | Czechia  | Aš             | 369.4    | 5.1           | 1990         |
| Labe_po        | Run            | Czechia  | Kolín          | 1243.6   | 0.0           | 1942         |
| asfaltu        |                |          |                |          |               |              |
| Ondřejník      | Run            | Czechia  | Lhotka         | 1082.0   | 123.2         | 1922         |
| sedlo -        |                |          |                |          |               |              |
| Ondřejník      |                |          |                |          |               |              |
| vr...          |                |          |                |          |               |              |
| Tygří výzva,   | Run            | Czechia  | Liberec -      | 871.7    | 279.0         | 1822         |
| sklon 32% :)   |                |          | Horní Hanychov |          |               |              |
| Červená podél  | Ride           | Czechia  | Třeboň         | 1580.8   | 0.0           | 1745         |
| Zlaté stoky do |                |          |                |          |               |              |
| T...           |                |          |                |          |               |              |
| Nová           | Ride           | Czechia  | Horšovský Týn  | 1817.8   | 11.2          | 1622         |
| cyklopěšina z  |                |          |                |          |               |              |
| Peřiny do H... |                |          |                |          |               |              |
| Od bývalé      | Hike           | Czechia  | Liberec        | 2046.4   | 341.2         | 1568         |
| sáňkařské      |                |          |                |          |               |              |
| dráhy po m...  |                |          |                |          |               |              |
| Koupaliště     | Run            | Czechia  | Vlašim         | 348.2    | 0.0           | 1555         |
| sprint         |                |          |                |          |               |              |
| Mezi zábranama | Run            | Czech    | Jaroměř        | 1067.3   | 3.5           | 1514         |
| (proti proudu) |                | Republic |                |          |               |              |
| rovinka kolem  | Run            | Czechia  | Čtyřkoly       | 800.7    | 0.0           | 1447         |
| Sázavy:Plynovo |                |          |                |          |               |              |
| d-...          |                |          |                |          |               |              |
| Ježánky(Visala | Hike           | Czechia  | Morávka        | 1810.9   | 120.8         | 1413         |
| je) - Bílý     |                |          |                |          |               |              |
| Kříž ...       |                |          |                |          |               |              |
| Zrucskej       | Ride           | Czech    | Zruč nad       | 732.4    | 74.7          | 1334         |
| smrtak         |                | Republic | Sázavou        |          |               |              |
| podle Labe do  | Ride           | Czech    | Kojice         | 1697.1   | 16.0          | 1326         |
| Týnce          |                | Republic |                |          |               |              |
| Z Doubravky k  | Run            | Czechia  | Hořice         | 796.5    | 44.2          | 1319         |
| Josefu         |                |          |                |          |               |              |
| Okruhy Ochozou | Run            | Czechia  | Nové Město na  | 734.3    | 92.9          | 1265         |
| - Výběh na     |                |          | Moravě         |          |               |              |
| Haru...        |                |          |                |          |               |              |
| Most - Most -> | Run            | Czechia  | Břeclav        | 807.1    | 0.0           | 1233         |
| Břeclav        |                |          |                |          |               |              |
| Hlavní třídou  | Run            | Czechia  | Havířov        | 928.7    | 9.8175        | 1230         |
| nahoru         |                |          |                |          |               |              |
| Stadion - 400  | Run            | Czechia  | Dačice         | 429.6    | 2.4           | 1193         |
| m              |                |          |                |          |               |              |
| Rybnik         | Run            | Czechia  | Kroměříž       | 439.1    | 0.0           | 1184         |
| Pláně - Černý  | Hike           | Czechia  | Světlá pod     | 1207.9   | 135.4         | 1182         |
| vrch           |                |          | Ještědem       |          |               |              |
| Opavska down   | Run            | Czech    | Ostrava        | 1456.7   | 0.0           | 1166         |
| 1/2            |                | Republic |                |          |               |              |
| Ořešník        | Hike           | Czechia  | Hejnice        | 2324.7   | 375.7         | 1108         |
| Karlov - k     | Hike           | Czechia  | Malá Morávka   | 4217.1   | 337.4         | 1055         |
| Velkému kotli  |                |          |                |          |               |              |
| Luisino údolí  | Hike           | Czechia  | Deštné v       | 1921.9   | 227.799       | 1050         |
| - Velká Deštná |                |          | Orlických      |          |               |              |
|                |                |          | horách         |          |               |              |
| Berounka       | Run            | Czechia  | Beroun         | 327.1    | 6.4           | 1026         |
| sprint         |                |          |                |          |               |              |
| Po červené na  | Hike           | Czechia  | Prášily        | 2460.8   | 216.1         | 995          |
| Předěl         |                |          |                |          |               |              |
| Svaty kopecek  | Hike           | Czechia  | Mikulov        | 707.3    | 100.378       | 975          |
| up             |                |          |                |          |               |              |
| Brno Circuit   | Run            | null     | null           | 5252.02  | 95.705        | 892          |
| Pod Vilemínkou | Hike           | Poland   | null           | 4939.8   | 595.0         | 844          |
| - Kralický     |                |          |                |          |               |              |
| Sněž...        |                |          |                |          |               |              |
| Výpřež -       | Hike           | Czechia  | okres Liberec  | 1529.8   | 223.0         | 841          |
| Ještěd (po     |                |          |                |          |               |              |
| červené)       |                |          |                |          |               |              |
| kopec na hrad  | Hike           | Czechia  | null           | 673.7    | 105.169       | 819          |
| BL Boletice -  | Run            | Czechia  | Horní Planá    | 982.8    | 2.9           | 813          |
| rovinka na     |                |          |                |          |               |              |
| hřebe...       |                |          |                |          |               |              |
| Neklid ->      | Hike           | Czechia  | Jáchymov       | 2199.9   | 127.2         | 800          |
| Klínovec       |                |          |                |          |               |              |
| Pod rozhlednu  | Hike           | Czechia  | Lelekovice     | 891.5    | 170.2         | 780          |
| Babi lom       |                |          |                |          |               |              |
| Videlské       | Hike           | Czechia  | Vrbno pod      | 2784.8   | 421.716       | 675          |
| sedlo-Švýcárna |                |          | Pradědem       |          |               |              |
| Modrava -      | Hike           | Czechia  | Modrava        | 2654.1   | 88.8          | 644          |
| Tříjezerní     |                |          |                |          |               |              |
| slať           |                |          |                |          |               |              |
| VR #11 finish  | Run            | Czechia  | Vyšší Brod     | 962.4    | 3.0           | 643          |
| Hadí stezka    | Run            | Czechia  | Sušice         | 1001.1   | 148.4         | 624          |
| (Svatobor)     |                |          |                |          |               |              |
| Borůvková hora | Hike           | Czechia  | Javorník       | 1772.3   | 170.4         | 591          |
| part II        |                |          |                |          |               |              |
| Ostaš          | Hike           | Czechia  | Žďár nad       | 2150.3   | 107.158       | 567          |
|                |                |          | Metují         |          |               |              |
| Ručičky -      | Hike           | Czechia  | Harrachov      | 2791.8   | 207.8         | 562          |
| Krakonošova    |                |          |                |          |               |              |
| snídaně ...    |                |          |                |          |               |              |
| Čerťák -       | Hike           | Czechia  | Rokytnice nad  | 4614.7   | 79.8          | 531          |
| Ručičky (po    |                |          | Jizerou        |          |               |              |
| modré)         |                |          |                |          |               |              |
| Říp po žluté   | Hike           | Czechia  | Mnetěš         | 371.0    | 78.0          | 518          |
| na vyhlídku    |                |          |                |          |               |              |
| 15% Stoupák    | Hike           | Czechia  | Bílý Potok     | 2642.3   | 0.0           | 506          |
| Bártlovka->Pal |                |          |                |          |               |              |
| iční...        |                |          |                |          |               |              |
| Posázavskou k  | Hike           | Czechia  | Hradištko      | 2310.8   | 17.5533       | 471          |
| odbočce před   |                |          |                |          |               |              |
| sch...         |                |          |                |          |               |              |
| Pavlov - Dívčí | Run            | Czech    | Pavlov         | 903.9    | 0.0           | 423          |
| hrad climb     |                | Republic |                |          |               |              |
| podél          | Run            | Czechia  | Čáslav         | 612.5    | 0.0           | 418          |
| Podměstského   |                |          |                |          |               |              |
| rybníku        |                |          |                |          |               |              |
| Kočičí žleb -  | Hike           | Czechia  | Brno           | 1771.6   | 100.0         | 402          |
| Ríšova         |                |          |                |          |               |              |
| studánka       |                |          |                |          |               |              |
| Dneboh -       | Hike           | Czechia  | Mnichovo       | 486.3    | 76.896        | 376          |
| Drábské        |                |          | Hradiště       |          |               |              |
| Světničky      |                |          |                |          |               |              |
| Zig-zag na     | Hike           | Czechia  | Lipová-lázně   | 2777.7   | 320.3         | 371          |
| Šerák          |                |          |                |          |               |              |
| Kraličák       | Run            | Czechia  | Staré Město    | 1571.0   | 201.8         | 359          |
| Skyrace - 2.   |                |          |                |          |               |              |
| kopec          |                |          |                |          |               |              |
| Podél tratě do | Run            | Czechia  | Praha-Klánovic | 2663.3   | 8.0           | 322          |
| Úval           |                |          | e              |          |               |              |
| Soláň-Tanečnic | Hike           | Czechia  | Hutisko-Solane | 4425.3   | 199.2         | 314          |
| a              |                |          | c              |          |               |              |
| Hilo to Mauna  | Ride           | United   | Hilo           | 68605.4  | 4284.12       | 309          |
| Kea            |                | States   |                |          |               |              |
| Dlouhe Strane  | Ride           | Czechia  | Loučná nad     | 12619.0  | 891.8         | 308          |
| od Loucnej     |                |          | Desnou         |          |               |              |
| Valy           | Run            | Czechia  | Litomyšl       | 561.3    | 0.0           | 283          |
| Tříjezerní     | Hike           | Czechia  | Modrava        | 3326.0   | 2.6           | 253          |
| slať - Rokyta  |                |          |                |          |               |              |
| Hadí stezka na | Hike           | Czechia  | Hrádek         | 1020.9   | 167.4         | 232          |
| Svatobor 🐍    |                |          |                |          |               |              |
| Sněžník od     | Hike           | Czechia  | Děčín          | 2915.9   | 316.0         | 224          |
| Děčína (po     |                |          |                |          |               |              |
| červené)       |                |          |                |          |               |              |
| Hrad Vevěří -  | Hike           | Czechia  | Brno           | 7882.0   | 125.2         | 209          |
| Hráz           |                |          |                |          |               |              |
| Šumbera pom.   | Hike           | Czechia  | Kanice         | 1107.6   | 11.0          | 186          |
| odb. - vysílač |                |          |                |          |               |              |
| Há...          |                |          |                |          |               |              |
| Stoupání na    | Hike           | Czechia  | Jamolice       | 598.3    | 111.2         | 92           |
| Templštejn     |                |          |                |          |               |              |
| Lacinův kámen  | Hike           | Czechia  | Tišnov         | 1900.0   | 181.0         | 91           |
| - Velká Skála  |                |          |                |          |               |              |
| Harusák Climb  | Hike           | Czechia  | Nové Město na  | 683.6    | 107.2         | 71           |
|                |                |          | Moravě         |          |               |              |