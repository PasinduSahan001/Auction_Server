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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) NOT NULL,
  `Phone_Number` varchar(10) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Address` varchar(200) DEFAULT NULL,
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `Phone_Number_UNIQUE` (`Phone_Number`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Pasindu','Sahan','0774515356','pasindusahan001@gmail.com','1234',' 437/2 Palanwaththa, Pannipitiya'),(12,'Pasindu','Sahan','0112846301','pasindusahan10@gmail.com','123',NULL),(13,'Pasindu','Sahan','077451584','pasindusahan11@gmail.com','123',NULL),(17,'Pasindu_s','Sahan_s','123456789','pasindusahan12@gmail.com','123',NULL),(18,'Pasindu','Sahan','0774615356','pasindusahan13@gmail.com','123',NULL),(2,'Pasindu','Sahan_02','0774555556','pasindusahan2@gmail.com','123456',NULL),(5,'Pasindu','Sahan','0774555558','pasindusahan4@gmail.com','123456',NULL),(6,'Pasindu','Rathnayaka','0774555560','pasindusahan5@gmail.com','123','437/2  බයවුන පාර, ඇද යට'),(7,'Pasindu','Rathnayaka','0774555561','pasindusahan6@gmail.com','1234',NULL),(8,'Pasindu','Sahan_03','0774555567','pasindusahan7@gmail.com','1234',NULL),(9,'Pasindu','Sahan_04','0774555568','pasindusahan8@gmail.com','1234',NULL),(11,'Pasindu','Sahan','0774555517','pasindusahan9@gmail.com','123',NULL),(19,'shamika','konara','0778319011','shamika@gmail.com','123',NULL),(20,'shamika','konara','0778216673','shamikaaq@gmail.com','123',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-29 21:06:29
