DELETE FROM digital_asset_storage;
DELETE FROM data_storage_location;
DELETE FROM data_provider;
DELETE FROM digital_asset;
DELETE FROM user;
DELETE FROM organisation;

INSERT INTO organisation(id,name)
VALUES
	(1,'Institut de la Préservation digitale');


INSERT INTO user (id,username,email,first_name,last_name,password_hash,organisation_id)
VALUES
	(1,'habib','h.hourany@gmail.com','Habib','El Hourani','pbkdf2:sha256:150000$BUabOlFq$efd6e49727596d8522bc1759bdaa4dccaffdc50e2e645dd962ebf8a5bf5413fd',1);


INSERT INTO data_provider(id,name)
VALUES
	(1,'Amazon'),
	(2,'Google'),
	(3,'Microsoft');
	
INSERT INTO data_storage_location(id,data_provider_id,name,continent,country)
VALUES
(1,1,'US East (Ohio)','Amérique du Nord','Etats-Unis'),
(2,1,'US East (N. Virginia)','Amérique du Nord','Etats-Unis'),
(3,1,'US West (N. California)','Amérique du Nord','Etats-Unis'),
(4,1,'US West (Oregon)','Amérique du Nord','Etats-Unis'),
(5,1,'Asia Pacific (Hong Kong)','Asie-Pacifique','Hong Kong'),
(6,1,'Asia Pacific (Mumbai)','Asie-Pacifique','Inde'),
(7,1,'Asia Pacific (Osaka-Local)','Asie-Pacifique','Japon'),
(8,1,'Asia Pacific (Seoul)','Asie-Pacifique','Corée du Sud'),
(9,1,'Asia Pacific (Singapore)','Asie-Pacifique','Singapour'),
(10,1,'Asia Pacific (Sydney)','Asie-Pacifique','Australie'),
(11,1,'Asia Pacific (Tokyo)','Asie-Pacifique','Japon'),
(12,1,'Canada (Central)','Amérique du Nord','Canada'),
(13,1,'Europe (Frankfurt)','Europe','Allemagne'),
(14,1,'Europe (Ireland)','Europe','Irlande'),
(15,1,'Europe (London)','Europe','Grande-Bretagne'),
(16,1,'Europe (Paris)','Europe','France'),
(17,1,'Europe (Stockholm)','Europe','Suède'),
(18,1,'Middle East (Bahrain)','Asie-Pacifique','Bahrain'),
(19,1,'South America (São Paulo)','Amérique du Sud','Brésil'),
(20,2,'NORTHAMERICA-NORTHEAST1','Amérique du Nord','Canada'),
(21,2,'US-CENTRAL1','Amérique du Nord','Etats-Unis'),
(22,2,'US-EAST1','Amérique du Nord','Etats-Unis'),
(23,2,'US-EAST4','Amérique du Nord','Etats-Unis'),
(24,2,'US-WEST1','Amérique du Nord','Etats-Unis'),
(25,2,'US-WEST2','Amérique du Nord','Etats-Unis'),
(26,2,'SOUTHAMERICA-EAST1','Amérique du Sud','Brésil'),
(27,2,'EUROPE-NORTH1','Europe','Finlande'),
(28,2,'EUROPE-WEST1','Europe','Belgique'),
(29,2,'EUROPE-WEST2','Europe','Grande-Bretagne'),
(30,2,'EUROPE-WEST3','Europe','Allemagne'),
(31,2,'EUROPE-WEST4','Europe','Pays-Bas'),
(32,2,'EUROPE-WEST6','Europe','Suisse'),
(33,2,'ASIA-EAST1','Asie-Pacifique','Taïwan'),
(34,2,'ASIA-EAST2','Asie-Pacifique','Hong Kong'),
(35,2,'ASIA-NORTHEAST1','Asie-Pacifique','Japon'),
(36,2,'ASIA-NORTHEAST2','Asie-Pacifique','Japon'),
(37,2,'ASIA-SOUTH1','Asie-Pacifique','Inde'),
(38,2,'ASIA-SOUTHEAST1','Asie-Pacifique','Singapour'),
(39,2,'AUSTRALIA-SOUTHEAST1','Asie-Pacifique','Australie'),
(40,3,'Canada East','Amérique du Nord','Canada'),
(41,3,'Canada Central','Amérique du Nord','Canada'),
(42,3,'US Gov Iowa','Amérique du Nord','etats-Unis'),
(43,3,'Central US','Amérique du Nord','etats-Unis'),
(44,3,'North Central US','Amérique du Nord','etats-Unis'),
(45,3,'US DoD East','Amérique du Nord','etats-Unis'),
(46,3,'East US','Amérique du Nord','etats-Unis'),
(47,3,'East US 2','Amérique du Nord','etats-Unis'),
(48,3,'US Gov Virginia','Amérique du Nord','etats-Unis'),
(49,3,'US DoD Central','Amérique du Nord','etats-Unis'),
(50,3,'West US 2','Amérique du Nord','etats-Unis'),
(51,3,'West Central US','Amérique du Nord','etats-Unis'),
(52,3,'West US','Amérique du Nord','etats-Unis'),
(53,3,'US Gov Arizona','Amérique du Nord','etats-Unis'),
(54,3,'South Central US','Amérique du Nord','etats-Unis'),
(55,3,'US Gov Texas','Amérique du Nord','etats-Unis'),
(56,3,'Brazil South','Amérique du Sud','Brésil'),
(57,3,'Norway West','Europe','Norvège'),
(58,3,'West Europe','Europe','Pays-Bas'),
(59,3,'UK South','Europe','Grande-Bretagne'),
(60,3,'North Europe','Europe','Irlande'),
(61,3,'UK West','Europe','Grande-Bretagne'),
(62,3,'France Central','Europe','France'),
(63,3,'France South','Europe','France'),
(64,3,'Switzerland West','Europe','Suisse'),
(65,3,'Switzerland North','Europe','Suisse'),
(66,3,'Germany Central','Europe','Allemagne'),
(67,3,'Germany Northeast','Europe','Allemagne'),
(68,3,'Germany North','Europe','Allemagne'),
(69,3,'Germany West Central','Europe','Allemagne'),
(70,3,'Norway East','Europe','Norvège'),
(71,3,'South Africa West','Afrique','Afrique du Sud'),
(72,3,'South Africa North','Afrique','Afrique du Sud'),
(73,3,'UAE Central','Asie-Pacifique','Emirats Arabes Unis'),
(74,3,'UAE North','Asie-Pacifique','Emirats Arabes Unis'),
(75,3,'West India','Asie-Pacifique','Inde'),
(76,3,'Central India','Asie-Pacifique','Inde'),
(77,3,'South India','Asie-Pacifique','Inde'),
(78,3,'Southeast Asia','Asie-Pacifique','Singapour'),
(79,3,'China North','Asie-Pacifique','Chine'),
(80,3,'China North 2','Asie-Pacifique','Chine'),
(81,3,'Korea Central','Asie-Pacifique','Corée du Sud'),
(82,3,'Korea South','Asie-Pacifique','Corée du Sud'),
(83,3,'China East','Asie-Pacifique','Chine'),
(84,3,'China East 2','Asie-Pacifique','Chine'),
(85,3,'East Asia','Asie-Pacifique','Chine'),
(86,3,'Japan East','Asie-Pacifique','Japon'),
(87,3,'Japan West','Asie-Pacifique','Japon'),
(88,3,'Australia East','Asie-Pacifique','Australie'),
(89,3,'Australia Southeast','Asie-Pacifique','Australie'),
(90,3,'Australia Central','Asie-Pacifique','Australie'),
(91,3,'Australia Central 2','Asie-Pacifique','Australie');