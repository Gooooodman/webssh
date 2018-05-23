/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.21 : Database - xyf
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`xyf` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `xyf`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (2,'Can change log entry',1,'change_logentry');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (3,'Can delete log entry',1,'delete_logentry');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (4,'Can view log entry',1,'view_logentry');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (5,'Can add group',2,'add_group');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (6,'Can change group',2,'change_group');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (7,'Can delete group',2,'delete_group');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (8,'Can add permission',3,'add_permission');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (9,'Can change permission',3,'change_permission');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (10,'Can delete permission',3,'delete_permission');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (11,'Can add user',4,'add_user');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (12,'Can change user',4,'change_user');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (13,'Can delete user',4,'delete_user');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (14,'Can view group',2,'view_group');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (15,'Can view permission',3,'view_permission');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (16,'Can view user',4,'view_user');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (17,'Can add content type',5,'add_contenttype');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (18,'Can change content type',5,'change_contenttype');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (19,'Can delete content type',5,'delete_contenttype');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (20,'Can view content type',5,'view_contenttype');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (21,'Can add session',6,'add_session');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (22,'Can change session',6,'change_session');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (23,'Can delete session',6,'delete_session');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (24,'Can view session',6,'view_session');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (25,'Can add CMD结果',7,'add_cmd_log');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (26,'Can change CMD结果',7,'change_cmd_log');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (27,'Can delete CMD结果',7,'delete_cmd_log');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (28,'Can add 主机SSH用户',8,'add_sshuser');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (29,'Can change 主机SSH用户',8,'change_sshuser');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (30,'Can delete 主机SSH用户',8,'delete_sshuser');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (31,'Can add 主机分组',9,'add_hostgroup');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (32,'Can change 主机分组',9,'change_hostgroup');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (33,'Can delete 主机分组',9,'delete_hostgroup');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (34,'Can add CMD记录',10,'add_cmd');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (35,'Can change CMD记录',10,'change_cmd');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (36,'Can delete CMD记录',10,'delete_cmd');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (37,'Can add 常用命令/脚本',11,'add_sh');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (38,'Can change 常用命令/脚本',11,'change_sh');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (39,'Can delete 常用命令/脚本',11,'delete_sh');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (40,'Can add 主机',12,'add_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (41,'Can change 主机',12,'change_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (42,'Can delete 主机',12,'delete_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (43,'Can deploy host',12,'deploy_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (44,'Can webssh host',12,'webssh_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (45,'Can grep host',12,'grep_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (46,'Can run_sh host',12,'run_sh_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (47,'Can run_cmd host',12,'run_cmd_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (48,'Can other_do host',12,'other_do_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (49,'Can view CMD记录',10,'view_cmd');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (50,'Can view CMD结果',7,'view_cmd_log');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (51,'Can view 主机',12,'view_host');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (52,'Can view 主机分组',9,'view_hostgroup');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (53,'Can view 常用命令/脚本',11,'view_sh');
insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (54,'Can view 主机SSH用户',8,'view_sshuser');;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$36000$yKoLTqUjHegR$m5QG57Jc41XOddYqIDUksgiNnyHszo+Wb/ivk1X83gA=','2018-05-23 09:56:30',1,'xyf','','','xyf@xyf.com',1,1,'2018-05-23 09:56:09');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `cmdb_cmd` */

DROP TABLE IF EXISTS `cmdb_cmd`;

CREATE TABLE `cmdb_cmd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cmd` longtext NOT NULL,
  `ctype` smallint(6) DEFAULT NULL,
  `text` longtext,
  `createtime` datetime DEFAULT NULL,
  `end` tinyint(1) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cmdb_cmd_user_id_a8b87ae9_fk_auth_user_id` (`user_id`),
  CONSTRAINT `cmdb_cmd_user_id_a8b87ae9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_cmd` */

/*Table structure for table `cmdb_cmd_host` */

DROP TABLE IF EXISTS `cmdb_cmd_host`;

CREATE TABLE `cmdb_cmd_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cmd_id` int(11) NOT NULL,
  `host_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_cmd_host_cmd_id_host_id_a16a2a28_uniq` (`cmd_id`,`host_id`),
  KEY `cmdb_cmd_host_host_id_d5233af9_fk_cmdb_host_id` (`host_id`),
  CONSTRAINT `cmdb_cmd_host_cmd_id_46175922_fk_cmdb_cmd_id` FOREIGN KEY (`cmd_id`) REFERENCES `cmdb_cmd` (`id`),
  CONSTRAINT `cmdb_cmd_host_host_id_d5233af9_fk_cmdb_host_id` FOREIGN KEY (`host_id`) REFERENCES `cmdb_host` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_cmd_host` */

/*Table structure for table `cmdb_cmd_log` */

DROP TABLE IF EXISTS `cmdb_cmd_log`;

CREATE TABLE `cmdb_cmd_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` datetime DEFAULT NULL,
  `text` longtext,
  `cmd_id` int(11) NOT NULL,
  `host_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cmdb_cmd_log_cmd_id_563ed8aa_fk_cmdb_cmd_id` (`cmd_id`),
  KEY `cmdb_cmd_log_host_id_497f94bd_fk_cmdb_host_id` (`host_id`),
  CONSTRAINT `cmdb_cmd_log_cmd_id_563ed8aa_fk_cmdb_cmd_id` FOREIGN KEY (`cmd_id`) REFERENCES `cmdb_cmd` (`id`),
  CONSTRAINT `cmdb_cmd_log_host_id_497f94bd_fk_cmdb_host_id` FOREIGN KEY (`host_id`) REFERENCES `cmdb_host` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_cmd_log` */

/*Table structure for table `cmdb_host` */

DROP TABLE IF EXISTS `cmdb_host`;

CREATE TABLE `cmdb_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `hostname` varchar(50) NOT NULL,
  `ip` char(39) NOT NULL,
  `port` int(11) DEFAULT NULL,
  `other_ip` varchar(100) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `asset_type` smallint(6) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `cpu_model` varchar(100) DEFAULT NULL,
  `cpu_num` varchar(100) DEFAULT NULL,
  `memory` varchar(30) DEFAULT NULL,
  `disk` varchar(255) DEFAULT NULL,
  `vendor` varchar(150) DEFAULT NULL,
  `sn` varchar(150) DEFAULT NULL,
  `ports` longtext,
  `createtime` datetime DEFAULT NULL,
  `changetime` datetime DEFAULT NULL,
  `agenttime` datetime DEFAULT NULL,
  `buydate` date DEFAULT NULL,
  `position` varchar(250) DEFAULT NULL,
  `sernumb` varchar(150) DEFAULT NULL,
  `sercode` varchar(150) DEFAULT NULL,
  `tomcat` varchar(100) NOT NULL,
  `tomcat_ver` varchar(50) NOT NULL,
  `jdk_ver` varchar(50) NOT NULL,
  `kernel` varchar(60) NOT NULL,
  `text` longtext,
  `admin_id` int(11) DEFAULT NULL,
  `group_id` int(11),
  `machine_id` int(11) DEFAULT NULL,
  `ssh_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  KEY `cmdb_host_admin_id_02740357_fk_auth_user_id` (`admin_id`),
  KEY `cmdb_host_group_id_bcc2faaa_fk_cmdb_hostgroup_id` (`group_id`),
  KEY `cmdb_host_machine_id_c7f9f667_fk_cmdb_host_id` (`machine_id`),
  KEY `cmdb_host_ssh_user_id_f4ee2e86_fk_cmdb_sshuser_id` (`ssh_user_id`),
  CONSTRAINT `cmdb_host_admin_id_02740357_fk_auth_user_id` FOREIGN KEY (`admin_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `cmdb_host_group_id_bcc2faaa_fk_cmdb_hostgroup_id` FOREIGN KEY (`group_id`) REFERENCES `cmdb_hostgroup` (`id`),
  CONSTRAINT `cmdb_host_machine_id_c7f9f667_fk_cmdb_host_id` FOREIGN KEY (`machine_id`) REFERENCES `cmdb_host` (`id`),
  CONSTRAINT `cmdb_host_ssh_user_id_f4ee2e86_fk_cmdb_sshuser_id` FOREIGN KEY (`ssh_user_id`) REFERENCES `cmdb_sshuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_host` */

insert  into `cmdb_host`(`id`,`name`,`hostname`,`ip`,`port`,`other_ip`,`status`,`asset_type`,`os`,`cpu_model`,`cpu_num`,`memory`,`disk`,`vendor`,`sn`,`ports`,`createtime`,`changetime`,`agenttime`,`buydate`,`position`,`sernumb`,`sercode`,`tomcat`,`tomcat_ver`,`jdk_ver`,`kernel`,`text`,`admin_id`,`group_id`,`machine_id`,`ssh_user_id`) values (1,'1111','www','192.168.80.238',22,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'','2018-05-23 10:03:52','2018-05-23 10:52:21',NULL,'2018-05-23',NULL,NULL,NULL,'/data/app/tomcat','','','','',NULL,3,NULL,1);

/*Table structure for table `cmdb_host_user` */

DROP TABLE IF EXISTS `cmdb_host_user`;

CREATE TABLE `cmdb_host_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_host_user_host_id_user_id_a4322dbf_uniq` (`host_id`,`user_id`),
  KEY `cmdb_host_user_user_id_7f436184_fk_auth_user_id` (`user_id`),
  CONSTRAINT `cmdb_host_user_host_id_f5755e3c_fk_cmdb_host_id` FOREIGN KEY (`host_id`) REFERENCES `cmdb_host` (`id`),
  CONSTRAINT `cmdb_host_user_user_id_7f436184_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_host_user` */

/*Table structure for table `cmdb_host_usergroup` */

DROP TABLE IF EXISTS `cmdb_host_usergroup`;

CREATE TABLE `cmdb_host_usergroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_host_usergroup_host_id_group_id_6e69ad5e_uniq` (`host_id`,`group_id`),
  KEY `cmdb_host_usergroup_group_id_aa9843b0_fk_auth_group_id` (`group_id`),
  CONSTRAINT `cmdb_host_usergroup_group_id_aa9843b0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `cmdb_host_usergroup_host_id_808fccdb_fk_cmdb_host_id` FOREIGN KEY (`host_id`) REFERENCES `cmdb_host` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_host_usergroup` */

/*Table structure for table `cmdb_hostgroup` */

DROP TABLE IF EXISTS `cmdb_hostgroup`;

CREATE TABLE `cmdb_hostgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `ip` varchar(20) NOT NULL,
  `desc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_hostgroup` */

insert  into `cmdb_hostgroup`(`id`,`name`,`ip`,`desc`) values (3,'组1','',NULL);
insert  into `cmdb_hostgroup`(`id`,`name`,`ip`,`desc`) values (4,'组2','',NULL);

/*Table structure for table `cmdb_sh` */

DROP TABLE IF EXISTS `cmdb_sh`;

CREATE TABLE `cmdb_sh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `sh` smallint(6) DEFAULT NULL,
  `cmd` longtext,
  `text` longtext,
  `createtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_sh_sh_fname_7195a6c2_uniq` (`sh`,`fname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_sh` */

/*Table structure for table `cmdb_sshuser` */

DROP TABLE IF EXISTS `cmdb_sshuser`;

CREATE TABLE `cmdb_sshuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `changetime` datetime DEFAULT NULL,
  `text` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_sshuser_name_username_883fa28d_uniq` (`name`,`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `cmdb_sshuser` */

insert  into `cmdb_sshuser`(`id`,`name`,`username`,`password`,`changetime`,`text`) values (1,'80.238','root','sdTSKtzVa2VQYxiCWi4ZEQ==','2018-05-23 10:51:33','');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

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
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (1,'2018-05-23 10:06:06','1','1',1,'[{\"added\": {}}]',9,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (2,'2018-05-23 10:06:08','2','2',1,'[{\"added\": {}}]',9,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (3,'2018-05-23 10:06:18','1','1111 - 192.168.80.11',2,'[{\"changed\": {\"fields\": [\"group\"]}}]',12,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (4,'2018-05-23 10:48:29','1','1111 - 192.168.80.11',2,'[{\"changed\": {\"fields\": [\"group\"]}}]',12,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (5,'2018-05-23 10:48:43','1','1',3,'',9,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (6,'2018-05-23 10:48:43','2','2',3,'',9,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (7,'2018-05-23 10:51:33','1','80.238 - root',1,'[{\"added\": {}}]',8,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (8,'2018-05-23 10:51:54','1','1111 - 192.168.80.238',2,'[{\"changed\": {\"fields\": [\"ssh_user\"]}}]',12,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (9,'2018-05-23 10:52:05','3','组1',1,'[{\"added\": {}}]',9,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (10,'2018-05-23 10:52:10','4','组2',1,'[{\"added\": {}}]',9,1);
insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (11,'2018-05-23 10:52:21','1','1111 - 192.168.80.238',2,'[{\"changed\": {\"fields\": [\"group\"]}}]',12,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (2,'auth','group');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (3,'auth','permission');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (4,'auth','user');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (10,'cmdb','cmd');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (7,'cmdb','cmd_log');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (12,'cmdb','host');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (9,'cmdb','hostgroup');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (11,'cmdb','sh');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (8,'cmdb','sshuser');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (5,'contenttypes','contenttype');
insert  into `django_content_type`(`id`,`app_label`,`model`) values (6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (2,'auth','0001_initial','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (3,'admin','0001_initial','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (4,'admin','0002_logentry_remove_auto_add','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (5,'contenttypes','0002_remove_content_type_name','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (6,'auth','0002_alter_permission_name_max_length','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (7,'auth','0003_alter_user_email_max_length','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (8,'auth','0004_alter_user_username_opts','2018-05-23 09:31:00');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (9,'auth','0005_alter_user_last_login_null','2018-05-23 09:31:01');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (10,'auth','0006_require_contenttypes_0002','2018-05-23 09:31:01');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (11,'auth','0007_alter_validators_add_error_messages','2018-05-23 09:31:01');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (12,'auth','0008_alter_user_username_max_length','2018-05-23 09:31:01');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (13,'cmdb','0001_initial','2018-05-23 09:31:02');
insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (14,'sessions','0001_initial','2018-05-23 09:31:02');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('cct8e6s7uk7cgxojc9ayqm92ndixztas','NjZmNjE3MWRjZTI5MTRmOTViODIyNTQzZTdlZmU5NzRhNjg3MGQzOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMyNWNlNThlODgzMmU4Y2M0ODMyZDU4Yjc3NzdmMWNjOWM0YmZhYjAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2018-06-06 09:56:30');
insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('chn85ae50d193495ad8d8e9cde900eee','MTI5NmE1YzE5MWU4NDE1YzQ3ZDRmMzFkYmZiNzY0Nzc2MWRmYmIyNjp7InNlc3Npb25pZCI6ImNjdDhlNnM3dWs3Y2d4b2pjOWF5cW05Mm5kaXh6dGFzIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzI1Y2U1OGU4ODMyZThjYzQ4MzJkNThiNzc3N2YxY2M5YzRiZmFiMCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2018-06-06 10:53:53');
insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('chn98b7555f7a8d53218d52413ad5428','MTI5NmE1YzE5MWU4NDE1YzQ3ZDRmMzFkYmZiNzY0Nzc2MWRmYmIyNjp7InNlc3Npb25pZCI6ImNjdDhlNnM3dWs3Y2d4b2pjOWF5cW05Mm5kaXh6dGFzIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzI1Y2U1OGU4ODMyZThjYzQ4MzJkNThiNzc3N2YxY2M5YzRiZmFiMCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2018-06-06 10:52:32');
insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('chnb31cc5385956bd5056d8ea3550434','MjgwZDkyM2NmN2Y5NjE4MTc5MzgwMjM3Yzc5OGJkZTdjMTFmNDIzNDp7InNlc3Npb25pZCI6ImNjdDhlNnM3dWs3Y2d4b2pjOWF5cW05Mm5kaXh6dGFzIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzI1Y2U1OGU4ODMyZThjYzQ4MzJkNThiNzc3N2YxY2M5YzRiZmFiMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2018-06-06 10:56:21');
insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('chnbe803073a43e0f470907915987614','MTI5NmE1YzE5MWU4NDE1YzQ3ZDRmMzFkYmZiNzY0Nzc2MWRmYmIyNjp7InNlc3Npb25pZCI6ImNjdDhlNnM3dWs3Y2d4b2pjOWF5cW05Mm5kaXh6dGFzIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzI1Y2U1OGU4ODMyZThjYzQ4MzJkNThiNzc3N2YxY2M5YzRiZmFiMCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2018-06-06 10:52:35');
insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('chnbeb7b5a63dfb1f7c634493120b508','MTI5NmE1YzE5MWU4NDE1YzQ3ZDRmMzFkYmZiNzY0Nzc2MWRmYmIyNjp7InNlc3Npb25pZCI6ImNjdDhlNnM3dWs3Y2d4b2pjOWF5cW05Mm5kaXh6dGFzIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzI1Y2U1OGU4ODMyZThjYzQ4MzJkNThiNzc3N2YxY2M5YzRiZmFiMCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2018-06-06 10:52:37');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
