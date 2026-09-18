-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: mysql-8.0
-- Время создания: Май 19 2025 г., 23:29
-- Версия сервера: 8.0.41
-- Версия PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `bukvoezhka`
--

-- --------------------------------------------------------

--
-- Структура таблицы `bindings`
--

CREATE TABLE `bindings` (
  `binding_id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `bindings`
--

INSERT INTO `bindings` (`binding_id`, `name`) VALUES
(1, 'Жёсткий'),
(2, 'Мягкий');

-- --------------------------------------------------------

--
-- Структура таблицы `cards`
--

CREATE TABLE `cards` (
  `card_id` int NOT NULL,
  `author` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `publisher` varchar(200) DEFAULT NULL,
  `publish_year` int DEFAULT NULL,
  `binding` int DEFAULT NULL,
  `condition_` int DEFAULT NULL,
  `card_type` int NOT NULL,
  `card_status` int DEFAULT NULL,
  `user` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `cards`
--

INSERT INTO `cards` (`card_id`, `author`, `name`, `publisher`, `publish_year`, `binding`, `condition_`, `card_type`, `card_status`, `user`) VALUES
(1, 'Л. Н. Толстой', 'Война и мир', NULL, 0, NULL, NULL, 1, 1, 0),
(2, 'И. С. Тургенев', 'Отцы и дети', 'Библиотека всемирной литературы', 1971, 1, 1, 1, NULL, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `card_statuses`
--

CREATE TABLE `card_statuses` (
  `status_id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `card_statuses`
--

INSERT INTO `card_statuses` (`status_id`, `name`) VALUES
(1, 'Принята'),
(2, 'Отклонена');

-- --------------------------------------------------------

--
-- Структура таблицы `card_types`
--

CREATE TABLE `card_types` (
  `type_id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `card_types`
--

INSERT INTO `card_types` (`type_id`, `name`) VALUES
(1, 'Готов поделиться'),
(2, 'Хочу в свою библиотеку');

-- --------------------------------------------------------

--
-- Структура таблицы `conditions`
--

CREATE TABLE `conditions` (
  `condition_id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `conditions`
--

INSERT INTO `conditions` (`condition_id`, `name`) VALUES
(1, 'Б/У'),
(2, 'Новое');

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `role_id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`role_id`, `name`) VALUES
(1, 'Администратор'),
(2, 'Обычный пользователь');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `login` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`user_id`, `login`, `name`, `phone_number`, `email`, `password`, `role`) VALUES
(1, 'testuser', 'Иванов Иван Иванович', '+7 999 999 99 99', 'example@example.ru', 'bookworm', 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `bindings`
--
ALTER TABLE `bindings`
  ADD PRIMARY KEY (`binding_id`);

--
-- Индексы таблицы `cards`
--
ALTER TABLE `cards`
  ADD PRIMARY KEY (`card_id`),
  ADD KEY `card_type` (`card_type`),
  ADD KEY `card_status` (`card_status`),
  ADD KEY `binding` (`binding`),
  ADD KEY `condition_` (`condition_`);

--
-- Индексы таблицы `card_statuses`
--
ALTER TABLE `card_statuses`
  ADD PRIMARY KEY (`status_id`);

--
-- Индексы таблицы `card_types`
--
ALTER TABLE `card_types`
  ADD PRIMARY KEY (`type_id`);

--
-- Индексы таблицы `conditions`
--
ALTER TABLE `conditions`
  ADD PRIMARY KEY (`condition_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `users_ibfk_1` (`role`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `bindings`
--
ALTER TABLE `bindings`
  MODIFY `binding_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `cards`
--
ALTER TABLE `cards`
  MODIFY `card_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `card_statuses`
--
ALTER TABLE `card_statuses`
  MODIFY `status_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `card_types`
--
ALTER TABLE `card_types`
  MODIFY `type_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `conditions`
--
ALTER TABLE `conditions`
  MODIFY `condition_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `cards`
--
ALTER TABLE `cards`
  ADD CONSTRAINT `cards_ibfk_1` FOREIGN KEY (`card_type`) REFERENCES `card_types` (`type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `cards_ibfk_2` FOREIGN KEY (`card_status`) REFERENCES `card_statuses` (`status_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `cards_ibfk_3` FOREIGN KEY (`binding`) REFERENCES `bindings` (`binding_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `cards_ibfk_4` FOREIGN KEY (`condition_`) REFERENCES `conditions` (`condition_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role`) REFERENCES `roles` (`role_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
