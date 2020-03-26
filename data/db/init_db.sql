DELETE FROM storage_asset_history;
DELETE FROM storage_asset;
DELETE FROM storage_data_location;
DELETE FROM storage_data_provider;
DELETE FROM digital_asset_history;
DELETE FROM digital_asset;
DELETE FROM collection;
DELETE FROM user;
DELETE FROM organisation;

INSERT INTO organisation(id,name)
VALUES
	(1,'Institut de la Préservation digitale');

INSERT INTO user (id,username,email,first_name,last_name,password_hash,organisation_id)
VALUES
	(1,'habib','h.hourany@gmail.com','Habib','El Hourani','pbkdf2:sha256:150000$BUabOlFq$efd6e49727596d8522bc1759bdaa4dccaffdc50e2e645dd962ebf8a5bf5413fd',1);

INSERT INTO collection(id,name,description,organisation_id)
VALUES
	(1,'Manuscripts de Caedmon','Collection contenant les Manuscripts de Caedmon', 1),
	(2,'Apocalypse flamande','Collection contenant Apocalypse flamande', 1);

INSERT INTO storage_data_provider(id,name)
VALUES
	(1,'Amazon'),
	(2,'Google'),
	(3,'Microsoft');
	
INSERT INTO storage_data_location(id,data_provider_id,name,continent,country,longitude,latitude)
VALUES
(1,1,'US East (Ohio)','Amérique du Nord','Etats-Unis','-82.9','39.9'),
(2,1,'US East (N. Virginia)','Amérique du Nord','Etats-Unis','-77.4','37.5'),
(3,1,'US West (N. California)','Amérique du Nord','Etats-Unis','-121.5','38.6'),
(4,1,'US West (Oregon)','Amérique du Nord','Etats-Unis','-122.7','45.5'),
(5,1,'Asia Pacific (Hong Kong)','Asie-Pacifique','Hong Kong','62','14'),
(6,1,'Asia Pacific (Mumbai)','Asie-Pacifique','Inde','41','4'),
(7,1,'Asia Pacific (Osaka-Local)','Asie-Pacifique','Japon','-70','34'),
(8,1,'Asia Pacific (Seoul)','Asie-Pacifique','Corée du Sud','162','47'),
(9,1,'Asia Pacific (Singapore)','Asie-Pacifique','Singapour','-49','-13'),
(10,1,'Asia Pacific (Sydney)','Asie-Pacifique','Australie','-71','25'),
(11,1,'Asia Pacific (Tokyo)','Asie-Pacifique','Japon','-158','3'),
(12,1,'Canada (Central)','Amérique du Nord','Canada','163','-24'),
(13,1,'Europe (Frankfurt)','Europe','Allemagne','128','14'),
(14,1,'Europe (Ireland)','Europe','Irlande','-46','27'),
(15,1,'Europe (London)','Europe','Grande-Bretagne','66','45'),
(16,1,'Europe (Paris)','Europe','France','-179','4'),
(17,1,'Europe (Stockholm)','Europe','Suède','179','33'),
(18,1,'Middle East (Bahrain)','Asie-Pacifique','Bahrain','-36','28'),
(19,1,'South America (São Paulo)','Amérique du Sud','Brésil','-25','46'),
(20,2,'NORTHAMERICA-NORTHEAST1','Amérique du Nord','Canada','62','3'),
(21,2,'US-CENTRAL1','Amérique du Nord','Etats-Unis','46','29'),
(22,2,'US-EAST1','Amérique du Nord','Etats-Unis','-92','-43'),
(23,2,'US-EAST4','Amérique du Nord','Etats-Unis','-160','11'),
(24,2,'US-WEST1','Amérique du Nord','Etats-Unis','161','0'),
(25,2,'US-WEST2','Amérique du Nord','Etats-Unis','83','-25'),
(26,2,'SOUTHAMERICA-EAST1','Amérique du Sud','Brésil','63','-34'),
(27,2,'EUROPE-NORTH1','Europe','Finlande','95','-22'),
(28,2,'EUROPE-WEST1','Europe','Belgique','143','43'),
(29,2,'EUROPE-WEST2','Europe','Grande-Bretagne','131','-16'),
(30,2,'EUROPE-WEST3','Europe','Allemagne','133','-32'),
(31,2,'EUROPE-WEST4','Europe','Pays-Bas','116','34'),
(32,2,'EUROPE-WEST6','Europe','Suisse','-122','-48'),
(33,2,'ASIA-EAST1','Asie-Pacifique','Taïwan','-119','30'),
(34,2,'ASIA-EAST2','Asie-Pacifique','Hong Kong','-53','31'),
(35,2,'ASIA-NORTHEAST1','Asie-Pacifique','Japon','177','-17'),
(36,2,'ASIA-NORTHEAST2','Asie-Pacifique','Japon','162','28'),
(37,2,'ASIA-SOUTH1','Asie-Pacifique','Inde','-39','-10'),
(38,2,'ASIA-SOUTHEAST1','Asie-Pacifique','Singapour','-100','-9'),
(39,2,'AUSTRALIA-SOUTHEAST1','Asie-Pacifique','Australie','169','42'),
(40,3,'Canada East','Amérique du Nord','Canada','124','36'),
(41,3,'Canada Central','Amérique du Nord','Canada','15','-16'),
(42,3,'US Gov Iowa','Amérique du Nord','etats-Unis','-22','-13'),
(43,3,'Central US','Amérique du Nord','etats-Unis','162','-18'),
(44,3,'North Central US','Amérique du Nord','etats-Unis','125','0'),
(45,3,'US DoD East','Amérique du Nord','etats-Unis','69','-36'),
(46,3,'East US','Amérique du Nord','etats-Unis','-143','30'),
(47,3,'East US 2','Amérique du Nord','etats-Unis','-96','-38'),
(48,3,'US Gov Virginia','Amérique du Nord','etats-Unis','-100','16'),
(49,3,'US DoD Central','Amérique du Nord','etats-Unis','40','-25'),
(50,3,'West US 2','Amérique du Nord','etats-Unis','-33','19'),
(51,3,'West Central US','Amérique du Nord','etats-Unis','-84','-33'),
(52,3,'West US','Amérique du Nord','etats-Unis','8','-50'),
(53,3,'US Gov Arizona','Amérique du Nord','etats-Unis','-44','14'),
(54,3,'South Central US','Amérique du Nord','etats-Unis','89','24'),
(55,3,'US Gov Texas','Amérique du Nord','etats-Unis','-97.8','34'),
(56,3,'Brazil South','Amérique du Sud','Brésil','-76','-26'),
(57,3,'Norway West','Europe','Norvège','-81','-41'),
(58,3,'West Europe','Europe','Pays-Bas','-70','6'),
(59,3,'UK South','Europe','Grande-Bretagne','117','19'),
(60,3,'North Europe','Europe','Irlande','-98','9'),
(61,3,'UK West','Europe','Grande-Bretagne','-163','-26'),
(62,3,'France Central','Europe','France','-46','-11'),
(63,3,'France South','Europe','France','-18','-11'),
(64,3,'Switzerland West','Europe','Suisse','111','-3'),
(65,3,'Switzerland North','Europe','Suisse','-105','-50'),
(66,3,'Germany Central','Europe','Allemagne','-151','-7'),
(67,3,'Germany Northeast','Europe','Allemagne','180','14'),
(68,3,'Germany North','Europe','Allemagne','-94','-16'),
(69,3,'Germany West Central','Europe','Allemagne','129','-46'),
(70,3,'Norway East','Europe','Norvège','-97','-42'),
(71,3,'South Africa West','Afrique','Afrique du Sud','69','-38'),
(72,3,'South Africa North','Afrique','Afrique du Sud','23','15'),
(73,3,'UAE Central','Asie-Pacifique','Emirats Arabes Unis','-146','28'),
(74,3,'UAE North','Asie-Pacifique','Emirats Arabes Unis','178','30'),
(75,3,'West India','Asie-Pacifique','Inde','-171','19'),
(76,3,'Central India','Asie-Pacifique','Inde','-64','-10'),
(77,3,'South India','Asie-Pacifique','Inde','116','-16'),
(78,3,'Southeast Asia','Asie-Pacifique','Singapour','105','-25'),
(79,3,'China North','Asie-Pacifique','Chine','7','-3'),
(80,3,'China North 2','Asie-Pacifique','Chine','5','0'),
(81,3,'Korea Central','Asie-Pacifique','Corée du Sud','99','-36'),
(82,3,'Korea South','Asie-Pacifique','Corée du Sud','-79','35'),
(83,3,'China East','Asie-Pacifique','Chine','-40','-10'),
(84,3,'China East 2','Asie-Pacifique','Chine','-104','-25'),
(85,3,'East Asia','Asie-Pacifique','Chine','-97','-10'),
(86,3,'Japan East','Asie-Pacifique','Japon','18','44'),
(87,3,'Japan West','Asie-Pacifique','Japon','-45','19'),
(88,3,'Australia East','Asie-Pacifique','Australie','-40','45'),
(89,3,'Australia Southeast','Asie-Pacifique','Australie','-137','-45'),
(90,3,'Australia Central','Asie-Pacifique','Australie','119','-47'),
(91,3,'Australia Central 2','Asie-Pacifique','Australie','125','32')