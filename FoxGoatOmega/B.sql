-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: FoxGoatOmega
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `EqnStore`
--

DROP TABLE IF EXISTS `EqnStore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `EqnStore` (
  `Equation` varchar(255) DEFAULT NULL,
  `Solution_Set` varchar(255) DEFAULT NULL,
  `Time_Instant` time DEFAULT NULL,
  `User` varchar(255) DEFAULT NULL,
  `Function_Class` varchar(255) DEFAULT NULL,
  `Date_Instant` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EqnStore`
--

LOCK TABLES `EqnStore` WRITE;
/*!40000 ALTER TABLE `EqnStore` DISABLE KEYS */;
INSERT INTO `EqnStore` VALUES ('x**2+3*x+2','[-2.0, -1.0]','10:16:24','Jacob','[\'Algebraic\']','2019-08-08'),('x**2+3*x+2','[-2.0, -1.0]','10:16:24','Jacob','[\'Algebraic\']','2019-08-08'),('x**5+3**x-4','[1.0]','10:17:31','Jacob','[\'Exponential\']','2019-08-08'),('3**(x**3)-5','[1.136]','10:19:50','JackB','[\'Exponential\']','2019-08-08'),('x**8+6*x**3+5','[-1.301, -1.0]','10:27:36','Jacob','[\'Algebraic\']','2019-08-08'),('3**x-6','[1.631]','10:28:28','Jacob','[\'Exponential\']','2019-08-08'),('2*x+5','[-2.5]','10:35:29','kjgakusf','[\'Algebraic\']','2019-08-08'),('3*x**2+4-5**x','[1.449]','11:03:30','WasWolf','[\'Exponential\']','2019-08-08'),('3*x**2-4+5**x','[-1.131, 0.636]','11:04:54','WasWolf','[\'Exponential\']','2019-08-08'),('3*x**2-4+5**x','[-1.131, 0.636]','11:05:51','WasWolf','[\'Exponential\']','2019-08-08'),('x**2+5*x+1','[-4.791, -0.209]','11:34:01','Jacob','[\'Algebraic\']','2019-08-08'),('x**2-x-1','[-0.618, 1.618]','13:06:22','Jacob','[\'Algebraic\']','2019-08-08'),('x**4+2*x+21','[]','13:10:41','DFAHKMD,','[\'Algebraic\']','2019-08-08'),('3*x**4-2*x**2+1','[]','18:24:33','A','[\'Algebraic\']','2019-08-08'),('5**(log(x**2))-2','[-1.24, 1.24]','08:42:19','JackEra','[\'Misc\']','2019-08-09'),('5**4*x-5**2**x','[0.008, 2.163]','12:02:50','Abacus','[\'Exponential\']','2019-08-09'),('3*sin(4*x+2)-5*log(x**2)','[-0.768, 0.75]','12:45:59','Kuraa','[\'Misc\']','2019-08-09'),('5*x+3*sin(x+3)','[-0.202]','08:46:11','TheEnder','[\'Trigonometric\']','2019-08-10'),('3*x**3+4*x**2+5*log(x)','[0.628]','11:23:59','SuperWeird','[\'Logarithmic\']','2019-08-10'),('x**8+32*x+245','[]','11:39:54','u56twjf','[\'Algebraic\']','2019-08-10'),('x**7+24*x+143','[-1.922]','11:41:36','alkhfljq,','[\'Algebraic\']','2019-08-10'),('3**x**7+5**x**3+4*sin(log(x))','[0.001, 0.073, 0.541]','12:53:05','Jacob','[\'Misc\']','2019-08-10'),('5/(9+(3*x-5/x))**(0.5)','[]','17:17:55','Abhilash','[\'Exponential\']','2019-08-10'),('3*x**23+891*x+1023','[-1.111]','20:24:42','wadyghfakew','[\'Algebraic\']','2019-08-10'),('5*x**45+1723*x+98765','[-1.245]','20:27:14','./,/;\'//;./:?>','[\'Algebraic\']','2019-08-10'),('3**sin(log(x))-2','[0.004, 0.022, 1.979]','08:17:48','TheEnder','[\'Misc\']','2019-08-11'),('sin(x)','[0.0, 3.142, 6.283]','08:26:36','VirginTrig','[\'Trigonometric\']','2019-08-11'),('x-tan(x)','[0.0, 4.493]','08:34:46','Abhilash','[\'Trigonometric\']','2019-08-11'),('2-x+sin(x)','[2.554]','09:35:38','A','[\'Trigonometric\']','2019-08-11'),('4567*x**2323+1234*x+145367','[-1.001]','21:11:55','hjxdghfgmhv,j.kb','[\'Algebraic\']','2019-08-11'),('tan(log(2**x))','[0.0, 4.532]','21:45:12','Jacob','[\'Misc\']','2019-08-11'),('10*x**4-3*x**2-1','[-0.707, 0.707]','08:14:00','Jacob','[\'Algebraic\']','2019-08-12'),('5*x**5+4*x**4+3*x**3+2*x**2+1','[-0.912]','14:24:19','JackEra','[\'Algebraic\']','2019-08-12'),('5*x**5+4*x**4+3*x**3+2*x**2+x+1','[-0.79]','14:24:56','JackEra','[\'Algebraic\']','2019-08-12'),('x+sin(x)+5*log(x**2+3)','[-36.836]','17:25:33','Jacob','[\'Misc\']','2019-08-13'),('4**sin(x)+5*log(x)-3','[0.972]','07:19:22','Abacus','[\'Misc\']','2019-08-14'),('x**9-5*x**4+3*x**2+log(x)-5','[1.365]','23:49:29','Abacus','[\'Logarithmic\']','2019-08-14'),('x**8-4*x+3','[0.787, 1.0]','23:50:47','Abacus','[\'Algebraic\']','2019-08-14'),('(sin(x)/x)**2','[3.142, 6.283]','00:53:27','Jacob','[\'Trigonometric\']','2019-08-16'),('6*x**2+7*x-3','[-1.5, 0.333]','01:09:09','Lizabeth','[\'Algebraic\']','2019-08-16'),('2*x**2-7*x-15','[-1.5, 5.0]','01:10:00','Lizabeth','[\'Algebraic\']','2019-08-16'),('3*x**2-(5**(0.5))*x+4','[0.373]','01:11:36','Lizabeth','[\'Algebraic\']','2019-08-16'),('3*(x**2)-5*(2**(0.5))*x+4','[0.943, 1.414]','01:12:40','Lizabeth','[\'Algebraic\']','2019-08-16'),('5*cos(2*x)-3*cos(4*x)-2*sin(4*x)','[1.093, 2.212, 4.235, 5.354]','17:01:45','Jacob','[\'Trigonometric\']','2019-09-10'),('np.exp(x)-1-100*(1+x)','[-1.006, 6.64]','07:13:17','Jacob','[\'Algebraic\']','2019-09-13'),('x**2+3*x+2','[-2.0, -1.0]','11:10:56','Jacob','[\'Algebraic\']','2019-09-14'),('(1-2*x)**2-3600*(2+x)*(x**2)','[-1.998, -0.012, 0.011]','07:47:41','Jacob','[\'Algebraic\']','2019-09-22'),('((9-2*x)**2)*(1-x)-4','[0.922]','05:41:08','Jacob','[\'Algebraic\']','2019-10-10'),('(3*x/(np.pi))+(cos(x))-1','[0.0]','03:24:52','Jacob','[\'Trigonometric\']','2019-10-25'),('x**2+41-np.abs(15*x+15)','[-8.0, -7.0, 2.0, 13.0]','09:54:12','Jacob','[\'Algebraic\']','2019-10-25'),('x**3-15*x**2+15*x-1','[0.072, 1.0, 13.928]','21:19:37','Jacob','[\'Algebraic\']','2019-10-28'),('(x-1)*(x**3-15*x**2+15*x-1)-2*(6*x**3-20*x**2+6*x)','[0.04, 0.446, 2.24, 25.274]','21:35:50','Jacob','[\'Algebraic\']','2019-10-28'),('x**3-3888*x+2','[-62.354, 0.001, 62.354]','07:13:18','Jacob','[\'Algebraic\']','2019-11-09');
/*!40000 ALTER TABLE `EqnStore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-11  5:58:07
