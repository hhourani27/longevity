DELETE FROM storage_asset_history;
DELETE FROM storage_asset;
DELETE FROM storage_strategy;
DELETE FROM storage_data_location;
DELETE FROM storage_data_provider;
DELETE FROM digital_asset_history;
DELETE FROM digital_asset;
DELETE FROM collection;
DELETE FROM user;
DELETE FROM organisation;

DELETE FROM country;
DELETE FROM format;

INSERT INTO organisation(id,name)
VALUES
	(1,'Institut Bergerac');

INSERT INTO user (id,username,email,first_name,last_name,password_hash,organisation_id)
VALUES
	(1,'habib','h.hourany@gmail.com','Habib','El Hourani','pbkdf2:sha256:150000$BUabOlFq$efd6e49727596d8522bc1759bdaa4dccaffdc50e2e645dd962ebf8a5bf5413fd',1);


INSERT INTO format(id,media,name,version)
VALUES
	(1,'image','jpeg',''),
	(2,'image','png',''),
	(3,'text','pdf','A-3'),
	(4,'audio','ogg','');

INSERT INTO country(id,name,region,ind_fragile_state_index,ind_ict_dev_index,ind_hdi)
VALUES
	(1,'Afrique du Sud','Afrique','71.1','4.96','0.705'),
	(2,'Allemagne','Europe','24.7','8.39','0.939'),
	(3,'Australie','Europe','19.7','8.24','0.938'),
	(4,'Bahrain','Asie-Pacifique','63.8','7.6','0.838'),
	(5,'Belgique','Europe','28.6','7.81','0.919'),
	(6,'Brésil','Amérique du Sud','71.8','6.12','0.761'),
	(7,'Canada','Amérique du Nord','20','7.93','0.922'),
	(8,'Chine','Asie-Pacifique','71.1','7.83','0.758'),
	(9,'Corée du Sud','Asie-Pacifique','33.7','8.85','0.906'),
	(10,'Emirats Arabes Unis','Asie-Pacifique','40.1','7.21','0.866'),
	(11,'Etats-Unis','Amérique du Nord','38','8.18','0.92'),
	(12,'Finlande','Europe','16.9','7.88','0.925'),
	(13,'France','Europe','32','8.24','0.891'),
	(14,'Grande-Bretagne','Europe','36.7','8.65','0.92'),
	(15,'Hong Kong','Asie-Pacifique','52.4','8.61','0.939'),
	(16,'Inde','Asie-Pacifique','74.4','3.03','0.647'),
	(17,'Irlande','Europe','20.6','8.02','0.942'),
	(18,'Japon','Asie-Pacifique','34.3','8.43','0.915'),
	(19,'Norvège','Europe','18','8.45','0.954'),
	(20,'Pays-Bas','Europe','24.8','8.4','0.933'),
	(21,'Singapour','Asie-Pacifique','28.1','7.85','0.935'),
	(22,'Suède','Europe','20.3','8.41','0.937'),
	(23,'Suisse','Europe','18.7','8.66','0.946'),
	(24,'Taïwan','Asie-Pacifique','61.1','7.8','0.923');


INSERT INTO storage_data_provider(id,name,ind_current_ratio,ind_quick_ratio,ind_return_on_assets,ind_accounts_receivable_turnover_ratio,ind_operating_cash_flow_ratio,ind_pretax_net_profit_margin,ind_inventory_turnover,description)
VALUES
	(1,'Amazon','3.27','5.97','0.8','0.46','0.57','0.95','57.7',"(NASDAQ : AMZN4) est une entreprise de commerce électronique américaine basée à Seattle. Elle est un des géants du Web, regroupés sous l'acronyme GAFAM5, aux côtés de Google, Apple, Facebook et Microsoft."),
	(2,'Google','3.35','3.37','0.14','0.14','0.04','0.21','68.28',"est une entreprise américaine de services technologiques fondée en 1998 dans la Silicon Valley, en Californie, par Larry Page et Sergey Brin, créateurs du moteur de recherche Google."),
	(3,'Microsoft','2.53','5.39','0.98','0.37','0.03','0.56','44.68',"est une multinationale informatique et micro-informatique américaine, fondée en 1975 par Bill Gates et Paul Allen. Microsoft est la première capitalisation boursière du NASDAQ. En 2018, le chiffre d'affaires s’élevait à 110,36 milliards de dollars.");

	
INSERT INTO storage_data_location(id,data_provider_id,name,country_id,longitude,latitude)
VALUES
(1,1,'US East (Ohio)',11,'-82.9','39.9'),
(2,1,'US East (N. Virginia)',11,'-77.4','37.5'),
(3,1,'US West (N. California)',11,'-121.5','38.6'),
(4,1,'US West (Oregon)',11,'-122.7','45.5'),
(5,1,'Asia Pacific (Hong Kong)',15,'114','22'),
(6,1,'Asia Pacific (Mumbai)',16,'73','19'),
(7,1,'Asia Pacific (Osaka-Local)',18,'136','35'),
(8,1,'Asia Pacific (Seoul)',9,'127','37'),
(9,1,'Asia Pacific (Singapore)',21,'103.7','1.4'),
(10,1,'Asia Pacific (Sydney)',3,'151','-34'),
(11,1,'Asia Pacific (Tokyo)',18,'140','36'),
(12,1,'Canada (Central)',7,'-99','52'),
(13,1,'Europe (Frankfurt)',2,'9','50'),
(14,1,'Europe (Ireland)',17,'-7','53'),
(15,1,'Europe (London)',14,'-0.4','51'),
(16,1,'Europe (Paris)',13,'3','49'),
(17,1,'Europe (Stockholm)',22,'18','60'),
(18,1,'Middle East (Bahrain)',4,'50.5','25.9'),
(19,1,'South America (São Paulo)',6,'-46','-23'),
(20,2,'NORTHAMERICA-NORTHEAST1',7,'-66','46'),
(21,2,'US-CENTRAL1',11,'-97','42'),
(22,2,'US-EAST1',11,'-74','42'),
(23,2,'US-EAST4',11,'-77','40'),
(24,2,'US-WEST1',11,'-122','41'),
(25,2,'US-WEST2',11,'-116','34'),
(26,2,'SOUTHAMERICA-EAST1',6,'-41','-14'),
(27,2,'EUROPE-NORTH1',12,'25','61'),
(28,2,'EUROPE-WEST1',5,'4','51'),
(29,2,'EUROPE-WEST2',14,'-1.5','52'),
(30,2,'EUROPE-WEST3',2,'7','50'),
(31,2,'EUROPE-WEST4',20,'5.3','52'),
(32,2,'EUROPE-WEST6',23,'8','47'),
(33,2,'ASIA-EAST1',24,'121','24'),
(34,2,'ASIA-EAST2',15,'114','22'),
(35,2,'ASIA-NORTHEAST1',18,'139','36'),
(36,2,'ASIA-NORTHEAST2',18,'134','35'),
(37,2,'ASIA-SOUTH1',16,'78','11'),
(38,2,'ASIA-SOUTHEAST1',21,'103.7','1.4'),
(39,2,'AUSTRALIA-SOUTHEAST1',3,'150','-36'),
(40,3,'Canada East',7,'-73','47'),
(41,3,'Canada Central',7,'-113','55'),
(42,3,'US Gov Iowa',11,'-93.2','41.8'),
(43,3,'Central US',11,'-92','37'),
(44,3,'North Central US',11,'-93','47'),
(45,3,'US DoD East',11,'-78','37'),
(46,3,'East US',11,'-70','44'),
(47,3,'East US 2',11,'-72','42'),
(48,3,'US Gov Virginia',11,'-77.8','37.7'),
(49,3,'US DoD Central',11,'-100','38'),
(50,3,'West US 2',11,'-119','39'),
(51,3,'West Central US',11,'-109','40'),
(52,3,'West US',11,'-123','40'),
(53,3,'US Gov Arizona',11,'-111.9','33.8'),
(54,3,'South Central US',11,'-98','35'),
(55,3,'US Gov Texas',11,'-97.8','23'),
(56,3,'Brazil South',6,'-53','-31'),
(57,3,'Norway West',19,'6','60'),
(58,3,'West Europe',20,'5.4','52'),
(59,3,'UK South',14,'-1.8','51'),
(60,3,'North Europe',17,'-9','52'),
(61,3,'UK West',14,'-4','52'),
(62,3,'France Central',13,'2','47'),
(63,3,'France South',13,'3','44'),
(64,3,'Switzerland West',23,'7','47'),
(65,3,'Switzerland North',23,'8','47'),
(66,3,'Germany Central',2,'11','52'),
(67,3,'Germany Northeast',2,'8','53'),
(68,3,'Germany North',2,'11','54'),
(69,3,'Germany West Central',2,'9','49'),
(70,3,'Norway East',19,'11','60'),
(71,3,'South Africa West',1,'19','-33'),
(72,3,'South Africa North',1,'28','-26'),
(73,3,'UAE Central',10,'55','24'),
(74,3,'UAE North',10,'56','25'),
(75,3,'West India',16,'74','17'),
(76,3,'Central India',16,'78','20'),
(77,3,'South India',16,'77','11'),
(78,3,'Southeast Asia',21,'103.7','1.4'),
(79,3,'China North',8,'115','39'),
(80,3,'China North 2',8,'118','37'),
(81,3,'Korea Central',9,'128','36'),
(82,3,'Korea South',9,'127','35'),
(83,3,'China East',8,'121','30'),
(84,3,'China East 2',8,'120','28'),
(85,3,'East Asia',8,'115','23'),
(86,3,'Japan East',18,'140','37'),
(87,3,'Japan West',18,'131','33'),
(88,3,'Australia East',3,'151','-31'),
(89,3,'Australia Southeast',3,'148','-37'),
(90,3,'Australia Central',3,'132','-29'),
(91,3,'Australia Central 2',3,'133','-24');


INSERT INTO collection(id,name,description,organisation_id)
VALUES
	(1,'Manuscripts de Caedmon','Collection contenant les Manuscripts de Caedmon', 1),
	(2,'Apocalypse flamande','Collection contenant Apocalypse flamande', 1);


INSERT INTO storage_strategy(id,collection_id,strategy)
VALUES
	(1,1,'{"strategy":{"level":1,"redundancy":{"provider":0,"location":0},"regions":["Europe","Amérique du Nord"]},"instance":{"storage_locations":[{"id":16,"region":"","country":"","provider":{"id":1,"name":""}},{"id":27,"region":"","country":"","provider":{"id":2,"name":""}},{"id":86,"region":"","country":"","provider":{"id":3,"name":""}}]}}'),
	(2,2,'{"strategy":{"level":1,"redundancy":{"provider":0,"location":0},"regions":["Europe","Amérique du Nord"]},"instance":{"storage_locations":[{"id":17,"region":"","country":"","provider":{"id":1,"name":""}},{"id":66,"region":"","country":"","provider":{"id":3,"name":""}}]}}')