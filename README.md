## Silence VPN

Silence VPN is a project aimed at providing a secure and private virtual private network (VPN) solution. It allows users to establish encrypted connections to the internet, ensuring their online activities remain anonymous and protected from prying eyes.

The project focuses on simplicity, ease of use, and strong security measures. It offers a user-friendly interface, allowing users to connect to VPN servers with just a few clicks. Silence VPN also employs robust encryption algorithms to safeguard data transmission and protect user privacy.

With Silence VPN, users can bypass geographical restrictions, access blocked websites, and protect their sensitive information from hackers and surveillance. It is designed for individuals, businesses, and organizations that prioritize online privacy and security.


# Install Database

```sql

--
-- Table structure for `plans`
--

CREATE TABLE `plans` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `duration` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `user` varchar(255) NOT NULL,
  `rank` varchar(255) NOT NULL,
  `plans` varchar(255) NOT NULL,
  `duration` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```

## Config database connection

```py

# Config SQL

class ConfigurationDb(object):
    def __init__(self):
        self.host = 'localhost'
        self.user = 'YOUR_USERNAME_DB'
        self.password = 'YOUR_PASS_DB'
        self.db = 'YOUR_NAME_DB'

````