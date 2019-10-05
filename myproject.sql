-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 06, 2019 at 01:41 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `myproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_admin`
--

CREATE TABLE IF NOT EXISTS `tbl_admin` (
  `adminid` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`adminid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_admin`
--

INSERT INTO `tbl_admin` (`adminid`, `password`) VALUES
('admin@gmail.com', 'admin@123');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_complain`
--

CREATE TABLE IF NOT EXISTS `tbl_complain` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `subject` varchar(300) NOT NULL,
  `complain` varchar(600) NOT NULL,
  `postdate` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tbl_complain`
--

INSERT INTO `tbl_complain` (`cid`, `username`, `userid`, `subject`, `complain`, `postdate`) VALUES
(1, 'Raj Kumar Verma', 'raj@gmail.com', 'Hello', 'hi', '2019-03-25 14:45:35'),
(2, 'Raj Verma', 'raj@gmail.com', 'jd', 'djgdfgd', '2019-04-01 15:49:31');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_enquiry`
--

CREATE TABLE IF NOT EXISTS `tbl_enquiry` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `enquiry_text` varchar(600) NOT NULL,
  `enquiry_date` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tbl_enquiry`
--

INSERT INTO `tbl_enquiry` (`id`, `name`, `gender`, `mobileno`, `email`, `enquiry_text`, `enquiry_date`) VALUES
(1, 'Raj Verma', 'Male', '38456348', 'raj@gmail.com', 'Hello', '2019-03-13 14:39:15'),
(2, 'Satish Kumar', 'Male', '45454545454', 's@gmail.com', 'hi', '2019-03-14 13:57:18');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE IF NOT EXISTS `tbl_feedback` (
  `fid` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `subject` varchar(300) NOT NULL,
  `feedback` varchar(600) NOT NULL,
  `postdate` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`fid`, `name`, `userid`, `subject`, `feedback`, `postdate`) VALUES
(1, 'Raj Kumar Verma', 'raj@gmail.com', 'hi', 'hello', '2019-03-16 15:32:47'),
(2, 'Raj Kumar Verma', 'raj@gmail.com', 'abc', 'xyz', '2019-03-25 14:18:21');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE IF NOT EXISTS `tbl_login` (
  `userid` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`userid`, `password`, `status`) VALUES
('raj@gmail.com', 'xyz', 'true'),
('aman@gmail.com', '123', 'true');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_registration`
--

CREATE TABLE IF NOT EXISTS `tbl_registration` (
  `name` varchar(100) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mobileno` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `address` varchar(250) NOT NULL,
  `reg_date` varchar(50) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_registration`
--

INSERT INTO `tbl_registration` (`name`, `dob`, `gender`, `mobileno`, `email`, `qualification`, `address`, `reg_date`) VALUES
('Raj Verma', '2019-03-13', 'Male', '38456348', 'raj@gmail.com', 'MCA', 'lucknow', '2019-03-13 16:02:14'),
('Aman Kumar', '2019-03-14', 'Male', '38456348', 'aman@gmail.com', 'BCA', 'lucknow', '2019-03-14 13:58:05');
