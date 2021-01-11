/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : clockodillo

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 20/12/2020 10:21:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for blacklist_tokens
-- ----------------------------
DROP TABLE IF EXISTS `blacklist_tokens`;
CREATE TABLE `blacklist_tokens` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(1000) DEFAULT NULL,
  `blacklisted_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of blacklist_tokens
-- ----------------------------
BEGIN;
INSERT INTO `blacklist_tokens` VALUES (13, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDg0NjQ0NDMsImlhdCI6MTYwODM3ODAzOCwic3ViIjo2fQ.6ebGrWZUyCYqeKaB8aP_FmLXk5K0Q-rHXPOKpI-OAhQ', '2020-12-19 17:15:17');
COMMIT;

-- ----------------------------
-- Table structure for device
-- ----------------------------
DROP TABLE IF EXISTS `device`;
CREATE TABLE `device` (
  `id` int NOT NULL AUTO_INCREMENT,
  `device_name` varchar(255) DEFAULT NULL,
  `mac_address` varchar(255) DEFAULT NULL,
  `is_active` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for timer
-- ----------------------------
DROP TABLE IF EXISTS `timer`;
CREATE TABLE `timer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timer_duration` float DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `mac_address` varchar(500) DEFAULT NULL,
  `is_complete` int DEFAULT NULL,
  `is_cancel` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `device_id` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of timer
-- ----------------------------
BEGIN;
INSERT INTO `timer` VALUES (1, 15, 'mac for time generator', '24RTX-90OPL', 0, 0, 6, NULL, '2020-12-20 08:34:20', '2020-12-20 08:34:20');
INSERT INTO `timer` VALUES (2, 200, 'Test Description', NULL, 1, 0, 6, NULL, '2020-12-20 08:37:39', '2020-12-20 10:20:06');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_tfa` tinyint(1) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (6, 'janith2011@gmail.com', '$2b$12$5TAr3sR2PNFBMY2Q1AAo0.SBcyKlqksL9r9jAKFwpwuJaMVtQBSVS', '2020-12-19 16:59:16', 1, 0, 1);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
