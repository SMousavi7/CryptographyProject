import numpy as np 
Sbox1 = [
['112', '130', '44', '236', '179', '39', '192', '229'],
['228', '133', '87', '53', '234', '12', '174', '65'],
['35', '239', '107', '147', '69', '25', '165', '33'],
['237', '14', '79', '78', '29', '101', '146', '189'],
['134', '184', '175', '143', '124', '235', '31', '206'],
['62', '48', '220', '95', '94', '197', '11', '26'],
['166', '225', '57', '202', '213', '71', '93', '61'],
['217', '1', '90', '214', '81', '86', '108', '77'],
['139', '154', '102', '251', '204', '176', '45', '116'],
['18', '43', '32', '24', '177', '132', '35', '43'],
['223', '76', '203', '194', '52', '126', '118', '5'],
['109', '183', '169', '49', '209', '23', '4', '215'],
['20', '88', '58', '97', '222', '27', '17', '28'],
['50', '15', '156', '22', '83', '24', '242', '34'],
['254', '68', '207', '178', '195', '181', '122', '145'],
['36', '8', '232', '168', '96', '252', '105', '80'],
['170', '208', '160', '125', '161', '137', '98', '151'],
['84', '91', '30', '149', '224', '255', '100', '80'],
['16', '196', '0', '72', '163', '247', '117', '219'],
['138', '3', '230', '218', '9', '63', '221', '148'],
['135', '92', '131', '2', '205', '74', '144', '51'],
['115', '103', '246', '243', '157', '127', '191', '226'],
['82', '155', '216', '38', '200', '55', '198', '59'],
['129', '150', '111', '75', '19', '190', '99', '46'],
['233', '121', '167', '140', '159', '110', '188', '142'],
['4', '141', '245', '249', '182', '47', '188', '233'],
['120', '152', '6', '106', '231', '70', '113', '186'],
['212', '37', '171', '66', '136', '162', '141', '250'],
['114', '7', '185', '85', '248', '238', '172', '10'],
['54', '73', '4', '104', '60', '56', '24', '1'],
['64', '40', '211', '123', '187', '201', '67', '193'],
['21', '227', '173', '244', '119', '199', '128', '158']
]

Sbox2 = [
['224', '5', '88', '217', '103', '78', '129', '203'],   
['201', '11', '174', '106', '213', '24', '93', '130'],  
['70', '223', '214', '39', '138', '50', '75', '66'],  
['219', '28', '158', '156', '58', '202', '37', '123'],  
['13', '113', '95', '31', '248', '215', '62', '157'],  
['124', '96', '185', '190', '188', '139', '22', '52'],  
['77', '195', '114', '149', '171', '142', '186', '122'],
['179', '2', '180', '173', '162', '172', '216', '154'], 
['23', '53', '204', '247', '153', '97', '90', '232'],  
['36', '86', '64', '48', '99', '9', '70', '86'],        
['191', '152', '151', '133', '104', '252', '236', '10'],
['218', '111', '83', '98', '163', '46', '8', '175'],    
['40', '176', '116', '194', '189', '54', '34', '56'],  
['100', '30', '57', '44', '166', '48', '229', '68'],    
['253', '136', '159', '101', '135', '107', '244', '35'],
['72', '16', '209', '81', '192', '249', '210', '160'],
['85', '161', '65', '250', '67', '19', '196', '47'],
['168', '182', '60', '43', '193', '255', '200', '160'],
['32', '137', '0', '144', '71', '239', '234', '183'],
['21', '6', '205', '181', '18', '126', '187', '41'],
['15', '184', '7', '4', '155', '148', '33', '102'],
['230', '206', '237', '231', '59', '254', '127', '197'],
['164', '55', '177', '76', '145', '110', '141', '118'],
['3', '45', '222', '150', '38', '125', '198', '92'],
['211', '242', '79', '25', '63', '220', '121', '29'],
['8', '27', '235', '243', '109', '94', '121', '211'],
['240', '49', '12', '212', '207', '140', '226', '117'],
['169', '74', '87', '132', '17', '69', '27', '245'],
['228', '14', '115', '170', '241', '221', '89', '20'],
['108', '146', '8', '208', '120', '112', '48', '2'],
['128', '80', '167', '246', '119', '147', '134', '131'],
['42', '199', '91', '233', '238', '143', '1', '61']
]

Sbox3 = [
['56', '65', '22', '118', '217', '147', '96', '242'],
['114', '194', '171', '154', '117', '6', '87', '160'],
['145', '247', '181', '201', '162', '140', '210', '144'],
['246', '7', '167', '39', '142', '178', '73', '222'],
['67', '92', '215', '199', '62', '245', '143', '103'],
['31', '24', '110', '175', '47', '226', '133', '13'],
['83', '240', '156', '101', '234', '163', '174', '158'],
['236', '128', '45', '107', '168', '43', '54', '166'],
['197', '77', '51', '253', '102', '88', '150', '58'],
['9', '149', '16', '12', '216', '66', '145', '149'],
['239', '38', '229', '97', '26', '63', '59', '130'],
['182', '219', '212', '152', '232', '139', '2', '235'],
['10', '44', '29', '176', '111', '141', '136', '14'],
['25', '135', '78', '11', '169', '12', '121', '17'],
['127', '34', '231', '89', '225', '218', '61', '200'],
['18', '4', '116', '84', '48', '126', '180', '40'],
['85', '104', '80', '190', '208', '196', '49', '203'],
['42', '173', '15', '202', '112', '255', '50', '40'],
['8', '98', '0', '36', '209', '251', '186', '237'],
['69', '129', '115', '109', '132', '159', '238', '74'],
['195', '46', '193', '1', '230', '37', '72', '153'],
['185', '179', '123', '249', '206', '191', '223', '113'],
['41', '205', '108', '19', '100', '155', '99', '157'],
['192', '75', '183', '165', '137', '95', '177', '23'],
['244', '188', '211', '70', '207', '55', '94', '71'],
['2', '198', '250', '252', '91', '151', '94', '244'],
['60', '76', '3', '53', '243', '35', '184', '93'],
['106', '146', '213', '33', '68', '81', '198', '125'],
['57', '131', '220', '170', '124', '119', '86', '5'],
['27', '164', '2', '52', '30', '28', '12', '128'],
['32', '20', '233', '189', '221', '228', '161', '224'],
['138', '241', '214', '122', '187', '227', '64', '79']
]

Sbox4 = [
['112', '44', '179', '192', '228', '87', '234', '174'],
['35', '107', '69', '165', '237', '79', '29', '146'],
['134', '175', '124', '31', '62', '220', '94', '11'],
['166', '57', '213', '93', '217', '90', '81', '108'],
['139', '102', '204', '45', '18', '32', '177', '35'],
['223', '203', '52', '118', '109', '169', '209', '4'],
['20', '58', '222', '17', '50', '156', '83', '242'],
['254', '207', '195', '122', '36', '232', '96', '105'],
['170', '160', '161', '98', '84', '30', '224', '100'],
['16', '0', '163', '117', '138', '230', '9', '221'],
['135', '131', '205', '144', '115', '246', '157', '191'],
['82', '216', '200', '198', '129', '111', '19', '99'],
['233', '167', '159', '188', '4', '245', '182', '188'],
['120', '6', '231', '113', '212', '171', '136', '141'],
['114', '185', '248', '172', '54', '4', '60', '24'],
['64', '211', '187', '67', '21', '173', '119', '128'],
['112', '44', '179', '192', '228', '87', '234', '174'],
['35', '107', '69', '165', '237', '79', '29', '146'],
['134', '175', '124', '31', '62', '220', '94', '11'],
['166', '57', '213', '93', '217', '90', '81', '108'],
['139', '102', '204', '45', '18', '32', '177', '35'],
['223', '203', '52', '118', '109', '169', '209', '4'],
['20', '58', '222', '17', '50', '156', '83', '242'],
['254', '207', '195', '122', '36', '232', '96', '105'],
['170', '160', '161', '98', '84', '30', '224', '100'],
['16', '0', '163', '117', '138', '230', '9', '221'],
['135', '131', '205', '144', '115', '246', '157', '191'],
['82', '216', '200', '198', '129', '111', '19', '99'],
['233', '167', '159', '188', '4', '245', '182', '188'],
['120', '6', '231', '113', '212', '171', '136', '141'],
['114', '185', '248', '172', '54', '4', '60', '24'],
['64', '211', '187', '67', '21', '173', '119', '128']
]

Sbox5 = [
['30fb40d4','9fa0ff0b','6beccd2f','3f258c7a','1e213f2f','9c004dd3','6003e540','cf9fc949'],
['bfd4af27','88bbbdb5','e2034090','98d09675','6e63a0e0','15c361d2','c2e7661d','22d4ff8e'],
['28683b6f','c07fd059','ff2379c8','775f50e2','43c340d3','df2f8656','887ca41a','a2d2bd2d'],
['a1c9e0d6','346c4819','61b76d87','22540f2f','2abe32e1','aa54166b','22568e3a','a2d341d0'],
['66db40c8','a784392f','004dff2f','2db9d2de','97943fac','4a97c1d8','527644b7','b5f437a7'],
['b82cbaef','d751d159','6ff7f0ed','5a097a1f','827b68d0','90ecf52e','22b0c054','bc8e5935'],
['4b6d2f7f','50bb64a2','d2664910','bee5812d','b7332290','e93b159f','b48ee411','4bff345d'],
['fd45c240','ad31973f','c4f6d02e','55fc8165','d5b1caad','a1ac2dae','a2d4b76d','c19b0c50'],
['882240f2','0c6e4f38','a4e4bfd7','4f5ba272','564c1d2f','c59c5319','b949e354','b04669fe'],
['b1b6ab8a','c71358dd','6385c545','110f935d','57538ad5','6a390493','e63d37e0','2a54f6b3'],
['3a787d5f','6276a0b5','19a6fcdf','7a42206a','29f9d4d5','f61b1891','bb72275e','aa508167'],
['38901091','c6b505eb','84c7cb8c','2ad75a0f','874a1427','a2d1936b','2ad286af','aa56d291'],
['d7894360','425c750d','93b39e26','187184c9','6c00b32d','73e2bb14','a0bebc3c','54623779'],
['64459eab','3f328b82','7718cf82','59a2cea6','04ee002e','89fe78e6','3fab0950','325ff6c2'],
['81383f05','6963c5c8','76cb5ad6','d49974c9','ca180dcf','380782d5','c7fa5cf6','8ac31511'],
['35e79e13','47da91d0','f40f9086','a7e2419e','31366241','051ef495','aa573b04','4a805d8d'],
['548300d0','00322a3c','bf64cddf','ba57a68e','75c6372b','50afd341','a7c13275','915a0bf5'],
['6b54bfab','2b0b1426','ab4cc9d7','449ccd82','f7fbf265','ab85c5f3','1b55db94','aad4e324'],
['cfa4bd3f','2deaa3e2','9e204d02','c8bd25ac','eadf55b3','d5bd9e98','e31231b2','2ad5ad6c'],
['954329de','adbe4528','d8710f69','aa51c90f','aa786bf6','22513f1e','aa51a79b','2ad344cc'],
['7b5a41f0','d37cfbad','1b069505','41ece491','b4c332e6','032268d4','c9600acc','ce387e6d'],
['bf6bb16c','6a70fb78','0d03d9c9','d4df39de','e01063da','4736f464','5ad328d8','b347cc96'],
['75bb0fc3','98511bfb','4ffbcc35','b58bcf6a','e11f0abc','bfc5fe4a','a70aec10','ac39570a'],
['3f04442f','6188b153','e0397a2e','5727cb79','9ceb418f','1cacd68d','2ad37c96','0175cb9d'],
['c69dff09','c75b65f0','d9db40d8','ec0e7779','4744ead4','b11c3274','dd24cb9e','7e1c54bd'],
['f01144f9','d2240eb1','9675b3fd','a3ac3755','d47c27af','51c85f4d','56907596','a5bb15e6'],
['580304f0','ca042cf1','011a37ea','8dbfaadb','35ba3e4a','3526ffa0','c37b4d09','bc306ed9'],
['98a52666','5648f725','ff5e569d','0ced63d0','7c63b2cf','700b45e1','d5ea50f1','85a92872'],
['af1fbda7','d4234870','a7870bf3','2d3b4d79','42e04198','0cd0ede7','26470db8','f881814c'],
['474d6ad7','7c0c5e5c','d1231959','381b7298','f5d2f4db','ab838653','6e2f1e23','83719c9e'],
['bd91e046','9a56456e','dc39200c','20c8c571','962bda1c','e1e696ff','b141ab08','7cca89b9'],
['1a69e783','02cc4843','a2f7c579','429ef47d','427b169c','5ac9f049','dd8f0f00','5c8165bf'],
]

Sbox6 = [
['1f201094','ef0ba75b','69e3cf7e','393f4380','fe61cf7a','eec5207a','55889c94','72fc0651'],
['ada7ef79','4e1d7235','d55a63ce','de0436ba','99c430ef','5f0c0794','18dcdb7d','a1d6eff3'],
['a0b52f7b','59e83605','ee15b094','e9ffd909','dc440086','ef944459','ba83ccb3','e0c3cdfb'],
['d1da4181','3b092ab1','f997f1c1','a5e6cf7b','01420ddb','e4e7ef5b','25a1ff41','e180f806'],
['1fc41080','179bee7a','d37ac6a9','fe5830a4','98de8b7f','77e83f4e','79929269','24fa9f7b'],
['e113c85b','acc40083','d7503525','f7ea615f','62143154','0d554b63','5d681121','c866c359'],
['3d63cf73','cee234c0','d4d87e87','5c672b21','071f6181','39f7627f','361e3084','e4eb573b'],
['602f64a4','d63acd9c','1bbc4635','9e81032d','2701f50c','99847ab4','a0e3df79','ba6cf38c'],
['10843094','2537a95e','f46f6ffe','a1ff3b1f','208cfb6a','8f458c74','d9e0a227','4ec73a34'],
['fc884f69','3e4de8df','ef0e0088','3559648d','8a45388c','1d804366','721d9bfd','a58684bb'],
['e8256333','844e8212','128d8098','fed33fb4','ce280ae1','27e19ba5','d5a6c252','e49754bd'],
['c5d655dd','eb667064','77840b4d','a1b6a801','84db26a9','e0b56714','21f043b7','e5d05860'],
['54f03084','066ff472','a31aa153','dadc4755','b5625dbf','68561be6','83ca6b94','2d6ed23b'],
['eccf01db','a6d3d0ba','b6803d5c','af77a709','33b4a34c','397bc8d6','5ee22b95','5f0e5304'],
['81ed6f61','20e74364','b45e1378','de18639b','881ca122','b96726d1','8049a7e8','22b7da7b'],
['5e552d25','5272d237','79d2951c','c60d894c','488cb402','1ba4fe5b','a4b09f6b','1ca815cf'],
['a20c3005','8871df63','b9de2fcb','0cc6c9e9','0beeff53','e3214517','b4542835','9f63293c'],
['ee41e729','6e1d2d7c','50045286','1e6685f3','f33401c6','30a22c95','31a70850','60930f13'],
['73f98417','a1269859','ec645c44','52c877a9','cdff33a6','a02b1741','7cbad9a2','2180036f'],
['50d99c08','cb3f4861','c26bd765','64a3f6ab','80342676','25a75e7b','e4e6d1fc','20c710e6'],
['cdf0b680','17844d3b','31eef84d','7e0824e4','2ccb49eb','846a3bae','8ff77888','ee5d60f6'],
['7af75673','2fdd5cdb','a11631c1','30f66f43','b3faec54','157fd7fa','ef8579cc','d152de58'],
['db2ffd5e','8f32ce19','306af97a','02f03ef8','99319ad5','c242fa0f','a7e3ebb0','c68e4906'],
['b8da230c','80823028','dcdef3c8','d35fb171','088a1bc8','bec0c560','61a3c9e8','bca8f54d'],
['c72feffa','22822e99','82c570b4','d8d94e89','8b1c34bc','301e16e6','273be979','b0ffeaa6'],
['61d9b8c6','00b24869','b7ffce3f','08dc283b','43daf65a','f7e19798','7619b72f','8f1c9ba4'],
['dc8637a0','16a7d3b1','9fc393b7','a7136eeb','c6bcc63e','1a513742','ef6828bc','520365d6'],
['2d6a77ab','3527ed4b','821fd216','095c6e2e','db92f2fb','5eea29cb','145892f5','91584f7f'],
['5483697b','2667a8cc','85196048','8c4bacea','833860d4','0d23e0f9','6c387e8a','0ae6d249'],
['b284600c','d835731d','dcb1c647','ac4c56ea','3ebd81b3','230eabb0','6438bc87','f0b5b1fa'],
['8f5ea2b3','fc184642','0a036b7a','4fb089bd','649da589','a345415e','5c038323','3e5d3bb9'],
['43d79572','7e6dd07c','06dfdf1e','6c6cc4ef','7160a539','73bfbe70','83877605','4523ecf1'],
]

Sbox7 = [
['8defc240','25fa5d9f','eb903dbf','e810c907','47607fff','369fe44b','8c1fc644','aececa90'],
['beb1f9bf','eefbcaea','e8cf1950','51df07ae','920e8806','f0ad0548','e13c8d83','927010d5'],
['11107d9f','07647db9','b2e3e4d4','3d4f285e','b9afa820','fade82e0','a067268b','8272792e'],
['553fb2c0','489ae22b','d4ef9794','125e3fbc','21fffcee','825b1bfd','9255c5ed','1257a240'],
['4e1a8302','bae07fff','528246e7','8e57140e','3373f7bf','8c9f8188','a6fc4ee8','c982b5a5'],
['a8c01db7','579fc264','67094f31','f2bd3f5f','40fff7c1','1fb78dfc','8e6bd2c1','437be59b'],
['99b03dbf','b5dbc64b','638dc0e6','55819d99','a197c81c','4a012d6e','c5884a28','ccc36f71'],
['b843c213','6c0743f1','8309893c','0feddd5f','2f7fe850','d7c07f7e','02507fbf','5afb9a04'],
['a747d2d0','1651192e','af70bf3e','58c31380','5f98302e','727cc3c4','0a0fb402','0f7fef82'],
['8c96fdad','5d2c2aae','8ee99a49','50da88b8','8427f4a0','1eac5790','796fb449','8252dc15'],
['efbd7d9b','a672597d','ada840d8','45f54504','fa5d7403','e83ec305','4f91751a','925669c2'],
['23efe941','a903f12e','60270df2','0276e4b6','94fd6574','927985b2','8276dbcb','02778176'],
['f8af918d','4e48f79e','8f616ddf','e29d840e','842f7d83','340ce5c8','96bbb682','93b4b148'],
['ef303cab','984faf28','779faf9b','92dc560d','224d1e20','8437aa88','7d29dc96','2756d3dc'],
['8b907cee','b51fd240','e7c07ce3','e566b4a1','c3e9615e','3cf8209d','6094d1e3','cd9ca341'],
['5c76460e','00ea983b','d4d67881','fd47572c','f76cedd9','bda8229c','127dadaa','438a074e'],
['1f97c090','081bdb8a','93a07ebe','b938ca15','97b03cff','3dc2c0f8','8d1ab2ec','64380e51'],
['68cc7bfb','d90f2788','12490181','5de5ffd4','dd7ef86a','76a2e214','b9a40368','925d958f'],
['4b39fffa','ba39aee9','a4ffd30b','faf7933b','6d498623','193cbcfa','27627545','825cf47a'],
['61bd8ba0','d11e42d1','cead04f4','127ea392','10428db7','8272a972','9270c4a8','127de50b'],
['285ba1c8','3c62f44f','35c0eaa5','e805d231','428929fb','b4fcdf82','4fb66a53','0e7dc15b'],
['1f081fab','108618ae','fcfd086d','f9ff2889','694bcc11','236a5cae','12deca4d','2c3f8cc5'],
['d2d02dfe','f8ef5896','e4cf52da','95155b67','494a488c','b9b6a80c','5c8f82bc','89d36b45'],
['3a609437','ec00c9a9','44715253','0a874b49','d773bc40','7c34671c','02717ef6','4feb5536'],
['a2d02fff','d2bf60c4','d43f03c0','50b4ef6d','07478cd1','006e1888','a2e53f55','b9e6d4bc'],
['a2048016','97573833','d7207d67','de0f8f3d','72f87b33','abcc4f33','7688c55d','7b00a6b0'],
['947b0001','570075d2','f9bb88f8','8942019e','4264a5ff','856302e0','72dbd92b','ee971b69'],
['6ea22fde','5f08ae2b','af7a616d','e5c98767','cf1febd2','61efc8c2','f1ac2571','cc8239c2'],
['67214cb8','b1e583d1','b7dc3e62','7f10bdce','f90a5c38','0ff0443d','606e6dc6','60543a49'],
['5727c148','2be98a1d','8ab41738','20e1be24','af96da0f','68458425','99833be5','600d457d'],
['282f9350','8334b362','d91d1120','2b6d8da0','642b1e31','9c305a00','52bce688','1b03588a'],
['f7baefd5','4142ed9c','a4315c11','83323ec5','dfef4636','a133c501','e9d3531c','ee353783'],
]

Sbox8 = [
['9db30420','1fb6e9de','a7be7bef','d273a298','4a4f7bdb','64ad8c57','85510443','fa020ed1'],
['7e287aff','e60fb663','095f35a1','79ebf120','fd059d43','6497b7b1','f3641f63','241e4adf'],
['28147f5f','4fa2b8cd','c9430040','0cc32220','fdd30b30','c0a5374f','1d2d00d9','24147b15'],
['ee4d111a','0fca5167','71ff904c','2d195ffe','1a05645f','0c13fefe','081b08ca','05170121'],
['80530100','e83e5efe','ac9af4f8','7fe72701','d2b8ee5f','06df4261','bb9e9b8a','7293ea25'],
['ce84ffdf','f5718801','3dd64b04','a26f263b','7ed48400','547eebe6','446d4ca0','6cf3d6f5'],
['2649abdf','aea0c7f5','36338cc1','503f7e93','d3772061','11b638e1','72500e03','f80eb2bb'],
['abe0502e','ec8d77de','57971e81','e14f6746','c9335400','6920318f','081dbb99','ffc304a5'],
['4d351805','7f3d5ce3','a6c866c6','5d5bcca9','daec6fea','9f926f91','9f46222f','3991467d'],
['a5bf6d8e','1143c44f','43958302','d0214eeb','022083b8','3fb6180c','18f8931e','281658e6'],
['26486e3e','8bd78a70','7477e4c1','b506e07c','f32d0a25','79098b02','e4eabb81','28123b23'],
['69dead38','1574ca16','df871b62','211c40b7','a51a9ef9','0014377b','041e8ac8','09114003'],
['bd59e4d2','e3d156d5','4fe876d5','2f91a340','557be8de','00eae4a7','0ce5c2ec','4db4bba6'],
['e756bdff','dd3369ac','ec17b035','06572327','99afc8b0','56c8c391','6b65811c','5e146119'],
['6e85cb75','be07c002','c2325577','893ff4ec','5bbfc92d','d0ec3b25','b7801ab7','8d6d3b24'],
['20c763ef','c366a5fc','9c382880','0ace3205','aac9548a','eca1d7c7','041afa32','1d16625a'],
['6701902c','9b757a54','31d477f7','9126b031','36cc6fdb','c70b8b46','d9e66a48','56e55a79'],
['026a4ceb','52437eff','2f8f76b4','0df980a5','8674cde3','edda04eb','17a9be04','2c18f4df'],
['b7747f9d','ab2af7b4','efc34d20','2e096b7c','1741a254','e5b6a035','213d42f6','2c1c7c26'],
['61c2f50f','6552daf9','d2c231f8','25130f69','d8167fa2','0418f2c8','001a96a6','0d1526ab'],
['63315c21','5e0a72ec','49bafefd','187908d9','8d0dbd86','311170a7','3e9b640c','cc3e10d7'],
['d5cad3b6','0caec388','f73001e1','6c728aff','71eae2a1','1f9af36e','cfcbd12f','c1de8417'],
['ac07be6b','cb44a1d8','8b9b0f56','013988c3','b1c52fca','b4be31cd','d8782806','12a3a4e2'],
['6f7de532','58fd7eb6','d01ee900','24adffc2','f4990fc5','9711aac5','001d7b95','82e5e7d2'],
['109873f6','00613096','c32d9521','ada121ff','29908415','7fbb977f','af9eb3db','29c9ed2a'],
['5ce2a465','a730f32c','d0aa3fe8','8a5cc091','d49e2ce7','0ce454a9','d60acd86','015f1919'],
['77079103','dea03af6','78a8565e','dee356df','21f05cbe','8b75e387','b3c50651','b8a5c3ef'],
['d8eeb6d2','e523be77','c2154529','2f69efdf','afe67afb','f470c4b2','f3e0eb5b','d6cc9876'],
['39e4460c','1fda8538','1987832f','ca007367','a99144f8','296b299e','492fc295','9266beab'],
['b5676e69','9bd3ddda','df7e052f','db25701c','1b5e51ee','f65324e6','6afce36c','0316cc04'],
['8644213e','b7dc59d0','7965291f','ccd6fd43','41823979','932bcdf6','b657c34d','4edfd282'],
['7ae5290c','3cb9536b','851e20fe','9833557e','13ecf0b0','d3ffb372','3f85c5c1','0aef7ed2'],
]

def string_to_padded_binary_array(input_str):
    """
    Convert a string to a binary array from its UTF-8 encoding and pad the array 
    to ensure its size is a multiple of 16.
    """
    utf8_bytes = input_str.encode('utf-8')
    binary_array = [format(byte, '08b') for byte in utf8_bytes]
    padding_length = (16 - len(binary_array) % 16) % 16
    binary_array.extend(['00000000'] * padding_length) 
    return binary_array

def binary_array_to_integer(binary_array):
    """
    Convert an array of binary strings into a single integer.
    """
    combined_binary = ''.join(binary_array)
    result = int(combined_binary, 2)
    return result
def binary_with_pad(num, length=32):
    """
    Convert an integer to a binary string, padded with leading zeros to the specified length.
    """
    return bin(num)[2:].zfill(length)
def binary_xor_array(arr1, arr2):
    return [bin(int(arr1[i], 2) ^ int(arr2[i], 2))[2:].zfill(len(arr1[i])) for i in range(len(arr1))]

def chuncking_binary(num):
    return num[0:8], num[8:16], num[16:24], num[24:32]
def change_of_Sbox(character, number_of_Sbox):
    row = int(character[0:5], 2)
    col = int(character[5:], 2)
    
    match number_of_Sbox:
        case 1:
            return Sbox1[row][col]
        case 2:
            return Sbox2[row][col]
        case 3:
            return Sbox3[row][col]
        case 4:
            return Sbox4[row][col]
        case 5:
            return Sbox5[row][col]
        case 6:
            return Sbox6[row][col]
        case 7:
            return Sbox7[row][col]
        case 8:
            return Sbox8[row][col]
def flat_arr(arr):
    return [item for sublist in arr for item in sublist]
def pre_key1(x):
    z = [''] * 16
    z1 = binary_array_to_integer(x[0:4]) ^ int(change_of_Sbox(x[13], 5), 16) ^ int(change_of_Sbox(x[15], 6),16) ^ int(change_of_Sbox(x[12], 7),16) ^ int(change_of_Sbox(x[14], 8), 16) ^ int(change_of_Sbox(x[8], 7), 16)
    z[0], z[1], z[2], z[3] = chuncking_binary(bin(z1)[2:].zfill(32))
    z2 = binary_array_to_integer(x[8:12]) ^ int(change_of_Sbox(z[0], 5), 16) ^ int(change_of_Sbox(z[2], 6), 16) ^ int(change_of_Sbox(z[1], 7), 16) ^ int(change_of_Sbox(z[3], 8), 16) ^ int(change_of_Sbox(x[10], 8), 16)
    z[4], z[5], z[6], z[7] = chuncking_binary(bin(z2)[2:].zfill(32))
    z3 = binary_array_to_integer(x[12:16]) ^ int(change_of_Sbox(z[7], 5), 16) ^ int(change_of_Sbox(z[6], 6), 16) ^ int(change_of_Sbox(z[5], 7), 16) ^ int(change_of_Sbox(z[4], 8), 16) ^ int(change_of_Sbox(x[9], 5), 16)
    z[8], z[9], z[10], z[11] = chuncking_binary(bin(z3)[2:].zfill(32))
    z4 = binary_array_to_integer(x[4:8]) ^ int(change_of_Sbox(z[10], 5), 16) ^ int(change_of_Sbox(z[9], 6), 16) ^ int(change_of_Sbox(z[11], 7), 16) ^ int(change_of_Sbox(z[8], 8), 16) ^ int(change_of_Sbox(x[11], 6), 16)
    z[12], z[13], z[14], z[15] = chuncking_binary(bin(z4)[2:].zfill(32))
    return z
def pre_key2(z):
    x = [''] * 16
    x1 = binary_array_to_integer(z[8:12]) ^ int(change_of_Sbox(z[5], 5), 16) ^ int(change_of_Sbox(z[7], 6),16) ^ int(change_of_Sbox(z[4], 7),16) ^ int(change_of_Sbox(z[6], 8), 16) ^ int(change_of_Sbox(z[0], 7), 16)
    x[0], x[1], x[2], x[3] = chuncking_binary(bin(x1)[2:].zfill(32))
    x2 = binary_array_to_integer(z[0:4]) ^ int(change_of_Sbox(x[0], 5), 16) ^ int(change_of_Sbox(x[2], 6), 16) ^ int(change_of_Sbox(x[1], 7), 16) ^ int(change_of_Sbox(x[3], 8), 16) ^ int(change_of_Sbox(z[2], 8), 16)
    x[4], x[5], x[6], x[7] = chuncking_binary(bin(x2)[2:].zfill(32))
    x3 = binary_array_to_integer(z[4:8]) ^ int(change_of_Sbox(x[7], 5), 16) ^ int(change_of_Sbox(x[6], 6), 16) ^ int(change_of_Sbox(x[5], 7), 16) ^ int(change_of_Sbox(x[4], 8), 16) ^ int(change_of_Sbox(z[1], 5), 16)
    x[8], x[9], x[10], x[11] = chuncking_binary(bin(x3)[2:].zfill(32))
    x4 = binary_array_to_integer(z[12:16]) ^ int(change_of_Sbox(x[10], 5), 16) ^ int(change_of_Sbox(x[9], 6), 16) ^ int(change_of_Sbox(x[11], 7), 16) ^ int(change_of_Sbox(x[8], 8), 16) ^ int(change_of_Sbox(z[11], 6), 16)
    x[12], x[13], x[14], x[15] = chuncking_binary(bin(x4)[2:].zfill(32))
    return x
def key_gen1(z):
    k_first = int(change_of_Sbox(z[8], 5), 16) ^ int(change_of_Sbox(z[9], 6), 16) ^ int(change_of_Sbox(z[7], 7), 16) ^ int(change_of_Sbox(z[6], 8), 16) ^ int(change_of_Sbox(z[2], 5), 16)
    k_second = int(change_of_Sbox(z[10], 5), 16) ^ int(change_of_Sbox(z[11], 6), 16) ^ int(change_of_Sbox(z[5], 7), 16) ^ int(change_of_Sbox(z[4], 8), 16) ^ int(change_of_Sbox(z[6], 6), 16)
    K1 = (bin(k_first)[2:] + bin(k_second)[2:])
    k_third = int(change_of_Sbox(z[12], 5), 16) ^ int(change_of_Sbox(z[13], 6), 16) ^ int(change_of_Sbox(z[3], 7), 16) ^ int(change_of_Sbox(z[2], 8), 16) ^ int(change_of_Sbox(z[9], 7), 16)
    k_forth = int(change_of_Sbox(z[14], 5), 16) ^ int(change_of_Sbox(z[15], 6), 16) ^ int(change_of_Sbox(z[1], 7), 16) ^ int(change_of_Sbox(z[0], 8), 16) ^ int(change_of_Sbox(z[13], 8), 16)
    K2 = (bin(k_third)[2:] + bin(k_forth)[2:])
    return K1, K2
def key_gen2(x):
    k_first = int(change_of_Sbox(x[3], 5), 16) ^ int(change_of_Sbox(x[2], 6), 16) ^ int(change_of_Sbox(x[12], 7), 16) ^ int(change_of_Sbox(x[13], 8), 16) ^ int(change_of_Sbox(x[8], 5), 16)
    k_second = int(change_of_Sbox(x[1], 5), 16) ^ int(change_of_Sbox(x[0], 6), 16) ^ int(change_of_Sbox(x[14], 7), 16) ^ int(change_of_Sbox(x[15], 8), 16) ^ int(change_of_Sbox(x[13], 6), 16)
    K3 = (bin(k_first)[2:] + bin(k_second)[2:])
    k_third = int(change_of_Sbox(x[7], 5), 16) ^ int(change_of_Sbox(x[6], 6), 16) ^ int(change_of_Sbox(x[8], 7), 16) ^ int(change_of_Sbox(x[9], 8), 16) ^ int(change_of_Sbox(x[3], 7), 16)
    k_forth = int(change_of_Sbox(x[5], 5), 16) ^ int(change_of_Sbox(x[4], 6), 16) ^ int(change_of_Sbox(x[10], 7), 16) ^ int(change_of_Sbox(x[11], 8), 16) ^ int(change_of_Sbox(x[7], 8), 16)
    K4 = (bin(k_forth)[2:] + bin(k_third)[2:])
    return K3, K4
def key_gen3(z):
    k_first = int(change_of_Sbox(z[3], 5), 16) ^ int(change_of_Sbox(z[2], 6), 16) ^ int(change_of_Sbox(z[12], 7), 16) ^ int(change_of_Sbox(z[13], 8), 16) ^ int(change_of_Sbox(z[9], 5), 16)
    k_second = int(change_of_Sbox(z[1], 5), 16) ^ int(change_of_Sbox(z[0], 6), 16) ^ int(change_of_Sbox(z[14], 7), 16) ^ int(change_of_Sbox(z[15], 8), 16) ^ int(change_of_Sbox(z[12], 6), 16)
    K1 = (bin(k_first)[2:] + bin(k_second)[2:])
    k_third = int(change_of_Sbox(z[7], 5), 16) ^ int(change_of_Sbox(z[6], 6), 16) ^ int(change_of_Sbox(z[8], 7), 16) ^ int(change_of_Sbox(z[9], 8), 16) ^ int(change_of_Sbox(z[2], 7), 16)
    k_forth = int(change_of_Sbox(z[5], 5), 16) ^ int(change_of_Sbox(z[4], 6), 16) ^ int(change_of_Sbox(z[10], 7), 16) ^ int(change_of_Sbox(z[11], 8), 16) ^ int(change_of_Sbox(z[6], 8), 16)
    K2 = (bin(k_third)[2:] + bin(k_forth)[2:])
    return K1, K2
def key_gen4(x):
    k_first = int(change_of_Sbox(x[8], 5), 16) ^ int(change_of_Sbox(x[9], 6), 16) ^ int(change_of_Sbox(x[7], 7), 16) ^ int(change_of_Sbox(x[6], 8), 16) ^ int(change_of_Sbox(x[3], 5), 16)
    k_second = int(change_of_Sbox(x[10], 5), 16) ^ int(change_of_Sbox(x[11], 6), 16) ^ int(change_of_Sbox(x[5], 7), 16) ^ int(change_of_Sbox(x[4], 8), 16) ^ int(change_of_Sbox(x[7], 6), 16)
    K3 = (bin(k_first)[2:] + bin(k_second)[2:])
    k_third = int(change_of_Sbox(x[12], 5), 16) ^ int(change_of_Sbox(x[13], 6), 16) ^ int(change_of_Sbox(x[3], 7), 16) ^ int(change_of_Sbox(x[2], 8), 16) ^ int(change_of_Sbox(x[8], 7), 16)
    k_forth = int(change_of_Sbox(x[14], 5), 16) ^ int(change_of_Sbox(x[15], 6), 16) ^ int(change_of_Sbox(x[1], 7), 16) ^ int(change_of_Sbox(x[0], 8), 16) ^ int(change_of_Sbox(x[13], 8), 16)
    K4 = (bin(k_third)[2:] + bin(k_forth)[2:])
    return K3, K4
def generate_keys(x):
    z = pre_key1(x)
    x = pre_key2(z)
    K1,K2 = key_gen1(z)
    K3,K4 = key_gen2(x)
    z = pre_key1(x)
    x = pre_key2(z)
    K5,K6 = key_gen3(z)
    K7,K8 = key_gen4(x)
    z = pre_key1(x)
    x = pre_key2(z)
    K9,K10 = key_gen1(z)
    K11,K12 = key_gen2(x)
    z = pre_key1(x)
    x = pre_key2(z)
    K13,K14 = key_gen3(z)
    K15,K16 = key_gen4(x)
    return [K1,K2,K3,K4,K5,K6,K7,K8,K9,K10,K11,K12,K13,K14,K15,K16]
def decode_binary_array_with_errors(arr):
    """
    Decode an array of binary strings (each 8 bits) into a UTF-8 string.
    Invalid UTF-8 sequences are replaced with a placeholder character.
    """
    byte_array = bytearray([int(binary, 2) for binary in arr])
    decoded_string = byte_array.decode("utf-8", errors="replace")
    return decoded_string

def round_function(sub_key, x):
    z1 = int(x[0], 2) ^ int(sub_key[7], 2)
    z2 = int(x[1], 2) ^ int(sub_key[6], 2)
    z3 = int(x[2], 2) ^ int(sub_key[5], 2)
    z4 = int(x[3], 2) ^ int(sub_key[4], 2)
    z5 = int(x[4], 2) ^ int(sub_key[3], 2)
    z6 = int(x[5], 2) ^ int(sub_key[2], 2)
    z7 = int(x[6], 2) ^ int(sub_key[1], 2)
    z8 = int(x[7], 2) ^ int(sub_key[0], 2)
    
    z1 = int(change_of_Sbox(bin(z1)[2:].zfill(8), 1), 10)
    z2 = int(change_of_Sbox(bin(z2)[2:].zfill(8), 2), 10)
    z3 = int(change_of_Sbox(bin(z3)[2:].zfill(8), 3), 10)
    z4 = int(change_of_Sbox(bin(z4)[2:].zfill(8), 4), 10)
    z5 = int(change_of_Sbox(bin(z5)[2:].zfill(8), 2), 10)
    z6 = int(change_of_Sbox(bin(z6)[2:].zfill(8), 3), 10)
    z7 = int(change_of_Sbox(bin(z7)[2:].zfill(8), 4), 10)
    z8 = int(change_of_Sbox(bin(z8)[2:].zfill(8), 1), 10)
    coef = np.array([
        [0,1,1,1,1,0,0,1],
        [1,0,1,1,1,1,0,0],
        [1,1,0,1,0,1,1,0],
        [1,1,1,0,0,0,1,1],
        [0,1,1,1,1,1,1,0],
        [1,0,1,1,0,1,1,1],
        [1,1,0,1,1,0,1,1],
        [1,1,1,0,1,1,0,1],])
    
    Z = np.array([z1,z2,z3,z4,z5,z6,z7,z8])
    Z = [bin(i)[2:].zfill(8) for i in Z]
    Z = [[int(i) for i in j] for j in Z]
    result = np.dot(coef,Z)
    result = [i % 2 for i in result]
    result = [''.join([str(i) for i in row])[2:] for row in result]
    return result

def int_to_binary_array(num):
    """
    Convert an integer to a 64-bit binary string and split it into an array of 8 strings,
    each containing 8 bits.
    """
    binary_string = bin(num)[2:].zfill(64)
    binary_array = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    return binary_array

def encryption_feistel(text, key):
    left = text[:8]
    right = text[8:]
    for i in range(16):
        round_key = key[i]
        right_binary = ''.join(right)  # Join the array into a single binary string
        if len(right_binary) < 64:
            right_binary = right_binary.zfill(64)  # Pad with leading zeros if necessary
        
        # Split the 64-bit binary string back into 8-bit chunks
        right = [right_binary[i:i+8] for i in range(0, 64, 8)]
        after_round_function = round_function(round_key, right)
        after_xor = binary_array_to_integer(left) ^ binary_array_to_integer(after_round_function)
        new_right = int_to_binary_array(after_xor)
        left , right = right, new_right
    return right + left

def decryption_feistel(cypher_text, key):
    left = cypher_text[0:8]
    right = cypher_text[8:]
    for i in range(16):
        round_key = key[(15-i)]
        right_binary = ''.join(right)  # Join the array into a single binary string
        if len(right_binary) < 64:
            right_binary = right_binary.zfill(64)  # Pad with leading zeros if necessary
        # Split the 64-bit binary string back into 8-bit chunks
        right = [right_binary[i:i+8] for i in range(0, 64, 8)]
        after_round_function = round_function(round_key, right)
        after_xor = binary_array_to_integer(left) ^ binary_array_to_integer(after_round_function)
        new_right = int_to_binary_array(after_xor)
        left , right = right, new_right
    return right + left

def EBC_mode_encryption(plain_text, key):
    plain_text = string_to_padded_binary_array(plain_text)
    plain_text = [plain_text[i:i+16] for i in range(0, len(plain_text), 16)]
    cipher_chunks = []

    for plain_chunk in plain_text:
        keys = generate_keys(key)
        cipher = encryption_feistel(plain_chunk, keys)
        cipher_chunks.append(cipher)

    final_cipher = flat_arr(cipher_chunks)
    return final_cipher

def EBC_mode_decryption(cipher_text, key):
    cipher_text = [cipher_text[i:i+16] for i in range(0, len(cipher_text), 16)]
    plain_chunks = []

    for cipher_chunk in cipher_text:
        keys = generate_keys(key)
        plain = decryption_feistel(cipher_chunk, keys)
        plain_chunks.append(plain)

    final_plain = flat_arr(plain_chunks)
    return final_plain

def OFB_mode_encryption(plain_text, key, initial):
    plain_text = string_to_padded_binary_array(plain_text)
    plain_text = [plain_text[i:i+16] for i in range(0, len(plain_text), 16)]
    cipher_chunks = []
    feedback = initial

    for plain_chunk in plain_text:
        keys = generate_keys(key)
        feedback = encryption_feistel(feedback, keys)
        chunk = binary_xor_array(plain_chunk, feedback)
        cipher_chunks.append(chunk)

    final_cipher = flat_arr(cipher_chunks)
    return final_cipher

def OFB_mode_decryption(cipher_text, key, initial):
    cipher_text = [cipher_text[i:i+16] for i in range(0, len(cipher_text), 16)]
    plain_chunks = []
    feedback = initial

    for cipher_chunk in cipher_text:
        keys = generate_keys(key)
        feedback = encryption_feistel(feedback, keys)
        chunk = binary_xor_array(cipher_chunk, feedback)
        plain_chunks.append(chunk)

    final_plain = flat_arr(plain_chunks)
    return final_plain

def CBC_mode_encryption(plain_text, key, initial):
    plain_text = string_to_padded_binary_array(plain_text)
    plain_text = [plain_text[i:i+16] for i in range(0, len(plain_text), 16)]
    cipher_chunks = []
    previous = initial

    for plain_chunk in plain_text:
        keys = generate_keys(key)
        xored_chunk = binary_xor_array(plain_chunk, previous)
        chunk = encryption_feistel(xored_chunk, keys)
        cipher_chunks.append(chunk)
        previous = chunk

    final_cipher = flat_arr(cipher_chunks)
    return final_cipher

def CBC_mode_decryption(cipher_text, key, initial):
    cipher_text = [cipher_text[i:i+16] for i in range(0, len(cipher_text), 16)]
    plain_chunks = []
    previous = initial

    for cipher_chunk in cipher_text:
        keys = generate_keys(key)
        decrypted_chunk = decryption_feistel(cipher_chunk, keys)
        
        # Ensure decrypted_chunk is 16 bytes
        if len(decrypted_chunk) > 16:
            decrypted_chunk = decrypted_chunk[:16]  # Truncate to 16 bytes if necessary
        
        chunk = binary_xor_array(decrypted_chunk, previous)
        plain_chunks.append(chunk)
        previous = cipher_chunk

    final_plain = flat_arr(plain_chunks)
    
    
    return final_plain
def CTR_mode_encryption(plain_text, key, initial):
    plain_text = string_to_padded_binary_array(plain_text)
    plain_text = [plain_text[i:i+16] for i in range(0, len(plain_text), 16)]
    cipher_chunks = []
    ctr = initial

    for plain_chunk in plain_text:
        keys = generate_keys(key)
        ctr_for_this_block = encryption_feistel(ctr, keys)
        chunk = binary_xor_array(plain_chunk, ctr_for_this_block)
        cipher_chunks.append(chunk)
        ctr = int_to_binary_array(binary_array_to_integer(ctr) + 1)

    final_cipher = flat_arr(cipher_chunks)
    return final_cipher

def CTR_mode_decryption(cipher_text, key, initial):
    cipher_text = [cipher_text[i:i+16] for i in range(0, len(cipher_text), 16)]
    plain_chunks = []
    ctr = initial

    for cipher_chunk in cipher_text:
        keys = generate_keys(key)
        ctr_for_this_block = encryption_feistel(ctr, keys)
        chunk = binary_xor_array(cipher_chunk, ctr_for_this_block)
        plain_chunks.append(chunk)
        ctr = int_to_binary_array(binary_array_to_integer(ctr) + 1)

    final_plain = flat_arr(plain_chunks)
    return final_plain

# # Example usage
# x = ['10010110', '10111010', '11110000', '01110100', '00101001', '01100010', '00110111', '11100010', '00010110', '10000010', '10000001', '01100011', '00000110', '00001010', '00010100', '11011000']
# initial = ['10101000'] * 16
# cipher_text = EBC_mode_encryption("hello this is a test and i want this text to be more long enough so i can test my code", x)
# print(f"this is binary of encrypted: {cipher_text} and len of it is: {len(cipher_text)}")
# print("Cipher Text:", decode_binary_array_with_errors(cipher_text))

# plain_text = EBC_mode_decryption(cipher_text, x)
# print(f"this is binary of decrypted: {plain_text} and len of it is: {len(plain_text)}")
# print("Decrypted Text:", decode_binary_array_with_errors(plain_text))

# Encryption and Decryption Example for OFB mode
# cipher_text = CBC_mode_encryption("hello this is a test and i want this text to be more long enough so i can test my code", x, initial)
# print(f"this is binary of encrypted: {cipher_text} and len of it is: {len(cipher_text)}")
# print("Cipher Text:", decode_binary_array_with_errors(cipher_text))

# plain_text = CBC_mode_decryption(cipher_text, x, initial)
# print(f"this is binary of decrypted: {plain_text} and len of it is: {len(plain_text)}")
# print("Decrypted Text:", decode_binary_array_with_errors(plain_text))
