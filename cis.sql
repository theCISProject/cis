-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 27, 2010 at 08:32 AM
-- Server version: 5.1.41
-- PHP Version: 5.3.2-1ubuntu4.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cis`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_message`
--

CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=98 ;

--
-- Dumping data for table `auth_message`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=100 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add message', 4, 'add_message'),
(11, 'Can change message', 4, 'change_message'),
(12, 'Can delete message', 4, 'delete_message'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(22, 'Can add log entry', 8, 'add_logentry'),
(23, 'Can change log entry', 8, 'change_logentry'),
(24, 'Can delete log entry', 8, 'delete_logentry'),
(25, 'Can add report', 9, 'add_report'),
(26, 'Can change report', 9, 'change_report'),
(27, 'Can delete report', 9, 'delete_report'),
(28, 'Can add reporter''s information', 10, 'add_information'),
(29, 'Can change reporter''s information', 10, 'change_information'),
(30, 'Can delete reporter''s information', 10, 'delete_information'),
(31, 'Can add detail', 11, 'add_detail'),
(32, 'Can change detail', 11, 'change_detail'),
(33, 'Can delete detail', 11, 'delete_detail'),
(34, 'Can add action', 12, 'add_action'),
(35, 'Can change action', 12, 'change_action'),
(36, 'Can delete action', 12, 'delete_action'),
(37, 'Can add accused', 13, 'add_accused'),
(38, 'Can change accused', 13, 'change_accused'),
(39, 'Can delete accused', 13, 'delete_accused'),
(40, 'Can add arrest', 14, 'add_arrest'),
(41, 'Can change arrest', 14, 'change_arrest'),
(42, 'Can delete arrest', 14, 'delete_arrest'),
(43, 'Can add register', 15, 'add_register'),
(44, 'Can change register', 15, 'change_register'),
(45, 'Can delete register', 15, 'delete_register'),
(46, 'Can add remark', 16, 'add_remark'),
(47, 'Can change remark', 16, 'change_remark'),
(48, 'Can delete remark', 16, 'delete_remark'),
(49, 'Can add report book', 17, 'add_reportbook'),
(50, 'Can change report book', 17, 'change_reportbook'),
(51, 'Can delete report book', 17, 'delete_reportbook'),
(52, 'Can add forensic', 18, 'add_forensic'),
(53, 'Can change forensic', 18, 'change_forensic'),
(54, 'Can delete forensic', 18, 'delete_forensic'),
(55, 'Can add accused', 19, 'add_accused'),
(56, 'Can change accused', 19, 'change_accused'),
(57, 'Can delete accused', 19, 'delete_accused'),
(58, 'Can add complainant', 20, 'add_complainant'),
(59, 'Can change complainant', 20, 'change_complainant'),
(60, 'Can delete complainant', 20, 'delete_complainant'),
(61, 'Can add property', 21, 'add_property'),
(62, 'Can change property', 21, 'change_property'),
(63, 'Can delete property', 21, 'delete_property'),
(64, 'Can add officer', 22, 'add_officer'),
(65, 'Can change officer', 22, 'change_officer'),
(66, 'Can delete officer', 22, 'delete_officer'),
(67, 'Can add result', 23, 'add_result'),
(68, 'Can change result', 23, 'change_result'),
(69, 'Can delete result', 23, 'delete_result'),
(70, 'Can add location', 24, 'add_location'),
(71, 'Can change location', 24, 'change_location'),
(72, 'Can delete location', 24, 'delete_location'),
(73, 'Can add country', 25, 'add_country'),
(74, 'Can change country', 25, 'change_country'),
(75, 'Can delete country', 25, 'delete_country'),
(76, 'Can add region', 26, 'add_region'),
(77, 'Can change region', 26, 'change_region'),
(78, 'Can delete region', 26, 'delete_region'),
(79, 'Can add district', 27, 'add_district'),
(80, 'Can change district', 27, 'change_district'),
(81, 'Can delete district', 27, 'delete_district'),
(82, 'Can add ward', 28, 'add_ward'),
(83, 'Can change ward', 28, 'change_ward'),
(84, 'Can delete ward', 28, 'delete_ward'),
(85, 'Can add police station', 29, 'add_station'),
(86, 'Can change police station', 29, 'change_station'),
(87, 'Can delete police station', 29, 'delete_station'),
(88, 'Can add offense category', 30, 'add_offensecategory'),
(89, 'Can change offense category', 30, 'change_offensecategory'),
(90, 'Can delete offense category', 30, 'delete_offensecategory'),
(91, 'Can add offense', 31, 'add_offense'),
(92, 'Can change offense', 31, 'change_offense'),
(93, 'Can delete offense', 31, 'delete_offense'),
(94, 'Can add station police', 32, 'add_stationpolice'),
(95, 'Can change station police', 32, 'change_stationpolice'),
(96, 'Can delete station police', 32, 'delete_stationpolice'),
(97, 'Can add police profile', 33, 'add_policeprofile'),
(98, 'Can change police profile', 33, 'change_policeprofile'),
(99, 'Can delete police profile', 33, 'delete_policeprofile');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', '', '', 'admin@admin.com', 'sha1$6b8a3$c8c1994c4223648a6f67ccb1f2ec62ef5c479b01', 1, 1, 1, '2010-07-26 21:22:15', '2010-07-26 21:22:01');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `book_accused`
--

CREATE TABLE IF NOT EXISTS `book_accused` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `sex` varchar(6) NOT NULL,
  `nationality` varchar(80) NOT NULL,
  `postal_address` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `book_accused_report_id` (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `book_accused`
--


-- --------------------------------------------------------

--
-- Table structure for table `book_action`
--

CREATE TABLE IF NOT EXISTS `book_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `status` varchar(80) NOT NULL,
  `officer_name` varchar(80) NOT NULL,
  `final_disposal` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `report_id` (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `book_action`
--


-- --------------------------------------------------------

--
-- Table structure for table `book_arrest`
--

CREATE TABLE IF NOT EXISTS `book_arrest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `status` varchar(80) NOT NULL,
  `name` varchar(80) NOT NULL,
  `ppr_number` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `book_arrest_report_id` (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `book_arrest`
--


-- --------------------------------------------------------

--
-- Table structure for table `book_detail`
--

CREATE TABLE IF NOT EXISTS `book_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `reporter_information_id` int(11) NOT NULL,
  `officer_name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reporter_information_id` (`reporter_information_id`),
  KEY `book_detail_report_id` (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `book_detail`
--


-- --------------------------------------------------------

--
-- Table structure for table `book_information`
--

CREATE TABLE IF NOT EXISTS `book_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `sex` varchar(6) NOT NULL,
  `age` int(11) NOT NULL,
  `nationality` varchar(80) NOT NULL,
  `occupation` varchar(80) NOT NULL,
  `postal_address` longtext NOT NULL,
  `phone_number` varchar(80) NOT NULL,
  `e_mail` varchar(80) NOT NULL,
  `voter_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_information_report_id` (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `book_information`
--


-- --------------------------------------------------------

--
-- Table structure for table `book_report`
--

CREATE TABLE IF NOT EXISTS `book_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serial_number` varchar(80) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `investigation_number` int(11) DEFAULT NULL,
  `property_detail` longtext NOT NULL,
  `status` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `book_report`
--


-- --------------------------------------------------------

--
-- Table structure for table `core_policeprofile`
--

CREATE TABLE IF NOT EXISTS `core_policeprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `police_id` int(11) NOT NULL,
  `station_id` int(11) NOT NULL,
  `phone_number` varchar(13) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `created_date` datetime NOT NULL,
  `edited_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `police_id` (`police_id`),
  KEY `core_policeprofile_station_id` (`station_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `core_policeprofile`
--


-- --------------------------------------------------------

--
-- Table structure for table `core_stationpolice`
--

CREATE TABLE IF NOT EXISTS `core_stationpolice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `police_code` varchar(255) NOT NULL,
  `created_date` datetime NOT NULL,
  `edited_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `core_stationpolice`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_user_id` (`user_id`),
  KEY `django_admin_log_content_type_id` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=105 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2010-07-26 21:23:26', 1, 30, '1', 'Makosa dhidi ya maadili ya jamii', 1, ''),
(2, '2010-07-26 21:23:38', 1, 30, '2', 'Makosa ya kuwania mali', 1, ''),
(3, '2010-07-26 21:23:50', 1, 30, '3', 'Makosa dhidi ya binadamu', 1, ''),
(4, '2010-07-26 21:24:29', 1, 30, '4', 'Ajali za majeruhi', 1, ''),
(5, '2010-07-26 21:24:40', 1, 30, '5', 'Ajali za vifo', 1, ''),
(6, '2010-07-26 21:25:09', 1, 30, '6', 'Makosa ya kuvunja utulivu', 1, ''),
(7, '2010-07-26 21:25:57', 1, 30, '7', 'Makosa ya maandishi ya kubuni, utengenezaji sarafu na sawa na hayo', 1, ''),
(8, '2010-07-26 21:26:11', 1, 30, '7', 'Makosa ya maandishi ya kubuni, utengenezaji sarafu na sawa na hayo', 2, 'Changed rank.'),
(9, '2010-07-26 21:27:15', 1, 30, '8', 'Makosa ya majaribio, njama za kutenda au uhalifu', 1, ''),
(10, '2010-07-26 21:27:46', 1, 30, '9', 'Makosa juu ya usimamizi wa mamlaka halai', 1, ''),
(11, '2010-07-26 21:28:30', 1, 30, '10', 'Makosa ya uzembe barabani', 1, ''),
(12, '2010-07-26 21:28:48', 1, 30, '11', 'Makosa ya kupuuzia sheria za barabarani', 1, ''),
(13, '2010-07-26 21:29:38', 1, 31, '1', 'Madawa ya kulevya', 1, ''),
(14, '2010-07-26 21:29:51', 1, 31, '2', 'Banghi', 1, ''),
(15, '2010-07-26 21:30:05', 1, 31, '3', 'Mirungi', 1, ''),
(16, '2010-07-26 21:30:17', 1, 31, '4', 'Nyaraka za serikali', 1, ''),
(17, '2010-07-26 21:30:31', 1, 31, '5', 'Magendo', 1, ''),
(18, '2010-07-26 21:30:43', 1, 31, '6', 'Rushwa', 1, ''),
(19, '2010-07-26 21:30:52', 1, 31, '7', 'Pombe ya moshi', 1, ''),
(20, '2010-07-26 21:31:18', 1, 31, '8', 'Mitambo ya pombe ya moshi', 1, ''),
(21, '2010-07-26 21:31:29', 1, 31, '9', 'Kupatikana na risasi', 1, ''),
(22, '2010-07-26 21:31:40', 1, 31, '10', 'Kupatikana na silaha', 1, ''),
(23, '2010-07-26 21:32:42', 1, 31, '11', 'Wizi wa kutumia silaha', 1, ''),
(24, '2010-07-26 21:33:04', 1, 31, '12', 'Unyang''anyi wa kutumia silaha', 1, ''),
(25, '2010-07-26 21:33:13', 1, 31, '11', 'Wizi wa silaha', 2, 'Changed offense_title.'),
(26, '2010-07-26 21:33:39', 1, 31, '13', 'Unyang''anyi wa kutumia nguvu', 1, ''),
(27, '2010-07-26 21:33:54', 1, 31, '14', 'Wizi wa kwenye mabenki', 1, ''),
(28, '2010-07-26 21:34:19', 1, 31, '15', 'Wizi kwenye serikali za mitaa', 1, ''),
(29, '2010-07-26 21:34:29', 1, 31, '16', 'Kuchoma moto nyumba', 1, ''),
(30, '2010-07-26 21:34:56', 1, 31, '17', 'Mauaji', 1, ''),
(31, '2010-07-26 21:35:04', 1, 31, '18', 'Kubaka', 1, ''),
(32, '2010-07-26 21:35:17', 1, 31, '19', 'Wizi wa watoto', 1, ''),
(33, '2010-07-26 21:35:27', 1, 31, '20', 'Kutoa mimba', 1, ''),
(34, '2010-07-26 21:35:38', 1, 31, '21', 'Kutorosha watoto', 1, ''),
(35, '2010-07-26 21:35:50', 1, 31, '22', 'Kumtaja mtu mchawi', 1, ''),
(36, '2010-07-26 21:36:04', 1, 31, '23', 'Kujaribu kujiua', 1, ''),
(37, '2010-07-26 21:37:10', 1, 31, '24', 'Kuchocheza mashambulio', 1, ''),
(38, '2010-07-26 21:37:27', 1, 31, '25', 'Kuficha uhahini', 1, ''),
(39, '2010-07-26 21:37:42', 1, 31, '26', 'Kuleta vita vya wenyeji', 1, ''),
(40, '2010-07-26 21:38:01', 1, 31, '27', 'Mihuri ya kubuni', 1, ''),
(41, '2010-07-26 21:38:14', 1, 31, '28', 'Tume za siri', 1, ''),
(42, '2010-07-26 21:38:28', 1, 31, '29', 'Kujifanya mtu mwingine', 1, ''),
(43, '2010-07-26 21:39:31', 1, 31, '30', 'Ushawishi wa uchochezi', 1, ''),
(44, '2010-07-26 21:39:47', 1, 31, '31', 'Waficha uhalifu', 1, ''),
(45, '2010-07-26 21:39:59', 1, 31, '32', 'Njama', 1, ''),
(46, '2010-07-26 21:40:20', 1, 31, '33', 'Kutumia madaraka vibaya', 1, ''),
(47, '2010-07-26 21:40:39', 1, 31, '34', 'Makosa ya husuyo usimamizi wa haki', 1, ''),
(48, '2010-07-26 21:41:19', 1, 31, '35', 'Kuwakinga watumishi wa mahakama za sheria', 1, ''),
(49, '2010-07-26 21:41:52', 1, 31, '36', 'Kuendesha ovyo', 1, ''),
(50, '2010-07-26 21:42:08', 1, 31, '37', 'Mwendo kasi mkali', 1, ''),
(51, '2010-07-26 21:42:25', 1, 31, '38', 'Kutofunga mkanda', 1, ''),
(52, '2010-07-26 21:42:44', 1, 31, '39', 'Kukiuka taa za barabarani', 1, ''),
(53, '2010-07-26 21:43:16', 1, 31, '40', 'Gari ya mizigo kupakia abiria', 1, ''),
(54, '2010-07-26 22:04:47', 1, 19, '1', 'Allen Machary', 1, ''),
(55, '2010-07-26 22:05:18', 1, 19, '2', 'Salome Maro', 1, ''),
(56, '2010-07-26 22:05:54', 1, 19, '3', 'Irene Togolai', 1, ''),
(57, '2010-07-26 22:06:01', 1, 19, '2', 'Salome Maro', 2, 'Changed gender.'),
(58, '2010-07-26 22:06:33', 1, 19, '4', 'Auson Kisanga', 1, ''),
(59, '2010-07-26 22:07:28', 1, 20, '1', 'Name :John Francis   Age: 23', 1, ''),
(60, '2010-07-26 22:08:20', 1, 20, '2', 'Name :Adnan Salim   Age: 23', 1, ''),
(61, '2010-07-26 22:09:01', 1, 20, '3', 'Name :Sovello Hildebrand   Age: 25', 1, ''),
(62, '2010-07-26 22:09:29', 1, 18, '1', 'Forensic info in TCRO Number:1', 1, ''),
(63, '2010-07-26 22:09:43', 1, 18, '2', 'Forensic info in TCRO Number:2', 1, ''),
(64, '2010-07-26 22:10:00', 1, 18, '3', 'Forensic info in TCRO Number:3', 1, ''),
(65, '2010-07-26 22:10:21', 1, 22, '1', 'Name: Mbwana Mbura   Position: COPLO', 1, ''),
(66, '2010-07-26 22:10:33', 1, 22, '2', 'Name: Tumaini Foya   Position: OCD', 1, ''),
(67, '2010-07-26 22:10:48', 1, 22, '3', 'Name: Shaban Ally   Position: ODC', 1, ''),
(68, '2010-07-26 22:11:04', 1, 22, '4', 'Name: Mariam Ngaya   Position: COPLO', 1, ''),
(69, '2010-07-26 22:11:16', 1, 21, '1', 'Stollen: 50000000    Recovered: 40000', 1, ''),
(70, '2010-07-26 22:11:24', 1, 21, '2', 'Stollen: 64700000    Recovered: 834000', 1, ''),
(71, '2010-07-26 22:11:33', 1, 21, '3', 'Stollen: 89300000    Recovered: 178000', 1, ''),
(72, '2010-07-26 22:12:06', 1, 21, '6', 'Stollen: 562000    Recovered: 723400', 1, ''),
(73, '2010-07-26 22:12:30', 1, 16, '1', 'O-going', 1, ''),
(74, '2010-07-26 22:12:39', 1, 16, '2', 'On trial', 1, ''),
(75, '2010-07-26 22:12:48', 1, 16, '3', 'Case Closed', 1, ''),
(76, '2010-07-26 22:12:55', 1, 16, '4', 'Case discarded', 1, ''),
(77, '2010-07-26 22:13:02', 1, 16, '5', 'Case re-opened', 1, ''),
(78, '2010-07-26 22:13:56', 1, 23, '1', 'Case was challenging but fine    Date :2010-06-06', 1, ''),
(79, '2010-07-26 22:14:07', 1, 23, '2', 'Case had lot of trouble    Date :2010-04-17', 1, ''),
(80, '2010-07-26 22:14:24', 1, 23, '3', 'Case had many accomplices    Date :2010-07-06', 1, ''),
(81, '2010-07-26 22:14:44', 1, 23, '4', 'Case had one of our men injured badly    Date :2010-07-27', 1, ''),
(82, '2010-07-26 22:15:51', 1, 25, '1', 'Tanzania', 1, ''),
(83, '2010-07-26 22:15:54', 1, 26, '2', 'Dar es salaam', 1, ''),
(84, '2010-07-26 22:15:56', 1, 27, '3', 'Kinondoni', 1, ''),
(85, '2010-07-26 22:15:59', 1, 28, '4', 'Ubungo', 1, ''),
(86, '2010-07-26 22:16:02', 1, 29, '5', 'Mlimani', 1, ''),
(87, '2010-07-26 22:17:26', 1, 27, '6', 'Ilala', 1, ''),
(88, '2010-07-26 22:17:32', 1, 28, '7', 'Pugu Bombani', 1, ''),
(89, '2010-07-26 22:17:36', 1, 29, '8', 'Pugu Kajiungeni', 1, ''),
(90, '2010-07-26 22:18:11', 1, 28, '9', 'Posta', 1, ''),
(91, '2010-07-26 22:18:16', 1, 29, '10', 'City Centre', 1, ''),
(92, '2010-07-26 22:18:44', 1, 17, '1', 'Station:Mlimani IR Number:1', 1, ''),
(93, '2010-07-26 22:19:19', 1, 17, '2', 'Station:Mlimani IR Number:2', 1, ''),
(94, '2010-07-26 22:19:32', 1, 17, '3', 'Station:Mlimani IR Number:3', 1, ''),
(95, '2010-07-26 22:19:42', 1, 17, '4', 'Station:Pugu Kajiungeni IR Number:111', 1, ''),
(96, '2010-07-26 22:20:03', 1, 17, '5', 'Station:Pugu Kajiungeni IR Number:2', 1, ''),
(97, '2010-07-26 22:20:16', 1, 17, '6', 'Station:Pugu Kajiungeni IR Number:3', 1, ''),
(98, '2010-07-26 22:20:24', 1, 17, '7', 'Station:City Centre IR Number:1', 1, ''),
(99, '2010-07-26 22:20:30', 1, 17, '8', 'Station:City Centre IR Number:2', 1, ''),
(100, '2010-07-26 22:21:01', 1, 17, '4', 'Station:Pugu Kajiungeni IR Number:1', 2, 'Changed ir_number.'),
(101, '2010-07-26 22:21:37', 1, 15, '1', 'Report book: Station:Mlimani IR Number:1    Complainant Name :John Francis   Age: 23', 1, ''),
(102, '2010-07-26 22:21:56', 1, 15, '2', 'Report book: Station:Mlimani IR Number:2    Complainant Name :Adnan Salim   Age: 23', 1, ''),
(103, '2010-07-26 22:22:17', 1, 15, '3', 'Report book: Station:Pugu Kajiungeni IR Number:2    Complainant Name :Sovello Hildebrand   Age: 25', 1, ''),
(104, '2010-07-26 22:41:43', 1, 15, '22', 'Report book: Station:Pugu Kajiungeni IR Number:1    Complainant Name :Sovello Hildebrand   Age: 25', 2, 'Changed offense.');

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'message', 'auth', 'message'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'site', 'sites', 'site'),
(8, 'log entry', 'admin', 'logentry'),
(9, 'report', 'book', 'report'),
(10, 'reporter''s information', 'book', 'information'),
(11, 'detail', 'book', 'detail'),
(12, 'action', 'book', 'action'),
(13, 'accused', 'book', 'accused'),
(14, 'arrest', 'book', 'arrest'),
(15, 'register', 'investigation', 'register'),
(16, 'remark', 'investigation', 'remark'),
(17, 'report book', 'investigation', 'reportbook'),
(18, 'forensic', 'investigation', 'forensic'),
(19, 'accused', 'investigation', 'accused'),
(20, 'complainant', 'investigation', 'complainant'),
(21, 'property', 'investigation', 'property'),
(22, 'officer', 'investigation', 'officer'),
(23, 'result', 'investigation', 'result'),
(24, 'location', 'locations', 'location'),
(25, 'country', 'locations', 'country'),
(26, 'region', 'locations', 'region'),
(27, 'district', 'locations', 'district'),
(28, 'ward', 'locations', 'ward'),
(29, 'police station', 'locations', 'station'),
(30, 'offense category', 'offenses', 'offensecategory'),
(31, 'offense', 'offenses', 'offense'),
(32, 'station police', 'core', 'stationpolice'),
(33, 'police profile', 'core', 'policeprofile');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4a25296eca8c5e752fbb4af5b4c57961', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5kNzU4Mzc4MTY0MDE2NWY4MmVl\nMGQ3ZmZhYzk2MmUxMQ==\n', '2010-08-09 21:22:15');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_accused`
--

CREATE TABLE IF NOT EXISTS `investigation_accused` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `address` longtext,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `nationality` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `investigation_accused`
--

INSERT INTO `investigation_accused` (`id`, `first_name`, `last_name`, `address`, `age`, `gender`, `nationality`) VALUES
(1, 'Allen', 'Machary', 'KIMARA\r\nKINDONI\r\nDAR ES SALAAM', 23, 'M', 'Mchaga'),
(2, 'Salome', 'Maro', 'TEGETA\r\nKINONDONI\r\nDAR ES SALAAM', 23, 'F', 'Mchaga'),
(3, 'Irene', 'Togolai', 'KOROGWE\r\nTANGA', 23, 'F', 'Mpare'),
(4, 'Auson', 'Kisanga', 'KUNDUCHI\r\nKINONDONI\r\nDAR ES SALAAM', 23, 'M', 'Mhaya');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_complainant`
--

CREATE TABLE IF NOT EXISTS `investigation_complainant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `occupation` varchar(80) NOT NULL,
  `religion` varchar(80) NOT NULL,
  `tribe` varchar(80) NOT NULL,
  `residence` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `investigation_complainant`
--

INSERT INTO `investigation_complainant` (`id`, `first_name`, `last_name`, `age`, `occupation`, `religion`, `tribe`, `residence`) VALUES
(1, 'John', 'Francis', 23, 'Software Developer', 'Christian', 'Mhaya', 'PUGU SEC. SCHOOL\r\nUKONGA - ILALA\r\nDAR ES SLAAM\r\nTANZANIA'),
(2, 'Adnan', 'Salim', 23, 'System Analyst', 'Muslim', 'Mzigua', 'TABATA\r\nILALA\r\nDAR ES SALAAM\r\n'),
(3, 'Sovello', 'Hildebrand', 25, 'Engineer', 'Christian', 'Msukuma', 'HANDENI\r\nTANGA');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_forensic`
--

CREATE TABLE IF NOT EXISTS `investigation_forensic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tcro_number` int(11) NOT NULL,
  `dispatch_date` date NOT NULL,
  `return_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `investigation_forensic`
--

INSERT INTO `investigation_forensic` (`id`, `tcro_number`, `dispatch_date`, `return_date`) VALUES
(1, 1, '2010-06-14', '2010-07-23'),
(2, 2, '2010-05-17', '2010-06-16'),
(3, 3, '2009-09-05', '2010-05-25');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_officer`
--

CREATE TABLE IF NOT EXISTS `investigation_officer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `position` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `investigation_officer`
--

INSERT INTO `investigation_officer` (`id`, `first_name`, `last_name`, `position`) VALUES
(1, 'Mbwana', 'Mbura', 'COPLO'),
(2, 'Tumaini', 'Foya', 'OCD'),
(3, 'Shaban', 'Ally', 'ODC'),
(4, 'Mariam', 'Ngaya', 'COPLO');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_property`
--

CREATE TABLE IF NOT EXISTS `investigation_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stollen` int(11) NOT NULL,
  `recovered` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `investigation_property`
--

INSERT INTO `investigation_property` (`id`, `stollen`, `recovered`) VALUES
(1, 50000000, 40000),
(2, 64700000, 834000),
(3, 89300000, 178000),
(4, 2147483647, 2147483647),
(5, 2147483647, 723400),
(6, 562000, 723400);

-- --------------------------------------------------------

--
-- Table structure for table `investigation_register`
--

CREATE TABLE IF NOT EXISTS `investigation_register` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reportbook_id` int(11) NOT NULL,
  `complainant_id` int(11) NOT NULL,
  `property_id` int(11) NOT NULL,
  `officer_id` int(11) NOT NULL,
  `offense_id` int(11) NOT NULL,
  `accused_id` int(11) NOT NULL,
  `forensic_id` int(11) DEFAULT NULL,
  `results_id` int(11) NOT NULL,
  `remarks_id` int(11) NOT NULL,
  `court_case_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `investigation_register_reportbook_id` (`reportbook_id`),
  KEY `investigation_register_complainant_id` (`complainant_id`),
  KEY `investigation_register_property_id` (`property_id`),
  KEY `investigation_register_officer_id` (`officer_id`),
  KEY `investigation_register_offense_id` (`offense_id`),
  KEY `investigation_register_accused_id` (`accused_id`),
  KEY `investigation_register_forensic_id` (`forensic_id`),
  KEY `investigation_register_results_id` (`results_id`),
  KEY `investigation_register_remarks_id` (`remarks_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `investigation_register`
--

INSERT INTO `investigation_register` (`id`, `reportbook_id`, `complainant_id`, `property_id`, `officer_id`, `offense_id`, `accused_id`, `forensic_id`, `results_id`, `remarks_id`, `court_case_number`) VALUES
(1, 1, 1, 4, 3, 4, 2, 2, 4, 2, 1),
(2, 2, 2, 4, 2, 11, 3, 2, 3, 4, NULL),
(3, 5, 3, 4, 2, 7, 3, 3, 3, 3, NULL),
(4, 6, 1, 5, 3, 32, 2, 2, 1, 1, 1),
(5, 8, 1, 1, 2, 9, 2, 1, 3, 5, 2),
(6, 1, 3, 3, 1, 31, 1, 1, 2, 5, 3),
(7, 6, 3, 4, 3, 18, 1, 2, 1, 5, 4),
(8, 1, 1, 2, 3, 17, 2, 1, 2, 3, 5),
(9, 2, 3, 2, 4, 20, 2, 2, 1, 2, 6),
(10, 8, 3, 3, 1, 15, 3, 2, 1, 3, 7),
(11, 5, 1, 3, 1, 4, 3, 2, 1, 5, 8),
(12, 7, 3, 6, 3, 38, 1, 3, 1, 3, 9),
(13, 8, 2, 6, 2, 6, 2, 3, 1, 1, 10),
(14, 2, 3, 4, 1, 23, 2, 2, 3, 2, 11),
(15, 2, 1, 1, 4, 18, 2, 1, 2, 5, 12),
(16, 1, 3, 6, 3, 27, 1, 3, 3, 2, 13),
(17, 2, 3, 2, 2, 20, 4, 1, 2, 2, 14),
(18, 6, 2, 3, 1, 22, 1, 3, 1, 2, 15),
(19, 6, 1, 3, 1, 3, 2, 3, 3, 1, 16),
(20, 7, 2, 4, 3, 26, 3, 3, 1, 5, 17),
(21, 4, 2, 6, 3, 33, 4, 1, 3, 2, 18),
(22, 4, 3, 6, 3, 2, 2, 1, 1, 4, 19);

-- --------------------------------------------------------

--
-- Table structure for table `investigation_remark`
--

CREATE TABLE IF NOT EXISTS `investigation_remark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `investigation_remark`
--

INSERT INTO `investigation_remark` (`id`, `description`) VALUES
(1, 'O-going'),
(2, 'On trial'),
(3, 'Case Closed'),
(4, 'Case discarded'),
(5, 'Case re-opened');

-- --------------------------------------------------------

--
-- Table structure for table `investigation_reportbook`
--

CREATE TABLE IF NOT EXISTS `investigation_reportbook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `station_id` int(11) NOT NULL,
  `book_date` date NOT NULL,
  `ir_number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `investigation_reportbook_station_id` (`station_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `investigation_reportbook`
--

INSERT INTO `investigation_reportbook` (`id`, `station_id`, `book_date`, `ir_number`) VALUES
(1, 5, '2010-06-14', 1),
(2, 5, '2010-06-09', 2),
(3, 5, '2010-06-29', 3),
(4, 8, '2010-06-22', 1),
(5, 8, '2010-04-03', 2),
(6, 8, '2010-06-30', 3),
(7, 10, '2010-07-04', 1),
(8, 10, '2010-07-29', 2);

-- --------------------------------------------------------

--
-- Table structure for table `investigation_result`
--

CREATE TABLE IF NOT EXISTS `investigation_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `explanation` longtext NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `investigation_result`
--

INSERT INTO `investigation_result` (`id`, `explanation`, `date`) VALUES
(1, 'Case was challenging but fine', '2010-06-06'),
(2, 'Case had lot of trouble', '2010-04-17'),
(3, 'Case had many accomplices', '2010-07-06'),
(4, 'Case had one of our men injured badly', '2010-07-27');

-- --------------------------------------------------------

--
-- Table structure for table `locations_country`
--

CREATE TABLE IF NOT EXISTS `locations_country` (
  `location_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`location_ptr_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locations_country`
--

INSERT INTO `locations_country` (`location_ptr_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `locations_district`
--

CREATE TABLE IF NOT EXISTS `locations_district` (
  `location_ptr_id` int(11) NOT NULL,
  `region_id` int(11) NOT NULL,
  PRIMARY KEY (`location_ptr_id`),
  KEY `locations_district_region_id` (`region_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locations_district`
--

INSERT INTO `locations_district` (`location_ptr_id`, `region_id`) VALUES
(3, 2),
(6, 2);

-- --------------------------------------------------------

--
-- Table structure for table `locations_location`
--

CREATE TABLE IF NOT EXISTS `locations_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `code` varchar(30) DEFAULT NULL,
  `added_date` datetime NOT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `locations_location`
--

INSERT INTO `locations_location` (`id`, `name`, `code`, `added_date`, `modified_date`) VALUES
(1, 'Tanzania', '255', '2010-07-26 22:15:45', NULL),
(2, 'Dar es salaam', 'DSM', '2010-07-26 22:15:37', NULL),
(3, 'Kinondoni', 'KINO', '2010-07-26 22:15:24', NULL),
(4, 'Ubungo', 'UBUNGO', '2010-07-26 22:15:09', NULL),
(5, 'Mlimani', 'MLIMANI', '2010-07-26 22:14:57', NULL),
(6, 'Ilala', 'ILALA', '2010-07-26 22:16:34', NULL),
(7, 'Pugu Bombani', 'PUGU BOMBANI', '2010-07-26 22:16:17', NULL),
(8, 'Pugu Kajiungeni', 'KAJIUNGENI', '2010-07-26 22:16:02', NULL),
(9, 'Posta', 'POSTA', '2010-07-26 22:17:54', NULL),
(10, 'City Centre', 'CITY CENTRE', '2010-07-26 22:17:36', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `locations_region`
--

CREATE TABLE IF NOT EXISTS `locations_region` (
  `location_ptr_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`location_ptr_id`),
  KEY `locations_region_country_id` (`country_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locations_region`
--

INSERT INTO `locations_region` (`location_ptr_id`, `country_id`) VALUES
(2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `locations_station`
--

CREATE TABLE IF NOT EXISTS `locations_station` (
  `location_ptr_id` int(11) NOT NULL,
  `ward_id` int(11) NOT NULL,
  PRIMARY KEY (`location_ptr_id`),
  KEY `locations_station_ward_id` (`ward_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locations_station`
--

INSERT INTO `locations_station` (`location_ptr_id`, `ward_id`) VALUES
(5, 4),
(8, 7),
(10, 9);

-- --------------------------------------------------------

--
-- Table structure for table `locations_ward`
--

CREATE TABLE IF NOT EXISTS `locations_ward` (
  `location_ptr_id` int(11) NOT NULL,
  `district_id` int(11) NOT NULL,
  PRIMARY KEY (`location_ptr_id`),
  KEY `locations_ward_district_id` (`district_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locations_ward`
--

INSERT INTO `locations_ward` (`location_ptr_id`, `district_id`) VALUES
(4, 3),
(7, 6),
(9, 3);

-- --------------------------------------------------------

--
-- Table structure for table `offenses_offense`
--

CREATE TABLE IF NOT EXISTS `offenses_offense` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `offense_category_id` int(11) NOT NULL,
  `offense_title` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `offenses_offense_offense_category_id` (`offense_category_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=41 ;

--
-- Dumping data for table `offenses_offense`
--

INSERT INTO `offenses_offense` (`id`, `offense_category_id`, `offense_title`) VALUES
(1, 1, 'Madawa ya kulevya'),
(2, 1, 'Banghi'),
(3, 1, 'Mirungi'),
(4, 1, 'Nyaraka za serikali'),
(5, 1, 'Magendo'),
(6, 1, 'Rushwa'),
(7, 1, 'Pombe ya moshi'),
(8, 1, 'Mitambo ya pombe ya moshi'),
(9, 1, 'Kupatikana na risasi'),
(10, 1, 'Kupatikana na silaha'),
(11, 2, 'Wizi wa silaha'),
(12, 2, 'Unyang''anyi wa kutumia silaha'),
(13, 2, 'Unyang''anyi wa kutumia nguvu'),
(14, 2, 'Wizi wa kwenye mabenki'),
(15, 2, 'Wizi kwenye serikali za mitaa'),
(16, 2, 'Kuchoma moto nyumba'),
(17, 3, 'Mauaji'),
(18, 3, 'Kubaka'),
(19, 3, 'Wizi wa watoto'),
(20, 3, 'Kutoa mimba'),
(21, 3, 'Kutorosha watoto'),
(22, 3, 'Kumtaja mtu mchawi'),
(23, 3, 'Kujaribu kujiua'),
(24, 6, 'Kuchocheza mashambulio'),
(25, 6, 'Kuficha uhahini'),
(26, 6, 'Kuleta vita vya wenyeji'),
(27, 7, 'Mihuri ya kubuni'),
(28, 7, 'Tume za siri'),
(29, 7, 'Kujifanya mtu mwingine'),
(30, 8, 'Ushawishi wa uchochezi'),
(31, 8, 'Waficha uhalifu'),
(32, 8, 'Njama'),
(33, 9, 'Kutumia madaraka vibaya'),
(34, 9, 'Makosa ya husuyo usimamizi wa haki'),
(35, 9, 'Kuwakinga watumishi wa mahakama za sheria'),
(36, 10, 'Kuendesha ovyo'),
(37, 10, 'Mwendo kasi mkali'),
(38, 11, 'Kutofunga mkanda'),
(39, 11, 'Kukiuka taa za barabarani'),
(40, 10, 'Gari ya mizigo kupakia abiria');

-- --------------------------------------------------------

--
-- Table structure for table `offenses_offensecategory`
--

CREATE TABLE IF NOT EXISTS `offenses_offensecategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `offense_section` varchar(20) NOT NULL,
  `rank` varchar(14) NOT NULL,
  `category_name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_name` (`category_name`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `offenses_offensecategory`
--

INSERT INTO `offenses_offensecategory` (`id`, `offense_section`, `rank`, `category_name`) VALUES
(1, 'CRIMINAL', 'MAJOR', 'Makosa dhidi ya maadili ya jamii'),
(2, 'CRIMINAL', 'MAJOR', 'Makosa ya kuwania mali'),
(3, 'CRIMINAL', 'MAJOR', 'Makosa dhidi ya binadamu'),
(4, 'TRAFFIC', 'MAJOR', 'Ajali za majeruhi'),
(5, 'TRAFFIC', 'MAJOR', 'Ajali za vifo'),
(6, 'CRIMINAL', 'MINOR', 'Makosa ya kuvunja utulivu'),
(7, 'CRIMINAL', 'MINOR', 'Makosa ya maandishi ya kubuni, utengenezaji sarafu na sawa na hayo'),
(8, 'CRIMINAL', 'MINOR', 'Makosa ya majaribio, njama za kutenda au uhalifu'),
(9, 'CRIMINAL', 'MINOR', 'Makosa juu ya usimamizi wa mamlaka halai'),
(10, 'TRAFFIC', 'MINOR', 'Makosa ya uzembe barabani'),
(11, 'TRAFFIC', 'MINOR', 'Makosa ya kupuuzia sheria za barabarani');
