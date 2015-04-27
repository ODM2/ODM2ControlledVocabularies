-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: jws.uwrl.usu.edu    Database: odmcvsconfig
-- ------------------------------------------------------
-- Server version	5.5.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add api access',7,'add_apiaccess'),(20,'Can change api access',7,'change_apiaccess'),(21,'Can delete api access',7,'delete_apiaccess'),(22,'Can add api key',8,'add_apikey'),(23,'Can change api key',8,'change_apikey'),(24,'Can delete api key',8,'delete_apikey'),(25,'Can add Action Type Control Vocabulary',9,'add_actiontype'),(26,'Can change Action Type Control Vocabulary',9,'change_actiontype'),(27,'Can delete Action Type Control Vocabulary',9,'delete_actiontype'),(28,'Can add Action Type CV Request',10,'add_actiontyperequest'),(29,'Can change Action Type CV Request',10,'change_actiontyperequest'),(30,'Can delete Action Type CV Request',10,'delete_actiontyperequest'),(31,'Can add Method Type Control Vocabulary',11,'add_methodtype'),(32,'Can change Method Type Control Vocabulary',11,'change_methodtype'),(33,'Can delete Method Type Control Vocabulary',11,'delete_methodtype'),(34,'Can add Method Type CV Request',12,'add_methodtyperequest'),(35,'Can change Method Type CV Request',12,'change_methodtyperequest'),(36,'Can delete Method Type CV Request',12,'delete_methodtyperequest'),(37,'Can add Organization Type Control Vocabulary',13,'add_organizationtype'),(38,'Can change Organization Type Control Vocabulary',13,'change_organizationtype'),(39,'Can delete Organization Type Control Vocabulary',13,'delete_organizationtype'),(40,'Can add Organization Type CV Request',14,'add_organizationtyperequest'),(41,'Can change Organization Type CV Request',14,'change_organizationtyperequest'),(42,'Can delete Organization Type CV Request',14,'delete_organizationtyperequest'),(43,'Can add Sampling Feature Geo-type CV',15,'add_samplingfeaturegeotype'),(44,'Can change Sampling Feature Geo-type CV',15,'change_samplingfeaturegeotype'),(45,'Can delete Sampling Feature Geo-type CV',15,'delete_samplingfeaturegeotype'),(46,'Can add Sampling Feature Geo-type CV Request',16,'add_samplingfeaturegeotyperequest'),(47,'Can change Sampling Feature Geo-type CV Request',16,'change_samplingfeaturegeotyperequest'),(48,'Can delete Sampling Feature Geo-type CV Request',16,'delete_samplingfeaturegeotyperequest'),(49,'Can add Sampling Feature Type CV',17,'add_samplingfeaturetype'),(50,'Can change Sampling Feature Type CV',17,'change_samplingfeaturetype'),(51,'Can delete Sampling Feature Type CV',17,'delete_samplingfeaturetype'),(52,'Can add Sampling Feature Type CV Request',18,'add_samplingfeaturetyperequest'),(53,'Can change Sampling Feature Type CV Request',18,'change_samplingfeaturetyperequest'),(54,'Can delete Sampling Feature Type CV Request',18,'delete_samplingfeaturetyperequest'),(55,'Can add Site Type Control Vocabulary',19,'add_sitetype'),(56,'Can change Site Type Control Vocabulary',19,'change_sitetype'),(57,'Can delete Site Type Control Vocabulary',19,'delete_sitetype'),(58,'Can add Site Type CV Request',20,'add_sitetyperequest'),(59,'Can change Site Type CV Request',20,'change_sitetyperequest'),(60,'Can delete Site Type CV Request',20,'delete_sitetyperequest'),(61,'Can add namespace',21,'add_namespace'),(62,'Can change namespace',21,'change_namespace'),(63,'Can delete namespace',21,'delete_namespace'),(64,'Can add node',22,'add_node'),(65,'Can change node',22,'change_node'),(66,'Can delete node',22,'delete_node'),(67,'Can add field relation',23,'add_fieldrelation'),(68,'Can change field relation',23,'change_fieldrelation'),(69,'Can delete field relation',23,'delete_fieldrelation'),(70,'Can add scheme',24,'add_scheme'),(71,'Can change scheme',24,'change_scheme'),(72,'Can delete scheme',24,'delete_scheme');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$QnvBt3Hv9XtG$hS2l1DGzP33WTWxGj4RrrrTVO2HEpwLYr0Uw5kk1h6Y=','2015-02-24 23:25:42',1,'Juan','','','juan.caraballo17@gmail.com',1,1,'2015-02-24 23:24:19'),(2,'pbkdf2_sha256$15000$5G2ha2Gz47WF$6SJcQQie6oTy/F/dzbburw/f1BWTRODuLkuYwpjeRGg=','2015-03-16 19:49:14',1,'Denver','','','',1,1,'2015-02-24 23:26:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=187 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-02-24 23:26:06','2','Denver',1,'',4,1),(2,'2015-02-24 23:26:22','2','Denver',2,'Changed is_staff and is_superuser.',4,1),(3,'2015-02-24 23:29:55','8','skos:Concept',1,'',22,2),(4,'2015-02-24 23:30:03','8','skos:Concept->term',1,'',23,2),(5,'2015-02-24 23:30:20','7','odm2:producesResult->produces_result',2,'Changed field_name.',23,2),(6,'2015-02-24 23:30:37','5','skos:exactMatch->provenance_uri',2,'Changed field_name.',23,2),(7,'2015-02-24 23:30:53','1','skos:prefLabel->name',2,'Changed field_name.',23,2),(8,'2015-02-24 23:31:29','dc','dc',1,'',21,2),(9,'2015-02-24 23:31:59','odm2','odm2',2,'Changed reference.',21,2),(10,'2015-02-24 23:32:31','9','skos:inScheme',1,'',22,2),(11,'2015-02-25 00:01:55','actionTypeCV','actionTypeCV',2,'Changed creator.',24,2),(12,'2015-02-26 21:26:30','methodTypeCV','methodTypeCV',1,'',24,2),(13,'2015-02-26 21:27:10','methodTypeCV','methodTypeCV',2,'Changed description and uri.',24,2),(14,'2015-02-26 21:30:47','organizationTypeCV','organizationTypeCV',1,'',24,2),(15,'2015-02-26 21:34:18','samplingFeatureGeotypeCV','samplingFeatureGeotypeCV',1,'',24,2),(16,'2015-02-26 21:34:44','samplingFeatureGeotypeCV','samplingFeatureGeotypeCV',2,'Changed uri.',24,2),(17,'2015-02-26 21:38:22','samplingFeatureTypeCV','samplingFeatureTypeCV',1,'',24,2),(18,'2015-02-26 21:41:46','siteTypeCV','siteTypeCV',1,'',24,2),(19,'2015-02-26 22:06:16','organizationTypeCV','organizationTypeCV',2,'Changed uri.',24,2),(20,'2015-02-26 22:41:27','siteTypeCV','siteTypeCV',2,'Changed title.',24,2),(21,'2015-02-26 22:46:38','aggregationStatisticCV','aggregationStatisticCV',1,'',24,2),(22,'2015-02-26 22:47:06','aggregationStatisticCV','aggregationStatisticCV',2,'Changed uri.',24,2),(23,'2015-02-26 22:48:01','annotationTypeCV','annotationTypeCV',1,'',24,2),(24,'2015-02-26 22:48:47','annotationTypeCV','annotationTypeCV',2,'Changed uri.',24,2),(25,'2015-02-26 22:49:08','aggregationStatisticCV','aggregationStatisticCV',2,'Changed uri.',24,2),(26,'2015-02-26 22:50:18','censorCodeCV','censorCodeCV',1,'',24,2),(27,'2015-02-26 22:51:46','datasetTypeCV','datasetTypeCV',1,'',24,2),(28,'2015-02-26 22:53:04','directiveTypeCV','directiveTypeCV',1,'',24,2),(29,'2015-02-26 22:54:26','elevationDatumCV','elevationDatumCV',1,'',24,2),(30,'2015-02-26 22:55:26','equipmentTypeCV','equipmentTypeCV',1,'',24,2),(31,'2015-02-26 22:56:32','propertyDataTypeCV','propertyDataTypeCV',1,'',24,2),(32,'2015-02-26 22:59:07','qualityCodeCV','qualityCodeCV',2,'Changed name, title and uri.',24,2),(33,'2015-02-26 23:00:21','referenceMaterialMediumCV','referenceMaterialMediumCV',1,'',24,2),(34,'2015-02-26 23:02:01','resultTypeCV','resultTypeCV',1,'',24,2),(35,'2015-02-26 23:03:19','sampledMediumCV','sampledMediumCV',1,'',24,2),(36,'2015-02-26 23:05:07','spatialOffsetTypeCV','spatialOffsetTypeCV',1,'',24,2),(37,'2015-02-26 23:06:27','speciationCV','speciationCV',1,'',24,2),(38,'2015-02-26 23:07:28','specimenMediumCV','specimenMediumCV',1,'',24,2),(39,'2015-02-26 23:08:29','specimenTypeCV','specimenTypeCV',1,'',24,2),(40,'2015-02-26 23:10:11','statusCV','statusCV',1,'',24,2),(41,'2015-02-26 23:11:16','taxonomicClassifierTypeCV','taxonomicClassifierTypeCV',1,'',24,2),(42,'2015-02-26 23:12:20','variableNameCV','variableNameCV',1,'',24,2),(43,'2015-02-26 23:13:39','variableTypeCV','variableTypeCV',1,'',24,2),(44,'2015-02-27 23:38:14','odm2','odm2',2,'Changed reference.',21,2),(45,'2015-02-27 23:41:41','actionTypeCV','actionTypeCV',2,'Changed uri.',24,2),(46,'2015-02-27 23:43:33','aggregationStatisticCV','aggregationStatisticCV',2,'Changed uri.',24,2),(47,'2015-02-27 23:43:56','annotationTypeCV','annotationTypeCV',2,'Changed uri.',24,2),(48,'2015-02-27 23:44:05','censorCodeCV','censorCodeCV',2,'Changed uri.',24,2),(49,'2015-02-27 23:44:16','datasetTypeCV','datasetTypeCV',2,'Changed uri.',24,2),(50,'2015-02-27 23:44:29','directiveTypeCV','directiveTypeCV',2,'Changed uri.',24,2),(51,'2015-02-27 23:44:36','elevationDatumCV','elevationDatumCV',2,'Changed uri.',24,2),(52,'2015-02-27 23:44:45','equipmentTypeCV','equipmentTypeCV',2,'Changed uri.',24,2),(53,'2015-02-27 23:44:58','methodTypeCV','methodTypeCV',2,'Changed uri.',24,2),(54,'2015-02-27 23:45:06','organizationTypeCV','organizationTypeCV',2,'Changed uri.',24,2),(55,'2015-02-27 23:45:15','propertyDataTypeCV','propertyDataTypeCV',2,'Changed uri.',24,2),(56,'2015-02-27 23:45:23','qualityCodeCV','qualityCodeCV',2,'Changed uri.',24,2),(57,'2015-02-27 23:45:31','referenceMaterialMediumCV','referenceMaterialMediumCV',2,'Changed uri.',24,2),(58,'2015-02-27 23:45:40','resultTypeCV','resultTypeCV',2,'Changed uri.',24,2),(59,'2015-02-27 23:45:57','sampledMediumCV','sampledMediumCV',2,'Changed uri.',24,2),(60,'2015-02-27 23:46:05','samplingFeatureGeotypeCV','samplingFeatureGeotypeCV',2,'Changed uri.',24,2),(61,'2015-02-27 23:46:25','samplingFeatureTypeCV','samplingFeatureTypeCV',2,'Changed uri.',24,2),(62,'2015-02-27 23:46:43','siteTypeCV','siteTypeCV',2,'Changed uri.',24,2),(63,'2015-02-27 23:46:53','spatialOffsetTypeCV','spatialOffsetTypeCV',2,'Changed uri.',24,2),(64,'2015-02-27 23:47:07','speciationCV','speciationCV',2,'Changed uri.',24,2),(65,'2015-02-27 23:47:14','specimenMediumCV','specimenMediumCV',2,'Changed uri.',24,2),(66,'2015-02-27 23:47:28','specimenTypeCV','specimenTypeCV',2,'Changed uri.',24,2),(67,'2015-02-27 23:47:44','statusCV','statusCV',2,'Changed uri.',24,2),(68,'2015-02-27 23:47:52','taxonomicClassifierTypeCV','taxonomicClassifierTypeCV',2,'Changed uri.',24,2),(69,'2015-02-27 23:47:58','variableNameCV','variableNameCV',2,'Changed uri.',24,2),(70,'2015-02-27 23:48:06','variableTypeCV','variableTypeCV',2,'Changed uri.',24,2),(71,'2015-03-03 23:48:38','variableTypeCV','variableTypeCV',2,'Changed description.',24,2),(72,'2015-03-03 23:49:47','variableNameCV','variableNameCV',2,'Changed description.',24,2),(73,'2015-03-03 23:50:17','taxonomicClassifierTypeCV','taxonomicClassifierTypeCV',2,'Changed description.',24,2),(74,'2015-03-03 23:50:31','statusCV','statusCV',2,'Changed description.',24,2),(75,'2015-03-03 23:50:44','specimenTypeCV','specimenTypeCV',2,'Changed description.',24,2),(76,'2015-03-03 23:50:57','specimenMediumCV','specimenMediumCV',2,'Changed description.',24,2),(77,'2015-03-03 23:51:13','speciationCV','speciationCV',2,'Changed description.',24,2),(78,'2015-03-03 23:51:32','spatialOffsetTypeCV','spatialOffsetTypeCV',2,'Changed description.',24,2),(79,'2015-03-03 23:51:44','siteTypeCV','siteTypeCV',2,'Changed description.',24,2),(80,'2015-03-03 23:52:11','samplingFeatureTypeCV','samplingFeatureTypeCV',2,'Changed description.',24,2),(81,'2015-03-03 23:52:16','samplingFeatureGeotypeCV','samplingFeatureGeotypeCV',2,'Changed description.',24,2),(82,'2015-03-03 23:53:25','sampledMediumCV','sampledMediumCV',2,'Changed description.',24,2),(83,'2015-03-03 23:53:46','resultTypeCV','resultTypeCV',2,'Changed description.',24,2),(84,'2015-03-03 23:54:13','referenceMaterialMediumCV','referenceMaterialMediumCV',2,'Changed description.',24,2),(85,'2015-03-03 23:54:31','qualityCodeCV','qualityCodeCV',2,'Changed description.',24,2),(86,'2015-03-03 23:54:45','propertyDataTypeCV','propertyDataTypeCV',2,'Changed description.',24,2),(87,'2015-03-03 23:56:43','organizationTypeCV','organizationTypeCV',2,'Changed description.',24,2),(88,'2015-03-03 23:58:10','methodTypeCV','methodTypeCV',2,'Changed description.',24,2),(89,'2015-03-03 23:58:27','equipmentTypeCV','equipmentTypeCV',2,'Changed description.',24,2),(90,'2015-03-03 23:58:47','elevationDatumCV','elevationDatumCV',2,'Changed description.',24,2),(91,'2015-03-03 23:59:05','directiveTypeCV','directiveTypeCV',2,'Changed description.',24,2),(92,'2015-03-03 23:59:58','datasetTypeCV','datasetTypeCV',2,'Changed description.',24,2),(93,'2015-03-04 00:00:26','censorCodeCV','censorCodeCV',2,'Changed description.',24,2),(94,'2015-03-04 00:01:10','annotationTypeCV','annotationTypeCV',2,'Changed description.',24,2),(95,'2015-03-04 00:01:22','aggregationStatisticCV','aggregationStatisticCV',2,'Changed description.',24,2),(96,'2015-03-04 00:01:35','actionTypeCV','actionTypeCV',2,'Changed description.',24,2),(97,'2015-03-04 00:34:08','10','odm2:offset1',1,'',22,2),(98,'2015-03-04 20:28:48','11','odm2:offset2',1,'',22,2),(99,'2015-03-04 20:28:58','12','odm2:offset3',1,'',22,2),(100,'2015-03-04 20:29:27','9','odm2:offset1->offset1',1,'',23,2),(101,'2015-03-04 20:29:54','10','odm2:offset2->offset2',1,'',23,2),(102,'2015-03-04 20:30:04','11','odm2:offset3->offset3',1,'',23,2),(103,'2015-03-05 00:12:03','variableTypeCV','variableTypeCV',2,'Changed uri.',24,2),(104,'2015-03-05 00:12:55','variableNameCV','variableNameCV',2,'Changed uri.',24,2),(105,'2015-03-05 00:18:00','taxonomicClassifierTypeCV','taxonomicClassifierTypeCV',2,'Changed uri.',24,2),(106,'2015-03-05 00:18:09','statusCV','statusCV',2,'Changed uri.',24,2),(107,'2015-03-05 00:18:17','specimenTypeCV','specimenTypeCV',2,'Changed uri.',24,2),(108,'2015-03-05 00:18:30','specimenMediumCV','specimenMediumCV',2,'Changed uri.',24,2),(109,'2015-03-05 00:18:39','speciationCV','speciationCV',2,'Changed uri.',24,2),(110,'2015-03-05 00:18:49','spatialOffsetTypeCV','spatialOffsetTypeCV',2,'Changed uri.',24,2),(111,'2015-03-05 00:18:57','siteTypeCV','siteTypeCV',2,'Changed uri.',24,2),(112,'2015-03-05 00:19:05','samplingFeatureTypeCV','samplingFeatureTypeCV',2,'Changed uri.',24,2),(113,'2015-03-05 00:19:16','samplingFeatureGeotypeCV','samplingFeatureGeotypeCV',2,'Changed uri.',24,2),(114,'2015-03-05 00:19:26','sampledMediumCV','sampledMediumCV',2,'Changed uri.',24,2),(115,'2015-03-05 00:19:37','resultTypeCV','resultTypeCV',2,'Changed uri.',24,2),(116,'2015-03-05 00:19:48','referenceMaterialMediumCV','referenceMaterialMediumCV',2,'Changed uri.',24,2),(117,'2015-03-05 00:19:57','qualityCodeCV','qualityCodeCV',2,'Changed uri.',24,2),(118,'2015-03-05 00:20:07','propertyDataTypeCV','propertyDataTypeCV',2,'Changed uri.',24,2),(119,'2015-03-05 00:20:21','organizationTypeCV','organizationTypeCV',2,'Changed uri.',24,2),(120,'2015-03-05 00:20:31','methodTypeCV','methodTypeCV',2,'Changed uri.',24,2),(121,'2015-03-05 00:20:45','equipmentTypeCV','equipmentTypeCV',2,'Changed uri.',24,2),(122,'2015-03-05 00:20:56','elevationDatumCV','elevationDatumCV',2,'Changed uri.',24,2),(123,'2015-03-05 00:21:23','directiveTypeCV','directiveTypeCV',2,'Changed uri.',24,2),(124,'2015-03-05 00:21:35','datasetTypeCV','datasetTypeCV',2,'Changed uri.',24,2),(125,'2015-03-05 00:21:47','censorCodeCV','censorCodeCV',2,'Changed uri.',24,2),(126,'2015-03-05 00:21:56','annotationTypeCV','annotationTypeCV',2,'Changed uri.',24,2),(127,'2015-03-05 00:22:04','aggregationStatisticCV','aggregationStatisticCV',2,'Changed uri.',24,2),(128,'2015-03-05 00:22:17','actionTypeCV','actionTypeCV',2,'Changed uri.',24,2),(129,'2015-03-16 21:22:50','variableType','variableType',2,'Changed name and uri.',24,2),(130,'2015-03-16 21:23:48','variableType','variableType',2,'Changed name and uri.',24,2),(131,'2015-03-16 21:24:24','variableName','variableName',2,'Changed name and uri.',24,2),(132,'2015-03-16 21:35:27','variableType','variableType',3,'',24,2),(133,'2015-03-16 21:35:32','variableName','variableName',3,'',24,2),(134,'2015-03-16 21:35:58','qualityCode','qualityCode',2,'Changed name and uri.',24,2),(135,'2015-03-16 21:40:08','actionType','actionType',2,'Changed name and uri.',24,2),(136,'2015-03-16 21:40:20','aggregationStatistic','aggregationStatistic',2,'Changed name and uri.',24,2),(137,'2015-03-16 21:40:33','aggregationStatistic','aggregationStatistic',2,'Changed name and uri.',24,2),(138,'2015-03-16 21:40:48','annotationType','annotationType',2,'Changed name and uri.',24,2),(139,'2015-03-16 21:41:05','censorCode','censorCode',2,'Changed name and uri.',24,2),(140,'2015-03-16 21:41:18','datasetType','datasetType',2,'Changed name and uri.',24,2),(141,'2015-03-16 21:41:32','directiveType','directiveType',2,'Changed name and uri.',24,2),(142,'2015-03-16 21:41:48','elevationDatum','elevationDatum',2,'Changed name and uri.',24,2),(143,'2015-03-16 21:42:02','equipmentType','equipmentType',2,'Changed name and uri.',24,2),(144,'2015-03-16 21:42:17','methodType','methodType',2,'Changed name and uri.',24,2),(145,'2015-03-16 21:42:27','organizationType','organizationType',2,'Changed name and uri.',24,2),(146,'2015-03-16 21:42:53','propertyDataType','propertyDataType',2,'Changed name and uri.',24,2),(147,'2015-03-16 21:43:10','referenceMaterialMedium','referenceMaterialMedium',2,'Changed name and uri.',24,2),(148,'2015-03-16 21:43:20','resultType','resultType',2,'Changed name and uri.',24,2),(149,'2015-03-16 21:43:37','sampledMedium','sampledMedium',2,'Changed name and uri.',24,2),(150,'2015-03-16 21:43:52','samplingFeatureGeotype','samplingFeatureGeotype',2,'Changed name and uri.',24,2),(151,'2015-03-16 21:44:04','samplingFeatureType','samplingFeatureType',2,'Changed name and uri.',24,2),(152,'2015-03-16 21:44:15','siteType','siteType',2,'Changed name and uri.',24,2),(153,'2015-03-16 21:44:29','spatialOffsetType','spatialOffsetType',2,'Changed name and uri.',24,2),(154,'2015-03-16 21:44:41','speciation','speciation',2,'Changed name and uri.',24,2),(155,'2015-03-16 21:44:52','specimenMedium','specimenMedium',2,'Changed name and uri.',24,2),(156,'2015-03-16 21:45:05','specimenType','specimenType',2,'Changed name and uri.',24,2),(157,'2015-03-16 21:45:19','status','status',2,'Changed name and uri.',24,2),(158,'2015-03-16 21:45:31','taxonomicClassifierType','taxonomicClassifierType',2,'Changed name and uri.',24,2),(159,'2015-03-16 21:45:43','variableName','variableName',2,'Changed name and uri.',24,2),(160,'2015-03-16 21:45:52','variableType','variableType',2,'Changed name and uri.',24,2),(161,'2015-03-16 21:46:30','variableTypeCV','variableTypeCV',3,'',24,2),(162,'2015-03-16 21:46:30','variableNameCV','variableNameCV',3,'',24,2),(163,'2015-03-16 21:46:30','taxonomicClassifierTypeCV','taxonomicClassifierTypeCV',3,'',24,2),(164,'2015-03-16 21:46:30','statusCV','statusCV',3,'',24,2),(165,'2015-03-16 21:46:30','specimenTypeCV','specimenTypeCV',3,'',24,2),(166,'2015-03-16 21:46:30','specimenMediumCV','specimenMediumCV',3,'',24,2),(167,'2015-03-16 21:46:30','speciationCV','speciationCV',3,'',24,2),(168,'2015-03-16 21:46:30','spatialOffsetTypeCV','spatialOffsetTypeCV',3,'',24,2),(169,'2015-03-16 21:46:30','siteTypeCV','siteTypeCV',3,'',24,2),(170,'2015-03-16 21:46:30','samplingFeatureTypeCV','samplingFeatureTypeCV',3,'',24,2),(171,'2015-03-16 21:46:30','samplingFeatureGeotypeCV','samplingFeatureGeotypeCV',3,'',24,2),(172,'2015-03-16 21:46:30','sampledMediumCV','sampledMediumCV',3,'',24,2),(173,'2015-03-16 21:46:30','resultTypeCV','resultTypeCV',3,'',24,2),(174,'2015-03-16 21:46:30','referenceMaterialMediumCV','referenceMaterialMediumCV',3,'',24,2),(175,'2015-03-16 21:46:30','qualityCodeCV','qualityCodeCV',3,'',24,2),(176,'2015-03-16 21:46:30','propertyDataTypeCV','propertyDataTypeCV',3,'',24,2),(177,'2015-03-16 21:46:30','organizationTypeCV','organizationTypeCV',3,'',24,2),(178,'2015-03-16 21:46:30','methodTypeCV','methodTypeCV',3,'',24,2),(179,'2015-03-16 21:46:30','equipmentTypeCV','equipmentTypeCV',3,'',24,2),(180,'2015-03-16 21:46:31','elevationDatumCV','elevationDatumCV',3,'',24,2),(181,'2015-03-16 21:46:31','directiveTypeCV','directiveTypeCV',3,'',24,2),(182,'2015-03-16 21:46:31','datasetTypeCV','datasetTypeCV',3,'',24,2),(183,'2015-03-16 21:46:31','censorCodeCV','censorCodeCV',3,'',24,2),(184,'2015-03-16 21:46:31','annotationTypeCV','annotationTypeCV',3,'',24,2),(185,'2015-03-16 21:46:31','aggregationStatisticCV','aggregationStatisticCV',3,'',24,2),(186,'2015-03-16 21:46:31','actionTypeCV','actionTypeCV',3,'',24,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'api access','tastypie','apiaccess'),(8,'api key','tastypie','apikey'),(9,'Action Type Control Vocabulary','cvservices','actiontype'),(10,'Action Type Control Vocabulary Request','cvservices','actiontyperequest'),(11,'Method Type Control Vocabulary','cvservices','methodtype'),(12,'Method Type Control Vocabulary Request','cvservices','methodtyperequest'),(13,'Organization Type Control Vocabulary','cvservices','organizationtype'),(14,'Organization Type Control Vocabulary Request','cvservices','organizationtyperequest'),(15,'Sampling Feature Geo-type Control Vocabulary','cvservices','samplingfeaturegeotype'),(16,'Sampling Feature Geo-type Control Vocabulary Request','cvservices','samplingfeaturegeotyperequest'),(17,'Sampling Feature Type Control Vocabulary','cvservices','samplingfeaturetype'),(18,'Sampling Feature Type Control Vocabulary Request','cvservices','samplingfeaturetyperequest'),(19,'Site Type Control Vocabulary','cvservices','sitetype'),(20,'Site Type Control Vocabulary Request','cvservices','sitetyperequest'),(21,'namespace','rdfserializer','namespace'),(22,'node','rdfserializer','node'),(23,'field relation','rdfserializer','fieldrelation'),(24,'scheme','rdfserializer','scheme');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-02-24 23:19:02'),(2,'auth','0001_initial','2015-02-24 23:19:07'),(3,'admin','0001_initial','2015-02-24 23:19:08'),(4,'cvservices','0001_initial','2015-02-24 23:19:08'),(5,'rdfserializer','0001_initial','2015-02-24 23:19:10'),(6,'rdfserializer','data_migration','2015-02-24 23:19:10'),(7,'sessions','0001_initial','2015-02-24 23:19:11'),(8,'tastypie','0001_initial','2015-02-24 23:19:13'),(9,'cvservices','0002_auto_20150224_1623','2015-02-24 23:23:29');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2x8w171w00c8zbbine211niqgga6rko9','YjcyYmM1ZTJjZjU2ZjIyMjkwMjc4NzM3YWVmYmJhYmZjYjUyZTM0ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjUyMjUxNmFkYTljOWU4N2YyMTY2MjU5NWI5OThhNjU4NjMzNmIxNWYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-03-10 23:25:42'),('d6b714mspipwdde8gd4424z8j8d1q3d6','Njg0MDgzNDUwNTQ0YzdhMDY5MTVlNWNmZTJmM2FhMTA2Y2JhZTJmYzp7fQ==','2015-03-10 23:24:26'),('gh0vaai4d6q5qviag8gk4wmrhnafy1gx','Nzc4MWU0ZWU2Mjc4ZGI2YzYyNTI5YWVhOTU5ZjQ1MzdhMmQwNWZlYzp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzOGI4ZjJiZjk0MWQ2MzU3NzdiY2M3OTc1ZDdkZGNlZDBkMTllMWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9','2015-03-13 23:36:44'),('whnskgnin4i6kr653dj0gba8qqyg4h4q','Nzc4MWU0ZWU2Mjc4ZGI2YzYyNTI5YWVhOTU5ZjQ1MzdhMmQwNWZlYzp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzOGI4ZjJiZjk0MWQ2MzU3NzdiY2M3OTc1ZDdkZGNlZDBkMTllMWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9','2015-03-30 19:49:14'),('zenomuaj3m0zpru58sypvc70t0aggfi0','Nzc4MWU0ZWU2Mjc4ZGI2YzYyNTI5YWVhOTU5ZjQ1MzdhMmQwNWZlYzp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzOGI4ZjJiZjk0MWQ2MzU3NzdiY2M3OTc1ZDdkZGNlZDBkMTllMWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9','2015-03-12 21:24:39');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fieldsrelations`
--

DROP TABLE IF EXISTS `fieldsrelations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fieldsrelations` (
  `fieldId` int(11) NOT NULL AUTO_INCREMENT,
  `fieldName` varchar(255) NOT NULL,
  `nodeId` int(11) NOT NULL,
  PRIMARY KEY (`fieldId`),
  KEY `FieldsRelations_d515995b` (`nodeId`),
  CONSTRAINT `FieldsRelations_nodeId_2e3a3ef3_fk_Nodes_nodeId` FOREIGN KEY (`nodeId`) REFERENCES `nodes` (`nodeId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fieldsrelations`
--

LOCK TABLES `fieldsrelations` WRITE;
/*!40000 ALTER TABLE `fieldsrelations` DISABLE KEYS */;
INSERT INTO `fieldsrelations` VALUES (1,'name',1),(2,'definition',2),(3,'note',3),(4,'provenance',4),(5,'provenance_uri',5),(6,'category',6),(7,'produces_result',7),(8,'term',8),(9,'offset1',10),(10,'offset2',11),(11,'offset3',12);
/*!40000 ALTER TABLE `fieldsrelations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namespaces`
--

DROP TABLE IF EXISTS `namespaces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namespaces` (
  `alias` varchar(128) NOT NULL,
  `reference` varchar(255) NOT NULL,
  PRIMARY KEY (`alias`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namespaces`
--

LOCK TABLES `namespaces` WRITE;
/*!40000 ALTER TABLE `namespaces` DISABLE KEYS */;
INSERT INTO `namespaces` VALUES ('dc','http://purl.org/dc/elements/1.1/'),('odm2','http://vocabulary.odm2.org/ODM2/ODM2Terms'),('skos','http://www.w3.org/2004/02/skos/core');
/*!40000 ALTER TABLE `namespaces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodes`
--

DROP TABLE IF EXISTS `nodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nodes` (
  `nodeId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `namespace_id` varchar(128) NOT NULL,
  PRIMARY KEY (`nodeId`),
  KEY `Nodes_cf7b1778` (`namespace_id`),
  CONSTRAINT `Nodes_namespace_id_72f973ac_fk_Namespaces_alias` FOREIGN KEY (`namespace_id`) REFERENCES `namespaces` (`alias`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodes`
--

LOCK TABLES `nodes` WRITE;
/*!40000 ALTER TABLE `nodes` DISABLE KEYS */;
INSERT INTO `nodes` VALUES (1,'prefLabel','skos'),(2,'definition','skos'),(3,'note','skos'),(4,'historyNote','skos'),(5,'exactMatch','skos'),(6,'category','odm2'),(7,'producesResult','odm2'),(8,'Concept','skos'),(9,'inScheme','skos'),(10,'offset1','odm2'),(11,'offset2','odm2'),(12,'offset3','odm2');
/*!40000 ALTER TABLE `nodes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schemes`
--

DROP TABLE IF EXISTS `schemes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schemes` (
  `name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `creator` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `uri` varchar(200) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schemes`
--

LOCK TABLES `schemes` WRITE;
/*!40000 ALTER TABLE `schemes` DISABLE KEYS */;
INSERT INTO `schemes` VALUES ('actionType','ODM2 ActionType Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of actions performed in making observations. Depending on the action type, the action may or may not produce an observation result.','http://vocabulary.odm2.org/actiontype'),('aggregationStatistic','ODM2 Aggregation Statistic Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the calculated statistic associated with recorded observations. The aggregation statistic is calculated over the time aggregation interval associated with the recorded observation. ','http://vocabulary.odm2.org/aggregationstatistic'),('annotationType','ODM2 Annotation Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of annotation. In ODM2 the annotation type determines whether the annotation forms a grouping of related entities (e.g., a group of sites or variables) or an annotation of a particular entity (e.g., a comment about an individual Site or data value). ','http://vocabulary.odm2.org/annotationtype'),('censorCode','ODM2 Censor Code Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing whether a data value was determined or whether the actual value is unknown due to right or left censoring.','http://vocabulary.odm2.org/censorcode'),('datasetType','ODM2 Dataset Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing types of Datasets in ODM2. Datasets are logical groupings of Results.','http://vocabulary.odm2.org/datasettype'),('directiveType','ODM2 Directive Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing types of directives under which observations are made. Examples include projects, monitoring programs, campaigns, etc.','http://vocabulary.odm2.org/directivetype'),('elevationDatum','ODM2 Elevation Datum Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing vertical datums. Vertical datums are used in ODM2 to specify the origin for elevations assocated with SamplingFeatures.','http://vocabulary.odm2.org/elevationdatum'),('equipmentType','ODM2 Equipment Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing types of equipment used for making observations. Examples include sensors, batteries, radios, dataloggers, samplers, etc.','http://vocabulary.odm2.org/equipmenttype'),('methodType','ODM2 MethodType Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing types of Methods associated with creating observations. MethodTypes correspond with ActionTypes in ODM2. An Action must be performed using an appropriate MethodType - e.g., a specimen collection Action should be associated with a specimen collection method.','http://vocabulary.odm2.org/methodtype'),('organizationType','ODM2 OrganizationType Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing types of Organizations. In ODM2, People may or may not be affiliated with an Organization. People can also be affiliated with more than one Organization.','http://vocabulary.odm2.org/organizationtype'),('propertyDataType','ODM2 Property Data Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the data type for an extension property in ODM2.  Extension properties can be added to many of the entities in ODM2 (e.g., Sites, Variables, etc.). The values of these extension properties must be of one of the listed primitive data types.','http://vocabulary.odm2.org/propertydatatype'),('qualityCode','ODM2 Quality Code Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the quality of the observation.','http://vocabulary.odm2.org/qualitycode'),('referenceMaterialMedium','ODM2 Reference Material Medium Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the physical medium of a reference material.','http://vocabulary.odm2.org/referencematerialmedium'),('resultType','ODM2 Result Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of the Result. In ODM2 Results are separated from, but related to their data values. Each ResultType has a set of related tables for storing the data values for any result of that type.','http://vocabulary.odm2.org/resulttype'),('sampledMedium','ODM2 Sampled Medium Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the physical medium within which an observation was made. For sensors this will be the physical medium in which the sensor is emplaced to make measurements. For Specimens, this will be the physical medium that was sampled.','http://vocabulary.odm2.org/sampledmedium'),('samplingFeatureGeotype','ODM2 SamplingFeatureGeotype Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the geospatial feature type associated with a SamplingFeature. For example, Site SamplingFeatures are represented as points. In ODM2, each SamplingFeature may have only one geospatial type, but a geospatial types may range from simple points to a complex polygons or even three dimensional volumes.\r\n','http://vocabulary.odm2.org/samplingfeaturegeotype'),('samplingFeatureType','SamplingFeatureType','ODM2 Working Group','A vocabulary for describing the type of SamplingFeature. Many different SamplingFeature types can be represented in ODM2. SamplingFeatures of type Site and Specimen will be the most common, but many different types of varying levels of complexity can be used.','http://vocabulary.odm2.org/samplingfeaturetype'),('siteType','ODM2 SiteType Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of a data collection Site. To some extent, these types represent the ultimate feature of interest that the site was established to measure. For example, a Stream Site was established to measure properties of a Stream.','http://vocabulary.odm2.org/sitetype'),('spatialOffsetType','ODM2 Spatial Offset Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of SpatialOffset that exists between two SamplingFeatures.','http://vocabulary.odm2.org/spatialoffsettype'),('speciation','ODM2 Speciation Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of SpatialOffset that exists between two SamplingFeatures.','http://vocabulary.odm2.org/speciation'),('specimenMedium','ODM2 Specimen Medium Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the physical medium of a physical Specimen.','http://vocabulary.odm2.org/specimenmedium'),('specimenType','ODM2 Specimen Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of a physical Specimen.','http://vocabulary.odm2.org/specimentype'),('status','ODM2 Status Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the data collection status of a Result. In ODM2 the StatusCV can be used to specify whether data collection is planned, ongoing, or complete.','http://vocabulary.odm2.org/status'),('taxonomicClassifierType','ODM2 Taxonomic Classifier Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing types of taxonomies from which descriptive terms used in an ODM2 database have been drawn. Taxonomic classifiers provide a way to classify Results and Specimens according to terms from a formal taxonomy.','http://vocabulary.odm2.org/taxonomicclassifiertype'),('variableName','ODM2 Variable Name Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the name of Variables.','http://vocabulary.odm2.org/variablename'),('variableType','ODM2 Variable Type Controlled Vocabulary','ODM2 Working Group','A vocabulary for describing the type of Variables. VariableTypes provide a way to group Variables into categories for easier querying and filtering.','http://vocabulary.odm2.org/variabletype');
/*!40000 ALTER TABLE `schemes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tastypie_apiaccess`
--

DROP TABLE IF EXISTS `tastypie_apiaccess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tastypie_apiaccess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifier` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `request_method` varchar(10) NOT NULL,
  `accessed` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apiaccess`
--

LOCK TABLES `tastypie_apiaccess` WRITE;
/*!40000 ALTER TABLE `tastypie_apiaccess` DISABLE KEYS */;
/*!40000 ALTER TABLE `tastypie_apiaccess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tastypie_apikey`
--

DROP TABLE IF EXISTS `tastypie_apikey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tastypie_apikey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(128) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `tastypie_apikey_3c6e0b8a` (`key`),
  CONSTRAINT `tastypie_apikey_user_id_e0b406b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apikey`
--

LOCK TABLES `tastypie_apikey` WRITE;
/*!40000 ALTER TABLE `tastypie_apikey` DISABLE KEYS */;
/*!40000 ALTER TABLE `tastypie_apikey` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-17 18:13:00
