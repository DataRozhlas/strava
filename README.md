Časosběrné sledování segmentů na Stravě. Půjde z něj například zjistit, kdy se šlape na Praděd a kdy se běhá po Stromovce.

Nad rámec dat ze Stravy se do ```segments.parquet``` počítá vzdálenost vzdušnou čarou mezi startem a cílem – užitečné pro odfiltrování oválů a velodromů, na kterých může pár lidí nadělat velké denní výkyvy v effortech.

## Poslední aktualizace

2025-01-06

## Sledované segmenty

" shape: (261, 7)
| name                                                  | activity_type | country       | city                             | distance | total_elevation_gain | effort_count |
| ---                                                   | ---           | ---           | ---                              | ---      | ---                  | ---          |
| str                                                   | str           | str           | str                              | f64      | f64                  | i64          |
|-------------------------------------------------------|---------------|---------------|----------------------------------|----------|----------------------|--------------|
| Richmond ITT1                                         | Ride          | UK            | London                           | 589.3    | 7.2                  | 4625706      |
| Box Hill 2.2k                                         | Ride          | UK            | Mole Valley District, Surrey, UK | 2296.62  | 119.1                | 1415731      |
| Die Eine Runde                                        | Ride          | Czechia       | Brno                             | 380.0    | 0.0                  | 1089698      |
| Overtake the Boris Bikes                              | Run           | UK            | London                           | 591.8    | 2.2                  | 663738       |
| Třebešín-dráha K                                      | Ride          | Czechia       | Prague                           | 347.2    | 0.0                  | 402245       |
| Alpe d'Huez                                           | Ride          | France        | Le Bourg D'Oisans                | 12024.9  | 1047.3               | 336372       |
| Sa Calobra - Coll dels Reis                           | Ride          | Spain         | Escorca                          | 9416.77  | 659.8                | 323412       |
| Opičí Časovka, Podolská vodárna - Dvorce              | Ride          | Czechia       | Prague                           | 1390.1   | 6.0                  | 323005       |
| Prostějov kolo dráha P                                | Ride          | Czechia       | Prostějov                        | 311.1    | 0.0                  | 251263       |
| Koppenberg                                            | Ride          | Belgium       | Oudenaarde                       | 556.595  | 63.1                 | 245118       |
| Mont Ventoux (par Bedoin)                             | Ride          | France        | Bédoin                           | 20741.8  | 1569.4               | 242103       |
| Stelvio - Bormio Turn Downhill                        | Ride          | Italy         | null                             | 2982.1   | 5.4                  | 235601       |
| Zweite hup u ZOO                                      | Ride          | Czechia       | Praha-Troja                      | 314.1    | 6.6                  | 234006       |
| Zbraslav - Komořany                                   | Ride          | Czechia       | Zbraslav                         | 2359.0   | 5.7                  | 216976       |
| Stadion Na Děkance                                    | Run           | Czechia       | Prague                           | 420.9    | 0.0                  | 215619       |
| Lužánky rovinka                                       | Run           | Czechia       | Brno-střed                       | 268.9    | 3.8                  | 180145       |
| Šlechtovka - finální rovinka                          | Run           | Czechia       | Praha 7                          | 225.4    | 0.0                  | 156359       |
| time trial at Svratka                                 | Ride          | Czechia       | Brno                             | 1438.1   | 20.6                 | 141864       |
| Passo Stelvio                                         | Ride          | Italy         | null                             | 23600.3  | 1840.3               | 139224       |
| Od posledního tunelu do Bílovic                       | Ride          | Czechia       | Bílovice nad Svitavou            | 827.8    | 6.2                  | 124484       |
| VUT horní dráha 400m                                  | Run           | Czechia       | Brno                             | 405.2    | 0.0                  | 109048       |
| Col du Tourmalet (par Luz-St-Sauveur)                 | Ride          | France        | Luz Saint Sauveur                | 18827.5  | 1397.7               | 99930        |
| Vítkov up sprint                                      | Run           | Czechia       | Prague                           | 118.2    | 6.0                  | 86621        |
| Pražačka 320                                          | Run           | Czechia       | Prague                           | 343.3    | 0.0                  | 75242        |
| Viveros-Paseo alameda                                 | Run           | Spain         | Valencia                         | 1722.9   | 18.0                 | 73160        |
| TJ Sokol okruh                                        | Run           | Czechia       | Prague                           | 418.8    | 5.7                  | 72849        |
| Kolo na stadionu v Třebíči                            | Run           | Czechia       | Třebíč                           | 475.6    | 6.2                  | 69590        |
| Srbsko - Hlásná Třebáň                                | Ride          | Czechia       | Srbsko                           | 5736.1   | 13.5                 | 61460        |
| Stezka do Zlina                                       | Ride          | Czechia       | Zlin                             | 1368.28  | 23.1348              | 60475        |
| Rokytka od myčky                                      | Ride          | Czechia       | Praha 14                         | 1823.0   | 4.0                  | 59010        |
| Dráha Plzeň okruh P                                   | Ride          | Czechia       | Pilsen                           | 361.9    | 0.0                  | 54673        |
| Sptint pod Býčí skálou                                | Ride          | Czechia       | Olomučany                        | 778.8    | 0.0                  | 53348        |
| 400 m - atletický okruh - Lokomotiva                  | Run           | Czechia       | Olomouc                          | 400.0    | 2.9                  | 52422        |
| Hvězda flat                                           | Run           | Czechia       | Praha 6                          | 1001.15  | 11.426               | 49909        |
| tenis 1K                                              | Run           | Czechia       | Brno                             | 1002.8   | 0.0                  | 49020        |
| Tyršák čtyřstofka                                     | Run           | Czechia       | Šumperk                          | 426.5    | 3.1                  | 46670        |
| Llanberis path bottom section to the road             | Hike          | UK            | Caernarfon                       | 2417.5   | 0.0                  | 45005        |
| Od dubu ke Gizele                                     | Run           | Czechia       | Prague                           | 385.7    | 2.9                  | 44623        |
| Revnicak Eve                                          | Ride          | Czechia       | Řevnice                          | 5562.4   | 287.8                | 43493        |
| Risova studanka - od zavory                           | Ride          | Czechia       | Brno                             | 2612.4   | 138.5                | 41396        |
| Most Legií (směr Kampa)                               | Run           | Czechia       | Praha 1                          | 328.1    | 2.08                 | 40264        |
| Jiráskovo nábřeží k Husovce                           | Ride          | Czechia       | České Budějovice                 | 1113.6   | 9.7                  | 39669        |
| Junglepark                                            | Run           | Czechia       | Brno                             | 367.37   | 25.6568              | 38084        |
| 400m-Jičín                                            | Run           | Czechia       | Jičín                            | 401.7    | 3.2                  | 38024        |
| Karlův most ONLY                                      | Run           | Czechia       | Prague                           | 289.0    | 2.8                  | 37490        |
| Stodůlecký - Nepomucký rybník                         | Run           | Czechia       | Praha 13                         | 542.0    | 0.0                  | 36838        |
| Smetanovy reverse                                     | Run           | Czechia       | Olomouc                          | 639.7    | 3.65364              | 35542        |
| Ještěd Finale konec před kostkami.                    | Ride          | Czechia       | Světlá pod Ještědem              | 763.9    | 69.2                 | 35105        |
| 400m                                                  | Run           | Czechia       | Pardubice V                      | 414.7    | 0.0                  | 33533        |
| Lužánky - Plochá dráha                                | Run           | Czechia       | Brno                             | 411.9    | 0.0                  | 32808        |
| Sedýlko - Praděd climb                                | Ride          | Czechia       | Loučná Nad Desnou                | 1210.1   | 69.9                 | 31977        |
| Sprintík křižovatka/skalní mlýn                       | Ride          | Czechia       | Blansko                          | 3075.3   | 222.0                | 30470        |
| Szpic Jested  last 3 km ( od rozc na Dub)             | Ride          | Czechia       | Liberec                          | 2926.9   | 236.7                | 30366        |
| Muglinovská→Hradní lávka (po pravém břehu)            | Ride          | Czechia       | Ostrava                          | 2847.9   | 46.4                 | 30174        |
| svadov—valtirov                                       | Ride          | Czechia       | Ústí nad Labem-Neštěmice         | 2883.8   | 7.0                  | 27238        |
| Lysá hora - 5 km                                      | Ride          | Czechia       | Staré Hamry                      | 4951.0   | 485.4                | 26025        |
| Údolí Svatý Jan                                       | Ride          | Czechia       | Beroun                           | 5730.4   | 38.8                 | 24900        |
| S&Ch20 Masarykův okruh                                | Ride          | Czechia       | Ostrovačice                      | 5136.6   | 78.0                 | 24520        |
| Maslovice - Kralupy                                   | Ride          | Czechia       | Máslovice                        | 5287.0   | 33.8                 | 24501        |
| Klinovec Top                                          | Ride          | Czechia       | Jáchymov                         | 940.2    | 58.0                 | 24427        |
| Stezka nábřeží                                        | Run           | Czechia       | Zlín                             | 588.5    | 5.4                  | 23788        |
| Stadion Čelákovice 400m (II.)                         | Run           | Czechia       | Čelákovice                       | 403.4    | 5.6                  | 23530        |
| Adamaov climb                                         | Ride          | Czechia       | Adamov                           | 3599.6   | 278.9                | 22707        |
| Juliska 400 m                                         | Run           | Czechia       | Prague                           | 410.1    | 10.8                 | 22164        |
| Papezov - Prazmo                                      | Ride          | Czechia       | Krásná                           | 7714.6   | 13.2                 | 21245        |
| Výstup na Klínovec                                    | Ride          | Czechia       | null                             | 1190.2   | 65.2                 | 20481        |
| Cyklostezka sprint směr Děčín                         | Ride          | Czechia       | Hřensko                          | 1001.9   | 27.9                 | 20268        |
| Malchor - Lysá Hora                                   | Hike          | Czechia       | Krásná                           | 727.9    | 120.2                | 20111        |
| Total brikule 🚀                                      | Ride          | Czechia       | Staré Město                      | 572.0    | 0.0                  | 19132        |
| Cyklostezka Náchod -> Velké Poříčí                    | Ride          | Czechia       | Náchod                           | 3593.0   | 11.5                 | 18864        |
| 400 m (track num. 2)                                  | Run           | Czechia       | Benešov                          | 406.8    | 0.0                  | 18817        |
| Podle Radbuzy                                         | Ride          | Czechia       | Pilsen                           | 2315.0   | 15.8                 | 18400        |
| Trinec-Tesin                                          | Ride          | Czechia       | Třinec                           | 4677.3   | 9.4                  | 17820        |
| MH - Klaster                                          | Ride          | Czechia       | Klášter Hradiště nad Jizerou     | 1458.9   | 4.8                  | 17589        |
| Benedikt - Parkoviště                                 | Run           | Czechia       | Most                             | 1995.5   | 35.7                 | 16628        |
| stezka                                                | Run           | Czechia       | České Budějovice                 | 1000.0   | 6.4                  | 16043        |
| Židlochovice -> Olympia                               | Ride          | Czechia       | Židlochovice                     | 12812.5  | 20.4                 | 15945        |
| Do sedla Klínovce po silnici                          | Ride          | Czechia       | Loučná pod Klínovcem             | 2782.7   | 177.4                | 15827        |
| Ovál ZŠ Štefánikova                                   | Run           | Czechia       | Hradec Králové                   | 269.6    | 0.0                  | 15633        |
| Tuhnice most-Drahovice most,stezka                    | Ride          | Czechia       | Karlovy Vary                     | 2383.8   | 0.0                  | 15542        |
| Mutěnka - z Kyjova po odbočku na hraběcí              | Ride          | Czechia       | Kyjov                            | 3713.4   | 0.0                  | 15204        |
| Kynšperský ATAK                                       | Ride          | Czechia       | Kynšperk nad Ohří                | 634.2    | 0.0                  | 15182        |
| Šárka Valley (short)                                  | Run           | Czechia       | Praha 6                          | 976.5    | 0.0                  | 15181        |
| Decin - Bad Schandau Abzweig Radwg                    | Ride          | Czechia       | Děčín                            | 18518.5  | 28.0                 | 15069        |
| Track Domažlice                                       | Run           | Czechia       | Domažlice                        | 397.4    | 5.6                  | 14708        |
| 400m - Sportovní areál Na Stoupách                    | Run           | Czechia       | Jihlava                          | 394.1    | 0.0                  | 14591        |
| Štvanická lávka (do Karlína)                          | Run           | Czechia       | Prague                           | 277.5    | 6.2                  | 14503        |
| Zlaťák konec - smrt                                   | Ride          | Czechia       | Vítkovice                        | 507.3    | 42.1                 | 14461        |
| Transformator k Butorance (u studanky)                | Hike          | Czechia       | Ostravice                        | 1537.0   | 158.4                | 14098        |
| Hradní lávka => Sýkorův most                          | Run           | Czechia       | Ostrava                          | 996.4    | 22.7                 | 14042        |
| k přehradě hop                                        | Ride          | Czechia       | Krásná Lípa                      | 315.9    | 21.4                 | 13871        |
| TJ Znojmo Lap                                         | Run           | Czechia       | Znojmo                           | 404.6    | 5.1                  | 13647        |
| Park 1                                                | Run           | Czechia       | Ostrava                          | 718.9    | 0.0                  | 13600        |
| mezi mosty                                            | Run           | Czechia       | Pardubice                        | 957.4    | 6.2                  | 12916        |
| Chrudim climb                                         | Ride          | Czechia       | Chrudim                          | 866.4    | 16.6                 | 12612        |
| Špindlerovka - část II. (od Černýho potoka nahoru)    | Ride          | Czechia       | Špindlerův Mlýn                  | 4162.3   | 232.3                | 12583        |
| Hostyn-od.zastavky.po.znacku.P                        | Ride          | Czechia       | Bystřice Pod Hostýnem            | 5103.32  | 340.8                | 12560        |
| Sedmička, Lipno {                                     | Ride          | Czechia       | Přední Výtoň                     | 4110.2   | 19.9                 | 12542        |
| Černý důl konec Hoffmanky                             | Ride          | Czechia       | Černý Důl                        | 3571.2   | 180.6                | 12541        |
| Solan last km                                         | Ride          | Czechia       | Hutisko-Solanec                  | 1105.9   | 77.4567              | 12358        |
| Eurovie - nadjezd Rosice                              | Ride          | Czechia       | Pardubice II                     | 1364.7   | 2.0                  | 12048        |
| Obří hřeben - stoupák                                 | Hike          | Poland        | Karpacz                          | 453.9    | 81.8                 | 11209        |
| Nová cyklostezka do Bosche  2                         | Ride          | Czechia       | Jihlava                          | 2526.5   | 22.2                 | 11048        |
| od hráze až na konec přehrady - silnice               | Run           | Czechia       | Liberec                          | 949.6    | 40.1                 | 10846        |
| Cyklostezka Stará huť-Dobříš                          | Ride          | Czechia       | Dobříš                           | 558.5    | 11.0                 | 10768        |
| most - Loket                                          | Ride          | Czechia       | Staré Sedlo                      | 2515.6   | 2.2                  | 10610        |
| Bunč climb                                            | Ride          | Czechia       | Kostelany                        | 1876.0   | 0.0                  | 10555        |
| Okolo Bobrůvky Tři Studně - Koupaliště NMNM           | Ride          | Czechia       | Nové Město na Moravě             | 918.5    | 0.0                  | 10461        |
| Daskabát flat                                         | Ride          | Czechia       | Velký Újezd                      | 1868.0   | 4.4                  | 10016        |
| Kolem stadionu                                        | Run           | Czechia       | Hradec Kralove                   | 449.9    | 0.0                  | 9726         |
| Krkonošská                                            | Ride          | Czechia       | Vrchlabí                         | 833.5    | 0.0                  | 9571         |
| Kleť k vysílači - finále                              | Ride          | Czechia       | Kájov                            | 2495.8   | 186.0                | 9563         |
| Velodrom 1kolo                                        | Ride          | Czechia       | Louny                            | 492.1    | 8.9                  | 9533         |
| Lednice - Bulhary                                     | Ride          | Czechia       | Lednice                          | 3609.1   | 15.5                 | 9504         |
| Rovinka Beranov                                       | Ride          | Czechia       | Malý Beranov                     | 948.2    | 6.4                  | 9373         |
| Lysa hora - jizni sjezdovka                           | Run           | Czechia       | Ostravice                        | 298.4    | 63.6                 | 9361         |
| Szlak czerwony, Schronisko Nad Łomniczką - Dom Śląski | Hike          | Poland        | Karpacz                          | 2131.5   | 344.6                | 9130         |
| plný kule z kolína                                    | Ride          | Czechia       | Kolín                            | 648.1    | 0.0                  | 8614         |
| Kaufland - Popendorf                                  | Ride          | Czechia       | Jičín                            | 1923.7   | 10.2                 | 8543         |
| Plácky-soutok                                         | Ride          | Czechia       | Hradec Králové                   | 3226.9   | 13.6                 | 8324         |
| Panelovka-Tichá 800m                                  | Run           | Czechia       | Mostkovice                       | 802.8    | 0.0                  | 8242         |
| Lípy (směrem do Jičína)                               | Run           | Czechia       | Jičín                            | 1714.8   | 7.6                  | 8066         |
| 611 - Mstetice                                        | Ride          | Czechia       | Jirny                            | 1681.0   | 0.0                  | 7891         |
| Šantovka - Kojeňák                                    | Ride          | Czechia       | Olomouc                          | 1139.4   | 3.0                  | 7871         |
| Ku řopíku                                             | Run           | Czechia       | Děčín                            | 794.7    | 4.4                  | 7752         |
| Třebíč - Stařeč po cyklostezce (LS)                   | Ride          | Czechia       | Stařeč                           | 881.7    | 18.6                 | 7745         |
| Máchovo kritérium - přes bory kolem vrchu Borný       | Ride          | Czechia       | Doksy                            | 4746.0   | 27.6                 | 7606         |
| Od Sanusu ke gymplu                                   | Run           | Czechia       | Hradec Králové                   | 575.0    | 8.2                  | 7505         |
| Vlevo dole jezero Most                                | Ride          | Czechia       | Most                             | 4725.9   | 11.9054              | 7502         |
| Od letňáku ke starému vchodu ZOO                      | Run           | Czechia       | Jihlava                          | 460.0    | 2.02579              | 7468         |
| Výrovka - Modré Sedlo                                 | Ride          | Czechia       | Pec pod Sněžkou                  | 1420.0   | 160.0                | 7446         |
| 2012 Pikes Peak Hill Climb                            | Ride          | United States | Woodland Park                    | 19471.3  | 1440.4               | 7331         |
| JestedSkyrace - last uphill - middle part             | Run           | Czechia       | Liberec                          | 1005.5   | 159.0                | 7297         |
| Od křižovatky do Strání po vysílač                    | Ride          | Czechia       | Strání                           | 2393.7   | 129.0                | 7241         |
| LS - Park Boost                                       | Run           | Czechia       | Bruntál                          | 381.4    | 2.2                  | 7240         |
| Bečva - Pustevny Uphill                               | Ride          | Czechia       | Prostřední Bečva                 | 9570.7   | 525.4                | 6990         |
| #ULhalf - Strekovske Nabrezi                          | Run           | Czechia       | Ústí nad Labem-Střekov           | 1435.9   | 9.8                  | 6927         |
| Šobes - sjezd                                         | Ride          | Czechia       | Podmolí                          | 1422.0   | 2.2                  | 6886         |
| Javorový od stanice lanovky                           | Hike          | Czechia       | Třinec                           | 1265.3   | 393.2                | 6878         |
| Klobouky Viadukt                                      | Ride          | Czechia       | Valašské Klobouky                | 1089.8   | 17.6                 | 6800         |
| Dom Śląski Up Hill                                    | Hike          | Czechia       | Pec pod Sněžkou                  | 2549.5   | 435.7                | 6770         |
| Javorník finish od Pinduly                            | Run           | Czechia       | Trojanovice                      | 1059.98  | 116.111              | 6355         |
| Tatran Třemošná                                       | Run           | Czechia       | Třemošná                         | 421.5    | 7.4                  | 6324         |
| Podél dálnice                                         | Ride          | Czechia       | Nepřevázka                       | 11403.1  | 44.9728              | 6232         |
| Sprint Páteček - Santos                               | Ride          | Czechia       | Sušice                           | 1792.3   | 6.8                  | 6200         |
| Tři prameny - Pravčická brána                         | Hike          | Czechia       | Hřensko                          | 1941.0   | 175.2                | 6175         |
| do Srní                                               | Ride          | Czechia       | Srní                             | 753.4    | 43.1                 | 6096         |
| Interval                                              | Run           | Czechia       | Olomouc                          | 848.8    | 0.0                  | 5909         |
| Hoštejn-Zábřeh                                        | Ride          | null          | null                             | 7688.6   | 0.0                  | 5898         |
| Benešovský brdek                                      | Ride          | Czechia       | Benešov u Semil                  | 1087.6   | 13.2                 | 5788         |
| Kuželna - Splav 800m                                  | Run           | Czechia       | Vsetín                           | 814.3    | 3.43077              | 5676         |
| Kvilda Bučina                                         | Ride          | Czechia       | Kvilda                           | 5645.6   | 139.2                | 5605         |
| Starý Kolín - Svatá Kateřina                          | Ride          | Czechia       | Starý Kolín                      | 2289.7   | 10.0                 | 5541         |
| Nové Lesy-Dvůr Králové                                | Ride          | null          | null                             | 3238.1   | 0.0                  | 5332         |
| Kerhartice-Choceň                                     | Ride          | Czechia       | Ústí nad Orlicí                  | 15217.4  | 41.2                 | 5216         |
| Stojka na Pancíř                                      | Ride          | Czechia       | Železná Ruda                     | 382.6    | 39.3                 | 5008         |
| Ciclo Via BNL -> K                                    | Run           | Czechia       | Brandýs nad Labem-Stará Boleslav | 1025.6   | 0.0                  | 4982         |
| Bludička-Opavice                                      | Run           | Czechia       | Opava                            | 578.4    | 2.4                  | 4901         |
| Final climb ke srubu na Deštnou                       | Ride          | Czechia       | Deštné v Orlických horách        | 667.2    | 54.5                 | 4899         |
| Od lávky k lávce                                      | Run           | Czechia       | Rakovník                         | 302.1    | 0.0                  | 4879         |
| Sjezd Blatno-Březenec                                 | Ride          | Czechia       | Blatno                           | 3672.7   | 2.2                  | 4810         |
| Luby end                                              | Run           | Czechia       | Klatovy                          | 517.7    | 0.0                  | 4694         |
| Vojenský ovál 400M                                    | Run           | Czechia       | Hradec Králové                   | 410.8    | 0.0                  | 4509         |
| 400 metrů, 44 120 diváků                              | Run           | Czechia       | Brno-Královo Pole                | 427.7    | 4.1                  | 4461         |
| Luční bouda - Sněžka                                  | Hike          | Czechia       | Pec pod Sněžkou                  | 3347.1   | 231.8                | 4451         |
| Pustevny - Radhošť                                    | Hike          | Czechia       | Trojanovice                      | 3632.9   | 166.0                | 4411         |
| stupani k vetr. mlynu Kuzelov                         | Ride          | Czechia       | Javorník                         | 1865.9   | 32.2                 | 4403         |
| hurá na Říp                                           | Ride          | null          | null                             | 617.5    | 0.0                  | 4245         |
| Červená voda - Suchý vrch                             | Ride          | Czechia       | Červená Voda                     | 6543.5   | 261.2                | 4104         |
| Dlouhá míle                                           | Run           | Czechia       | Sušice                           | 1515.0   | 4.0                  | 4033         |
| Pod Homoli Climb                                      | Ride          | Czechia       | Liberk                           | 1547.8   | 89.7                 | 3982         |
| Šup do parku                                          | Run           | Czechia       | Plzeň 1                          | 424.9    | 0.0                  | 3939         |
| Tuhnická lávka -Chebský most                          | Run           | Czechia       | Karlovy Vary                     | 1058.3   | 6.8                  | 3931         |
| Nábřeží                                               | Run           | Czechia       | Kadaň                            | 1319.6   | 21.4                 | 3882         |
| Dářská rašeliniště                                    | Ride          | Czechia       | Radostín                         | 3293.8   | 16.0                 | 3864         |
| panelka k bráně ˇerchova                              | Ride          | Czechia       | Pec                              | 530.6    | 60.4                 | 3862         |
| Kozí hřbety - Luční bouda                             | Hike          | Czechia       | Špindlerův Mlýn                  | 1993.7   | 16.8                 | 3837         |
| Hradiště - čtyřstovka                                 | Run           | Czechia       | Uherské Hradiště                 | 437.7    | 0.0                  | 3792         |
| Pisek podel reky I                                    | Run           | null          | null                             | 708.4    | 7.6                  | 3740         |
| Opavice od zatáčky                                    | Run           | Czechia       | Krnov                            | 672.8    | 0.0                  | 3673         |
| U Jordánu do kopce                                    | Run           | Czechia       | Tábor                            | 984.6    | 20.3                 | 3607         |
| Ruda -> Gerlovka                                      | Ride          | Czechia       | Železná Ruda                     | 3222.9   | 144.0                | 3598         |
| Pec - Sněžka (přes Obřák)                             | Hike          | Czechia       | Pec pod Sněžkou                  | 6374.3   | 870.3                | 3521         |
| Kopeček - od kruháče k bazilice                       | Run           | Czechia       | Samotišky                        | 776.1    | 109.8                | 3360         |
| Debř-Michalovice ☠                                    | Run           | Czechia       | Hrdlořezy                        | 1122.2   | 12.0                 | 3179         |
| Kopec pod Barborou                                    | Ride          | Czechia       | Kutna Hora                       | 838.6    | 41.6                 | 3032         |
| segment z Tábora                                      | Ride          | Czechia       | Tábor                            | 819.3    | 43.0                 | 2996         |
| Gránické údolí - Central Part DOWN                    | Run           | Czechia       | Znojmo                           | 1026.2   | 0.0                  | 2730         |
| Segment                                               | Run           | Czechia       | Ctiněves                         | 565.1    | 131.4                | 2682         |
| Richtrovy boudy - Výrovka                             | Hike          | Czechia       | Pec pod Sněžkou                  | 1350.1   | 194.4                | 2681         |
| Kleť                                                  | Hike          | Czechia       | Holubov                          | 1899.1   | 362.1                | 2653         |
| Železniční most => Jez Vítkovice                      | Run           | Czechia       | Ostrava                          | 2136.6   | 34.5                 | 2612         |
| Le Grande Classico                                    | Ride          | Czechia       | Spálov                           | 1790.4   | 23.3                 | 2557         |
| Snezka po schodech                                    | Run           | null          | null                             | 743.4    | 173.0                | 2502         |
| Rovinka od kruháče k bazénu                           | Run           | Czechia       | Klatovy                          | 732.4    | 0.0                  | 2437         |
| Jesenice-Blatno DH                                    | Ride          | Czechia       | Jesenice                         | 3956.5   | 2.4                  | 2353         |
| Špindlerův Mlýn - Školní                              | Hike          | Czechia       | Špindlerův Mlýn                  | 385.2    | 78.2                 | 2303         |
| Giro di Tyrš                                          | Run           | Czechia       | Aš                               | 369.4    | 5.1                  | 1990         |
| Labe_po asfaltu                                       | Run           | Czechia       | Kolín                            | 1243.6   | 0.0                  | 1942         |
| Ondřejník sedlo - Ondřejník vrchol                    | Run           | Czechia       | Lhotka                           | 1082.0   | 123.2                | 1922         |
| Tygří výzva, sklon 32% :)                             | Run           | Czechia       | Liberec - Horní Hanychov         | 871.7    | 279.0                | 1822         |
| Červená podél Zlaté stoky do Třeboně                  | Ride          | Czechia       | Třeboň                           | 1580.8   | 0.0                  | 1745         |
| Nová cyklopěšina z Peřiny do HTčka                    | Ride          | Czechia       | Horšovský Týn                    | 1817.8   | 11.2                 | 1622         |
| Od bývalé sáňkařské dráhy po modré na Ještěd          | Hike          | Czechia       | Liberec                          | 2046.4   | 341.2                | 1568         |
| Koupaliště sprint                                     | Run           | Czechia       | Vlašim                           | 348.2    | 0.0                  | 1555         |
| Mezi zábranama (proti proudu)                         | Run           | Czechia       | Jaroměř                          | 1067.3   | 3.5                  | 1514         |
| rovinka kolem Sázavy:Plynovod-křižovatka u Mostu      | Run           | Czechia       | Čtyřkoly                         | 800.7    | 0.0                  | 1447         |
| Ježánky(Visalaje) - Bílý Kříž (směr Visalaje)         | Hike          | Czechia       | Morávka                          | 1810.9   | 120.8                | 1413         |
| Zrucskej smrtak                                       | Ride          | Czechia       | Zruč nad Sázavou                 | 732.4    | 74.7                 | 1334         |
| podle Labe do Týnce                                   | Ride          | Czechia       | Kojice                           | 1697.1   | 16.0                 | 1326         |
| Z Doubravky k Josefu                                  | Run           | Czechia       | Hořice                           | 796.5    | 44.2                 | 1319         |
| Okruhy Ochozou - Výběh na Harusák (0,76 km / 105 m)   | Run           | Czechia       | Nové Město na Moravě             | 734.3    | 92.9                 | 1265         |
| Most - Most -> Břeclav                                | Run           | Czechia       | Břeclav                          | 807.1    | 0.0                  | 1233         |
| Hlavní třídou nahoru                                  | Run           | Czechia       | Havířov                          | 928.7    | 9.8175               | 1230         |
| Stadion - 400 m                                       | Run           | Czechia       | Dačice                           | 429.6    | 2.4                  | 1193         |
| Rybnik                                                | Run           | Czechia       | Kroměříž                         | 439.1    | 0.0                  | 1184         |
| Pláně - Černý vrch                                    | Hike          | Czechia       | Světlá pod Ještědem              | 1207.9   | 135.4                | 1182         |
| Opavska down 1/2                                      | Run           | Czechia       | Ostrava                          | 1456.7   | 0.0                  | 1166         |
| Ořešník                                               | Hike          | Czechia       | Hejnice                          | 2324.7   | 375.7                | 1108         |
| Karlov - k Velkému kotli                              | Hike          | Czechia       | Malá Morávka                     | 4217.1   | 337.4                | 1055         |
| Luisino údolí - Velká Deštná                          | Hike          | Czechia       | Deštné v Orlických horách        | 1921.9   | 227.799              | 1050         |
| Berounka sprint                                       | Run           | Czechia       | Beroun                           | 327.1    | 6.4                  | 1026         |
| Po červené na Předěl                                  | Hike          | Czechia       | Prášily                          | 2460.8   | 216.1                | 995          |
| Svaty kopecek up                                      | Hike          | Czechia       | Mikulov                          | 707.3    | 100.378              | 975          |
| Brno Circuit                                          | Run           | null          | null                             | 5252.02  | 95.705               | 892          |
| Pod Vilemínkou - Kralický Sněžník (žlutá)             | Hike          | Poland        | null                             | 4939.8   | 595.0                | 844          |
| Výpřež - Ještěd (po červené)                          | Hike          | Czechia       | okres Liberec                    | 1529.8   | 223.0                | 841          |
| kopec na hrad                                         | Hike          | Czechia       | null                             | 673.7    | 105.169              | 819          |
| BL Boletice - rovinka na hřebeni                      | Run           | Czechia       | Horní Planá                      | 982.8    | 2.9                  | 813          |
| Neklid -> Klínovec                                    | Hike          | Czechia       | Jáchymov                         | 2199.9   | 127.2                | 800          |
| Pod rozhlednu Babi lom                                | Hike          | Czechia       | Lelekovice                       | 891.5    | 170.2                | 780          |
| Videlské sedlo-Švýcárna                               | Hike          | Czechia       | Vrbno pod Pradědem               | 2784.8   | 421.716              | 675          |
| Modrava - Tříjezerní slať                             | Hike          | Czechia       | Modrava                          | 2654.1   | 88.8                 | 644          |
| VR #11 finish                                         | Run           | Czechia       | Vyšší Brod                       | 962.4    | 3.0                  | 643          |
| Hadí stezka (Svatobor)                                | Run           | Czechia       | Sušice                           | 1001.1   | 148.4                | 624          |
| Borůvková hora part II                                | Hike          | Czechia       | Javorník                         | 1772.3   | 170.4                | 591          |
| Ostaš                                                 | Hike          | Czechia       | Žďár nad Metují                  | 2150.3   | 107.158              | 567          |
| Ručičky - Krakonošova snídaně (po žluté)              | Hike          | Czechia       | Harrachov                        | 2791.8   | 207.8                | 562          |
| Čerťák - Ručičky (po modré)                           | Hike          | Czechia       | Rokytnice nad Jizerou            | 4614.7   | 79.8                 | 531          |
| Říp po žluté na vyhlídku                              | Hike          | Czechia       | Mnetěš                           | 371.0    | 78.0                 | 518          |
| 15% Stoupák Bártlovka->Paličník                       | Hike          | Czechia       | Bílý Potok                       | 2642.3   | 0.0                  | 506          |
| Posázavskou k odbočce před schody                     | Hike          | Czechia       | Hradištko                        | 2310.8   | 17.5533              | 471          |
| Pavlov - Dívčí hrad climb                             | Run           | Czechia       | Pavlov                           | 903.9    | 0.0                  | 423          |
| podél Podměstského rybníku                            | Run           | Czechia       | Čáslav                           | 612.5    | 0.0                  | 418          |
| Kočičí žleb - Ríšova studánka                         | Hike          | Czechia       | Brno                             | 1771.6   | 100.0                | 402          |
| Dneboh - Drábské Světničky                            | Hike          | Czechia       | Mnichovo Hradiště                | 486.3    | 76.896               | 376          |
| Zig-zag na Šerák                                      | Hike          | Czechia       | Lipová-lázně                     | 2777.7   | 320.3                | 371          |
| Kraličák Skyrace - 2. kopec                           | Run           | Czechia       | Staré Město                      | 1571.0   | 201.8                | 359          |
| Podél tratě do Úval                                   | Run           | Czechia       | Praha-Klánovice                  | 2663.3   | 8.0                  | 322          |
| Soláň-Tanečnica                                       | Hike          | Czechia       | Hutisko-Solanec                  | 4425.3   | 199.2                | 314          |
| Hilo to Mauna Kea                                     | Ride          | United States | Hilo                             | 68605.4  | 4284.12              | 309          |
| Dlouhe Strane od Loucnej                              | Ride          | Czechia       | Loučná nad Desnou                | 12619.0  | 891.8                | 308          |
| Valy                                                  | Run           | Czechia       | Litomyšl                         | 561.3    | 0.0                  | 283          |
| Tříjezerní slať - Rokyta                              | Hike          | Czechia       | Modrava                          | 3326.0   | 2.6                  | 253          |
| Hadí stezka na Svatobor 🐍                            | Hike          | Czechia       | Hrádek                           | 1020.9   | 167.4                | 232          |
| Sněžník od Děčína (po červené)                        | Hike          | Czechia       | Děčín                            | 2915.9   | 316.0                | 224          |
| Hrad Vevěří - Hráz                                    | Hike          | Czechia       | Brno                             | 7882.0   | 125.2                | 209          |
| Šumbera pom. odb. - vysílač Hády                      | Hike          | Czechia       | Kanice                           | 1107.6   | 11.0                 | 186          |
| Stoupání na Templštejn                                | Hike          | Czechia       | Jamolice                         | 598.3    | 111.2                | 92           |
| Lacinův kámen - Velká Skála                           | Hike          | Czechia       | Tišnov                           | 1900.0   | 181.0                | 91           |
| Harusák Climb                                         | Hike          | Czechia       | Nové Město na Moravě             | 683.6    | 107.2                | 71           |