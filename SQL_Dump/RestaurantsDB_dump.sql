-- MySQL dump 10.13  Distrib 9.0.1, for macos15.1 (arm64)
--
-- Host: localhost    Database: RestaurantsDB
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AppUser`
--

DROP TABLE IF EXISTS `AppUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AppUser` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `JoinDate` date DEFAULT NULL,
  `UserName` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppUser`
--

LOCK TABLES `AppUser` WRITE;
/*!40000 ALTER TABLE `AppUser` DISABLE KEYS */;
INSERT INTO `AppUser` VALUES (1,'2024-11-13','danimellok','dmello@chapman.edu');
/*!40000 ALTER TABLE `AppUser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `high_rated_restaurants`
--

DROP TABLE IF EXISTS `high_rated_restaurants`;
/*!50001 DROP VIEW IF EXISTS `high_rated_restaurants`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `high_rated_restaurants` AS SELECT 
 1 AS `RestaurantName`,
 1 AS `Country`,
 1 AS `City`,
 1 AS `Cuisine`,
 1 AS `MichelinRating`,
 1 AS `OverallRating`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `MenuItem`
--

DROP TABLE IF EXISTS `MenuItem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MenuItem` (
  `MenuItemID` int NOT NULL AUTO_INCREMENT,
  `DishName` varchar(100) DEFAULT NULL,
  `DishRating` int DEFAULT NULL,
  `Notes` text,
  `RestaurantID` int DEFAULT NULL,
  PRIMARY KEY (`MenuItemID`),
  KEY `RestaurantID` (`RestaurantID`),
  CONSTRAINT `menuitem_ibfk_1` FOREIGN KEY (`RestaurantID`) REFERENCES `Restaurant` (`RestaurantID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MenuItem`
--

LOCK TABLES `MenuItem` WRITE;
/*!40000 ALTER TABLE `MenuItem` DISABLE KEYS */;
/*!40000 ALTER TABLE `MenuItem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Restaurant`
--

DROP TABLE IF EXISTS `Restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Restaurant` (
  `RestaurantID` int NOT NULL AUTO_INCREMENT,
  `RestaurantName` varchar(100) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `Cuisine` varchar(100) DEFAULT NULL,
  `MichelinRating` int DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`RestaurantID`)
) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Restaurant`
--

LOCK TABLES `Restaurant` WRITE;
/*!40000 ALTER TABLE `Restaurant` DISABLE KEYS */;
INSERT INTO `Restaurant` VALUES (1,'Naga','Brazil','Sao Paulo','Japanese',NULL,2,1),(2,'Quintal Debetti','Brazil','Sao Paulo','Steakhouse',NULL,2,1),(3,'Le Jazz','Brazil','Sao Paulo','Italian',NULL,1,1),(4,'Huto Kohi','Brazil','Sao Paulo','Japanese',NULL,2,1),(5,'Marcearia Amauri','Brazil','Sao Paulo','French',NULL,2,1),(6,'Nino & Cucina','Brazil','Sao Paulo','Italian',NULL,2,1),(7,'Mug SP (brunch)','Brazil','Sao Paulo','Italian',NULL,2,1),(8,'Musa','Brazil','Sao Paulo','Japanese',NULL,2,1),(9,'Lá Serena','Brazil','Sao Paulo','Italian',NULL,2,1),(10,'Votre Brasserie (Pinheiros)','Brazil','Sao Paulo','French',NULL,2,1),(11,'Rooftop Fasano Hotel Itaim','Brazil','Sao Paulo','Brazilian',NULL,2,1),(12,'Giugiu (CJ Shops)','Brazil','Sao Paulo','Italian',NULL,2,1),(13,'Murakami','Brazil','Sao Paulo','Italian',NULL,2,1),(14,'Lido (Pinheiros)','Brazil','Sao Paulo','Italian',NULL,2,1),(15,'Restaurante Êze','Brazil','Sao Paulo','Japanese',NULL,2,1),(16,'Florio','Italy','Palermo','Italian',NULL,3,1),(17,'Kentia al Trapittu','Italy','Cefalu','Italian',NULL,3,1),(18,'Zagara','Italy','Sciacca','Mediterranean',NULL,1,1),(19,'Liola','Italy','Sciacca','Italian',NULL,1,1),(20,'Cinque Archi','Italy','Taormina','Seafood',NULL,3,1),(21,'Liola Osteria and Bar','Italy','Taormina','Italian',NULL,1,1),(22,'Bistrô du Monde','Italy','Taormina','Italian',NULL,1,1),(23,'Vila Sant’Andrea','Italy','Taormina','Italian',NULL,2,1),(24,'Teatro44','Italy','Taormina','Seafood',NULL,2,1),(25,'La Botte','Italy','Taormina','Italian',NULL,1,1),(26,'Area M','Italy','Siracusa','Seafood',NULL,2,1),(27,'Gusto Liberrima','Italy','Lecce','Italian',NULL,3,1),(28,'Doppiozero','Italy','Lecce','Italian',NULL,2,1),(29,'La Torre di Merlino','Italy','Lecce','Italian',NULL,2,1),(30,'Mora mora beach club','Italy','Lecce','Beach Club',NULL,1,1),(31,'Masseria Torricella','Italy','Alberobello','Seafood',NULL,2,1),(32,'Cala Masciola','Italy','Salvelletrri','Italian',NULL,2,1),(33,'La Frasca','Italy','Salvelletrri','Vegetarian',NULL,2,1),(34,'La Calce','Italy','Salvelletrri','Italian',NULL,1,1),(35,'Bancone','UK','London','Italian',NULL,2,1),(36,'The Italian Greyhound','UK','London','Italian',NULL,1,1),(37,'Berners Tavern','UK','London','British',NULL,1,1),(38,'VyTA','UK','London','Italian',NULL,1,1),(39,'Schwarzreiter Tagesbar & Restaurant','Germany','Munich','German',NULL,1,1),(40,'Matsuhisa','Germany','Munich','Japanese',NULL,2,1),(41,'L\'ATELIER ROBUCHON','Swizterland','Geneve','French',2,3,1),(42,'Il Lago','Swizterland','Geneve','Italian',1,2,1),(43,'Le Jardinier','Swizterland','Geneve','French',NULL,3,1),(44,'Flamel','Swizterland','Lugano','Italian',NULL,1,1),(45,'Tango','Swizterland','Lugano','Pizza/Bar',NULL,1,1),(46,'La Dispensa','Swizterland','Lugano','Italian',NULL,1,1),(47,'Crea','Swizterland','Lugano','Italian',NULL,2,1),(48,'Agua','Swizterland','Lugano','Italian',NULL,1,1),(49,'Baur’s Au Lac','Swizterland','Zurich','French',NULL,1,1),(50,'Le Raymond Bar','Swizterland','Zurich','Bar',NULL,1,1),(51,'La Stanza','Swizterland','Zurich','Bar',NULL,2,1),(52,'Old Inn','Swizterland','Zurich','Swiss',NULL,1,1),(53,'Bianchi','Swizterland','Zurich','Seafood',NULL,2,1),(54,'Ornellaia','Swizterland','Zurich','Italian',NULL,2,1),(55,'Bindella','Swizterland','Zurich','Italian',NULL,2,1),(56,'Savoy','Swizterland','Zurich','French',NULL,2,1),(57,'Zeughauskeller','Swizterland','Zurich','Swiss',NULL,1,1),(58,'Wild Bowl','Swizterland','Zurich','Japanese',NULL,1,1),(59,'Ona Poke','Swizterland','Zurich','Japanese',NULL,1,1),(60,'Moser’s','Swizterland','Zurich','Swiss',NULL,1,1),(61,'Haus am Fluss','Swizterland','Zurich','Bar',NULL,1,1),(62,'Bocuci','Swizterland','Zurich','Italian',NULL,2,1),(63,'Zunfthaus zur Waag','Swizterland','Zurich','Swiss',NULL,2,1),(64,'Edvard','Austria','Vienna','Austrian',1,3,1),(65,'OPUS','Austria','Vienna','French',1,1,1),(66,'Trattoria Martinelli','Austria','Vienna','Italian',NULL,2,1),(67,'A’Frisela','Austria','Vienna','Italian',NULL,1,1),(68,'Pastamara','Austria','Vienna','Italian',NULL,2,1),(69,'Fabios','Austria','Vienna','Italian',NULL,2,1),(70,'Meissl & Schadn','Austria','Vienna','Austrian',NULL,1,1),(71,'Le Bol','Austria','Vienna','Italian',NULL,1,1),(72,'Enoteca Cavaluccio','Austria','Vienna','Italian',NULL,2,1),(73,'Oberlaa','Austria','Vienna','Italian',NULL,2,1),(74,'Musset','France','Paris','French',NULL,1,1),(75,'Daroco','France','Paris','French',NULL,1,1),(76,'Le Maurice Alain Ducasse','France','Paris','French',2,2,1),(77,'Le Relais de l’Entrecôte','France','Paris','French',NULL,1,1),(78,'Saint Honoré Lock','France','Paris','French',NULL,2,1),(79,'Avenue','France','Paris','French',NULL,2,1),(80,'GB Roofgarden','Greece','Athenas','Mediterranean',NULL,2,1),(81,'Aleria','Greece','Athenas','Greek/Contemporary',NULL,2,1),(82,'Nobelos','Greece','Zakynthos','Greek',NULL,2,1),(83,'Nobile','Greece','Zakynthos','Greek',NULL,2,1),(84,'Banana Baya','Greece','Zakynthos','Beach Club',NULL,2,1),(85,'Narcissus','Greece','Mykonos','Italian',NULL,2,1),(86,'Remezzo','Greece','Mykonos','Greek/Contemporary',NULL,1,1),(87,'L’artirsta','Greece','Mykonos','Italian',NULL,1,1),(88,'S’perisma','Greece','Santorini','Greek',NULL,1,1),(89,'Nikki Beach','Greece','Santorini','Beach Club',NULL,1,1),(90,'FortyOne BeachClub','Greece','Santorini','Beach Club',NULL,1,1),(91,'Selene','Greece','Santorini','Greek/Contemporary',NULL,3,1),(92,'Sea side BeachClub','Greece','Santorini','Beach Club',NULL,1,1),(93,'Black Rock','Greece','Santorini','Greek',NULL,1,1),(94,'Fable & Spirit','United States','Newport','American',NULL,1,1),(95,'Oliver’s Osteria','United States','Laguna Beach','Italian',NULL,1,1),(96,'Lumiere','United States','Los Angeles','French',NULL,1,1),(97,'CUT by Wolfgang Puck','United States','Los Angeles','Steak',NULL,2,1),(98,'Zinc','United States','Newport','American',NULL,1,1),(99,'The Terrace at Maybourne','United States','Los Angeles','Italian',NULL,2,1),(100,'Osteria Mozza','United States','Los Angeles','Italian',NULL,1,1),(101,'Joey Newport Beach','United States','Newport','American',NULL,1,1),(102,'A Crystal Cove','United States','Newport','American',NULL,1,1),(103,'Sushi Roku','United States','Newport','Japanese',NULL,2,1),(104,'Bluefin','United States','Newport','Japanese',NULL,1,1),(105,'Selanne Steak','United States','Laguna Beach','Steak',NULL,2,1),(106,'A Restaurant','United States','Newport','Steak',NULL,1,1),(107,'Olivetta','United States','Los Angeles','Italian',NULL,2,1),(108,'Fiish','United States','Los Angeles','Japanese',NULL,1,1),(109,'Splashes Surf & Sand','United States','Laguna Beach','Seafood',NULL,1,1),(110,'The Capital Grill','United States','Costa Mesa','Steak',NULL,1,1),(111,'Polo Lounge at Beverly Hills Hotel','United States','Los Angeles','American',NULL,2,1),(112,'The Belvedere at The Peninsula','United States','Los Angeles','French',NULL,2,1),(113,'Jean-Georges Waldorf Beverly Hills','United States','Long Beach','French',NULL,2,1),(114,'Spago','United States','Los Angeles','American',NULL,2,1),(115,'The Little Door','United States','West Hollywood','French',NULL,2,1),(116,'The Restaurant at Hotel Bel-Air','United States','Los Angeles','American',NULL,1,1),(117,'Cecconi’s West Hollywood','United States','Los Angeles','Italian',NULL,2,1),(118,'Rothschild’s','United States','Corona Del Mar','Italian',NULL,1,1),(119,'Nobu','United States','Newport','Japanese',NULL,2,1),(120,'Rooftop Waldorf Astoria','United States','Los Angeles','American',NULL,2,1),(121,'Dantes','United States','Los Angeles','Bar',NULL,2,1),(122,'The Arthur J','United States','Manhattan Beach','Steak',NULL,1,1),(123,'Nando','United States','Manhattan Beach','Italian',NULL,2,1),(124,'Culina at Four Seasons Hotel','United States','Los Angeles','Italian',NULL,2,1),(125,'The Nice Guy','United States','Los Angeles','Italian/Bar',NULL,1,1),(126,'Nerano','United States','Beverly Hills','Italian',NULL,1,1),(127,'Pasjoli','United States','Santa Monica','French',NULL,1,1),(128,'Catch LA','United States','Los Angeles','Japanese/Steak',NULL,1,1),(129,'Chateau Marmont','United States','West Hollywood','American',NULL,1,1),(130,'Broadway','United States','Laguna','American',NULL,1,1),(131,'Ysabel','United States','West Hollywood','Italian',NULL,2,1),(132,'Camphor','United States','Los Angeles','French',NULL,2,1),(133,'Fig @ 313','United States','San Clemente','American',NULL,1,1),(134,'Mother Wolf','United States','West Hollywood','Italian',NULL,2,1),(135,'Cento','United States','Los Angeles','Italian',NULL,2,1),(136,'San Laurel','United States','Los Angeles','Spanish',NULL,2,1),(137,'Água Viva','United States','Los Angeles','Spanish',NULL,2,1),(138,'Stella','United States','West Hollywood','Italian',NULL,2,1),(139,'Sun Deck','United States','San Diego','Burger',NULL,1,1),(140,'The Desmond','United States','San Diego','Seafood',NULL,1,1),(141,'Catania','United States','San Diego','Italian',NULL,1,1),(142,'Cesarina','United States','San Diego','Italian',NULL,2,1),(143,'Birdseye','United States','San Diego','Burger',NULL,2,1),(144,'Asa Bakery','United States','San Diego','Bakery',NULL,1,1),(145,'Monsieur Benjamin','United States','San Fransico','French',NULL,1,1),(146,'Sierra Mar','United States','Big Sur','French',NULL,2,1),(147,'Stokes Adobe','United States','Monterey','French',NULL,2,1),(148,'Casanova','United States','Carmel','French',NULL,1,1),(149,'Chez Noir','United States','Carmel','Seafood',NULL,1,1),(150,'Tre Lune','United States','Montecito','Italian',NULL,1,1),(151,'Blackbird','United States','Santa Barbara','American',NULL,2,1),(152,'Caruso’s','United States','Montecito','Italian',NULL,2,1),(153,'Ca Dario','United States','Montecito','Italian',NULL,1,1),(154,'The Ritz Carlton - Countour','United States','New York City','Italian',NULL,1,1),(155,'Harry Cipriani','United States','New York City','Italian',NULL,2,1),(156,'Casa Lever','United States','New York City','Italian',NULL,1,1),(157,'Serafino','United States','New York City','Italian',NULL,1,1),(158,'Bryan Park Steakhouse','United States','New York City','Steak',NULL,1,1),(159,'Nurs-et','United States','New York City','Steak',NULL,2,1),(160,'Jean-George','United States','New York City','French',2,3,1),(161,'Majorelle','United States','New York City','French',1,2,1),(162,'Benoit','United States','New York City','French',NULL,2,1),(163,'Vicolina','United States','New York City','Italian',NULL,1,1),(164,'Il Gattopardo','United States','New York City','Italian',NULL,2,1),(165,'Fig & Olive','United States','New York City','American',NULL,1,1),(166,'Joe’s Pizza','United States','New York City','Pizza',NULL,2,1),(167,'Nubeluz rooftop','United States','New York City','Bar',NULL,2,1),(168,'Ralph’s coffee','United States','New York City','Coffee',NULL,1,1),(169,'Devoción','United States','New York City','Coffee',NULL,2,1),(170,'Cecconi’s Dumbo','United States','New York City','Italian',NULL,2,1),(171,'Le Jardinier','United States','New York City','French',NULL,3,1),(172,'Fasano','United States','New York City','Italian',NULL,2,1),(173,'Cipriani','United States','Las Vegas','Italian',NULL,2,1),(174,'Allegro','United States','Las Vegas','Italian',NULL,1,1),(175,'No.9 Park','United States','Boston','French',NULL,2,1),(176,'Taj Boston','United States','Boston','Italian',NULL,1,1),(177,'Zuma','United States','Miami','Japanese',NULL,2,1),(178,'Forte dei Marmi','United States','Miami','Italian/Seafood',NULL,2,1),(179,'Casatua','United States','Miami','Italian',NULL,2,1),(180,'Sant Ambroeus','United States','Miami','Italian',NULL,2,1),(181,'Renato’s','United States','Palm Beach','Italian',NULL,1,1),(182,'Lido Restaurant Four Seasons','United States','Palm Beach','Italian',NULL,2,1),(183,'LPM Restaurant','United States','Miami','French',NULL,2,1),(184,'Novikov','United States','Miami','Japanese',NULL,1,1),(187,'teste234','United States','Los Angeles','American',NULL,2,1);
/*!40000 ALTER TABLE `Restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Review` (
  `ReviewID` int NOT NULL AUTO_INCREMENT,
  `OveralRating` smallint DEFAULT NULL,
  `FoodRating` smallint DEFAULT NULL,
  `ServiceRating` smallint DEFAULT NULL,
  `VisitID` int DEFAULT NULL,
  PRIMARY KEY (`ReviewID`),
  KEY `VisitID` (`VisitID`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`VisitID`) REFERENCES `Visit` (`VisitID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Review`
--

LOCK TABLES `Review` WRITE;
/*!40000 ALTER TABLE `Review` DISABLE KEYS */;
INSERT INTO `Review` VALUES (1,2,NULL,NULL,1),(2,2,NULL,NULL,2),(3,1,NULL,NULL,3),(4,2,NULL,NULL,4),(5,2,NULL,NULL,5),(6,2,NULL,NULL,6),(7,2,NULL,NULL,7),(8,2,NULL,NULL,8),(9,2,NULL,NULL,9),(10,2,NULL,NULL,10),(11,2,NULL,NULL,11),(12,2,NULL,NULL,12),(13,2,NULL,NULL,13),(14,2,NULL,NULL,14),(15,2,NULL,NULL,15),(16,3,NULL,NULL,16),(17,3,NULL,NULL,17),(18,1,NULL,NULL,18),(19,1,NULL,NULL,19),(20,3,NULL,NULL,20),(21,1,NULL,NULL,21),(22,1,NULL,NULL,22),(23,2,NULL,NULL,23),(24,2,NULL,NULL,24),(25,1,NULL,NULL,25),(26,2,NULL,NULL,26),(27,3,NULL,NULL,27),(28,2,NULL,NULL,28),(29,2,NULL,NULL,29),(30,1,NULL,NULL,30),(31,2,NULL,NULL,31),(32,2,NULL,NULL,32),(33,2,NULL,NULL,33),(34,1,NULL,NULL,34),(35,2,NULL,NULL,35),(36,1,NULL,NULL,36),(37,1,NULL,NULL,37),(38,1,NULL,NULL,38),(39,1,NULL,NULL,39),(40,2,NULL,NULL,40),(41,3,NULL,NULL,41),(42,2,NULL,NULL,42),(43,3,NULL,NULL,43),(44,1,NULL,NULL,44),(45,1,NULL,NULL,45),(46,1,NULL,NULL,46),(47,2,NULL,NULL,47),(48,1,NULL,NULL,48),(49,1,NULL,NULL,49),(50,1,NULL,NULL,50),(51,2,NULL,NULL,51),(52,1,NULL,NULL,52),(53,2,NULL,NULL,53),(54,2,NULL,NULL,54),(55,2,NULL,NULL,55),(56,2,NULL,NULL,56),(57,1,NULL,NULL,57),(58,1,NULL,NULL,58),(59,1,NULL,NULL,59),(60,1,NULL,NULL,60),(61,1,NULL,NULL,61),(62,2,NULL,NULL,62),(63,2,NULL,NULL,63),(64,3,NULL,NULL,64),(65,1,NULL,NULL,65),(66,2,NULL,NULL,66),(67,1,NULL,NULL,67),(68,2,NULL,NULL,68),(69,2,NULL,NULL,69),(70,1,NULL,NULL,70),(71,1,NULL,NULL,71),(72,2,NULL,NULL,72),(73,2,NULL,NULL,73),(74,1,NULL,NULL,74),(75,1,NULL,NULL,75),(76,2,NULL,NULL,76),(77,1,NULL,NULL,77),(78,2,NULL,NULL,78),(79,2,NULL,NULL,79),(80,2,NULL,NULL,80),(81,2,NULL,NULL,81),(82,2,NULL,NULL,82),(83,2,NULL,NULL,83),(84,2,NULL,NULL,84),(85,2,NULL,NULL,85),(86,1,NULL,NULL,86),(87,1,NULL,NULL,87),(88,1,NULL,NULL,88),(89,1,NULL,NULL,89),(90,1,NULL,NULL,90),(91,3,NULL,NULL,91),(92,1,NULL,NULL,92),(93,1,NULL,NULL,93),(94,1,NULL,NULL,94),(95,1,NULL,NULL,95),(96,1,NULL,NULL,96),(97,2,NULL,NULL,97),(98,1,NULL,NULL,98),(99,2,NULL,NULL,99),(100,1,NULL,NULL,100),(101,1,NULL,NULL,101),(102,1,NULL,NULL,102),(103,2,NULL,NULL,103),(104,1,NULL,NULL,104),(105,2,NULL,NULL,105),(106,1,NULL,NULL,106),(107,2,NULL,NULL,107),(108,1,NULL,NULL,108),(109,1,NULL,NULL,109),(110,1,NULL,NULL,110),(111,2,NULL,NULL,111),(112,2,NULL,NULL,112),(113,2,NULL,NULL,113),(114,2,NULL,NULL,114),(115,2,NULL,NULL,115),(116,1,NULL,NULL,116),(117,2,NULL,NULL,117),(118,1,NULL,NULL,118),(119,2,NULL,NULL,119),(120,2,NULL,NULL,120),(121,2,NULL,NULL,121),(122,1,NULL,NULL,122),(123,2,NULL,NULL,123),(124,2,NULL,NULL,124),(125,1,NULL,NULL,125),(126,1,NULL,NULL,126),(127,1,NULL,NULL,127),(128,1,NULL,NULL,128),(129,1,NULL,NULL,129),(130,1,NULL,NULL,130),(131,2,NULL,NULL,131),(132,2,NULL,NULL,132),(133,1,NULL,NULL,133),(134,2,NULL,NULL,134),(135,2,NULL,NULL,135),(136,2,NULL,NULL,136),(137,2,NULL,NULL,137),(138,2,NULL,NULL,138),(139,1,NULL,NULL,139),(140,1,NULL,NULL,140),(141,1,NULL,NULL,141),(142,2,NULL,NULL,142),(143,2,NULL,NULL,143),(144,1,NULL,NULL,144),(145,1,NULL,NULL,145),(146,2,NULL,NULL,146),(147,2,NULL,NULL,147),(148,1,NULL,NULL,148),(149,1,NULL,NULL,149),(150,1,NULL,NULL,150),(151,2,NULL,NULL,151),(152,2,NULL,NULL,152),(153,1,NULL,NULL,153),(154,1,NULL,NULL,154),(155,2,NULL,NULL,155),(156,1,NULL,NULL,156),(157,1,NULL,NULL,157),(158,1,NULL,NULL,158),(159,2,NULL,NULL,159),(160,3,NULL,NULL,160),(161,2,NULL,NULL,161),(162,2,NULL,NULL,162),(163,1,NULL,NULL,163),(164,2,NULL,NULL,164),(165,1,NULL,NULL,165),(166,2,NULL,NULL,166),(167,2,NULL,NULL,167),(168,1,NULL,NULL,168),(169,2,NULL,NULL,169),(170,2,NULL,NULL,170),(171,3,NULL,NULL,171),(172,2,NULL,NULL,172),(173,2,NULL,NULL,173),(174,1,NULL,NULL,174),(175,2,NULL,NULL,175),(176,1,NULL,NULL,176),(177,2,NULL,NULL,177),(178,2,NULL,NULL,178),(179,2,NULL,NULL,179),(180,2,NULL,NULL,180),(181,1,NULL,NULL,181),(182,2,NULL,NULL,182),(183,2,NULL,NULL,183),(184,1,NULL,NULL,184),(187,2,3,2,187);
/*!40000 ALTER TABLE `Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visit`
--

DROP TABLE IF EXISTS `Visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Visit` (
  `VisitID` int NOT NULL AUTO_INCREMENT,
  `VisitDate` datetime DEFAULT NULL,
  `VisitPrice` decimal(10,2) DEFAULT NULL,
  `Reservation` varchar(50) DEFAULT NULL,
  `RestaurantID` int DEFAULT NULL,
  `UserID` int DEFAULT NULL,
  PRIMARY KEY (`VisitID`),
  KEY `UserID` (`UserID`),
  KEY `RestaurantID` (`RestaurantID`),
  CONSTRAINT `visit_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `AppUser` (`UserID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `visit_ibfk_2` FOREIGN KEY (`RestaurantID`) REFERENCES `Restaurant` (`RestaurantID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visit`
--

LOCK TABLES `Visit` WRITE;
/*!40000 ALTER TABLE `Visit` DISABLE KEYS */;
INSERT INTO `Visit` VALUES (1,NULL,NULL,NULL,1,1),(2,NULL,NULL,NULL,2,1),(3,NULL,NULL,NULL,3,1),(4,NULL,NULL,NULL,4,1),(5,NULL,NULL,NULL,5,1),(6,NULL,NULL,NULL,6,1),(7,NULL,NULL,NULL,7,1),(8,NULL,NULL,NULL,8,1),(9,NULL,NULL,NULL,9,1),(10,NULL,NULL,NULL,10,1),(11,NULL,NULL,NULL,11,1),(12,NULL,NULL,NULL,12,1),(13,NULL,NULL,NULL,13,1),(14,NULL,NULL,NULL,14,1),(15,NULL,NULL,NULL,15,1),(16,NULL,NULL,NULL,16,1),(17,NULL,NULL,NULL,17,1),(18,NULL,NULL,NULL,18,1),(19,NULL,NULL,NULL,19,1),(20,NULL,NULL,NULL,20,1),(21,NULL,NULL,NULL,21,1),(22,NULL,NULL,NULL,22,1),(23,NULL,NULL,NULL,23,1),(24,NULL,NULL,NULL,24,1),(25,NULL,NULL,NULL,25,1),(26,NULL,NULL,NULL,26,1),(27,NULL,NULL,NULL,27,1),(28,NULL,NULL,NULL,28,1),(29,NULL,NULL,NULL,29,1),(30,NULL,NULL,NULL,30,1),(31,NULL,NULL,NULL,31,1),(32,NULL,NULL,NULL,32,1),(33,NULL,NULL,NULL,33,1),(34,NULL,NULL,NULL,34,1),(35,NULL,NULL,NULL,35,1),(36,NULL,NULL,NULL,36,1),(37,NULL,NULL,NULL,37,1),(38,NULL,NULL,NULL,38,1),(39,NULL,NULL,NULL,39,1),(40,NULL,NULL,NULL,40,1),(41,NULL,NULL,NULL,41,1),(42,NULL,NULL,NULL,42,1),(43,NULL,NULL,NULL,43,1),(44,NULL,NULL,NULL,44,1),(45,NULL,NULL,NULL,45,1),(46,NULL,NULL,NULL,46,1),(47,NULL,NULL,NULL,47,1),(48,NULL,NULL,NULL,48,1),(49,NULL,NULL,NULL,49,1),(50,NULL,NULL,NULL,50,1),(51,NULL,NULL,NULL,51,1),(52,NULL,NULL,NULL,52,1),(53,NULL,NULL,NULL,53,1),(54,NULL,NULL,NULL,54,1),(55,NULL,NULL,NULL,55,1),(56,NULL,NULL,NULL,56,1),(57,NULL,NULL,NULL,57,1),(58,NULL,NULL,NULL,58,1),(59,NULL,NULL,NULL,59,1),(60,NULL,NULL,NULL,60,1),(61,NULL,NULL,NULL,61,1),(62,NULL,NULL,NULL,62,1),(63,NULL,NULL,NULL,63,1),(64,NULL,NULL,NULL,64,1),(65,NULL,NULL,NULL,65,1),(66,NULL,NULL,NULL,66,1),(67,NULL,NULL,NULL,67,1),(68,NULL,NULL,NULL,68,1),(69,NULL,NULL,NULL,69,1),(70,NULL,NULL,NULL,70,1),(71,NULL,NULL,NULL,71,1),(72,NULL,NULL,NULL,72,1),(73,NULL,NULL,NULL,73,1),(74,NULL,NULL,NULL,74,1),(75,NULL,NULL,NULL,75,1),(76,NULL,NULL,NULL,76,1),(77,NULL,NULL,NULL,77,1),(78,NULL,NULL,NULL,78,1),(79,NULL,NULL,NULL,79,1),(80,NULL,NULL,NULL,80,1),(81,NULL,NULL,NULL,81,1),(82,NULL,NULL,NULL,82,1),(83,NULL,NULL,NULL,83,1),(84,NULL,NULL,NULL,84,1),(85,NULL,NULL,NULL,85,1),(86,NULL,NULL,NULL,86,1),(87,NULL,NULL,NULL,87,1),(88,NULL,NULL,NULL,88,1),(89,NULL,NULL,NULL,89,1),(90,NULL,NULL,NULL,90,1),(91,NULL,NULL,NULL,91,1),(92,NULL,NULL,NULL,92,1),(93,NULL,NULL,NULL,93,1),(94,NULL,NULL,NULL,94,1),(95,NULL,NULL,NULL,95,1),(96,NULL,NULL,NULL,96,1),(97,NULL,NULL,NULL,97,1),(98,NULL,NULL,NULL,98,1),(99,NULL,NULL,NULL,99,1),(100,NULL,NULL,NULL,100,1),(101,NULL,NULL,NULL,101,1),(102,NULL,NULL,NULL,102,1),(103,NULL,NULL,NULL,103,1),(104,NULL,NULL,NULL,104,1),(105,NULL,NULL,NULL,105,1),(106,NULL,NULL,NULL,106,1),(107,NULL,NULL,NULL,107,1),(108,NULL,NULL,NULL,108,1),(109,NULL,NULL,NULL,109,1),(110,NULL,NULL,NULL,110,1),(111,NULL,NULL,NULL,111,1),(112,NULL,NULL,NULL,112,1),(113,NULL,NULL,NULL,113,1),(114,NULL,NULL,NULL,114,1),(115,NULL,NULL,NULL,115,1),(116,NULL,NULL,NULL,116,1),(117,NULL,NULL,NULL,117,1),(118,NULL,NULL,NULL,118,1),(119,NULL,NULL,NULL,119,1),(120,NULL,NULL,NULL,120,1),(121,NULL,NULL,NULL,121,1),(122,NULL,NULL,NULL,122,1),(123,NULL,NULL,NULL,123,1),(124,NULL,NULL,NULL,124,1),(125,NULL,NULL,NULL,125,1),(126,NULL,NULL,NULL,126,1),(127,NULL,NULL,NULL,127,1),(128,NULL,NULL,NULL,128,1),(129,NULL,NULL,NULL,129,1),(130,NULL,NULL,NULL,130,1),(131,NULL,NULL,NULL,131,1),(132,NULL,NULL,NULL,132,1),(133,NULL,NULL,NULL,133,1),(134,NULL,NULL,NULL,134,1),(135,NULL,NULL,NULL,135,1),(136,NULL,NULL,NULL,136,1),(137,NULL,NULL,NULL,137,1),(138,NULL,NULL,NULL,138,1),(139,NULL,NULL,NULL,139,1),(140,NULL,NULL,NULL,140,1),(141,NULL,NULL,NULL,141,1),(142,NULL,NULL,NULL,142,1),(143,NULL,NULL,NULL,143,1),(144,NULL,NULL,NULL,144,1),(145,NULL,NULL,NULL,145,1),(146,NULL,NULL,NULL,146,1),(147,NULL,NULL,NULL,147,1),(148,NULL,NULL,NULL,148,1),(149,NULL,NULL,NULL,149,1),(150,NULL,NULL,NULL,150,1),(151,NULL,NULL,NULL,151,1),(152,NULL,NULL,NULL,152,1),(153,NULL,NULL,NULL,153,1),(154,NULL,NULL,NULL,154,1),(155,NULL,NULL,NULL,155,1),(156,NULL,NULL,NULL,156,1),(157,NULL,NULL,NULL,157,1),(158,NULL,NULL,NULL,158,1),(159,NULL,NULL,NULL,159,1),(160,NULL,NULL,NULL,160,1),(161,NULL,NULL,NULL,161,1),(162,NULL,NULL,NULL,162,1),(163,NULL,NULL,NULL,163,1),(164,NULL,NULL,NULL,164,1),(165,NULL,NULL,NULL,165,1),(166,NULL,NULL,NULL,166,1),(167,NULL,NULL,NULL,167,1),(168,NULL,NULL,NULL,168,1),(169,NULL,NULL,NULL,169,1),(170,NULL,NULL,NULL,170,1),(171,NULL,NULL,NULL,171,1),(172,NULL,NULL,NULL,172,1),(173,NULL,NULL,NULL,173,1),(174,NULL,NULL,NULL,174,1),(175,NULL,NULL,NULL,175,1),(176,NULL,NULL,NULL,176,1),(177,NULL,NULL,NULL,177,1),(178,NULL,NULL,NULL,178,1),(179,NULL,NULL,NULL,179,1),(180,NULL,NULL,NULL,180,1),(181,NULL,NULL,NULL,181,1),(182,NULL,NULL,NULL,182,1),(183,NULL,NULL,NULL,183,1),(184,NULL,NULL,NULL,184,1),(187,'2024-11-15 00:00:00',323.00,'yes',187,1);
/*!40000 ALTER TABLE `Visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `high_rated_restaurants`
--

/*!50001 DROP VIEW IF EXISTS `high_rated_restaurants`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `high_rated_restaurants` AS select `restaurant`.`RestaurantName` AS `RestaurantName`,`restaurant`.`Country` AS `Country`,`restaurant`.`City` AS `City`,`restaurant`.`Cuisine` AS `Cuisine`,`restaurant`.`MichelinRating` AS `MichelinRating`,avg(`review`.`OveralRating`) AS `OverallRating` from ((`restaurant` left join `visit` on((`restaurant`.`RestaurantID` = `visit`.`RestaurantID`))) left join `review` on((`visit`.`VisitID` = `review`.`VisitID`))) where (`restaurant`.`MichelinRating` is not null) group by `restaurant`.`RestaurantID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-16 12:58:27
