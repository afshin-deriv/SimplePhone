SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS phonebook (
  id int(5) NOT NULL AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  phone varchar(50) NOT NULL,
  address varchar(255) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;


INSERT INTO phonebook (id, name, phone, address) VALUES
(1, 'Afshin Paydar', '06123456', 'Cyberjaya');
