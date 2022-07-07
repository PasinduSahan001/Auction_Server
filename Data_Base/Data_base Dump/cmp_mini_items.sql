-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.3    Database: cmp_mini
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_owner_id` int DEFAULT NULL,
  `item_image_link` varchar(150) DEFAULT NULL,
  `item_title` varchar(50) DEFAULT NULL,
  `item_category` varchar(45) DEFAULT NULL,
  `item_base_price` double DEFAULT NULL,
  `item_expiry_date` datetime DEFAULT NULL,
  `item_main_details` varchar(34) DEFAULT NULL,
  `item_details` text,
  `item_buyer` varchar(45) DEFAULT NULL,
  `item_sold_price` double DEFAULT NULL,
  `item_status` varchar(10) DEFAULT NULL,
  `time_extended` varchar(10) DEFAULT NULL,
  `priority` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  UNIQUE KEY `item_id_UNIQUE` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (73,1,'static\\image\\01.png','Ancient House','Residential',690000,'2022-01-15 15:46:35','Old Is Gold','Needs to be maintained','6',690002,'Sold','FALSE','Special'),(74,1,'static\\image\\02.png','Green House','Residential',6900000,'2022-01-28 00:00:00','3 Rooms And 1 Kitchen','If you like to enjoy your life. This is the right place for it. ','6',6900017,'Sold','FALSE','Normal'),(75,1,'static\\image\\03.png','White House','Residential',6200000,'2022-01-29 00:00:00','2 Rooms And 1 Kitchen','If you want to live your life happily, This is the right place for it.','1',NULL,'Expired','FALSE','Normal'),(76,1,'static\\image\\04.png','White House_02','Residential',6900000,'2022-01-30 00:00:00','3 Rooms And 1 Kitchen','If you want to live your life happily, This is the right place for it.',NULL,NULL,'Available','FALSE','Normal'),(77,1,'static\\image\\07.png','Natural Land','Raw Land',1900000,'2022-01-31 00:00:00','Natural Land','This is a suitable landscape for making a hotel.',NULL,NULL,'Available','FALSE','Normal'),(78,1,'static\\image\\08.png','Krajobraz Land','Raw Land',3500000,'2022-02-01 00:00:00','Land With Beautiful Sunrise','This is suitable land to build a farm.',NULL,NULL,'Available','FALSE','Normal'),(79,6,'static\\image\\09.png','Oetscher Land','Raw Land',6900000,'2022-02-02 00:00:00','Natural Land','This is suitable land to build a hotel.',NULL,NULL,'Available','FALSE','Normal'),(80,6,'static\\image\\10.png','Romanian Land','Raw Land',10000000,'2022-02-03 00:00:00','Natural Land','Natural Land With beautiful Lanscape',NULL,NULL,'Available','FALSE','Normal'),(81,6,'static\\image\\11.png','Horror House','Residential',100000,'2022-10-31 18:50:43','Holman Godaai','Include Mohini And Mahasona, ft',NULL,NULL,'Available','FALSE','Normal'),(82,6,'static\\image\\12.png','Tea Factory','Commercial',4000000000,'2022-01-15 19:00:22','ඩොලර් උල්පත','ඩොලර් ලංකාවට ගේන සුපිරිම ක්‍රමය. ගන්න කෙනා තමයි හොදටම කරන්නෙ.',NULL,NULL,'Expired','FALSE','Special'),(83,1,'static\\image\\13.png','Land_Testing_01','Raw Land',1000000,'2022-02-04 00:00:00','Natural Landscape','If you want to live your life happily, This is the right place for it.',NULL,NULL,'Available','FALSE','Normal'),(88,1,'static\\image\\14.png','house','Residential',690000,'2022-01-30 00:00:00','3 Rooms And 1 Kitchen','Well maintained ',NULL,NULL,'Available','FALSE','Normal'),(89,1,'static\\image\\15.png','House 01','Residential',320000,'2022-01-27 21:09:52','4 Rooms And 1 Kitchen','Well maintained ',NULL,NULL,'Expired','FALSE','Special'),(90,1,'static\\image\\14.png','House 03','Residential',100000,'2022-01-27 03:26:49','4 Rooms And 1 Kitchen','Well maintained ',NULL,NULL,'Expired','FALSE','Special');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-29 21:06:28
