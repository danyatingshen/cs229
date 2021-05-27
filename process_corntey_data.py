import util

cortney = {'(-1, -1, -1, -1)': [3.0354878902435303, 3.483689069747925, 2.453861713409424, 3.587308883666992],
 '(1, 1, 0, 0)': [2.2308409214019775, 2.2273731231689453, 1.4109151363372803, 2.9833202362060547],
 '(1, 1, 1, 0)': [4.1962339878082275, 2.9367380142211914, 2.009829044342041, 1.7939326763153076],
 '(1, 2, 0, 1)': [2.6941680908203125, 2.984971046447754, 2.8374037742614746, 2.8949038982391357],
 '(1, 2, 0, 0)': [2.329698085784912, 2.9931557178497314, 2.6555051803588867, 2.795552968978882],
 '(1, 2, 1, 0)': [4.675911903381348, 5.165306806564331, 4.936269998550415, 6.4709789752960205],
 '(1, 2, 2, 0)': [6.337523937225342, 4.219459056854248, 4.4139018058776855, 2.645124673843384],
 '(1, 3, 0, 2)': [3.890583038330078, 8.850495100021362, 3.449050188064575, 4.258002042770386],
 '(1, 3, 0, 1)': [3.169175148010254, 3.4025020599365234, 3.2324841022491455, 5.192010164260864],
 '(1, 3, 1, 1)': [4.208554029464722, 7.034392833709717, 3.339097738265991, 4.44398307800293],
 '(1, 3, 0, 0)': [8.725482940673828, 8.527411937713623, 4.482321739196777, 6.011060953140259],
 '(1, 3, 1, 0)': [6.149594068527222, 7.092045068740845, 4.8091819286346436, 5.372888088226318],
 '(1, 3, 2, 0)': [5.832963943481445, 6.82602596282959, 5.588354110717773, 4.436540842056274],
 '(1, 3, 2, 1)': [7.730515956878662, 2.8985819816589355, 2.3362841606140137, 4.040219783782959],
 '(1, 3, 3, 0)': [10.18107795715332, 10.165369987487793, 5.586869955062866, 2.999894142150879],
 '(2, 2, 0, 2)': [3.332476854324341, 4.0104498863220215, 3.489657163619995, 2.68103289604187],
 '(2, 2, 0, 1)': [3.780524969100952, 3.1689488887786865, 5.082064867019653, -2.084205150604248],
 '(2, 2, 1, 2)': [9.80224084854126, 9.461832284927368, 1.856194019317627, 2.159090042114258],
 '(2, 2, 1, 1)': [8.022507667541504, 4.185059070587158, 6.110944986343384, 6.873898983001709],
 '(2, 3, 0, 3)': [6.12713098526001, 2.651259183883667, 2.948064088821411, 4.381863832473755],
 '(2, 3, 0, 2)': [4.1964099407196045, 4.158540725708008, 2.5149998664855957, 5.146528959274292],
 '(2, 3, 0, 1)': [5.05587363243103, 6.451432943344116, 5.121021032333374, 5.781242847442627],
 '(2, 3, 1, 2)': [7.73237419128418, 6.7680580615997314, 9.452672004699707, 7.745106220245361],
 '(2, 3, 1, 1)': [7.330647945404053, 9.24365496635437, 5.6819682121276855, 5.796483993530273],
 '(2, 3, 2, 2)': [4.664674758911133, 6.7395031452178955, 3.128732204437256, 17.62172818183899],
 '(2, 3, 2, 1)': [9.63266110420227, 8.668097019195557, 8.115847826004028, 10.258949041366577],
 '(2, 2, 0, 0)': [8.528687000274658, 4.8330748081207275, 3.973886251449585, 3.6159818172454834],
 '(2, 2, 1, 0)': [8.365319013595581, 11.276368141174316, 5.852644920349121, 6.514219045639038],
 '(2, 2, 2, 0)': [18.45078682899475, -5.438171148300171, 7.53454327583313, 7.007725238800049],
 '(2, 3, 0, 0)': [-8.06286907196045, 8.597994089126587, 7.9736058712005615, 7.2471091747283936],
 '(2, 3, 1, 0)': [6.494438171386719, 7.438755989074707, 13.287014961242676, 9.45159387588501],
 '(2, 3, 2, 0)': [-11.161668062210083, 12.32227110862732, 8.13605809211731, 8.57193899154663],
 '(2, 3, 3, 0)': [10.249733209609985, 18.577992916107178, 26.11427593231201, 38.11210012435913],
 '(2, 3, 3, 1)': [6.799944877624512, 7.70749306678772, -11.174548864364624, 12.350812196731567],
 '(3, 3, 0, 4)': [4.3887012004852295, 2.860703945159912, 3.387770891189575, 2.374492883682251],
 '(3, 3, 0, 3)': [4.734586238861084, 3.1620380878448486, 5.160755395889282, 3.74056077003479],
 '(3, 3, 0, 2)': [5.1716742515563965, 5.325182914733887, 5.215519189834595, 6.9817728996276855],
 '(3, 3, 1, 4)': [3.01824688911438, 3.497915029525757, 4.977770805358887, 5.514249801635742],
 '(3, 3, 1, 3)': [-9.836711168289185, 13.442764043807983, 5.3224639892578125, 5.5700578689575195],
 '(3, 3, 1, 2)': [13.364296913146973, 6.571739912033081, 5.274071216583252, 5.93155312538147],
 '(3, 3, 0, 1)': [6.530955076217651, 7.6157801151275635, 5.427872896194458, 7.1048760414123535],
 '(3, 3, 1, 1)': [6.034627676010132, 10.270012140274048, 26.320838928222656, 11.12374997138977],
 '(3, 3, 2, 1)': [-14.403362035751343, 12.120222091674805, -33.29480981826782, 7.851277828216553],
 '(3, 3, 2, 2)': [15.24042010307312, 7.87050199508667, 10.503306865692139, -8.283658027648926],
 '(3, 3, 3, 1)': [12.17379903793335, 11.45517373085022, 6.981773853302002, 5.721510887145996],
 '(3, 3, 0, 0)': [11.017449140548706, 14.786878108978271, 15.445005178451538, 11.902357816696167],
 '(3, 3, 1, 0)': [13.425750017166138, 12.190569877624512, 8.464478969573975, 7.400122880935669],
 '(3, 3, 2, 0)': [17.146647930145264, 13.329339265823364, 16.55802583694458, 13.863050937652588],
 '(3, 3, 3, 0)': [-18.54138708114624, -25.93468976020813, -8.661436796188354, 18.845400094985962]}

util.save_q('data_cortney.txt', cortney)