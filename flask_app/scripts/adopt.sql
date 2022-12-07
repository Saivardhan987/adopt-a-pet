create database adoptaclick;
use adoptaclick;

CREATE TABLE IF NOT EXISTS `adoptaclick`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `adoptaclick`.`pets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `type` VARCHAR(255) NULL,
  `breed` VARCHAR(255) NULL,
  `age` INT NULL,
  `location` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `phone` VARCHAR(255) NULL,
  `gender` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  `image` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pets_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_pets_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `adoptaclick`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `adoptaclick`.`users_has_pets` (
  `user_id` INT NOT NULL,
  `pet_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `pet_id`),
  INDEX `fk_users_has_pets_pets1_idx` (`pet_id` ASC) VISIBLE,
  INDEX `fk_users_has_pets_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_pets_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `adoptaclick`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_pets_pets1`
    FOREIGN KEY (`pet_id`)
    REFERENCES `adoptaclick`.`pets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

select * from pets;