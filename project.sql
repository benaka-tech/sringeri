-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2021 at 11:40 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `devotees_details`
--

CREATE TABLE `devotees_details` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `address` varchar(100) NOT NULL,
  `state` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `temperature` int(11) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `id_card` varchar(100) NOT NULL,
  `checkin` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `devotees_details`
--

INSERT INTO `devotees_details` (`id`, `name`, `address`, `state`, `email`, `phone`, `temperature`, `photo`, `id_card`, `checkin`) VALUES
(12, 'benaka', 'tatanagar', 'Karnataka', 'cjayanth35@gmail.com', '9482937217', 0, 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos-20210312155800.png', 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-20210312155805.png', '2021-03-12'),
(13, 'jayanth', 'tatanagar', 'Karnataka', 'cjayanth35@gmail.com', '9482937217', 0, 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos-20210312160141.png', 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-20210312160159.png', '2021-03-12'),
(14, 'ChandraSekhar K', 'Hebbal', '', 'kalppachdra@gmail.com', '9480428309', 0, 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos-20210312160141.png', 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-20210312160159.png', '2021-03-12'),
(15, 'jayanth', 'tatanagar', 'Karnataka', 'cjayanth35@gmail.com', '9482937217', 0, 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos-20210312160504.png', 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-20210312160511.png', '2021-03-12'),
(16, 'Chandra', 'Hebbal', 'Andhra Pradesh', 'kalppa@gmail.com', '9428042309', 0, 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos-20210312160614.png', 'file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-20210312160624.png', '2021-03-12');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(11) NOT NULL,
  `password` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'benaka', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `devotees_details`
--
ALTER TABLE `devotees_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `devotees_details`
--
ALTER TABLE `devotees_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
