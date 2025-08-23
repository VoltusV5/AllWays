-- ================== USERS ==================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATE,
    updated_at DATE
);

-- ================== ROLES ==================
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- ================== USER_ROLES ==================
CREATE TABLE user_roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- ================== PROFILES ==================
CREATE TABLE profiles (
    user_id INT PRIMARY KEY,
    full_name VARCHAR(255),
    birthday DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ================== BOOKINGS ==================
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    created_at DATE,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ================== TICKETS ==================
CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    passenger_name VARCHAR(255),
    seat_number VARCHAR(20),
    issued_at DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);

-- ================== PAYMENTS ==================
CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount INT,
    status VARCHAR(50),
    paid_at DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(id)
);

-- ================== PROVIDERS ==================
CREATE TABLE providers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    contact_info VARCHAR(255)
);

-- ================== ROUTES ==================
CREATE TABLE routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    provider_id INT NOT NULL,
    name VARCHAR(255),
    FOREIGN KEY (provider_id) REFERENCES providers(id)
);

-- ================== STOPS ==================
CREATE TABLE stops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    latitude VARCHAR(50),
    longitude VARCHAR(50)
);

-- ================== SEGMENTS ==================
CREATE TABLE segments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT NOT NULL,
    stop_from_id INT NOT NULL,
    stop_to_id INT NOT NULL,
    duration INT,
    FOREIGN KEY (route_id) REFERENCES routes(id),
    FOREIGN KEY (stop_from_id) REFERENCES stops(id),
    FOREIGN KEY (stop_to_id) REFERENCES stops(id)
);

-- ================== SCHEDULES ==================
CREATE TABLE schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    segment_id INT NOT NULL,
    departure_time DATE,
    arrival_time DATE,
    FOREIGN KEY (segment_id) REFERENCES segments(id)
);
