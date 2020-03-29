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
(5,1,'Asia Pacific (Hong Kong)','Asie-Pacifique','Hong Kong','114','22'),
(6,1,'Asia Pacific (Mumbai)','Asie-Pacifique','Inde','73','19'),
(7,1,'Asia Pacific (Osaka-Local)','Asie-Pacifique','Japon','136','35'),
(8,1,'Asia Pacific (Seoul)','Asie-Pacifique','Corée du Sud','127','37'),
(9,1,'Asia Pacific (Singapore)','Asie-Pacifique','Singapour','103.7','1.4'),
(10,1,'Asia Pacific (Sydney)','Asie-Pacifique','Australie','151','-34'),
(11,1,'Asia Pacific (Tokyo)','Asie-Pacifique','Japon','140','36'),
(12,1,'Canada (Central)','Amérique du Nord','Canada','-99','52'),
(13,1,'Europe (Frankfurt)','Europe','Allemagne','9','50'),
(14,1,'Europe (Ireland)','Europe','Irlande','-7','53'),
(15,1,'Europe (London)','Europe','Grande-Bretagne','-0.4','51'),
(16,1,'Europe (Paris)','Europe','France','3','49'),
(17,1,'Europe (Stockholm)','Europe','Suède','18','60'),
(18,1,'Middle East (Bahrain)','Asie-Pacifique','Bahrain','50.5','25.9'),
(19,1,'South America (São Paulo)','Amérique du Sud','Brésil','-46','-23'),
(20,2,'NORTHAMERICA-NORTHEAST1','Amérique du Nord','Canada','-66','46'),
(21,2,'US-CENTRAL1','Amérique du Nord','Etats-Unis','-97','42'),
(22,2,'US-EAST1','Amérique du Nord','Etats-Unis','-74','42'),
(23,2,'US-EAST4','Amérique du Nord','Etats-Unis','-77','40'),
(24,2,'US-WEST1','Amérique du Nord','Etats-Unis','-122','41'),
(25,2,'US-WEST2','Amérique du Nord','Etats-Unis','-116','34'),
(26,2,'SOUTHAMERICA-EAST1','Amérique du Sud','Brésil','-41','-14'),
(27,2,'EUROPE-NORTH1','Europe','Finlande','25','61'),
(28,2,'EUROPE-WEST1','Europe','Belgique','4','51'),
(29,2,'EUROPE-WEST2','Europe','Grande-Bretagne','-1.5','52'),
(30,2,'EUROPE-WEST3','Europe','Allemagne','7','50'),
(31,2,'EUROPE-WEST4','Europe','Pays-Bas','5.3','52'),
(32,2,'EUROPE-WEST6','Europe','Suisse','8','47'),
(33,2,'ASIA-EAST1','Asie-Pacifique','Taïwan','121','24'),
(34,2,'ASIA-EAST2','Asie-Pacifique','Hong Kong','114','22'),
(35,2,'ASIA-NORTHEAST1','Asie-Pacifique','Japon','139','36'),
(36,2,'ASIA-NORTHEAST2','Asie-Pacifique','Japon','134','35'),
(37,2,'ASIA-SOUTH1','Asie-Pacifique','Inde','78','11'),
(38,2,'ASIA-SOUTHEAST1','Asie-Pacifique','Singapour','103.7','1.4'),
(39,2,'AUSTRALIA-SOUTHEAST1','Asie-Pacifique','Australie','150','-36'),
(40,3,'Canada East','Amérique du Nord','Canada','-73','47'),
(41,3,'Canada Central','Amérique du Nord','Canada','-113','55'),
(42,3,'US Gov Iowa','Amérique du Nord','Etats-Unis','-93.2','41.8'),
(43,3,'Central US','Amérique du Nord','Etats-Unis','-92','37'),
(44,3,'North Central US','Amérique du Nord','Etats-Unis','-93','47'),
(45,3,'US DoD East','Amérique du Nord','Etats-Unis','-78','37'),
(46,3,'East US','Amérique du Nord','Etats-Unis','-70','44'),
(47,3,'East US 2','Amérique du Nord','Etats-Unis','-72','42'),
(48,3,'US Gov Virginia','Amérique du Nord','Etats-Unis','-77.8','37.7'),
(49,3,'US DoD Central','Amérique du Nord','Etats-Unis','-100','38'),
(50,3,'West US 2','Amérique du Nord','Etats-Unis','-119','39'),
(51,3,'West Central US','Amérique du Nord','Etats-Unis','-109','40'),
(52,3,'West US','Amérique du Nord','Etats-Unis','-123','40'),
(53,3,'US Gov Arizona','Amérique du Nord','Etats-Unis','-111.9','33.8'),
(54,3,'South Central US','Amérique du Nord','Etats-Unis','-98','35'),
(55,3,'US Gov Texas','Amérique du Nord','Etats-Unis','-97.8','41'),
(56,3,'Brazil South','Amérique du Sud','Brésil','-53','-31'),
(57,3,'Norway West','Europe','Norvège','6','60'),
(58,3,'West Europe','Europe','Pays-Bas','5.4','52'),
(59,3,'UK South','Europe','Grande-Bretagne','-1.8','51'),
(60,3,'North Europe','Europe','Irlande','-9','52'),
(61,3,'UK West','Europe','Grande-Bretagne','-4','52'),
(62,3,'France Central','Europe','France','2','47'),
(63,3,'France South','Europe','France','3','44'),
(64,3,'Switzerland West','Europe','Suisse','7','47'),
(65,3,'Switzerland North','Europe','Suisse','8','47'),
(66,3,'Germany Central','Europe','Allemagne','11','52'),
(67,3,'Germany Northeast','Europe','Allemagne','8','53'),
(68,3,'Germany North','Europe','Allemagne','11','54'),
(69,3,'Germany West Central','Europe','Allemagne','9','49'),
(70,3,'Norway East','Europe','Norvège','11','60'),
(71,3,'South Africa West','Afrique','Afrique du Sud','19','-33'),
(72,3,'South Africa North','Afrique','Afrique du Sud','28','-26'),
(73,3,'UAE Central','Asie-Pacifique','Emirats Arabes Unis','55','24'),
(74,3,'UAE North','Asie-Pacifique','Emirats Arabes Unis','56','25'),
(75,3,'West India','Asie-Pacifique','Inde','74','17'),
(76,3,'Central India','Asie-Pacifique','Inde','78','20'),
(77,3,'South India','Asie-Pacifique','Inde','77','11'),
(78,3,'Southeast Asia','Asie-Pacifique','Singapour','103.7','1.4'),
(79,3,'China North','Asie-Pacifique','Chine','115','39'),
(80,3,'China North 2','Asie-Pacifique','Chine','118','37'),
(81,3,'Korea Central','Asie-Pacifique','Corée du Sud','128','36'),
(82,3,'Korea South','Asie-Pacifique','Corée du Sud','127','35'),
(83,3,'China East','Asie-Pacifique','Chine','121','30'),
(84,3,'China East 2','Asie-Pacifique','Chine','120','28'),
(85,3,'East Asia','Asie-Pacifique','Chine','115','23'),
(86,3,'Japan East','Asie-Pacifique','Japon','140','37'),
(87,3,'Japan West','Asie-Pacifique','Japon','131','33'),
(88,3,'Australia East','Asie-Pacifique','Australie','151','-31'),
(89,3,'Australia Southeast','Asie-Pacifique','Australie','148','-37'),
(90,3,'Australia Central','Asie-Pacifique','Australie','132','-29'),
(91,3,'Australia Central 2','Asie-Pacifique','Australie','133','-24')