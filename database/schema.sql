-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 29, 2025 at 06:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital_bed_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `admissions`
--

CREATE TABLE `admissions` (
  `admission_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `bed_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `admission_date` datetime NOT NULL,
  `discharge_date` datetime DEFAULT NULL,
  `admission_reason` varchar(255) NOT NULL,
  `status` enum('active','discharged','transferred') DEFAULT 'active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `reason_for_admission` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admissions`
--

INSERT INTO `admissions` (`admission_id`, `patient_id`, `bed_id`, `doctor_id`, `admission_date`, `discharge_date`, `admission_reason`, `status`, `created_at`, `updated_at`, `reason_for_admission`) VALUES
(32, 1, 1, 2, '2025-10-14 23:15:35', '2025-10-18 23:15:35', 'Stomach Flu', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(33, 2, 2, 2, '2025-10-19 23:15:35', '2025-10-21 23:15:35', 'Asthma Exacerbation', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(34, 8, 5, 2, '2025-10-09 23:15:35', '2025-10-17 23:15:35', 'Pneumonia', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(35, 9, 10, 2, '2025-09-29 23:15:35', '2025-10-06 23:15:35', 'Severe Dengue Fever', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(36, 10, 11, 2, '2025-10-24 23:15:35', '2025-10-27 23:15:35', 'Maternity', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(37, 3, 4, 2, '2025-10-24 23:15:35', NULL, 'Heart Disease', 'active', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(38, 4, 12, 2, '2025-10-19 23:15:35', NULL, 'Chronic Renal Failure', 'active', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(39, 5, 3, 2, '2025-10-26 23:15:35', NULL, 'Compound Fracture', 'active', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(40, 6, 13, 2, '2025-10-28 23:15:35', NULL, 'Post-Surgical Infection', 'active', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(41, 7, 14, 2, '2025-10-14 23:15:35', NULL, 'Severe COVID ARDS', 'active', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(42, 11, 15, 2, '2025-09-19 23:15:35', '2025-09-22 23:15:35', 'Gastroenteritis', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(43, 12, 16, 2, '2025-09-24 23:15:35', '2025-10-04 23:15:35', 'Minor Stroke Rehabilitation', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(44, 13, 17, 2, '2025-10-09 23:15:35', '2025-10-16 23:15:35', 'Bilateral Knee Replacement', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(45, 14, 18, 2, '2025-10-11 23:15:35', '2025-10-16 23:15:35', 'Appendicitis, post-op', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(46, 18, 19, 2, '2025-10-15 23:15:35', '2025-10-21 23:15:35', 'Road Traffic Accident (RTA)', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(47, 20, 20, 2, '2025-10-19 23:15:35', '2025-10-23 23:15:35', 'Chronic Pain Management', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(48, 21, 21, 2, '2025-10-21 23:15:35', '2025-10-26 23:15:35', 'Severe Dehydration, Elderly', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(49, 22, 22, 2, '2025-10-24 23:15:35', '2025-10-26 23:15:35', 'Flu/Viral Fever', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(50, 24, 26, 2, '2025-10-26 23:15:35', '2025-10-28 23:15:35', 'Post-Op Complication (Minor)', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(51, 25, 29, 2, '2025-10-11 23:15:35', '2025-10-19 23:15:35', 'Severe Dementia, Fall Injury', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(52, 15, 23, 2, '2025-09-14 23:15:35', '2025-09-26 23:15:35', 'Acute Myocardial Infarction (AMI)', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(53, 16, 24, 2, '2025-09-29 23:15:35', '2025-10-08 23:15:35', 'Severe Eclampsia', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(54, 17, 25, 2, '2025-10-13 23:15:35', '2025-10-28 23:15:35', 'Sepsis, Unknown Primary Source', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(55, 19, 27, 2, '2025-10-04 23:15:35', '2025-10-24 23:15:35', 'Tuberculosis (Active)', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL),
(56, 23, 28, 2, '2025-10-09 23:15:35', '2025-10-23 23:15:35', 'COVID-19 Positive', 'discharged', '2025-10-29 17:45:35', '2025-10-29 17:45:35', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `alos_statistics`
--

CREATE TABLE `alos_statistics` (
  `stat_id` int(11) NOT NULL,
  `bed_type` enum('general','icu','isolation') NOT NULL,
  `average_los` decimal(5,2) DEFAULT NULL,
  `total_admissions` int(11) DEFAULT 0,
  `total_days` int(11) DEFAULT 0,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alos_statistics`
--

INSERT INTO `alos_statistics` (`stat_id`, `bed_type`, `average_los`, `total_admissions`, `total_days`, `updated_at`) VALUES
(1, 'general', 4.83, 12, 58, '2025-10-29 17:46:07'),
(2, 'icu', 9.50, 4, 38, '2025-10-29 17:46:07'),
(3, 'isolation', 12.50, 4, 50, '2025-10-29 17:46:07');

-- --------------------------------------------------------

--
-- Table structure for table `audit_logs`
--

CREATE TABLE `audit_logs` (
  `log_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `action` varchar(255) NOT NULL,
  `table_name` varchar(50) DEFAULT NULL,
  `record_id` int(11) DEFAULT NULL,
  `old_value` text DEFAULT NULL,
  `new_value` text DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `audit_logs`
--

INSERT INTO `audit_logs` (`log_id`, `user_id`, `action`, `table_name`, `record_id`, `old_value`, `new_value`, `timestamp`) VALUES
(1, 1, 'Added new bed', 'beds', 6, NULL, NULL, '2025-10-29 16:11:05'),
(2, 2, 'Admitted new patient', 'admissions', 0, NULL, NULL, '2025-10-29 16:37:11'),
(3, 2, 'Transferred patient bed', 'bed_transfers', 0, NULL, NULL, '2025-10-29 16:37:44'),
(4, 2, 'Discharged patient', 'admissions', 1, NULL, NULL, '2025-10-29 16:37:56');

-- --------------------------------------------------------

--
-- Table structure for table `beds`
--

CREATE TABLE `beds` (
  `bed_id` int(11) NOT NULL,
  `bed_number` varchar(20) NOT NULL,
  `ward` varchar(50) NOT NULL,
  `bed_type` enum('general','icu','isolation') NOT NULL,
  `status` enum('available','occupied','maintenance') DEFAULT 'available',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `beds`
--

INSERT INTO `beds` (`bed_id`, `bed_number`, `ward`, `bed_type`, `status`, `created_at`, `updated_at`) VALUES
(1, 'B-GEN-001', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(2, 'B-GEN-002', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(3, 'B-GEN-003', 'Ward A', 'general', 'occupied', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(4, 'B-ICU-001', 'Ward B', 'icu', 'occupied', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(5, 'B-ISO-001', 'Ward C', 'isolation', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(6, 'B-ICU-002', 'Ward B', 'icu', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(7, 'B-GEN-004', 'Ward D', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(8, 'B-GEN-005', 'Ward D', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(9, 'B-ISO-002', 'Ward C', 'isolation', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(10, 'B-GEN-006', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(11, 'B-GEN-007', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(12, 'B-ICU-003', 'Ward B', 'icu', 'occupied', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(13, 'B-ISO-003', 'Ward C', 'isolation', 'occupied', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(14, 'B-ICU-004', 'Ward B', 'icu', 'occupied', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(15, 'B-GEN-008', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(16, 'B-GEN-009', 'Ward D', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(17, 'B-GEN-010', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(18, 'B-GEN-011', 'Ward D', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(19, 'B-GEN-012', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(20, 'B-GEN-013', 'Ward D', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(21, 'B-GEN-014', 'Ward A', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(22, 'B-GEN-015', 'Ward D', 'general', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(23, 'B-ICU-005', 'Ward B', 'icu', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(24, 'B-ICU-006', 'Ward B', 'icu', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(25, 'B-ICU-007', 'Ward B', 'icu', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(26, 'B-ICU-008', 'Ward B', 'icu', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(27, 'B-ISO-004', 'Ward C', 'isolation', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(28, 'B-ISO-005', 'Ward C', 'isolation', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(29, 'B-ISO-006', 'Ward C', 'isolation', 'available', '2025-10-29 17:45:35', '2025-10-29 17:45:35');

-- --------------------------------------------------------

--
-- Table structure for table `bed_transfers`
--

CREATE TABLE `bed_transfers` (
  `transfer_id` int(11) NOT NULL,
  `admission_id` int(11) NOT NULL,
  `from_bed_id` int(11) NOT NULL,
  `to_bed_id` int(11) NOT NULL,
  `transfer_date` datetime NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `patient_id` int(11) NOT NULL,
  `patient_name` varchar(100) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` enum('M','F','Other') DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `medical_history` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`patient_id`, `patient_name`, `age`, `gender`, `contact_number`, `medical_history`, `created_at`, `updated_at`) VALUES
(1, 'John Doe', 45, 'M', '555-0001', 'Hypertension, Diabetes', '2025-10-29 15:18:10', '2025-10-29 15:18:10'),
(2, 'Jane Smith', 32, 'F', '555-0002', 'Asthma', '2025-10-29 15:18:10', '2025-10-29 15:18:10'),
(3, 'Robert Johnson', 68, 'M', '555-0003', 'Heart Disease', '2025-10-29 15:18:10', '2025-10-29 15:18:10'),
(4, 'Rina Das', 55, 'F', '9876543210', 'Chronic Renal Failure, Hypertension', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(5, 'Arjun Singh', 28, 'M', '9988776655', 'Compound Fracture, Needs Surgery', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(6, 'Fatima Mirza', 62, 'F', '9001122334', 'Post-Surgical Infection', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(7, 'Karthik Nair', 40, 'M', '8080808080', 'Acute Respiratory Distress Syndrome (ARDS)', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(8, 'Leela Devi', 78, 'F', '7776665554', 'Community Acquired Pneumonia', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(9, 'Pranav Sharma', 35, 'M', '9119119119', 'Severe Dengue Fever', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(10, 'Neha Singh', 22, 'F', '8887776665', 'Maternity/Post-Partum Care', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(11, 'Suresh Patil', 48, 'M', '8989898989', 'Gastroenteritis', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(12, 'Geeta Varma', 52, 'F', '7878787878', 'Minor Stroke Rehabilitation', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(13, 'Mohan Joshi', 70, 'M', '9090909090', 'Bilateral Knee Replacement', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(14, 'Kiran Rao', 25, 'F', '9191919191', 'Appendicitis, post-op', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(15, 'Vimal Singh', 65, 'M', '8080808080', 'Acute Myocardial Infarction (AMI)', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(16, 'Pooja Nair', 38, 'F', '7070707070', 'Severe Eclampsia', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(17, 'Deepak Kumar', 55, 'M', '9292929292', 'Sepsis, Unknown Primary Source', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(18, 'Anjali Menon', 29, 'F', '9393939393', 'Road Traffic Accident (RTA)', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(19, 'Rakesh Shah', 60, 'M', '9494949494', 'Tuberculosis (Active)', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(20, 'Meera Desai', 42, 'F', '9595959595', 'Chronic Pain Management', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(21, 'Jayesh Pande', 75, 'M', '9696969696', 'Severe Dehydration, Elderly', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(22, 'Priya Iyer', 30, 'F', '9797979797', 'Flu/Viral Fever', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(23, 'Hema Reddy', 50, 'F', '9898989898', 'COVID-19 Positive', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(24, 'Anil Kapoor', 63, 'M', '9999999999', 'Post-Op Complication (Minor)', '2025-10-29 17:45:35', '2025-10-29 17:45:35'),
(25, 'Zoya Bano', 80, 'F', '8181818181', 'Severe Dementia, Fall Injury', '2025-10-29 17:45:35', '2025-10-29 17:45:35');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','doctor') NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `role`, `full_name`, `email`, `created_at`, `updated_at`) VALUES
(4, 'admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin', 'Priya Sharma (Hospital Director)', 'priya.sharma@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:51:01'),
(5, 'rkumar_finance', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin', 'Rajesh Kumar (Finance/Ops)', 'rajesh.k@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(6, 'dvarma_hr', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin', 'Deepa Varma (HR/Compliance)', 'deepa.v@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(7, 'ajoshi_it', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin', 'Arun Joshi (IT Systems Manager)', 'arun.j@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(8, 'dr_rohan', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Rohan Mehta (General Surgery)', 'rohan.m@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(9, 'dr_ayesha', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Ayesha Khan (Critical Care)', 'ayesha.k@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(10, 'dr_sanjay', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Sanjay Patel (Orthopedics)', 'sanjay.p@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(11, 'dr_kavya', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Kavya Rao (Emergency Medicine)', 'kavya.r@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(12, 'dr_vivek', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Vivek Singh (Cardiology)', 'vivek.s@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(13, 'dr_neha', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Neha Gupta (Pediatrics)', 'neha.g@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(14, 'dr_anil', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Anil Reddy (Neurology)', 'anil.r@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(15, 'dr_sangeeta', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Sangeeta Nair (Gynecology)', 'sangeeta.n@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(16, 'dr_gautam', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Gautam Shah (Anesthesia)', 'gautam.s@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(17, 'dr_fatima', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Fatima Ali (Radiology/ER)', 'fatima.a@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(18, 'dr_karan', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Karan Malhotra (Internal Medicine)', 'karan.m@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(19, 'dr_ishita', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Ishita Verma (Oncology)', 'ishita.v@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(20, 'dr_dev', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Dev Anand (Pulmonology)', 'dev.a@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(21, 'dr_zoya', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Zoya Mirza (General Practice)', 'zoya.m@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(22, 'dr_balaji', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Balaji Iyer (Gastroenterology)', 'balaji.i@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12'),
(23, 'dr_tina', 'f348d5628621f3d8f59c8cabda0f8eb0aa7e0514a90be7571020b1336f26c113', 'doctor', 'Dr. Tina Dsouza (Dermatology)', 'tina.d@hosp.in', '2025-10-29 16:46:12', '2025-10-29 16:46:12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admissions`
--
ALTER TABLE `admissions`
  ADD PRIMARY KEY (`admission_id`),
  ADD KEY `patient_id` (`patient_id`),
  ADD KEY `bed_id` (`bed_id`),
  ADD KEY `doctor_id` (`doctor_id`),
  ADD KEY `idx_admission_status` (`status`),
  ADD KEY `idx_admission_date` (`admission_date`);

--
-- Indexes for table `alos_statistics`
--
ALTER TABLE `alos_statistics`
  ADD PRIMARY KEY (`stat_id`);

--
-- Indexes for table `audit_logs`
--
ALTER TABLE `audit_logs`
  ADD PRIMARY KEY (`log_id`),
  ADD KEY `idx_audit_user` (`user_id`),
  ADD KEY `idx_audit_timestamp` (`timestamp`);

--
-- Indexes for table `beds`
--
ALTER TABLE `beds`
  ADD PRIMARY KEY (`bed_id`),
  ADD UNIQUE KEY `bed_number` (`bed_number`),
  ADD KEY `idx_bed_status` (`status`);

--
-- Indexes for table `bed_transfers`
--
ALTER TABLE `bed_transfers`
  ADD PRIMARY KEY (`transfer_id`),
  ADD KEY `admission_id` (`admission_id`),
  ADD KEY `from_bed_id` (`from_bed_id`),
  ADD KEY `to_bed_id` (`to_bed_id`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`patient_id`),
  ADD KEY `idx_patient_name` (`patient_name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admissions`
--
ALTER TABLE `admissions`
  MODIFY `admission_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `alos_statistics`
--
ALTER TABLE `alos_statistics`
  MODIFY `stat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `audit_logs`
--
ALTER TABLE `audit_logs`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `beds`
--
ALTER TABLE `beds`
  MODIFY `bed_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `bed_transfers`
--
ALTER TABLE `bed_transfers`
  MODIFY `transfer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `patient_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admissions`
--
ALTER TABLE `admissions`
  ADD CONSTRAINT `admissions_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  ADD CONSTRAINT `admissions_ibfk_2` FOREIGN KEY (`bed_id`) REFERENCES `beds` (`bed_id`),
  ADD CONSTRAINT `admissions_ibfk_3` FOREIGN KEY (`doctor_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `audit_logs`
--
ALTER TABLE `audit_logs`
  ADD CONSTRAINT `audit_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `bed_transfers`
--
ALTER TABLE `bed_transfers`
  ADD CONSTRAINT `bed_transfers_ibfk_1` FOREIGN KEY (`admission_id`) REFERENCES `admissions` (`admission_id`),
  ADD CONSTRAINT `bed_transfers_ibfk_2` FOREIGN KEY (`from_bed_id`) REFERENCES `beds` (`bed_id`),
  ADD CONSTRAINT `bed_transfers_ibfk_3` FOREIGN KEY (`to_bed_id`) REFERENCES `beds` (`bed_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
